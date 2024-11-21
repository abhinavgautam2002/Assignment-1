import json

def load_quiz_data():
    with open('quiz_data.json', 'r') as file:
        return json.load(file)

def save_user_results(user_responses, score):
    result_data = {
        "score": score,
        "responses": user_responses
    }
    with open('user_results.json', 'w') as file:
        json.dump(result_data, file, indent=4)

def run_quiz():
    quiz_data = load_quiz_data()
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
    
    save_user_results(user_answers, score)

run_quiz()
