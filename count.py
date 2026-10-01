n=int(input("Enter number of integers:"))
print("enter integers")
arr=list(map(int,input().split()))
print(arr)
minimum=arr[0]
maximum=arr[0]
smax=0
smin=0
for i in range(n):
    if maximum<arr[i]:
        smax=max
        maximum=arr[i]
       
    elif(arr[i]>smax and smax!=arr[i]):
        smax=arr[i]
    
    if(minimum>arr[i]):
        smin=min
        minimum=arr[i]
        
    elif(arr[i]>smin and smin!=arr[i]):
        smin=arr[i]
    
    
print(maximum)
print(minimum)
print(smax)
print(smin)