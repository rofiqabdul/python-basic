deret = int(input("Deret: "))

for i in range(deret):
    if i == 0:
        print("Deret A: ", end = "")
    print(i + 1, end=" ")
print("")
for i in range(deret):
    if i == 0:
        print("Deret B: ", end = "")
    print(deret, end=" ")
    deret -= 1
print("")