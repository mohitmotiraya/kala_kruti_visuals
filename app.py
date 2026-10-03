from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def home():
    return {
        "status": "success",
        "message": "Kalakruti Visuals API is running!"
    }

@app.get("/api/health")
def health():
    return {
        "status": "healthy"
    }
