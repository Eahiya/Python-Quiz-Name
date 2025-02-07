import time

def quiz_game():
    print("\n                                                   Quiz Game \n ")
    name = input("Please Enter Your Name: ")
    print(f'Hello, {name}!')
    
    play = input("Do you want to play a computer quiz game? (yes/no): \n ").strip().lower()
    if play != "yes":
        print("Okay, maybe next time!")
        return
    
    print("\nOkay, let's play! 😊\n")
    score = 0
    
    questions = {
        "What is the cleanest country in the world?": ["switzerland"],
        "Who was the most highly paid UFC athlete in 2021?": ["conor mcgregor", "conor"],
        "When did the 1st World War start?": ["1914", "nineteen fourteen"],
        "Who was the founder and CEO of Amazon.com?": ["jeff bezos", "jeffrey bezos"],
        "What is the capital of the United States of America?": ["washington dc", "washington"],
        "Which country has the highest population?": ["china"],
        "How many countries are there in the world?": ["195", "one hundred ninety-five"],
        "Who was the first person to step on the moon?": ["neil armstrong"],
        "What is the study of weather called?": ["meteorology"],
        "Which is the biggest continent in the world?": ["asia"],
        "What is the coldest planet in our solar system?": ["neptune"],
        "Approximately how many kilometers does 1 degree of latitude represent?": ["111", "one hundred eleven"],
        "Who is the most viewed and liked person on the internet?": ["dwayne johnson", "the rock"],
        "What is the most expensive thing ever built, costing around $100 billion?": ["international space station", "iss"],
        "What is the tallest mountain in the world?": ["mount everest", "everest"],
        "Which planet was first discovered through a telescope by Herschel in 1781?": ["uranus"],
        "How many times can a person be elected as the President of the USA?": ["2", "two"],
        "What is the 10th largest state in the USA?": ["michigan"],
        "Where is Area 51 located in the USA?": ["nevada"],
        "What does GPU stand for?": ["graphics processing unit"]
    }
    
    for question, correct_answers in questions.items():
        answer = input(f"{question}\n ").strip().lower()
        if answer in correct_answers:
            print("Correct Answer! 🎉\n")
            score += 1
        else:
            print(f"Incorrect Answer! The correct answer is: {correct_answers[0].title()}\n")
        time.sleep(1)
    
    print(f"\nCongratulations, {name}! You got {score} out of {len(questions)} questions correct!")
    print(f"Your final score is {(score / len(questions)) * 100:.2f}%.")

if __name__ == "__main__":
    quiz_game()
