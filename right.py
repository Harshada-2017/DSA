n=int(input("enter the numbers rows you want"))

for i in range(n):
    for j in range(i+1):
        print(chr(65 +i),end="")
    print()