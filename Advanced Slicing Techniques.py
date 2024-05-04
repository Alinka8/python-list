# Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures=temperatures[7:14]
print("Second week of tempretures ", second_week_temperatures)

# Task 2: Extract all the temperatures above 100.
for i in range (len (temperatures)):
   if temperatures[i]>100:
      print(temperatures[i])


# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures.reverse()
particular_temperatures=temperatures[5:10]
print("Reversed tempreture: ", temperatures)
print("Particular tempreture: ", particular_temperatures)

