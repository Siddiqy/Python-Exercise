num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Substraction")

ans = "y"

while ans == 'y' or ans == 'Y':
    math = int(input("Choice?: "))
    if math == 1:
        result = num1 + num2
    elif math == 2:
        result = num1 * num2
    elif math == 3:
        result = num1 / num2
    else:
        result = num1 - num2
    print(f"Result: {result}")
    ans = input("Do you want to continue?: ")

