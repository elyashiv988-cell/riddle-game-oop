from results import *
from riddles import *
import time
class RiddleGame:
    def __init__(self,
                player, 
                riddles: list[Riddle], 
                results: list[QuestionResult]
                ):
        self.player=player
        self.riddles=riddles
        self.results=results

    def start(self):
        print(f"Wellcome {self.player.get_username()}")
        for riddle in self.riddles:
        
            self.results.append(self.ask_riddle(riddle))
       
        return GameResult(self.player.get_username(), "date", 0, self.results)

    def ask_riddle(self,riddle: Riddle):

        riddle.display()
        start_time=time.time()
        while True:
            answer=input("Enter your answer: ")
            if riddle.check_answer(answer):
                print("Correct answer!")
                end_time=time.time()
                taken_time=end_time-start_time
                return QuestionResult(riddle.to_dict()["id"],riddle.get_type(),riddle.to_dict()["category"],time_taken=taken_time)
            else:
                print("Incorrect! try agein. ")       
        
      

    def print_summary(self,result):
        print(f"Player: {self.player.get_username()}\nTotal riddle: {result.get_total_riddles()}\nTotal time: {result.get_total_time()}")
        print("Average time by type:")
        for key in result.average_time_by_type():
            print(f"{key}: {result.average_time_by_type()[key]}")
        print("Average time by category:")
        for key in result.average_time_by_category():
            print(f"{key}: {result.average_time_by_category()[key]}")
