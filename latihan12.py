musim = input("Masukan musim: ")
hari = input("Masukan hari: ")

if musim.lower() == "hujan" and hari.lower() == "libur":
    print(f"Musim {musim} dan hari {hari} maka fadhila akan rehat di rumah")
elif musim.lower() == "hujan" and hari.lower() == "kerja":
    print(f"Musim {musim} dan hari {hari} maka fadhila akan pasrah kehujanan")
elif musim.lower() == "panas" and hari.lower() == "libur":
    print(f"Musim {musim} dan hari {hari} maka fadhila akan hangout dengan teman")
elif musim.lower() == "panas" and hari.lower() == "kerja":
    print(f"Musim {musim} dan hari {hari} maka fadhila akan kerja dengan semangat")
else:
    print("Error!")