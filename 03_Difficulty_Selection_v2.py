""" Difficulty Selection v2
Turns it into a function
"""


def difficulty_selection(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say 1, output: program continues on easy
        if answer == "1" or answer == "one":
            answer = "1"
            return answer

        # If they say 2, output: program continues on medium
        elif answer == "2" or answer == "two":
            answer = "2"
            return answer

        # If they say 3, output: program continues on hard
        elif answer == "3" or answer == "three":
            answer = "3"
            return answer

        # otherwise, show error
        else:
            print("Please answer 1, 2, or 3")


# Gets the difficulty the user wants
difficulty = difficulty_selection("What difficulty do you want to play?\n"
                                  "1 for easy, 2 for medium, 3 for hard: ")

