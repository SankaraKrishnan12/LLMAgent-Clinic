import json
from datetime import datetime

def log_action(action_name, payload, response):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action_name,
        "request": payload,
        "response": response
    }

    with open("audit_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
