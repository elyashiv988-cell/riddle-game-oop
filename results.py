
class QuestionResult:
    def __init__(
            self,
            riddle_id: int,
            riddle_type: str,
            category: str,
            time_taken: float
            ):
        self.riddle_id=riddle_id
        self.riddle_type=riddle_type
        self.category=category
        self.time_taken=time_taken


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

    def get_total_time(self):

        return round(sum(result.time_taken for result in self.question_results),2)
    
    def average_time_by_type(self):
        totals = {}
        counts = {}

        for res in self.question_results:
            
            totals[res.riddle_type] = totals.get(res.riddle_type, 0.0) + res.time_taken
            counts[res.riddle_type] = counts.get(res.riddle_type, 0) + 1

        return {
            r_type: round(totals[r_type] / counts[r_type], 2) for r_type in totals
        }

        
            
    def average_time_by_category(self):
        average_category={"Math":0,"English":0,"Geography":0,"Science":0,"History":0}
        for result in self.question_results:

            if result.category=="math":
                average_category["Math"]+=result.time_taken

            elif result.category=="english":
                average_category["English"]+=result.time_taken

            elif result.category=="geography":
                average_category["Geography"]+=result.time_taken

            elif result.category=="science":
                average_category["Science"]+=result.time_taken

            elif result.category=="history":
                average_category["History"]+=result.time_taken

        for key in average_category:

            average_category[key]=f"{average_category[key]:.2f}"
                
        return average_category

    def to_csv_row(self):
        pass

        
