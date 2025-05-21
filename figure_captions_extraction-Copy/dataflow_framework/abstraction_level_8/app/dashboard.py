### abstraction-level_8/app/dashboard.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from app.monitor import get_state

app = FastAPI()

@app.get("/status")
def status():
    return JSONResponse(get_state())


def start_dashboard():
    uvicorn.run(app, host="0.0.0.0", port=8000)