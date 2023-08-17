class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    
        def days_count(string):
            days = [31,28,31,30,31,30,31,31,30,31,30,31]
            month, day = string.split("-")
            return sum(days[:int(month)-1]) + int(day)

        end_date = days_count(min(leaveAlice, leaveBob))
        start_date = days_count(max(arriveAlice, arriveBob))

        return int(start_date <= end_date)*( end_date - start_date + 1)
