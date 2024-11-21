quiz_data = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "In which year did World War II end?", "answer": "1945"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "Which element has the chemical symbol O?", "answer": "Oxygen"}
]

def run_quiz():
    score = 0
    user_answers = []
    
    print("Welcome to the Quiz App!\n")
    
    for i, question_data in enumerate(quiz_data):
        print(f"Question {i+1}: {question_data['question']}")
        user_answer = input("Your answer: ").strip()
        user_answers.append(user_answer)
        
        if user_answer.lower() == question_data['answer'].lower():
            score += 1
    
    print("\nQuiz Finished!")
    print(f"Your score: {score} out of {len(quiz_data)}")
    
    print("\nYour Answers:")
    for i, answer in enumerate(user_answers):
        correct = "Correct" if answer.lower() == quiz_data[i]['answer'].lower() else "Incorrect"
        print(f"Question {i+1}: {answer} ({correct})")

run_quiz()
