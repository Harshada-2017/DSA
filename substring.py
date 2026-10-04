s = input("Enter the main string: ")
sub = input("Enter the substring: ")

count = 0
i = 0


n = 0
for ch in s:
    n += 1


m = 0
for ch in sub:
    m += 1


while i <= n - m:

    match = True
    j = 0

    while j < m:

        if s[i + j] != sub[j]:
            match = False
            break

        j += 1

    if match:
        count += 1

    i += 1


print("Occurrences =", count)