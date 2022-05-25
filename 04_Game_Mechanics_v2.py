""" Game_Mechanics v2
    Turns the playable quiz into a callable function

"""


# Game Mechanic function
def game_mechanics():
    # Information about the quiz
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
    # Works out the last previous answer that is then checked by the question value list
    answer_storer = ""
    # Works out score and total number of questions in the quiz
    score = int(0)
    total_questions = int(0)
    # breaks the while loop
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
# Prints final score
    print(f"You got {score} out of {total_questions}")


# Calls the game mechanics function
game_mechanics()
