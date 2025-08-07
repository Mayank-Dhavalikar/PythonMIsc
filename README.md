# 🧰 Personal Projects Collection

This repository is a collection of small, experimental, and portfolio-oriented projects built to test out ideas, explore technologies, and improve my coding skills.

> ⚠️ Most of these projects are not intended for production use — they serve as learning experiences or personal tools.

---

## 📌 Current Project: App Window Sidebar (Python)

A simple desktop utility that displays a sidebar listing all currently open application windows on your system (excluding itself). Clicking on any listed item brings that app to the front.

### ✅ Features

- Displays the names of all open application windows.
- Automatically excludes the sidebar window from the list.
- Clicking an app name brings it into focus (behind the sidebar).
- Built with Python using `tkinter` and `pywin32`.

### 🛠 Technologies Used

- Python 3
- Tkinter (GUI)
- pywin32 (for Windows API integration)

---

## 💡 Why This Project?

I often work on research, writing, or competitions where I juggle multiple apps — browsers, document editors, image viewers, etc. This tool serves as a lightweight "heads-up display" of all active apps, helping me stay focused and organized.

---

## 🧮 Project: CLI Calculator with Validation (Python)

A simple command-line calculator that safely evaluates math expressions entered by the user. It filters out invalid characters and incorrect operator combinations before using `eval()` for computation.

### ✅ Features

- Accepts basic math operations: `+`, `-`, `*`, `/`, `%`, and parentheses.
- Filters invalid characters using regular expressions.
- Detects incorrect operator sequences like `++`, `*/`, `+-`, etc.
- Catches syntax and type errors with friendly error messages.
- Suppresses traceback output for cleaner command-line usage.

### 🛠 Technologies Used

- Python 3
- `re` (regular expressions) for input validation
- `eval()` for evaluating safe expressions
- Error handling (`try-except`) for graceful failure

---

## 🗂️ More Projects Coming Soon...

This repo will be expanded with:
- Quick utilities
- Scripts and automation tools
- UI experiments
- Learning-focused builds
  
Stay tuned!

---

## 📄 License

[MIT License](LICENSE)
