# Calculate average score of a student
def calc_average(marks):
    total = 0  # Initialize total to 0
    for m in marks:
        total += m  # Add each mark to total
    average = total / len(marks)  # Calculate average
    return average  # Return the computed average

marks = [85, 90, 78, 92]  # List of marks
print("Average Score is", calc_average(marks))  # Print the average score