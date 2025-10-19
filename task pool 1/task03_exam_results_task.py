"""
Task 3 — Class Exam Results 📊

Requirements:
  - grades = [45, 72, 88, 91, 60, 55]
  - Compute average using a loop (avoid sum())
  - Gather grades strictly above the average into a new list
  - Print the average and the list

Practice: loop aggregation, conditional filtering

OUTPUT EXAMPLE
--------------
Average: 68.50
Above average: [72, 88, 91]
"""
grades = [45, 72, 88, 91, 60, 55]
print("(Starter) Grades:", grades)
# TODO: compute average via a loop (no sum())
grades_sum = 0
for i in grades:
    grades_sum = grades_sum+i
average = grades_sum/len(grades)
# TODO: build a list of grades > average
more_then_average = []
for i in grades:
    if i > average:
        more_then_average.append(i)
# TODO: print both
print(average, more_then_average)
