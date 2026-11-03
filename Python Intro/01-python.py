# Outputs text to the console; strings must be enclosed in quotes.
print("Hello")

# Creates variable 'x' without 'var', 'let', or 'const' (Python auto-detects types).
x = 5

# Assigns 7 to 't'; in Python, variables are created instantly on assignment (=).
t = 7

# Adds values of x and t, then prints the result (12) to the terminal.
print(x + t)

# Evaluates condition; colon (:) starts a block (Python uses indentation, not {}).
if 5 > 2:
    # Must be indented (standard 4 spaces); improper spacing causes an IndentationError.
    print("5 is greatter than 2")

    # Lines starting with '#' are single-line comments ignored by the interpreter.
    # this is a comment

    # Semicolons (;) chain multiple statements on one line, though newlines are preferred.
    print("How are you"); print("The grass is green"); print("Yo")
