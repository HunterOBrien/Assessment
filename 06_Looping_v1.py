""" Looping v1
This turns the quizzes into a re-playable loop
"""


# Function to format text object
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f" {top_bottom}\n {formatted_text}\n {top_bottom}"


# works out what difficulty the user wants
def difficulty_selection(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say 1, output: program continues on easy
        if answer == "1" or answer == "one":
            print()

        # If they say 2, output: program continues on medium
        elif answer == "2" or answer == "two":
            print()

        # If they say 3, output: program continues on hard
        elif answer == "3" or answer == "three":
            game_mechanics_hard()

        # otherwise, show error
        else:
            print("Please answer 1, 2, or 3")


# Hard quiz function
# Check game_mechanics_easy for comments in the function
# Testing function for looping
def game_mechanics_hard():
    questions_nums = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
    question_values = ["t", "f", "f", "f", "t", "t", "t", "f", "f", "t", "t", "f"]
    questions_text = ["Kohitatea is January",
                      "Hui-tangaru is March",
                      "Poutu-te-rangi is September",
                      "Paenga-whawha is December",
                      "Haratua is May",
                      "Pipiri is June",
                      "Hongongoi is July",
                      "Here-turi-koka is November",
                      "Maharu is March",
                      "Whiringa-a-nuku is October",
                      "Whiringa-a-rangi is November"
                      "Hakihea is January"]
    answer_storer = ""
    score = int(0)
    total_questions = int(0)
    quiz_loop_breaker = ""

    for questions_printer in range(len(questions_nums)):
        print(questions_nums[questions_printer])
        print(questions_text[questions_printer])
        answer_storer = input("enter answer here: ").lower()
        quiz_loop_breaker = "x"
        while quiz_loop_breaker == "x":
            if answer_storer == "f" or answer_storer == "t":
                if answer_storer == question_values[questions_printer]:
                    print("You got it right!")
                    score += 1
                    total_questions += 1
                    quiz_loop_breaker = "y"

                elif answer_storer != question_values[questions_printer]:
                    print("You got it wrong!")
                    total_questions += 1
                    quiz_loop_breaker = "y"

            else:
                print("please enter a valid input, (t or f)")
                quiz_loop_breaker = "y"
    print(formatter("!", "Well Played"))
    print(f"You got {score} out of {total_questions}")
    looping()


# Function to make the game a playable loop
def looping():
    finish_game = ""
    print("Do you want to do a Te Reo quiz?")
    play_again = input("If you want to play enter 'Y'\n"
                       "If you do not want to play enter 'N'\n "
                       ":  ").upper()

    while finish_game != "x":
        if play_again == "Y" or play_again == "YES":
            difficulty_selection("What difficulty do you want to play?\n"
                                 "1 for easy, 2 for medium, 3 for hard: ")

        elif play_again == "N" or play_again == "NO":
            print(formatter("*", "Thanks for playing... Goodbye"))
            finish_game = "x"
        else:
            print("Please enter a valid input (Y or N)")
            looping()


# Main
looping()
