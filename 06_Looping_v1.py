""" Looping v1
This turns the quizzes into a re-playable loop
"""


# works out what difficulty the user wants
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
    # Stores quiz values
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
    # Stores the previous answer and checks it against the question_values list
    answer_storer = ""
    # Keeps track of your score and the amount of questions
    score = int(0)
    total_questions = int(0)
    # Breaks the quiz loop
    quiz_loop_breaker = ""

    # For loop that does the quiz with the given variables
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
    # Prints the users final score
    print(f"You got {score} out of {total_questions}")


# Medium quiz function
# Check game_mechanics_easy for comments in the function
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
    print(f"You got {score} out of {total_questions}")


# Hard quiz function
# Check game_mechanics_easy for comments in the function
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
    print(f"You got {score} out of {total_questions}")
    looping()

def looping():
    print("Thanks for playing, would you like to play again?")
    play_again = input("If you want to play again enter 'Y'\n"
                       "If you do not want to play again enter 'N'\n "
                       ":  ").upper()

    while True:
        if play_again == "Y" or play_again == "YES":
            difficulty_selection()

        elif play_again == "N" or play_again == "NO":
            difficulty_selection()
        else:
            print("Please enter a valid input")


# Gets the difficulty the user wants
difficulty_selection("What difficulty do you want to play?\n"
                     "1 for easy, 2 for medium, 3 for hard: ")
