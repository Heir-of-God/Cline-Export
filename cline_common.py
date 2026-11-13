import json
import sys
from datetime import datetime


def format_timestamp(ts_ms):
    try:
        return datetime.fromtimestamp(ts_ms / 1000.0).strftime("%Y-%m-%d %H:%M:%S")
    except (TypeError, ValueError, OverflowError, OSError):
        return "Unknown Time"


def load_messages(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except OSError as e:
        sys.exit(f"Error: cannot read '{json_path}': {e.strerror}")
    except json.JSONDecodeError as e:
        sys.exit(f"Error parsing JSON: {e}")
    if not isinstance(data, list):
        sys.exit("Error: expected a list of messages (ui_messages.json).")
    return data


def classify(item):
    """Returns (role, text) where role is 'user', 'reasoning', 'model', 'plan' or None."""
    text = (item.get("text") or "").strip()
    if not text:
        return None, ""

    say_type = item.get("say")
    if say_type in ("task", "user_feedback"):
        return "user", text
    if say_type == "reasoning":
        return "reasoning", text
    if say_type in ("text", "completion_result"):
        return "model", text
    if item.get("ask") == "plan_mode_respond":
        try:
            return "plan", json.loads(text).get("response", text)
        except (json.JSONDecodeError, AttributeError):
            return "plan", text
    if item.get("ask") == "followup":
        return "model", format_followup(text)
    return None, ""


def format_followup(text):
    try:
        payload = json.loads(text)
        question = payload["question"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return text
    options = payload.get("options") or []
    return "\n".join([question, "", *(f"- {option}" for option in options)]).strip()


def render_export(title, formatted_blocks, empty_message):
    body = "\n\n---\n\n".join(formatted_blocks) if formatted_blocks else empty_message
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"# {title}\n\n*Generated on: {generated}*\n\n---\n\n{body}"
