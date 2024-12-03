import datetime

class Logger:
    @staticmethod
    def log_event(event):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {event}")
