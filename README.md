# 🧠 Smart Flashcard System - Backend (Flask + SQLite)

This is a backend project for a **Smart Flashcard System** developed as part of an assignment for **NNIIT Tech, Hyderabad**.

The system allows students to:

- Add flashcards by just providing a **question** and **answer**.
- Automatically **detects the subject** of the flashcard (e.g., Physics, Biology, etc.).
- Retrieve **a mixed set of flashcards** from different subjects for a given student.

---

## 🚀 Features

✅ Add flashcards without specifying the subject  
✅ Automatically infer the subject based on question text  
✅ Store data using **SQLite**  
✅ Retrieve flashcards by **mixed subjects**  
✅ Lightweight API with **Flask**  
✅ Built-in classifier (can be extended to ML later)

---

## 📁 Folder Structure
<pre> flashcard-app/ ├── app/ │ ├── __init__.py │ ├── app.py # Main Flask app with routes │ ├── models.py # Flashcard model (SQLAlchemy) │ ├── database.py # Database setup (SQLite) │ ├── classifier.py # Rule-based subject classifier │ └── model.pkl # Trained model (if used) ├── requirements.txt # Dependencies ├── run.py # Entry point to run the app ├── train_model.py # Script to train subject classification model ├── train_classifier.py # Rule-based classifier (alternative approach) ├── training_data.csv # Dataset for training classifier ├── README.md # Full documentation └── .gitignore # Git ignored files and folders </pre>


---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** — Web framework
- **SQLAlchemy** — ORM for database
- **SQLite** — Lightweight database (file-based)
- **Rule-based classifier** (easily replaceable with ML/NLP models)

---

## 📦 Installation

### 🔧 Prerequisites

Make sure Python 3 is installed. Then:

### 🔌 Step 1: Clone the repo
```
git clone https://github.com/rajesh-addala/flash_card_api.git
cd flashcard-app
```
### 🧪 Step 2: Create a virtual environment and activate it
```
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 📥 Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Running the App
You can run the Flask app using:
```bash
python run.py
```

The API will start at: http://127.0.0.1:5000/

### 📡 API Endpoints
1. Add a flashcard
```
POST /flashcard
Content-Type: application/json

{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}

Response:

{
  "message": "Flashcard added successfully",
  "subject": "Physics"
}
```
2. Get Flashcards by student (by Mixed Subjects)
```
GET /get-subject?student_id=stu001&limit=5
```
Response:
Returns a mix of flashcards across subjects for that student.
```[
  {
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  },
  {
    "question": "What is photosynthesis?",
    "answer": "A process used by plants to convert light into energy",
    "subject": "Biology"
  }
]
```
This project was developed as part of the NNIIT Tech Hyderabad assignment.


