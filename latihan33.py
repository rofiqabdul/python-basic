def menu():
    print("Menu:\n1. Proses\n2. Exit")

pilih_menu = 0
while pilih_menu != 2:
    menu()
    pilih_menu = int(input("pilih menu: "))

print("Exit system")