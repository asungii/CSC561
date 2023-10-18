def adjust_numbers(number):
    if number > 10:
        return number + 5
    elif number == 1:
        return number * 2
    else:
        return number - 3
    
def is_large_number(number):
    return number > 10

number_list = [5, 10, 15, 3]
adjusted_list = []
large_number_flags = []

for num in number_list:
    adjusted_list.append(adjust_numbers(num))
    large_number_flags.append(is_large_number(num))

print("Adjusted List:", adjusted_list)
print("Large Number Flags:", large_number_flags)