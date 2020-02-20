#zadanie 3 zikl
students_scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"{sum(students_scores)}") 

scores_sum = 1

for scores in students_scores:
    scores_sum += scores 
    print(scores_sum)

print(f"{sum(students_scores)/len(students_scores)}") 
