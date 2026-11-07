# Creates global variable 'x' in the outer module scope with value "Cool".
x = "Cool"

# Defines a function named 'myfunc'; colon (:) starts the indented function body.
def myfunc():
    # The 'global' keyword allows modifying the global 'x' instead of creating a local one.
    global x

    # Overwrites the global variable 'x' with the new string "lool".
    x = "lool"

# Calls/executes 'myfunc()', running the code inside that updates global 'x'.
myfunc()

# Prints "lool", proving that the function modified the global variable permanently.
print(x)
