# server.py

from fastapi import FastAPI
from state import state  # import the shared FileProcessingState instance

app = FastAPI()

@app.get("/stats")
def get_stats():
    return state.get_stats()

@app.get("/files")
def get_files():
    return {"processed_files": state.get_processed_files()}
