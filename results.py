
class QuestionResult:
    def __init__(self,
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
        
        sums={}
        counts={}

        for res in self.question_results:
            q_type=res.riddle_type
            time_taken=res.time_taken

            if q_type not in sums:
                sums[q_type] = 0.0
                counts[q_type] = 0

            sums[q_type] += time_taken
            counts[q_type] += 1

        averge={}
        for q_type in sums:
            avg=sums[q_type]/counts[q_type]
            averge[q_type]=round(avg,2)

        return averge
            
    def average_time_by_category(self):
        sums={}
        counts={}

        for res in self.question_results:
            q_category=res.category
            time_taken=res.time_taken

            if q_category not in sums:
                sums[q_category] = 0
                counts[q_category] = 0

            sums[q_category] += time_taken
            counts[q_category] += 1

        averge={}
        for q_category in sums:
            avg=sums[q_category]/counts[q_category]
            averge[q_category]=round(avg,2)

        return averge
            
    def to_csv_row(self):
        pass

        
