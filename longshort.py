s=input("Enter a sentence:")
word=""
longest=""
shortest=""
first=True

for ch in s:
    if ch!=" ":
        word=word+ch
    else:
        if word!="":

            # First word
            if first:
                longest = word
                shortest = word
                first = False

            else:

                # Find length of current word
                word_length = 0
                for x in word:
                    word_length += 1

                # Find length of longest
                longest_length = 0
                for x in longest:
                    longest_length += 1

                # Find length of shortest
                shortest_length = 0
                for x in shortest:
                    shortest_length += 1

                if word_length > longest_length:
                    longest = word

                if word_length < shortest_length:
                    shortest = word

            word = ""


# Check the last word
if word != "":

    if first:
        longest = word
        shortest = word

    else:

        word_length = 0
        for x in word:
            word_length += 1

        longest_length = 0
        for x in longest:
            longest_length += 1

        shortest_length = 0
        for x in shortest:
            shortest_length += 1

        if word_length > longest_length:
            longest = word

        if word_length < shortest_length:
            shortest = word


print("Longest word =", longest)
print("Shortest word =", shortest)
        