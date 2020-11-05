from datetime import datetime


def log(message: str):
    today = datetime.now()

    print(f"[{today.hour}:{today.minute}:{today.second}] {message}")