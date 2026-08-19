from riddles import *
import json

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
        raw_data=[]
        for riddle in riddles:
            raw_data.append(riddle.to_dict())
        with open(self.file_path,"w") as file:
            json.dump(raw_data,file,indent=4)

    def add_riddle(self,riddle:Riddle):
        riddle.id=input("enter ID riddle: ").strip()
        riddle.question=input("enter question riddle: ").strip()
        riddle.correct_answer=input("enter correct_answer riddle: ").strip()
        riddle.get_type=input("enter type riddle: ").strip()
        riddle.possible_answers=input("enter possible_answers riddle: (set , beetwine each) ").split(",")
        riddle.difficulty=input("enter difficulty riddle: ").strip()
        riddle.category=input("enter category riddle: ").strip()
        self.get_all_riddles().apeend(riddle)
        self.save_riddles(self.get_all_riddles())
        
    def get_all_riddles(self):
        return self.load_riddles()

    def get_riddle_by_id(self, riddle_id: int):
        pass

    def update_riddle(self, riddle_id: int, new_data: dict):
        pass

    def delete_riddle(self, riddle_id: int):
        pass


            

