n=int(input("Enter number of integers:"))
print("enter integers")
arr=list(map(int,input().split()))
print(arr)
flag=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]!=arr[j]:
            print(arr[j])
