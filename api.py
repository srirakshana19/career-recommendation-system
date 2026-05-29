from fastapi import FastAPI
from pydantic import BaseModel

from backend.recommender import recommend_career
from backend.database import save_recommendation
from backend.database import get_history

# Create FastAPI app
app = FastAPI()

# Input Schema
class UserInput(BaseModel):

    skills: str
    interests: str
    personality: str


# Home Route
@app.get("/")
def home():

    return {
        "message": "Career Recommendation API Running"
    }


# Recommendation Route
@app.post("/recommend")
def recommend(user: UserInput):

    # Get recommendations
    results = recommend_career(
        user.skills,
        user.interests,
        user.personality
    )

    # Extract career names
    career_names = [
        career
        for career, score in results
    ]

    # Save to database
    save_recommendation(
        user.skills,
        user.interests,
        user.personality,
        career_names
    )

    # Return recommendations
    return {
        "recommendations": results
    }


# History Route
@app.get("/history")
def history():

    data = get_history()

    return {
        "history": data
    }