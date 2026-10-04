s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in s:

    # Check alphabet
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):

        # Check vowel
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
           ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':

            vowels += 1

        else:
            consonants += 1

    # Check digit
    elif ch >= '0' and ch <= '9':
        digits += 1

    # Everything else
    else:
        special += 1


print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Special characters =", special)