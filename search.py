n=int(input("Enter number of integers:"))
print("enter integers")
arr=list(map(int,input().split()))
print(arr)
flag=0
b=int(input("enter number to search"))
for i in range(n):
    if arr[i]==b:
       flag=1       
if flag==1:
    print(b,"Is the element present in the array")
else:
    print(b,"Is not found in the array")