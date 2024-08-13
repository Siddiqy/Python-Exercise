start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start < end:
    for i in range(start, end+1):
        print(i)
else:
    for j in range(start+1, end, -1):
        print(j-1)
