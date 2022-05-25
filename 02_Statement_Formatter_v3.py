"""" Component 2 Statement Formatter v3
    Call function three times for tests
"""


# Function to format text object
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f" {top_bottom}\n {formatted_text}\n {top_bottom}"


# Main Routine
# Calling the formatter function with the text and symbol
print(formatter("-", "Welcome to the Te Reo quiz"))
print()
print(formatter("!", "You got 5/10 on the easy quiz"))
print()
print(formatter("*", "Thanks for playing... Goodbye"))
