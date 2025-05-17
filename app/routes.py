from flask import Blueprint, request, jsonify
from .models import Flashcard
from .database import db
from .classifier import predict_subject
import random

bp = Blueprint('api', __name__)

@bp.route('/flashcard', methods=['POST'])
def add_flashcard():
    data = request.json
    student_id = data.get('student_id')
    question = data.get('question')
    answer = data.get('answer')

    if not all([student_id, question, answer]):
        return jsonify({"error": "student_id, question and answer are required"}), 400

    subject = predict_subject(question)

    flashcard = Flashcard(student_id=student_id, question=question, answer=answer, subject=subject)
    db.session.add(flashcard)
    db.session.commit()

    return jsonify({
        "message": "Flashcard added successfully",
        "subject": subject
    }), 201

@bp.route('/get-subject', methods=['GET'])
def get_flashcards():
    student_id = request.args.get('student_id')
    limit = request.args.get('limit', default=5, type=int)

    if not student_id:
        return jsonify({"error": "student_id is required"}), 400

    # Query all flashcards for student
    flashcards = Flashcard.query.filter_by(student_id=student_id).all()

    # Group flashcards by subject
    subject_map = {}
    for card in flashcards:
        subject_map.setdefault(card.subject, []).append(card)

    # Create a mixed list taking one from each subject at a time until limit reached
    result = []
    subjects = list(subject_map.keys())
    idx = 0

    while len(result) < limit and subjects:
        subject = subjects[idx % len(subjects)]
        if subject_map[subject]:
            result.append(subject_map[subject].pop(0))
        else:
            subjects.remove(subject)
        idx += 1

    # Shuffle to mix subjects more randomly
    random.shuffle(result)

    # Return as list of dicts
    return jsonify([card.to_dict() for card in result])
