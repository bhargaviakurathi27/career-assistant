from fastapi import FastAPI

app = FastAPI(title="AI Career & Placement Assistant API")


@app.get("/api/health")
def health():
    """Tiny endpoint to check the server is alive."""
    return {"status": "ok"}