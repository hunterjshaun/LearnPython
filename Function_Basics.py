# DEFINING FUNCTIONS
# We can define a function by using 'def' and the function name, normally suing lowercase letters
# - After we define the name we can include zero or parameters.
# - When we define a parameter its going to be a variable that exist inside the body of the function.
def print_name(name):
    print(f"Name is {name}")
print_name('josh')
#>>> will print: Name is josh

#If you want to call a funtion and have that value saved to a variable you need to use the return statement
def add_two(num):
    return num + 2
    
result = add_two(2)
print(result)
#>>> will print: 4
def add(num1, num2):
    return num1 + num2
seven = add(1, 6)
print(seven)
#>>> will print: 7



#PARAMETERS VS ARGUMENTS
def contact_card(name, age, car_model): #Here we are defining parameters
    return f"{name} is {age} and drives a {car_model}"
print(contact_card('keith', 29, 'honda civic')) #these are the positional arguments we passed into the function

#arguments can also be done out of order using 'Keyword arguments'
print(contact_card(name='Josh', age=31, car_model='kia'))
#You can use all Positional arguments, all keyword arguments, or use positonal agurments first then use keyword arguments


