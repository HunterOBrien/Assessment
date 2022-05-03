"""" Te Reo quiz Yes No checker V1
Checks whether the user has played the quiz before
"""

# Ask the user if they have played before
show_instructions = input("Have you played this game before? : ").lower()
# If they say yes, output: program continues
if show_instructions == "yes" or show_instructions == "y":
    print("Program continues")
# If they say no, output: display instructions
elif show_instructions == "no" or show_instructions == "n":
    print("Give instructions")
# otherwise, show error
else:
    print("Please answer yes or no")

