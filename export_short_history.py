import sys

from cline_common import classify, format_timestamp, load_messages, render_export


def parse_chat_short_to_md(json_path, output_path):
    blocks = []

    for item in load_messages(json_path):
        role, text = classify(item)
        time_str = format_timestamp(item.get("ts"))

        if role == "user":
            blocks.append(f"## 👤 User Prompt\n*{time_str}*\n\n{text}")
        elif role in ("model", "plan"):
            blocks.append(f"## 🤖 Model Response\n*{time_str}*\n\n{text}")

    markdown = render_export(
        "📋 Compact Chat History (Prompts & Responses Only)",
        blocks,
        "_No conversational text data found in this log._",
    )
    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write(markdown)

    print(f"Success! Compact Markdown history exported to: {output_path}")


if __name__ == "__main__":
    input_json = "history.json"
    output_md = "chat_history_short.md"

    if len(sys.argv) > 1:
        input_json = sys.argv[1]
    if len(sys.argv) > 2:
        output_md = sys.argv[2]

    parse_chat_short_to_md(input_json, output_md)
