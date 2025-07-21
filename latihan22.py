huruf = ["A", "B", "C", "D", "E", "F"]

nilaiAcak = int(input("nilai acak: "))

if nilaiAcak > 5:
    print("error!")
else:
    if nilaiAcak % 2 != 0:
        print(f"huruf {huruf[nilaiAcak]}")
    else:
        print("bukan nilai ganjil")