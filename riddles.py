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
        if str(user_ans.lower())==str(self.correct_answer.lower()):
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
        self.__possible_answers=list(possible_answers)

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
    def __init__(self, id, question, correct_answer, difficulty, category):
        super().__init__(id, question, correct_answer, difficulty, category)
    def display(self):
        print(f"Question: {self.question}")

    def get_type(self):
        return "open"
