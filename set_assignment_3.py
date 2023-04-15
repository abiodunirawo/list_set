# Python program to remove duplicate amounts & print sum of amounts minus 7% vat

def remove_duplicates_and_print_sum_vat(amount):
    unique_amount = list(set(amount))
    total_sum = sum(unique_amount)
    vat = int(total_sum * 0.07)
    grand_total = total_sum - vat
    print("Original list: ", amount)
    print("Unique list: ", unique_amount)
    print("Total sum is: ", total_sum)
    print("VAT is: ", vat)

    return grand_total 


# Function test
my_amount = [29.50, 25.00, 25.00, 50.00, 60.00, 40.00, 40.00, 5.50]

result = remove_duplicates_and_print_sum_vat(my_amount)

print("Sum of amounts after vat: ", result)