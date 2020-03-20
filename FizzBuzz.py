new_list = []

for i in range (1, 101):
    if i%3 == 0 and i%5 == 0:
        new_list.append("FizzBuzz")
    elif i%3 == 0:
        new_list.append ("Fizz")
        
    elif i%5== 0:
        new_list.append ("Buzz")
    else:
        new_list.append (i)
        
print (new_list)

# print ('Marlene was here')
