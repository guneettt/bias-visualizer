from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google_trends import fetch_google_trends

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
        timeline = fetch_google_trends(query.keyword)

        # Calculate average interest
        values = [point['value'] for point in timeline if point['value'] is not None]
        avg_interest = sum(values) // len(values) if values else 0
        
        return {
            "google_interest": avg_interest,
            "timeline": timeline
        }
    except Exception as e:
        print("❌ Error:", str(e))
        return {"error": "Server error"}, 500
