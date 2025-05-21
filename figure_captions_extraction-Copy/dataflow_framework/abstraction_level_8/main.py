from app.monitor import start_monitoring
from app.dashboard import start_dashboard
import threading

if __name__ == "__main__":
    # Start monitoring in a background thread
    monitor_thread = threading.Thread(target=start_monitoring, daemon=True)
    monitor_thread.start()

    # Start FastAPI dashboard (this is a blocking call)
    start_dashboard()
