from flask import Flask, request, jsonify
import joblib
import random

app = Flask(__name__)

# Load the trained model
model = joblib.load('app/model.pkl')

# In-memory store for flashcards: {student_id: [flashcard_dicts]}
flashcards_db = {}

@app.route('/flashcard', methods=['POST'])
def add_flashcard():
    data = request.get_json()
    student_id = data.get('student_id')
    question = data.get('question')
    answer = data.get('answer')

    if not student_id or not question or not answer:
        return jsonify({"error": "student_id, question, and answer are required"}), 400

    # Predict subject using model
    subject = model.predict([question])[0]

    # Store flashcard
    flashcard = {
        "question": question,
        "answer": answer,
        "subject": subject
    }
    flashcards_db.setdefault(student_id, []).append(flashcard)

    return jsonify({
        "message": "Flashcard added successfully",
        "subject": subject
    }), 201

@app.route('/get-subject', methods=['GET'])
def get_flashcards():
    student_id = request.args.get('student_id')
    limit = int(request.args.get('limit', 5))

    if not student_id:
        return jsonify({"error": "student_id query parameter is required"}), 400

    student_flashcards = flashcards_db.get(student_id, [])

    if not student_flashcards:
        return jsonify([])

    # Group flashcards by subject
    subject_map = {}
    for card in student_flashcards:
        subject_map.setdefault(card['subject'], []).append(card)

    # Mix flashcards across subjects intelligently
    mixed_flashcards = []
    subjects = list(subject_map.keys())
    idx = {subj: 0 for subj in subjects}

    while len(mixed_flashcards) < limit:
        # Iterate subjects and pick one flashcard if available
        for subj in subjects:
            if idx[subj] < len(subject_map[subj]):
                mixed_flashcards.append(subject_map[subj][idx[subj]])
                idx[subj] += 1
                if len(mixed_flashcards) == limit:
                    break
        else:
            # No more flashcards available
            break

    random.shuffle(mixed_flashcards)  # Shuffle final batch

    return jsonify(mixed_flashcards)

@app.route('/clear-flashcards', methods=['POST'])
def clear_flashcards():
    flashcards_db.clear()
    return jsonify({"message": "Flashcards database cleared successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
