# Prints text followed by an automatic newline (\n), moving the next output to a new line.
print("First Line")

# Each standard print() statement outputs on a fresh line by default.
print("Second Line")

# 'end=" "' overrides the default newline, keeping the next output on the same line with a space.
print("Third Line", end=" ")

# Continues on the same line as 'Third Line' because of the previous end parameter.
print("Fourth Line")

# Numbers (integers/floats) do not use quotes; quotes are only for text (strings).
print(3)

# Prints numeric values directly to the console.
print(50)

# Evaluates arithmetic expressions first, then prints the calculated sum (80).
print(50 + 30)

# Commas separate arguments, auto-insert a space, and easily combine strings with numbers.
print("My name is Daniel and i'm", 5)

# Combining different data types with commas avoids the need for manual type conversion (str()).
print("I am", 25)
