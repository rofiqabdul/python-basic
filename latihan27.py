n = int(input("N= "))

for i in range(n):
    if i < n - 1:
        print(i + 1, end = ",")
    else:
        print(n)
print("")