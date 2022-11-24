# Map function:
def add_seven(my_number):
    outcome = []
    for numbers in my_number:
        numbers += 7
        outcome.append(numbers)
    return outcome


my_number = [500, 100, 3000, 20000]
add_seven(my_number)
