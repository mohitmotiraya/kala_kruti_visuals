from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/api")
def api_home():
    return {
        "status": "success",
        "message": "Kalakruti Visuals API is running!"
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy"
    }
