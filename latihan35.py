si_angka_1 = [100]
for i in range(5):
    if i > 0:
        si_angka_1.append(100 + (3 ** i))

n = int(input("N: "))
if n <= len(si_angka_1):
    for i in range(n):
        print(f"{si_angka_1[i]} adalah 'si angka 1'")
else:
    print("N bukan 'si angka 1'")