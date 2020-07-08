import requests
import json
import pprint
import random
import html


score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1"
endGame = ""

while endGame != "quit":
    r = requests.get(url)
    if(r.status_code != 200):
        endGame = print("Sorry, press enter to try again and type quit: ").lower()
    else:
        vaild_answer = False
        answer_number = 1
        data = json.loads(r.text)
        question = data["results"][0]["question"]
        answers = data["results"][0]["incorrect_answers"]
        correct_answer = data["results"][0]["correct_answer"]
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "-" + html.unescape(answer))
            answer_number += 1

        while vaild_answer == False:
            user_answer = input("\n Guess the correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid answer.")
                else:
                    valid_answer = True
            except:
                print("Invalid answer. Please use numbers Only.")

        
        user_answer = answers[int(user_answer) - 1]

        if user_answer == correct_answer:
            print("Correct answer! " + html.unescape(correct_answer) + " is correct answer.")
            score_correct += 1
        else:
            print("Wrong asnwer!" + html.unescape(user_answer) + " is incorrect, correct answer is " + html.unescape(correct_answer))
            score_incorrect += 1

        print("\n##############################################")
        print("\nYour Score")
        print("\nCorrect answers: " + str(score_correct))
        print("\nIncorrect answers: " + str(score_incorrect))
        print("\n##############################################")

        endGame = input("\n Press enter to play again or type quit to stop the play a game: ").lower()

print("\nThanks for Playing!")
