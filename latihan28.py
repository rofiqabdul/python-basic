alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

deret = int(input("deret: "))
for i in range(deret):
    print(alphabet_list[i].upper(), end = " ")
print("")