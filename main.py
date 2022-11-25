# Map function:
def add_seven(my_number):
    out_come = []
    for numbers in my_number:
        numbers += 7
        out_come.append(numbers)
    return out_come

my_number=[500, 100, 3000, 20000]
add_seven(my_number)

def add_seven_map(element):
    return element + 7
output_list= map(add_seven_map, my_number)
print(output_list)
type(output_list)
list(output_list)
# Using lambda function :
"""output=map(lambda input: what we want to return from the function, where we want to apply
the lambda function on its called iterable or list )"""
my_numbers= [1,2,3,4]
out_comes=map(lamda element+1: my_numbers)
list(out_comes)