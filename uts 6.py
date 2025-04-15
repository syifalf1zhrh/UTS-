class Rekening:
    def __init__(self, nama, no_rek, saldo):
        self.nama = nama
        self.no_rek = no_rek
        self.saldo = saldo
     
    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setor tunai Rp{jumlah} berhasil.")
        print(f"Saldo saat ini: Rp {self.saldo:,.2f}")
    
    def tarik_tunai(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Tarik tunai Rp{jumlah} berhasil.")
        else:
            print("Saldo tidak cukup untuk tarik tunai.")
        print(f"Saldo saat ini: Rp {self.saldo:,.2f}")
    
    def transfer(self, jumlah, rekening_tujuan):
        if self.saldo >= jumlah:    
            self.saldo -= jumlah
            rekening_tujuan.saldo += jumlah
            print(f"\nTransfer Rp{jumlah} ke rekening {rekening_tujuan.no_rek} berhasil.")
        else:
            print("Saldo tidak cukup untuk transfer.")

class Nasabah(Rekening):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def show_info(self):
        print(f"Nama            : {self.nama}")
        print(f"No Rekening     : {self.no_rek}")
        print(f"Saldo           : Rp {self.saldo:,.2f}")
        print("--------------------------------------")

n1= Nasabah("Budi", "5555", 500000.0)
n2= Nasabah("Wati", "6666", 2000000.0)

print("Data Awal Nasabah:")
n1.show_info()
n2.show_info()

#transaksi
print("\nTransaksi:")
print("Nasabah 1 setor tunai Rp1.000.000")
n1.setor_tunai(1000000)

print("\nNasabah 2 tarik tunai Rp1.000.000")
n2.tarik_tunai(1000000)

#transfer
print("\nTransfer Rp500.000 dari Nasabah 1 ke Nasabah 2")
n1.transfer(500000, n2)

print("=======================================================")
#data nasabah setelah transaksi dan tf
print("\nData Nasabah Setelah Transaksi dan Transfer:")
n1.show_info()
n2.show_info()