s= input("Enter a sentence: ")

word = ""

for ch in s:

    if ch != " ":
        word = word + ch

    else:

        # Find length of word
        count = 0

        for x in word:
            count += 1

        # Start from last character
        i = count - 1

        while i >= 0:
            print(word[i], end="")
            i -= 1

        print(" ", end="")

        word = ""


# Reverse the last word
count = 0

for x in word:
    count += 1

i = count - 1

while i >= 0:
    print(word[i], end="")
    i -= 1