"""  game mechanics v1
Creating a playable quiz that gives the users score

"""

questions_nums = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]

# Determines whether a question is true or false
question_values = ["f", "t", "t", "f", "t", "f", "t", "f", "f", "t"]
# Quiz questions
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
# Stores the last answer
answer_storer = ""
# Works out how many the player got right
score = int(0)
# Works out total question amount
total_questions = int(0)
# variable to break the quiz while loop
quiz_loop_breaker = ""

# For loop that does the actual quiz function
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
# Tells the user their final score
print(f"You got {score} out of {total_questions}")
