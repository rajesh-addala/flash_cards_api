import joblib

# Load model once
model = joblib.load('app/model.pkl')

def predict_subject(question: str) -> str:
    pred = model.predict([question])
    return pred[0]
