meeting_target = 0
below_target = 0
total_sales = 0
number_of_items = int(input("Enter number of items : "))

for i in range(number_of_items):
    sales = int(input(f"Enter sales for item {i + 1}: "))
    total_sales += sales

    if sales >= 500:
        meeting_target += 1
    else:
        below_target += 1


def calculate_average(total_sales, number_of_items):
    average = total_sales / number_of_items
    return average

print("CANTEEN SALES REPORT")
print(f"Average sales: {calculate_average(total_sales, number_of_items)}")
print(f"Meeting target: {meeting_target}")
print(f"Below target: {below_target}")