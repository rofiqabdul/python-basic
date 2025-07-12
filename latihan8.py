sepuluh = int(input("banyak uang 10 ribu: "))
lima = int(input("banyak uang 5 ribu: "))
duaPuluh = int(input("banyak uang 20 ribu: "))
belanja = int(input("biaya belanja: "))

totalUang = (10_000 * sepuluh) + (5_000 * lima) + (20_000 * duaPuluh)

print(f"Total uang: {totalUang}")
print(f"Sisa uang: {totalUang - belanja}")