n=int(input("Enter number of integers:"))
print("enter integers")
arr=list(map(int,input().split()))
print(arr)
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
print("sum",sum)