bulat = int(input("Masikuan bilangan bulat: "))

if bulat == 1 or bulat == 4 or bulat == 7:
    print("PAS")
elif bulat == 2 or bulat == 3 or bulat == 9:
    print("LEWAT")
elif bulat == 0 or bulat == 10 or bulat == 11:
    print("BINGO")
else:
    print("ERROR!")