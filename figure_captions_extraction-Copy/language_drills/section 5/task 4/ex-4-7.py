import json
from datetime import datetime


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Serialize datetime as ISO format
        return super().default(obj)


def main():
    # Serialize a datetime object using a custom encoder
    now = datetime.now()
    data = {"event_time": now}

    json_data = json.dumps(data, cls=CustomEncoder)
    print("Serialized with custom encoder:", json_data)


if __name__ == "__main__":
    main()
