#While loop
#while 1 < 2:
    #print('something')

count = 1
while count <= 4:
    print("looping")
    count += 1
  
  
  
    
#FOR LOOP
#Iterating a list
colors = ['blue','purple','green']
for color in colors:
    print('This color is ' + color)

#Iterating a tuple
#Works similar to a list
point = (1,2,3)
for pnt in point:
    print(pnt)



#Iterating dictionaries
ages = {'kevin' : 59, 'bob' : 40, 'kayla' : 21}
for key in ages:
    print(key)
    
for key, value in ages.items():
    print(key,value)

#NESTING LOOPS AND CONDITIONS
counter = 1
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1




#Controlling loop execution
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We are counting odd numbers: {count}")
    count += 1


count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We are counting odd nubmer: {count}")
    count += 1


colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)





    

