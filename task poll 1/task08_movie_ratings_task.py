"""
Task 8 — Movie Ratings Dashboard 📊

Requirements:
  - ratings = [4, 5, 3, 2, 5, 4, 5, 3, 4]
  - Use a loop to compute:
      * Average rating (1 decimal)
      * Count of 5-star reviews
  - Print both results on separate lines

Practice: loop aggregation, counting, formatting

OUTPUT EXAMPLE
--------------
Average rating: 3.9
Number of 5-star reviews: 3
"""

ratings = [4, 5, 3, 2, 5, 4, 5, 3, 4]
print("(Starter) Ratings:", ratings)
# TODO: compute average and number of 5-star reviews using loops only
counter = 0
average = 0
perfect_reviews_counter = 0
for i in ratings:
    counter = counter + 1
    average = average + i
    if i == 5:
        perfect_reviews_counter = perfect_reviews_counter + 1

print(f"Average rating: {round(average/counter)}\nNumber of 5-star reviews: {perfect_reviews_counter}")