tabungan = int(input("masukan uang: "))

while tabungan >= 50_000:
    if tabungan >= 750_000:
        print("bangkit akan memeli jas")
        tabungan -= 750_000
    elif tabungan >= 350_000:
        print("bangkit akan memeli jaket")
        tabungan -= 350_000
    elif tabungan >= 225_000:
        print("bangkit akan memeli kemeja")
        tabungan -= 225_000
    elif tabungan >= 100_000:
        print("bangkit akan memeli celana")
        tabungan -= 100_000
    elif tabungan >= 50_000:
        print("bangkit akan memeli kaos")
        tabungan -= 50_000

print(f"sisa tabungan {tabungan}")