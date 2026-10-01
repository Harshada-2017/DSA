s=input("enter a string")
vowels=0
consonants=0
digits=0
special=0

for i in range(len(s)):
    ch=s[i]
    
    if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
        vowels=vowels+1
    elif(ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
        consonants=consonants+1
    elif (ch>='0' and ch<='9'):
        digits=digits+1
    else:
        special=special+1
    
print("vowels",vowels)
print("Digits",digits)
print("consonants",consonants) 
print("special",special)       
