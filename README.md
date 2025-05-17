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
flashcard-app/
├── app/
│ ├── init.py
│ ├── app.py # Main Flask app with routes
│ ├── models.py # Flashcard model (SQLAlchemy)
│ ├── database.py # Database setup (SQLite)
│ ├── classifier.py # Rule-based subject classifier
├── requirements.txt # Dependencies
└── README.md # Full documentation


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
```bash
git clone https://github.com/rajesh-addala/flash_card_api.git
cd flashcard-app
