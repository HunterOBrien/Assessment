""" Te Reo Quiz base component v3
components added after they have been created and tested
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


# Function to format text object
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f" {top_bottom}\n {formatted_text}\n {top_bottom}"


def difficulty_selection(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say 1, output: program continues on easy
        if answer == "1" or answer == "one":
            game_mechanics_easy()

        # If they say 2, output: program continues on medium
        elif answer == "2" or answer == "two":
            game_mechanics_medium()

        # If they say 3, output: program continues on hard
        elif answer == "3" or answer == "three":
            game_mechanics_hard()

        # otherwise, show error
        else:
            print("Please answer 1, 2, or 3")


# Easy quiz function
def game_mechanics_easy():
    questions_nums = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]
    question_values = ["f", "t", "t", "f", "t", "f", "t", "f", "f", "t"]
    questions_text = [("Toru means one in Maori"),
                      "Whitu is number seven",
                      "Tekau is ten",
                      "Tahi is number three",
                      "Rima is five",
                      "Kore is nine",
                      "Ono is six",
                      "Waru is two",
                      "Rua is eight",
                      "Iwa is nine"]
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
                    print("You got it right, Great Job!")
                    score += 1
                    total_questions += 1
                    quiz_loop_breaker = "y"

                elif answer_storer != question_values[questions_printer]:
                    print("You got it wrong, Unlucky!")
                    total_questions += 1
                    quiz_loop_breaker = "y"

            else:
                print("please enter a valid input, (t or f)")
                quiz_loop_breaker = "y"
    print(formatter("!", "Well Done"))
    print(f"You got {score} out of {total_questions}!")
    looping()


# Medium quiz function
def game_mechanics_medium():
    questions_nums = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
    question_values = ["t", "t", "f", "f", "t", "t", "f", "f"]
    questions_text = ["There are two different Maori names for each day of the week",
                      "Rahina is one name for Monday",
                      "Ratu is a name for Wednesday",
                      "Raapa is a name for Monday",
                      "Rapare is the name for Thursday",
                      "Ramere is the name for Friday",
                      "Rahoroi is the name for Sunday",
                      "Ratapu is the name for Saturday", ]

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

    print(formatter("!", "Well Done"))
    print(f"You got {score} out of {total_questions}")
    looping()


# Hard quiz function
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
    print(formatter("!", "Well Done"))
    print(f"You got {score} out of {total_questions}")
    looping()


# Function to make the game a playable loop
def looping():
    finish_game = ""
    print()
    print("Do you want to do a Te Reo quiz?")
    print()
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


# Main routine goes here
print(formatter("-", "Welcome to the Te Reo quiz"))
print()

# Checks whether the user needs instructions
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# Main
looping()
