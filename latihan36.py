keranjang = []
for i in range(3):
    item = input(f"keranjang {i+1} = ")
    if item.isdigit():
        keranjang.append(int(item))
    else:
        keranjang.append(0)

dibawa = int(input("keranjang dibawa: "))
keranjang.pop(dibawa-1)
print(f"jumlah buah {sum(keranjang)}")