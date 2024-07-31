import rumus as geo

def utama():
    while True:
        print("\n=== Program Perhitungan Luas dan Keliling Bangun Datar ===")
        print("1. Segi Empat")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Keluar")

        pilihan = ambil_integer("Pilih bangun datar (1-5): ", 1, 5)

        if pilihan == 5:
            print("Terima kasih telah menggunakan program ini!")
            break

        if pilihan == 1:
            # Segi Empat
            sisi = ambil_float("Masukkan panjang sisi segi empat: ")
            luas, keliling = geo.segi_empat(sisi)
            nama = "Segi Empat"

        elif pilihan == 2:
            # Persegi Panjang
            panjang = ambil_float("Masukkan panjang persegi panjang: ")
            lebar = ambil_float("Masukkan lebar persegi panjang: ")
            luas, keliling = geo.persegi_panjang(panjang, lebar)
            nama = "Persegi Panjang"

        elif pilihan == 3:
            # Segitiga
            alas = ambil_float("Masukkan panjang alas segitiga: ")
            tinggi = ambil_float("Masukkan tinggi segitiga: ")
            sisi1 = ambil_float("Masukkan panjang sisi pertama segitiga: ")
            sisi2 = ambil_float("Masukkan panjang sisi kedua segitiga: ")
            sisi3 = ambil_float("Masukkan panjang sisi ketiga segitiga: ")
            luas, keliling = geo.segitiga(alas, tinggi, sisi1, sisi2, sisi3)
            nama = "Segitiga"

        elif pilihan == 4:
            # Lingkaran
            jari_jari = ambil_float("Masukkan jari-jari lingkaran: ")
            luas, keliling = geo.lingkaran(jari_jari)
            nama = "Lingkaran"

        tampilkan_hasil(nama, luas, keliling)


def tampilkan_hasil(nama, luas, keliling):
    print("\n=== Hasil Perhitungan ===")
    print(f"Nama Bangun Datar: {nama}")
    print(f"Luas: {luas:.2f}")
    print(f"Keliling: {keliling:.2f}")


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


if __name__ == "__main__":
    utama()
