# The 'if' and 'else' Statements
# EXAMPLE
# if 'a' < 'b':
#    print('CONDITON was true')
#
#EXAMPLE
name = input('What is your name? ')
if len(name) >= 6:
    print('Your name is long')
elif len(name) == 5:
    print('You name is 5 characters')
elif len(name) >=4:
    print('Your name is 4 or more characters')
else:
    print('Your name is short')



# you can add 'pass' to act as a placeholder
name1 = 'Kevin'
if name1 == 'Kevin':
    print('Hello Kevin')
else:
    pass

number = int(input("Pick a number between 1 - 100 "))
if number % 5 == 0 and number % 3 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Fizz')
elif number % 3 == 0:
    print('Buzz')
else: 
    print(number)