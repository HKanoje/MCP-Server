# 🗒️ MCP-Server: AI Sticky Notes

MCP-Server is a lightweight and modular Python server that allows you to **create**, **read**, and **summarize** sticky notes using AI tools. It’s built on top of `FastMCP`, providing a simple API-style interface for managing notes stored in a text file.

---

## 📦 Features

* ✅ Add new sticky notes
* ✅ View all notes
* ✅ Retrieve the latest note
* ✅ Generate AI-based summaries of notes

---

## 🧠 How It Works

The server uses `FastMCP` to expose simple tools and resources:

* `add_note(message)` → Adds a new note to the file.
* `read_notes()` → Returns all stored notes.
* `get_latest_note()` → Fetches the most recent note.
* `note_summary_prompt()` → Returns a summarization prompt for the notes.

All notes are stored in `notes.txt` in the same directory.

---

## 📁 Project Structure

```
MCP-Server/
│
├── main.py          # Entry point for the MCP server
├── notes.txt        # Storage for all sticky notes
├── .gitignore       # Git ignored files
└── README.md        # Project documentation
```

---


### 📜 Sample Notes File

After interacting with the server, your `notes.txt` might look like this:

```
Work meeting today at 10 AM
AI agents use autonomous decision-making to complete tasks without human intervention
Types of AI agents include virtual assistants, recommendation systems, and autonomous vehicles
Agent foundations research focuses on ensuring AI systems make decisions aligned with human values
Multi-agent systems involve multiple AI agents interacting and collaborating to solve complex problems
Reinforcement learning is commonly used to train AI agents through trial and error
AI agents often need to handle uncertainty and incomplete information when making decisions
Tools like LangChain and AutoGPT help developers create and deploy AI agents more easily
Ethical considerations in AI agents include transparency, accountability, and preventing harmful behaviors
Agentic AI systems can use tools and interact with external systems to accomplish goals
Claude Code is an agentic command line tool from Anthropic that lets developers delegate coding tasks to Claude
```

When you call `note_summary_prompt()`, it will generate a prompt like:

```
Summarize the current notes: Work meeting today at 10 AM ...
```

This lets your AI model produce a concise summary like:

> 📌 Summary: A calendar reminder and a comprehensive overview of AI agents, including types, development techniques (e.g., reinforcement learning), tools (LangChain, Claude Code), and ethical concerns.

---

## 🛠️ Requirements

* Python 3.7+
* `fastmcp` 

---

## ✨ Author

Created by [HKanoje](https://github.com/HKanoje) — feel free to reach out for feedback or collaboration!
