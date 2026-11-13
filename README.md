# Cline-Export

![GitHub created at](https://img.shields.io/github/created-at/Heir-of-God/Cline-Export)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python&logoColor=white)
![GitHub stars](https://img.shields.io/github/stars/Heir-of-God/Cline-Export)
![License](https://img.shields.io/github/license/Heir-of-God/Cline-Export)

## Welcome! 👋

Hi, I'm Hlib, a Software Engineering student. I use **Cline** (formerly known as **Claude Dev**), the VS Code extension, a lot, and I wanted a way to keep my chats as plain text. Cline has no built-in export, so I wrote two small Python scripts that turn its JSON chat logs into readable Markdown. 📝

They only use the standard library, so there is nothing to install besides Python itself.

## ✨ Features

- 📄 **Two export modes**
  - `export_full_history.py` keeps everything: your prompts, the model's replies, and its internal reasoning as blockquotes.
  - `export_short_history.py` keeps only your prompts and the model's replies, which is handy for a quick summary.
- 💬 Includes plan-mode replies, follow-up questions (with their options) and the final completion result.
- 🕒 Every message gets a timestamp.
- 🧹 Tool calls, command output and checkpoints are skipped, so the result reads like a conversation.
- ⚙️ Simple CLI: an input file, an optional output file, and `-h` for help.

## 📷 Example output

This is a short export of made-up sample data:

```markdown
# 📋 Compact Chat History (Prompts & Responses Only)

*Generated on: 2026-11-13 17:20:29*

---

## 👤 User Prompt
*2026-01-01 02:00:00*

Add a /health endpoint to my Flask app and write a test for it.

---

## 🤖 Model Response
*2026-01-01 02:09:00*

Should the endpoint also report the database status?

- Yes
- No

---

## 🤖 Model Response
*2026-01-01 02:11:00*

The `/health` endpoint returns `{"status": "ok"}` and `test_health.py` passes.
```

## 📥 Installation

1. Give this repository a ⭐ if you like it!
2. Make sure you have Python 3 installed.
3. Clone the repo:
   ```bash
   git clone https://github.com/Heir-of-God/Cline-Export.git
   cd Cline-Export
   ```
4. Find the log of the chat you want to export. Cline keeps every task in its own folder, containing `ui_messages.json` (the one these scripts read), `api_conversation_history.json` and `task_metadata.json`. On Windows the folders live in:
   ```
   %APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\tasks\<task_id>\
   ```

## 🎮 Usage

Pass the path to a `ui_messages.json` and, optionally, the name of the Markdown file to create:

```bash
python export_full_history.py path/to/ui_messages.json full_chat.md
python export_short_history.py path/to/ui_messages.json short_chat.md
```

Without arguments the scripts look for `history.json` in the current folder and write `chat_history_parsed.md` (full) or `chat_history_short.md` (short). `history.json` and exported `chat_history_*.md` files are listed in `.gitignore`, so your chats won't end up in a commit by accident.

Use `-h` to see all options.

## 📃 License

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file for details.

<p align="center">Show ❤️ By Starring This Repo💎</p>
