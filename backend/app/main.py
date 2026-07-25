"""
SurakshaCall AI — FastAPI Entry Point
Owner: Ron (backend/orchestration)
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="SurakshaCall AI",
    description="Privacy-first real-time scam call behavioral analyzer",
    version="0.1.0",
)

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

@app.get("/health")
async def health():
    return {"status": "ok", "message": "SurakshaCall AI is running locally."}
