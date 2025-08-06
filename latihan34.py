def menu():
    print("Menu:\n1. Ikan Bakar\n2. Ayam Panggang\n3. Iga Bakar")

pilih_menu = None 
daftar_menu = []
while pilih_menu != 0:
    menu()
    pilih_menu = int(input("tambah menu(0 selesai): "))
    if pilih_menu != 0:
        daftar_menu.append(pilih_menu)

print(f"menu dipilih {daftar_menu}")