"""  game mechanics v1
Creating functions that hold information about a quiz
and have a playable quiz function

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

questions_nums = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]
question_values_easy = ["f", "t", "t", "f", "t", "f", "t", "f", "f", "t"]
question_values = []
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
difficulty_check = difficulty


print(difficulty_check)
for questions_printer in range(len(questions_nums)):
    print(questions_nums[questions_printer])




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
