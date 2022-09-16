stock_prices = [("Apple", 200), ("Google", 400), ("Microsoft", 100)]

for item in stock_prices:
    print(item)

# tuple unpacking
for name, price in stock_prices:
    print(name)

##################################################

work_hours = [("Aby", 100), ("Billy", 4000), ("Cassy", 800)]


def employee_check(work_hours):

    current_max = 0
    employee_of_month = ""

    for name, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = name
        else:
            pass

    return (employee_of_month, current_max)


result = employee_check(work_hours)
name, hours = employee_check(work_hours)

print("Employee of the month : ", name)
