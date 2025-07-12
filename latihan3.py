a = 5
b = 10

print(f"var a = {a}")
print(f"var b = {b}")
print("tukar")

# cara 1 menggunakan variable penampung
temp = a
a = b
b = temp
print("\nCara 1")
print(f"var a = {a}")
print(f"var b = {b}")

#cara 2 menggunakan logika XOR
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print("\nCara 2")
print(f"var a = {a}")
print(f"var b = {b}")