class Riddle:
    def __init__(self,
                id,
                question,
                correct_answer,
                difficulty,
                category
                ):
        if isinstance(id,int):
            self.__id=id
        if isinstance(question,str):
            self.__question=question
        if isinstance(correct_answer,str):
            self.__correct_answer=correct_answer
        if isinstance(difficulty,str):
            self.__difficulty=difficulty
        if isinstance(category,str):
            self.__category=category

    @property
    def id(self) -> int:
        return self.__id
    @property
    def question(self) -> str:
        return self.__question
    @property
    def correct_answer(self) -> str:
        return self.__correct_answer
    @property
    def difficulty(self) -> str:
        return self.__difficulty
    @property
    def category(self) -> str:
        return self.__category

    def display(self):
        raise NotImplementedError

    def check_answer(self, user_ans):
        if str(user_ans.lower())==str(self.correct_answer):
            return True

    def get_type(self):
        raise NotImplementedError

    def to_dict(self):
        riddle={}
        riddle["id"]=self.id
        riddle["question"]=self.question
        riddle["correct_answer"]=self.correct_answer
        riddle["difficulty"]=self.difficulty
        riddle["category"]=self.category
        return riddle


class MultipleChoiceRiddle(Riddle):
    def __init__(self, id, question, correct_answer, difficulty, category,possible_answers):
        super().__init__(id, question, correct_answer, difficulty, category)
        self.__possible_answers=possible_answers

    @property
    def possible_answers(self):
        return self.__possible_answers

    def display(self):
        print(f"Qusetion: {self.question}\nAnswers: {self.possible_answers}")
    
    def get_possible_answers(self):
        return list(self.possible_answers)


class FourAnswerRiddle(MultipleChoiceRiddle):
    def __init__(self, id, question, correct_answer, difficulty, category, possible_answers):
        super().__init__(id, question, correct_answer, difficulty, category, possible_answers)
    
    def get_type(self):
        return "multiple_4"


class TwoAnswerRiddle(MultipleChoiceRiddle):
    def __init__(self, id, question, correct_answer, difficulty, category, possible_answers):
        super().__init__(id, question, correct_answer, difficulty, category, possible_answers)

    def get_type(self):
        return "multiple_2"


class OpenRiddle(Riddle):
    def __init__(self, riddle):
        super().__init__(riddle)

    def display(self):
        print(f"Question: {self.question}")

    def get_type(self):
        return "open"

class Player:
    def __init__(self, username:str):
        self.__username=username

    @property
    def username(self):
        return self.__username

    def get_username(self):
        return self.__username

    def rename(self, new_username):
        if len(new_username.strip())>2:
            self.__username=new_username


class QuestionResult:
    def __init__(
            self,
            riddle_id: int,
            riddle_type: str,
            category: str,
            time_taken: float
            ):
        self.__riddle_id=riddle_id
        self.__riddle_type=riddle_type
        self.__category=category
        self.__time_taken=time_taken


class GameResult:
    def __init__(self,
            username: str,
            date: str,
            total_time: float,
            question_results: list[QuestionResult]                
            ):
        self.__username=username
        self.__date=date
        self.__total_time=total_time
        self.question_results=question_results

    def get_total_riddles(self):
        return len(self.question_results)

    def average_time_by_type(self):
        pass

    def average_time_by_category(self):
        pass

    def to_csv_row(self):
        pass

class RiddleGame:
    def __init__(self,
                player: Player, 
                riddles: list[Riddle], 
                results: list[QuestionResult]
                ):
        self.player=player
        self.riddles=riddles
        self.results=results

    def strat(self):
        print(self.player.get_username())
        for riddle in self.riddles:
            self.ask_riddle(riddle)
            self.results.append(QuestionResult(riddle.id,riddle.get_type(),riddle.category,1))

    def ask_riddle(self,riddle: Riddle):

        if riddle["type"]=="multiple_4":
                        
            corrent_riddle=FourAnswerRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["difficulty"],riddle["category"],4)
        elif riddle["type"]=="multipl_2":
            corrent_riddle=TwoAnswerRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["difficulty"],riddle["category"],2)
        elif riddle["type"]=="open":
            corrent_riddle=OpenRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["difficulty"],riddle["category"])
            
        corrent_riddle.display()
        while True:
            if corrent_riddle.check_answer():
                print("Correct answer!")
                break
            else:
                print("Incorrect! try agein. ")       


    def print_summary(self, result: GameResult):
        print(self.results.get_total())


riddles= [
  {
    "id": 1,
    "question": "What is 5 + 7?",
    "correct_answer": "12",
    "type": "multiple_4",
    "possible_answers": ["10", "11", "12", "13"],
    "difficulty": "easy",
    "category": "math"
  },
  {
    "id": 2,
    "question": "What is the capital of France?",
    "correct_answer": "Paris",
    "type": "open",
    "possible_answers": [],
    "difficulty": "easy",
    "category": "geography"
  }
]


game=RiddleGame(Player("eli"),riddles,[])
game.strat()