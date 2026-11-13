import json
import os
import sys
from datetime import datetime


def format_timestamp(ts_ms):
    """Converts millisecond timestamp to a readable datetime string."""
    try:
        return datetime.fromtimestamp(ts_ms / 1000.0).strftime("%Y-%m-%d %H:%M:%S")
    except (TypeError, ValueError, OverflowError, OSError):
        return "Unknown Time"


def parse_chat_short_to_md(json_path, output_path):
    if not os.path.exists(json_path):
        print(f"Error: Source file '{json_path}' not found.")
        return

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return

    formatted_blocks = []

    for item in data:
        say_type = item.get("say")
        ask_type = item.get("ask")
        ts = item.get("ts")
        time_str = format_timestamp(ts)
        text_content = (item.get("text") or "").strip()

        if not text_content:
            continue

        if say_type in ("task", "user_feedback"):
            formatted_blocks.append(
                f"## 👤 User Prompt\n*{time_str}*\n\n{text_content}"
            )

        elif ask_type == "plan_mode_respond":
            try:
                payload = json.loads(text_content)
                actual_response = payload.get("response", text_content)
                formatted_blocks.append(
                    f"## 🤖 Model Response\n*{time_str}*\n\n{actual_response}"
                )
            except Exception:
                formatted_blocks.append(
                    f"## 🤖 Model Response\n*{time_str}*\n\n{text_content}"
                )

        elif say_type == "text":
            formatted_blocks.append(
                f"## 🤖 Model Response\n*{time_str}*\n\n{text_content}"
            )

    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write("# 📋 Compact Chat History (Prompts & Responses Only)\n\n")
        out_f.write(
            f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        )
        out_f.write("---\n\n")

        if not formatted_blocks:
            out_f.write("_No conversational text data found in this log._")
        else:
            out_f.write("\n\n---\n\n".join(formatted_blocks))

    print(f"Success! Compact Markdown history exported to: {output_path}")


if __name__ == "__main__":
    input_json = "history.json"
    output_md = "chat_history_short.md"

    if len(sys.argv) > 1:
        input_json = sys.argv[1]
    if len(sys.argv) > 2:
        output_md = sys.argv[2]

    parse_chat_short_to_md(input_json, output_md)
