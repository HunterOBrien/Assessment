"""  game mechanics v1
Creating functions that hold information about the quizzes

"""
import random

months_questions = [("Kohitatea is January", True),
                    ("Hui-tangaru is March", False),
                    ("Poutu-te-rangi is September", False),
                    ("Paenga-whawha is December", False),
                    ("Haratua is May", True),
                    ("Pipiri is June", True),
                    ("Hongongoi is July", True),
                    ("Here-turi-koka is November", False),
                    ("Maharu is March", False),
                    ("Whiringa-a-nuku is October", True),
                    ("Whiringa-a-rangi is November", True),
                    ("Hakihea is January", False)]

days_questions = [("There are two different Maori names for each day of the week", True),
                  ("Rahina is one name for Monday", True),
                  ("Ratu is a name for Wednesday", False),
                  ("Raapa is a name for Monday", False),
                  ("Rapare is the name for Thursday", True),
                  ("Ramere is the name for Friday", True),
                  ("Rahoroi is the name for Sunday", False),
                  ("Ratapu is the name for Saturday", False)]

numbers_questions = ["Toru means one in Maori",
                     "Whitu is number seven",
                     "Tekau is ten",
                     "Tahi is number three",
                     "Rima is five",
                     "Kore is nine",
                     "Ono is six",
                     "Waru is two",
                     "Rua is eight",
                     "Iwa is nine"]





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



if difficulty == 1:
    print(numbers_questions)
elif difficulty == 2:
    days_questions
elif difficulty == 3:
    months_questions
