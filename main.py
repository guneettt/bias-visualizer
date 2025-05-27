from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google_trends import fetch_google_trends
from reddit_scraper import fetch_reddit_data

app = FastAPI()

# Allow CORS for local Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body structure
class Query(BaseModel):
    keyword: str

@app.get("/")
def home():
    return {"message": "API is up!"}

@app.post("/analyze")
def analyze(query: Query):
    print("✅ Received:", query.keyword)

    try:
        google_score = fetch_google_trends(query.keyword)
        reddit_score = fetch_reddit_data(query.keyword)

        return {
            "google_interest": google_score,
            "reddit_mentions": reddit_score
        }
    except Exception as e:
        print("❌ Error:", str(e))
        return {"error": "Server error"}, 500
