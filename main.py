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
my_numbers = [1,2,3,4]
out_comes = map(lambda element : element+1, my_numbers)
list(out_comes)
# How to do power to a lists :

my_specific_number=[20,30,97]
my_power_lists = [25,30,20]
list(map(pow,my_specific_number,my_power_lists))
""" When you try to add both lists and do the power operation"""
def add_tovg(x,y):
    return x+y
list(map(add_tovg, my_specific_number,my_power_lists) )
# Using lambda expression:
list(map(lambda x,y:x+y, my_specific_number, my_power_lists ))
"""Use the map function to create a list that contains the number of occurrences of the letter n in each element in the provided list.
Store the output in a variable called mapped_list
Hints:
You should use map , lambda , count , and list
We implemented the code before for the occurrences in the poem exercise if you remember."""
input_list = ['What we think, we become.', 'Every moment is a fresh beginning.', 'Change the world by being yourself.',
              'Hate comes from intimidation, love comes from appreciation',
              'If I’m gonna tell a real story, I’m gonna start with my name.',
              'Oh, the things you can find, if you don’t stay behind.']
mapped_list = list(map(lambda x: x.count("n"), input_list))
