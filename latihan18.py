huruf = ["A", "B", "C", "D", "E", "F"]

nilaiAcak = int(input("nilai acak: "))

if nilaiAcak > 5:
    print("error!")
else:
    print(f"huruf {huruf[nilaiAcak]}")