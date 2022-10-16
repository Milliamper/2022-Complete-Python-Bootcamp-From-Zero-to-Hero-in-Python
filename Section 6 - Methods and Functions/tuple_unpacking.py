stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT",100)]

for a,b in stock_prices:
    print(a,b)


#############################################################

work_hours=[("Abby",100), ("Billy", 400), ("Cassie", 800)]

# return the employee of the month

def check_employee(mylist):

    current_max = 0
    best_employee = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            best_employee = employee

    print(f"The best employee is {best_employee} with {current_max} work hours")

check_employee(work_hours)
