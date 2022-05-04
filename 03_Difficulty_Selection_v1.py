# Functions go here
def difficulty_selection(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output: program continues
        if answer == "1" or answer == "one":
            answer = "Yes"
            return answer

        # If they say no, output: display instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # otherwise, show error
        else:
            print("Please answer yes or no")


difficulty = difficulty_selection("What difficulty do you want to play?\n"
                                  "1 for easy, 2 for medium, 3 for hard")
