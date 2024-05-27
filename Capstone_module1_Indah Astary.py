# Data dummy
cust_data = [
    {"Nama": "Indah", "Telepon": "081122336576", "Nomor Polisi": "b4460fbg", "Tagihan": "200000"},
    {"Nama": "Cindy", "Telepon": "085276760000", "Nomor Polisi": "b2344cnb", "Tagihan": "100000"},
    {"Nama": "Ninda", "Telepon": "081310761010", "Nomor Polisi": "b6767apa", "Tagihan": "100000"},
    {"Nama": "Tita", "Telepon": "085252079588", "Nomor Polisi": "b2334nrn", "Tagihan": "300000"},
]

for customer in cust_data:
    print(f"Nama: {customer['Nama']}, Telepon: {customer['Telepon']}, Nomor Polisi: {customer['Nomor Polisi']}, Tagihan: {customer['Tagihan']}")


def display_menu():
    print("\nMenu Data Konsumen Rental Mobil Sukses")
    print("1. Tampilkan Data Konsumen")
    print("2. Tambah Data Konsumen")
    print("3. Ubah Data Konsumen")
    print("4. Hapus Data Konsumen")
    print("5. Keluar")

def read_data(cust_data):
    if not cust_data:
        print("Tidak ada data untuk ditampilkan.")
    else:
        for idx, customer in enumerate(cust_data, start=1):
            print(f"{idx}. Nama: {customer['Nama']}, Telepon: {customer['Telepon']}, Nomor Polisi: {customer['Nomor Polisi']}, Tagihan: {customer['Tagihan']}")

def create_data(cust_data):
    nama = input("Masukkan nama: ")
    telp = input("Masukkan nomor telepon: ")
    nopol = input("Masukkan nomor polisi mobil: ")
    tagihan = input("Masukkan total tagihan rental mobil: ")
    customer = {"Nama": nama, "Telepon": telp, "Nomor Polisi": nopol, "Tagihan": tagihan}
    cust_data.append(customer)
    print("Data konsumen berhasil ditambahkan!")

def update_data(cust_data):
    try:
        idx = int(input("Masukkan indeks data konsumen yang ingin diubah: ")) - 1
        if 0 <= idx < len(cust_data):
            nama = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
            telp = input("Masukkan nomor telepon baru (kosongkan jika tidak ingin mengubah): ")
            nopol = input("Masukkan nomor polisi baru (kosongkan jika tidak ingin mengubah): ")
            tagihan = input("Masukkan jumlah tagihan baru (kosongkan jika tidak ingin mengubah): ")
            
            if nama:
                cust_data[idx]['Nama'] = nama
            if telp:
                cust_data[idx]['Telepon'] = telp
            if nopol:
                cust_data[idx]['Nomor Polisi'] = nopol
            if tagihan:
                cust_data[idx]['Tagihan'] = tagihan
            print("Data konsumen berhasil diperbarui!")
        else:
            print("Data konsumen tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def delete_data(cust_data):
    try:
        idx = int(input("Masukkan indeks data konsumen yang ingin dihapus: ")) - 1
        if 0 <= idx < len(cust_data):
            del cust_data[idx]
            print("Data konsumen berhasil dihapus!")
        else:
            print("Data konsumen tidak valid.")
    except ValueError:
        print("Input tidak valid.")

cust_data = []
while True:
    display_menu()
    pilihan = input("Pilih opsi (1-5): ")
    if pilihan == '1':
        read_data(cust_data)
    elif pilihan == '2':
        create_data(cust_data)
    elif pilihan == '3':
        update_data(cust_data)
    elif pilihan == '4':
        delete_data(cust_data)
    elif pilihan == '5':
        print("Program selesai disini. Terima kasih!")
        break
    else:
        print("Pilihan invalid. Coba lagi.")
