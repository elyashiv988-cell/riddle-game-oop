from riddles import *

class RiddleRepository:
    def __init__(self,file_path:str):
        self.file_path=file_path

    def load_riddles(self):

        riddles = []
        for item in self.file_path:

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


    def save_riddles(self,riddles:list[Riddle]):
        pass

