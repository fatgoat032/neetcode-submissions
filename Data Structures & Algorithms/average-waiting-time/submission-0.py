class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chief_free = 0
        l = []
        k = len(customers)
        for i in range(k):
            arrival = customers[i][0]
            prep_time = customers[i][1]
            start = max(chief_free, arrival)
            finish = start + prep_time
            waiting = finish - arrival
            l.append(waiting)
            chief_free = finish
        return sum(l) / len(l)



        