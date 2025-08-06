tabungan = int(input("masukan uang: "))
belanja =[]

while tabungan >= 50_000:
    if tabungan >= 750_000:
        belanja.append("jas")
        tabungan -= 750_000
    elif tabungan >= 350_000:
        belanja.append("jaket")
        tabungan -= 350_000
    elif tabungan >= 225_000:
        belanja.append("kemeja")
        tabungan -= 225_000
    elif tabungan >= 100_000:
        belanja.append("celana")
        tabungan -= 100_000
    elif tabungan >= 50_000:
        belanja.append("kaos")
        tabungan -= 50_000

for pakaian in belanja:
    print(f"bangkit membeli {pakaian}")

print(f"sisa tabungan {tabungan}")
print(f"total items: {len(belanja)}")