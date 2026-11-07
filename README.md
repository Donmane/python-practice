# Python Practice Notes

A beginner-friendly collection of Python code notes, syntax reminders, and practice scripts.

---

## Table of Contents
1. [01. Python Intro (`Python Intro/01-python.py`)](#1-python-intro)
2. [02. Python Output (`Python output/02-python.py`)](#2-python-output)
3. [03. Python Comments (`Python comment/03-python.py`)](#3-python-comments)
4. [04. Python Variables & Scope (`Pyhon Variables/04-python.py`)](#4-python-variables--scope)
4. [04. Python Variables & Scope (`Pyhon Variables/04-python.py`)](#4-python-variables--scope)

---

## 1. Python Intro
**File:** [`Python Intro/01-python.py`](Python%20Intro/01-python.py)

```python
x = 5               # Auto-typed; no 'var', 'let', or 'const' needed
t = 7
print(x + t)        # Outputs: 12

if 5 > 2:
    print("5 is greater than 2")  # 4 spaces indentation required
```

**Key concepts covered:**
- **No `var`, `let`, or `const`:** Python variables are created automatically when assigned with `=`. Types (`int`, `str`, `float`) are inferred dynamically.
- **Indentation & Blocks:** Python does not use curly braces `{}` to define code blocks. Blocks start with a colon (`:`) and require 4 spaces of indentation.
- **Indentation Errors:** Inconsistent spacing, unexpected indents, or missing indents after a colon trigger an `IndentationError`.
- **Comments:** Single-line comments start with `#` and are ignored by Python.
- **Semicolons (`;`):** Can separate multiple statements on one line, though newlines are PEP 8 standard.

---

## 2. Python Output
**File:** [`Python output/02-python.py`](Python%20output/02-python.py)

```python
print("First Line")
print("Third Line", end=" ")   # Keeps next print on the same line
print("Fourth Line")
print("Age:", 25)              # Comma auto-spaces and mixes types
```

**Key concepts covered:**
- **Default Line Ending:** `print()` automatically appends a newline (`\n`), placing consecutive print calls on new lines.
- **The `end` Parameter:** Use `print(..., end=" ")` to override the default newline and keep subsequent output on the same line.
- **Numbers vs. Strings:** Text requires quotes (`"..."`), while numbers (`int`, `float`) do not.
- **Calculations in Print:** Arithmetic expressions (e.g. `50 + 30`) are evaluated before being printed.
- **Multiple Arguments with Commas:** `print("Age:", 25)` automatically inserts a space between arguments and seamlessly combines strings with numbers without needing `str()`.

---

## 3. Python Comments
**File:** [`Python comment/03-python.py`](Python%20comment/03-python.py)

```python
# Single-line comment
# print("Disabled code")        # Commented out for testing

"""
Multi-line comment or docstring
written across multiple lines.
"""
print("Hello, World!")
```

**Key concepts covered:**
- **Single-Line Comments:** Any text following a `#` on that line is ignored by Python during execution.
- **Commenting Out Code:** Adding `#` in front of code stops it from executing without needing to delete it (useful for debugging).
- **Multi-Line Comments with `#`:** Python has no dedicated multi-line comment token; standard convention is stacking multiple `#` lines.
- **Multi-Line Strings as Comments:** Unassigned triple quotes (`"""..."""` or `'''...'''`) are discarded by Python at runtime, making them popular for multi-line notes and docstrings.

---

## 4. Python Variables & Scope
**File:** [`Pyhon Variables/04-python.py`](Pyhon%20Variables/04-python.py)

```python
x = "Cool"          # Global variable

def myfunc():
    global x        # Targets the global 'x' instead of creating a local one
    x = "lool"      # Modifies the global 'x'

myfunc()
print(x)            # Outputs: lool
```

**Key concepts covered:**
- **Global Scope:** Variables defined outside functions are global and accessible across the entire file.
- **Local Scope:** Variables created inside a function only exist within that function.
- **The `global` Keyword:** In Python, assigning to a variable inside a function creates a local variable by default. Using `global variable_name` informs Python to target and mutate the global-scoped variable instead.
- **Function Syntax:** Defined with `def function_name():` followed by a colon and an indented body (4 spaces).

---

## 4. Python Variables & Scope
**File:** [`Pyhon Variables/04-python.py`](Pyhon%20Variables/04-python.py)

```python
x = "Cool"          # Global variable

def myfunc():
    global x        # Targets the global 'x' instead of creating a local one
    x = "lool"      # Modifies the global 'x'

myfunc()
print(x)            # Outputs: lool
```

**Key concepts covered:**
- **Global Scope:** Variables defined outside functions are global and accessible across the entire file.
- **Local Scope:** Variables created inside a function only exist within that function.
- **The `global` Keyword:** In Python, assigning to a variable inside a function creates a local variable by default. Using `global variable_name` informs Python to target and mutate the global-scoped variable instead.
- **Function Syntax:** Defined with `def function_name():` followed by a colon and an indented body (4 spaces).
