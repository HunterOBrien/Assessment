"""  game mechanics v1
Creating functions that hold information about the quizzes

"""


def quizzes(question_text):
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
    questions_nums = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]
    current_question = questions_nums[0]
    while True:

        # Ask the user what difficulty they want
        answer = input(question_text).lower()

        # If they say 1, output: program continues on easy
        if answer == "1" or answer == "one":
            answer = "1"

            while current_question != "t" or "true" or "f" or "false":

                print(questions_text[0])
                question = input().lower()
                if question == "t" or question == "true":
                    print("You got it right!")

                elif question == "f" or "false":
                    print("unfortunate, that's incorrect!")
                else:
                    print("Please enter either True or False")


# Gets the difficulty the user wants and runs the quiz
quizzes("What difficulty do you want to play?\n"
        "1 for easy, 2 for medium, 3 for hard: ")
