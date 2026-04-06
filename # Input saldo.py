print("=== VENDING MACHINE ===")

# Input saldo
saldo = int(input("Masukkan saldo anda: Rp "))

# Validasi saldo negatif
if saldo < 0:
    print("Error: Saldo tidak boleh negatif!")
else:
    total = 0
    daftar_beli = []

    while True:
        print("\n=== MENU MINUMAN ===")
        print("1. Fanta - Rp7000")
        print("2. Teh Pucuk - Rp5000")
        print("3. Air Aqua - Rp3000")
        print("4. Nescafe - Rp10000")
        print("5. Indomilk - Rp7500")

        pilihan = input("Pilih minuman (1-5): ")

        # Menentukan harga
        if pilihan == "1":
            nama = "Fanta"
            harga = 7000
        elif pilihan == "2":
            nama = "Teh Pucuk"
            harga = 5000
        elif pilihan == "3":
            nama = "Air Aqua"
            harga = 3000
        elif pilihan == "4":
            nama = "Nescafe"
            harga = 10000
        elif pilihan == "5":
            nama = "Indomilk"
            harga = 7500
        else:
            print("❌ Pilihan tidak valid!")
            continue

        # Tambah ke total
        total += harga
        daftar_beli.append(nama)

        # Tanya lanjut
        lagi = input("Mau tambah minuman lagi? (y/n): ")
        if lagi.lower() == 'n':
            break

    # STRUK
    print("\n=== STRUK PEMBELIAN ===")
    for item in daftar_beli:
        print("-", item)
    print("Total Belanja: Rp", total)

    # CEK SALDO
    if saldo >= total:
        kembalian = saldo - total
        print("✅ Pembelian berhasil!")
        print("Kembalian: Rp", kembalian)
    else:
        kurang = total - saldo
        print("❌ Saldo tidak cukup!")
        print("Kekurangan: Rp", kurang)

print("\nTerima kasih sudah menggunakan vending machine!")