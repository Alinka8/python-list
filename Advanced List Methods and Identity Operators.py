# task 2 part 2: Check if the two lists are identical in terms of their content, regardless of order.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

identical = submitted == attended
print(identical)

# task 3 part 3:  Using list methods, remove any student from the attended list who did not submit their assignment.
attended.remove("Eve")
attended.remove("Frank")
print("They didn't submit their assignments", attended)