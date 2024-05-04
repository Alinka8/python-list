# task 1 part 1: Sort the grades in descending order and display the sorted list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print("Sorted grades in descending order:", grades)
print(grades)
# task 1 part 2: Calculate the average grade and display it.
count=sum(grades)/len(grades)
print("Average grade: ", count)
# task 1 part 3: Replace any grade below 80 with the value Failed.
for i in range(len(grades)):
   if grades[i]<80:
      grades[i] = "Failed"
print("Updated grades: ", grades)
