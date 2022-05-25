"""" Component 2 Statement Formatter v1
"""

# Parameters for formatting
symbol = "*"
text = "Hello World"
sides = symbol * 3

# Calculation to format text
formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)


# Printing the text
print(top_bottom)
print(formatted_text)
print(top_bottom)
