# Map function:
def add_seven(my_number):
    out_come = []
    for numbers in my_number:
        numbers += 7
        out_come.append(numbers)
    return out_come

my_number=[500, 100, 3000, 20000]
add_seven(my_number)

def add_seven_map(i):
    return element+7
output_list= map(add_seven_map,i)
print(output_list)