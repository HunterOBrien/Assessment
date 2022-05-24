""" Difficulty Selection v1, checks if the user has entered a 1, 2, or 3

"""

difficulty = input("What difficulty do you want to play?\n"
                   "1 for easy, 2 for medium, 3 for hard: ").lower()


# If they say 1, program continues on easy
if difficulty == "1" or difficulty == "one":
    print("Program continues (easy)")
# If they say 2, program continues on medium
elif difficulty == "2" or difficulty == "two":
    print("Program continues (medium)")

# If they say 3
elif difficulty == "3" or difficulty == "three":
    print("Program continues")
# otherwise, show error
else:
    print("Please answer 1, 2, or 3")
