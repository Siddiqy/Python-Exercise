
import math

shape = input('Enter shape name: ')

def calculate_area(value):
    if value == 'rectangle':
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))
        return print("The rectangle area is = ", width * height)
    elif value == 'circle':
        redius = int(input('Enter redius: '))
        return print("The circle area is = ", math.pi * redius ** 2)
    else:
        print("Please type a valid shape name!")
        
calculate_area(shape)


