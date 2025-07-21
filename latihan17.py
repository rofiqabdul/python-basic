pelajaran = 2_000
novel = 5_000
skripsi = 10_000

jumlahPelajaran = int(input("jumlah buku pelajaran: "))
jumlahNovel = int(input("jumlah buku novel: "))
jumlahSkripsi = int(input("jumlah buku skripsi: "))
lamaPinjaman = int(input("lama pinjaman: "))

totalBiaya = 0
if lamaPinjaman > 10:
    totalBiaya = (jumlahPelajaran * pelajaran) + (jumlahNovel * novel) + (jumlahSkripsi * skripsi) * (lamaPinjaman - 10)

print(f"total biaya: {totalBiaya}")