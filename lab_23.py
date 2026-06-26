# Greedy Algorithm - Activity Selection Problem

def activity_selection(start, finish):
   n = len(finish)

   print("Selected Activities:")
   i = 0
   print(i, end=" ")

   for j in range(1, n):
       if start[j] >= finish[i]:
           print(j, end=" ")
           i = j


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

activity_selection(start, finish)