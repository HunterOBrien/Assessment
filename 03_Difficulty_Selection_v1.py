""" Difficulty Selection v1, checks if the user has entered a 1, 2, or 3

"""

difficulty = input("What difficulty do you want to play?\n"
                   "1 for easy, 2 for medium, 3 for hard: ").lower()


# If they say yes, output: program continues
if difficulty == "1" or difficulty == "one":
    print("Program continues")
# If they say no, output: display instructions
elif difficulty == "2" or difficulty == "two":
    print("Give instructions")
# otherwise, show error
else:
    print("Please answer 1, 2, or 3")
