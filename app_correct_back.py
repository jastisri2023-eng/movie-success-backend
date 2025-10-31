from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow cross-origin requests (so Streamlit Cloud can call it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Review(BaseModel):
    movie: str
    review: str

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}

@app.post("/predict")
def predict_sentiment(data: Review):
    prob = round(random.uniform(0.4, 0.9), 2)
    label = "Hit" if prob > 0.65 else "Average"
    return {"movie": data.movie, "prediction": label, "confidence": prob}
