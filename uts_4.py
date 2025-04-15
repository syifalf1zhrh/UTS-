
class Rekening:
    def __init__(self, nama, no_rek, saldo):
        self.nama = nama
        self.no_rek = no_rek
        self.saldo = saldo

class Nasabah(Rekening):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def show_info(self):
        print(f"\nNama            : {self.nama}")
        print(f"No Rekening     : {self.no_rek}")
        print(f"Saldo           : Rp {self.saldo:,.2f}")
        print("===================================")

n1= Nasabah("Budi", "5555", 500000.0)
n2= Nasabah("Wati", "6666", 2000000.0)

print("Data Nasabah:")
n1.show_info()
n2.show_info()