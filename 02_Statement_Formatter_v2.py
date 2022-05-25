"""" Component 2 Statement Formatter v2
    changed v1 into a function
"""


# Function to format text
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n {formatted_text}\n {top_bottom}"


# Main Routine
text1 = input("Enter the statement you want to format: ")
symbol1 = input("What symbol do you want to use: ")
print()
print(formatter(symbol1, text1))

