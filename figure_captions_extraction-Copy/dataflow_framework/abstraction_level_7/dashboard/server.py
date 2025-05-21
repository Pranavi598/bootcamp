from fastapi import FastAPI
import uvicorn
from tracing.metrics_store import METRICS
from tracing.trace_store import TRACE_STORE
from tracing.error_store import ERROR_LOG

app = FastAPI()

@app.get("/stats")
def stats():
    return METRICS.get_stats()

@app.get("/trace")
def trace():
    return TRACE_STORE.get_all()

@app.get("/errors")
def errors():
    return ERROR_LOG.get_all()

def start_dashboard():
    uvicorn.run(app, host="0.0.0.0", port=8000)
