select = 'y'
sum = 0

while select == 'y' or select == 'Y':
    num = int(input("Entar a number: "))
    select = input("Continue Y or N: ")
    sum = sum + num
print(f"Sum: {sum}")