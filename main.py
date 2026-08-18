from game import*
from player import*
import json

def load_riddles_from_json():
    with open("data.json", "r") as file:
        raw_data = json.load(file)

    riddles = []
    for item in raw_data:

        if item["type"] == "multiple_4":
            riddle = FourAnswerRiddle(
                id=item["id"],
                question=item["question"],
                correct_answer=item["correct_answer"],
                possible_answers=item["possible_answers"],
                difficulty=item["difficulty"],
                category=item["category"],
            )
        elif item["type"] == "multiple_2":
            riddle = TwoAnswerRiddle(
                id=item["id"],
                question=item["question"],
                correct_answer=item["correct_answer"],
                possible_answers=item["possible_answers"],
                difficulty=item["difficulty"],
                category=item["category"],
            )
        elif item["type"] == "open":
            riddle = OpenRiddle(
                id=item["id"],
                question=item["question"],
                correct_answer=item["correct_answer"],
                difficulty=item["difficulty"],
                category=item["category"],
            )
        riddles.append(riddle)
    return riddles


game=RiddleGame(Player(input("Enter your name: ")),load_riddles_from_json(),[])
game.print_summary(game.start())

