# Cline Chat History Exporter 📝

A set of lightweight Python utilities to parse, format, and export **Cline** (formerly known as **"Claude Dev"**) VS Code chat logs from JSON into clean, readable Markdown documents.

## Why This Tool?

While **Cline** is my go-to AI coding assistant, its VS Code extension currently **lacks a native feature to export chat transcripts**.

When you need to review a long architectural discussion, share your debugging history with a teammate, or back up an insightful session, digging through raw JSON files is highly impractical. This tool bridge that gap by instantly converting complex logs into organized .md documentation.

---

## Features

This repository includes two parser variants depending on how much detail you want to extract:

1. **Detailed Parser (`export_full_history.py`)**
   - Groups consecutive text blocks logically.
   - Extracts and cleanly isolates the model's **Internal Reasoning** (`### 🧠 Internal Reasoning`) inside blockquotes.
   - Great for deep-diving into _how_ the model planned its solutions.

2. **Compact Parser (`export_short_history.py`)**
   - Filters out internal thinking/reasoning entirely.
   - Focuses purely on the core **User Prompts** and final **Model Responses**.
   - Ideal for quick, clean summaries of the final conversational outcomes.

---

## How to Locate Your Cline Chat Logs

Cline saves its history as JSON files locally. You can typically find them here:

- **Windows:** `...\Code\User\globalStorage\saoudrizwan.claude-dev\tasks\(task_id)\ui_messages.json`
- **macOS:** ???
- **Linux:** ???

(Also you can go to specific task directory from Cline interface)

Simply copy your target `ui_messages.json` log file as `history.json` into this repository directory to get started.

---

## Usage

Both scripts run natively using standard Python libraries—no external dependencies or `pip install` required.
