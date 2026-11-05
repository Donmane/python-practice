# Python Practice Notes

A beginner-friendly collection of Python code notes, syntax reminders, and practice scripts.

---

## Table of Contents
1. [01. Python Intro (`Python Intro/01-python.py`)](#1-python-intro)
2. [02. Python Output (`Python output/02-python.py`)](#2-python-output)

---

## 1. Python Intro
**File:** [`Python Intro/01-python.py`](Python%20Intro/01-python.py)

Key concepts covered:
- **No `var`, `let`, or `const`:** Python variables are created automatically when assigned with `=`. Types (`int`, `str`, `float`) are inferred dynamically.
- **Indentation & Blocks:** Python does not use curly braces `{}` to define code blocks. Blocks start with a colon (`:`) and require 4 spaces of indentation.
- **Indentation Errors:** Inconsistent spacing, unexpected indents, or missing indents after a colon trigger an `IndentationError`.
- **Comments:** Single-line comments start with `#` and are ignored by Python.
- **Semicolons (`;`):** Can be used to chain multiple statements on a single line, but PEP 8 encourages one statement per line.

---

## 2. Python Output
**File:** [`Python output/02-python.py`](Python%20output/02-python.py)

Key concepts covered:
- **Default Line Ending:** `print()` automatically appends a newline (`\n`), placing consecutive print calls on new lines.
- **The `end` Parameter:** Use `print(..., end=" ")` to override the default newline and keep subsequent output on the same line.
- **Numbers vs. Strings:** Text requires quotes (`"..."`), while numbers (`int`, `float`) do not.
- **Calculations in Print:** Arithmetic expressions (e.g. `50 + 30`) are evaluated before being printed.
- **Multiple Arguments with Commas:** `print("Age:", 25)` automatically inserts a space between arguments and seamlessly combines strings with numbers without needing `str()`.

