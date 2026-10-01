n=int(input("Enter number of integers:"))
print("enter integers")
arr=list(map(int,input().split()))
print(arr)
count=0
even=0
for i in range(n):
    if arr[i]%2!=0:
        count=count+1
   
    elif arr[i]%2==0:
        even=even+1
        print(even)
print(count)
print(even)