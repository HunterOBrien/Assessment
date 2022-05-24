"""  game mechanics v1
Creating functions that hold information about a quiz
and have a playable quiz function

"""

loop_break = ""
while loop_break != "x":
    # If they say 1, output: program continues on easy
    if difficulty == "1" or difficulty == "one":
        answer = "1"
        loop_break = "x"

    # If they say 2, output: program continues on medium
    elif difficulty == "2" or difficulty == "two":
        answer = "2"
        loop_break = "x"

    # If they say 3, output: program continues on hard
    elif difficulty == "3" or difficulty == "three":
        answer = "3"
        loop_break = "x"

    # If the input is not valid, loop through the while loop again
    else:
        print("Please enter a valid number (1, 2, or 3)")
        difficulty = (input("What difficulty do you want to play?\n"
                            "1 for easy, 2 for medium, 3 for hard: "))
