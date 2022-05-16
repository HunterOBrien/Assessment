"""" Te Reo quiz Yes No checker function v4
Based on 01_Yes_No_v3
Yes/No checking function
Added instructions function
"""


# Functions go here
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output: program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output: display instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # otherwise, show error
        else:
            print("Please answer yes or no")


# Function to display instructions
def instructions():
    print("***** How To Play the Quizzes *****")
    print()
    print("You can select from either easy, medium or hard quizzes")
    print()
    print("Enter t or f to answer true or false")
    print()
    print("At the end you will receive a score out of ten \ndepending on how may you got right")
    print()
    print("You can try again as many times as you like")


# Main routine goes here
# Checks whether the user needs instructions
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
