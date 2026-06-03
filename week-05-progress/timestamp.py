from datetime import datetime

def timestamp_actual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(timestamp_actual())


