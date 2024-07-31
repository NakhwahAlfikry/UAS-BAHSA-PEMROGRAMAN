class Barang:
    def properti(self, nama, harga, stok):
        #untuk mengatur properti barang
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}"


class ManajemenBarang:
    def __init__(self):
        self.barang_list = []

    def tambah_barang(self, nama, harga, stok):
        barang = Barang()
        barang.properti(nama, harga, stok)
        self.barang_list.append(barang)

    def tampilkan_barang(self):
        if not self.barang_list:
            return "Tidak ada data barang."
        return "\n".join(str(barang) for barang in self.barang_list)

    def hapus_barang(self, nama):
        for barang in self.barang_list:
            if barang.nama.lower() == nama.lower():
                self.barang_list.remove(barang)
                return f"Barang {nama} telah dihapus."
        return "Barang tidak ditemukan."

    def cari_barang(self, nama):
        for barang in self.barang_list:
            if barang.nama.lower() == nama.lower():
                return str(barang)
        return "Barang tidak ditemukan."

    def hitung_pembelian(self, nama, jumlah):
        for barang in self.barang_list:
            if barang.nama.lower() == nama.lower():
                if barang.stok >= jumlah:
                    barang.stok -= jumlah
                    total_pembelian = barang.harga * jumlah
                    return f"Pembelian berhasil. Total harga: Rp. {total_pembelian}"
                else:
                    return "Stok tidak cukup."
        return "Barang tidak ditemukan."


def ambil_float(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            return nilai
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")


def ambil_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            nilai = int(input(prompt))
            if (min_value is not None and nilai < min_value) or (max_value is not None and nilai > max_value):
                print(f"Input tidak valid. Silakan masukkan angka antara {min_value} dan {max_value}.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")


def utama():
    manajemen_barang = ManajemenBarang()
    
    while True:
        print("\n=== Menu Aplikasi Manajemen Barang ===")
        print("1. Input Data Barang")
        print("2. Tampil Data Barang")
        print("3. Hapus Data Barang")
        print("4. Cari Data Barang")
        print("5. Hitung Pembelian")
        print("6. Keluar")

        pilihan = ambil_integer("Pilih menu (1-6): ", 1, 6)

        if pilihan == 6:
            print("Terima kasih telah menggunakan aplikasi ini!")
            break

        if pilihan == 1:
            nama = input("Masukkan nama barang: ")
            harga = ambil_float("Masukkan harga barang: ")
            stok = ambil_integer("Masukkan stok barang: ")
            manajemen_barang.tambah_barang(nama, harga, stok)
            print(f"Barang {nama} telah ditambahkan.")

        elif pilihan == 2:
            print("\nData Barang:")
            print(manajemen_barang.tampilkan_barang())

        elif pilihan == 3:
            nama = input("Masukkan nama barang yang akan dihapus: ")
            print(manajemen_barang.hapus_barang(nama))

        elif pilihan == 4:
            nama = input("Masukkan nama barang yang akan dicari: ")
            print(manajemen_barang.cari_barang(nama))

        elif pilihan == 5:
            nama = input("Masukkan nama barang yang akan dibeli: ")
            jumlah = ambil_integer("Masukkan jumlah barang yang dibeli: ")
            print(manajemen_barang.hitung_pembelian(nama, jumlah))


if __name__ == "__main__":
    utama()
