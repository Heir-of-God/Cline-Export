from cline_common import (
    classify,
    format_timestamp,
    load_messages,
    parse_args,
    render_export,
)


def parse_chat_logs_to_md(json_path, output_path):
    blocks = []
    model_parts = []
    model_start_time = None

    def flush_model_block():
        nonlocal model_parts, model_start_time
        if model_parts:
            merged_text = "\n\n---\n\n".join(model_parts)
            blocks.append(f"## 🤖 Model Answering\n*{model_start_time}*\n\n{merged_text}")
            model_parts = []
            model_start_time = None

    for item in load_messages(json_path):
        role, text = classify(item)
        time_str = format_timestamp(item.get("ts"))

        if role == "user":
            flush_model_block()
            blocks.append(f"## 👤 User Prompt\n*{time_str}*\n\n{text}")
        elif role in ("reasoning", "model"):
            if not model_parts:
                model_start_time = time_str
            if role == "reasoning":
                quoted = "\n".join(f"> {line}" for line in text.split("\n"))
                model_parts.append(f"### 🧠 Internal Reasoning\n{quoted}")
            else:
                model_parts.append(text)

    flush_model_block()

    markdown = render_export(
        "📋 Chat History Export",
        blocks,
        "_No relevant chat text data found in this log._",
    )
    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write(markdown)

    print(f"Success! Beautiful Markdown history exported to: {output_path}")


if __name__ == "__main__":
    args = parse_args(
        "Export a Cline chat log to Markdown, including the model's reasoning.",
        "chat_history_parsed.md",
    )
    parse_chat_logs_to_md(args.input, args.output)
