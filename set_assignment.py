#  Python program to remove duplicates & print sum of numbers in a list

def remove_duplicates_and_print_sum(numbers):
    unique_numbers = list(set(numbers))
    total_sum = sum(unique_numbers)
    print("Original list: ", numbers)
    print("Unique list: ", unique_numbers)

    return total_sum 


# Function test
my_list = [5, 5, 2, 2, 6, 7,8]

result = remove_duplicates_and_print_sum(my_list)

print("Sum of unique elements: ", result)