def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print('Correct!')
        return 1
    else:
        print("Incorrect!")
        return 0

# Questions and answers stored in a dictionary
questions_answers = {
    "What does CPU stand for?": "central processing unit",
    "What does GPU stand for?": "graphics processing unit",
    "What does RAM stand for?": "random access memory",
    "What does PSU stand for?": "power supply unit",
}

print("Welcome to my computer quiz!")

# Initial check if the player wants to play
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Loop through the questions and answers
for question, answer in questions_answers.items():
    score += ask_question(question, answer)

total_questions = len(questions_answers)
print(f"You got {score} questions correct out of {total_questions}!")
print(f"You got {(score / total_questions) * 100:.2f}%.")
