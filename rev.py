n=int(input("Enter number of integers:"))
print("enter integers")
arr=list(map(int,input().split()))
print(arr)
for i in range(n-1,-1,-1):
    print(arr[i], end="")