bilangan_bulat = []
bilangan_genap = []
bilangan_ganjil = []

for i in range(10):
    bilangan_bulat.append(i + 1)
    bilangan_genap.append((i + 1) * 2)
    bilangan_ganjil.append((i + 1) * 2 - 1)

print("Bulat: ", end = " ")
for i in range(10):
    print(bilangan_bulat[i], end = " ")
print("")

print("Genap: ", end = " ")
for i in range(10):
    print(bilangan_genap[i], end = " ")
print("")

print("ganjil: ", end = " ")
for i in range(10):
    print(bilangan_ganjil[i], end= " ")

print("")