# Python program to get the largest and smallest number in a list

def largest_and_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest


# List of 15 numbers
numbers = [11, 45, 67, 23, 72, 34, 56, 88, 95, 9, 2, 10, 3, 81, 19]

# Get the largest and smallest number
largest, smallest = largest_and_smallest(numbers)

# Print the result
print("Largest number: ", largest)
print("Smallest number: ", smallest)