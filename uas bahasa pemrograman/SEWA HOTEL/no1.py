import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Fungsi untuk menghitung total bayar dan uang kembali
def hitung():
    try:
        # Ambil nilai dari input
        nama_petugas = entry_petugas.get()
        nama_customer = entry_customer.get()
        tanggal_checkin = entry_checkin.get()
        kode_kamar = entry_kode_kamar.get().upper()
        lama_sewa = int(entry_lama_sewa.get())
        uang_bayar = float(entry_uang_bayar.get())

        # Validasi input
        if not (nama_petugas and nama_customer and tanggal_checkin and kode_kamar):
            raise ValueError("Semua bidang harus diisi!")

        # Dictionary untuk harga kamar
        harga_kamar = {'M': ('Melati', 650000),
                       'S': ('Sakura', 550000),
                       'L': ('Lily', 400000),
                       'A': ('Anggrek', 350000)}

        if kode_kamar not in harga_kamar:
            raise ValueError("Kode kamar tidak valid!")

        # Mengambil nama kamar dan harga sewa
        nama_kamar, harga_sewa = harga_kamar[kode_kamar]

        # Hitung jumlah bayar
        jumlah_bayar = harga_sewa * lama_sewa

        # Hitung diskon
        ppn = 0.10 * jumlah_bayar if lama_sewa > 5 else 0.05 * jumlah_bayar if lama_sewa > 3 else 0

        # Hitung total bayar
        total_bayar = jumlah_bayar - ppn

        # Validasi apakah uang bayar cukup
        if uang_bayar < total_bayar:
            raise ValueError("Uang bayar tidak mencukupi! Silakan masukkan jumlah yang lebih besar atau sama dengan total bayar.")

        # Hitung uang kembali
        uang_kembali = uang_bayar - total_bayar

        # Tampilkan hasil
        bukti_pemesanan = (
            "Bukti Pemesanan Kamar\n"
            "Hotel “SEJUK ASRI”\n"
            "====================\n"
            f"Nama Petugas : {nama_petugas}\n"
            "J Selamat Mengerjakan J\n"
            "J Selamat Mengerjakan J\n"
            f"Nama Customer : {nama_customer}\n"
            f"Tanggal Check-in : {tanggal_checkin}\n"
            "=============================================\n"
            f"Nama Kamar Yang di pesan : {nama_kamar}\n"
            f"Harga sewa per malam : Rp. {harga_sewa:,}\n"
            f"Lama sewa : {lama_sewa} malam\n"
            f"PPN 10% : Rp. {ppn:,}\n"
            f"Jumlah Bayar : Rp. {jumlah_bayar:,}\n"
            f"Total Bayar : Rp. {total_bayar:,}\n"
            f"Uang Bayar : Rp. {uang_bayar:,}\n"
            f"Uang Kembali : Rp. {uang_kembali:,}\n"
        )

        # Menampilkan bukti pemesanan
        label_output.config(text=bukti_pemesanan)  # Mengganti teks di Label

    except ValueError as ve:
        messagebox.showerror("Kesalahan Input", str(ve))

# Inisialisasi GUI
root = tk.Tk()
root.title("Transaksi Pembayaran Hotel Sejuk Asri")
root.geometry("550x500")

# Mengatur style menggunakan ttk
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10, "bold"))

# Frame untuk judul
frame_title = ttk.Frame(root, padding=(20, 10))
frame_title.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Judul aplikasi
judul_label = ttk.Label(frame_title, text="Hotel “SEJUK ASRI”", font=("Arial", 16, "bold"))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Separator
separator = ttk.Separator(frame_title, orient='horizontal')
separator.grid(row=1, column=0, columnspan=2, sticky='ew', pady=(0, 10))

# Frame untuk input
frame_input = ttk.Frame(root, padding=(20, 10))
frame_input.grid(row=1, column=0, sticky=(tk.W, tk.E))

# List label dan entry
input_data = [
    ("Input Nama Petugas :", tk.StringVar(value='')),
    ("Input Nama Customer :", tk.StringVar(value='')),
    ("Input Tanggal Check-in (DD-MM-YYYY) :", tk.StringVar(value='')),
    ("========================================================", None),
    ("Pilih Kode Kamar [M/S/L/A] :", tk.StringVar(value='')),
    ("Input Lama Sewa :", tk.StringVar(value='')),  # Gunakan StringVar
    ("Input Uang Bayar :", tk.StringVar(value=''))  # Gunakan StringVar
]

# Membuat label dan entry menggunakan loop
entries = []
for idx, (label, var) in enumerate(input_data):
    if var is None:
        # Tampilkan separator
        ttk.Label(frame_input, text=label, font=("Arial", 10, "bold")).grid(row=idx, column=0, columnspan=2, pady=5)
    else:
        ttk.Label(frame_input, text=label).grid(row=idx, column=0, sticky=tk.W, padx=5, pady=5)
        entry = ttk.Entry(frame_input, textvariable=var, width=30)
        entry.grid(row=idx, column=1, padx=5, pady=5)
        entries.append(entry)

entry_petugas, entry_customer, entry_checkin, entry_kode_kamar, entry_lama_sewa, entry_uang_bayar = entries

# Tombol untuk menghitung
ttk.Button(frame_input, text="Hitung", command=hitung).grid(row=7, column=1, pady=10, sticky=tk.E)

# Frame untuk output
frame_output = ttk.Frame(root, padding=(20, 10))
frame_output.grid(row=2, column=0, sticky=(tk.W, tk.E))

# Label untuk hasil
label_output = ttk.Label(frame_output, text="", font=("Arial", 10), justify=tk.LEFT)
label_output.grid(row=0, column=0, padx=5, pady=5)

# Menjalankan aplikasi
root.mainloop()
