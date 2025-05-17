from .database import db

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    subject = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "subject": self.subject
        }
