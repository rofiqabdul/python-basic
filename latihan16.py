pelajaran = 2_000
novel = 5_000
skripsi = 10_000

jumlahPelajaran = int(input("jumlah buku pelajaran: "))
jumlahNovel = int(input("jumlah buku novel: "))
jumlahSkripsi = int(input("jumlah buku skripsi: "))
lamaPinjaman = int(input("lama pinjaman: "))

totalBiaya = (jumlahPelajaran * pelajaran) + (jumlahNovel * novel) + (jumlahSkripsi * skripsi) * lamaPinjaman

print(f"total biaya: {totalBiaya}")