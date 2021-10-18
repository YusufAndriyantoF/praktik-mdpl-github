def MetodeGarisLurus():
    print ("Metode Garis Lurus")
    Hargaperolehan = int(input("Harga perolehan: Rp "))
    Residu = int(input("Nilai residu: Rp "))
    UmurEkonomis = int(input("Umur ekonomis: "))
    print("Depresiasi = " + str((Hargaperolehan - Residu)/ UmurEkonomis))

def MetodeJamJasa():
    print ("Metode Jam jasa")
    Hargaperolehanjam = int(input("Harga perolehan jam : Rp "))
    Residujam = int(input("MNilai residu: Rp "))
    Taksiranhasilproduksi = int(input("Hasil produksi (unit):"))
    print("Depresiasi = " + str((Hargaperolehanjam - Residujam)/
Taksiranhasilproduksi)
    )
print(" *=====* Menu Metode Menghitung Depresiasi *=====* ")
print(" 1. MGL (Metode Garis Lurus) ")
print(" 2. MJJ (Metode Jam Jasa) ")

menu = int(input(" masukan metode : " ))
if menu == 1:
    MetodeGarisLurus()
elif menu == 2:
    MetodeJamJasa()