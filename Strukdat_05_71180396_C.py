class mobil:
    _merk = ""
    _tipe = ""
    _kapasitasBBM = 0
    _jenisBahanBakar =""

    def __init__(self,merk,tipe,kapasitasBBM,jenisBahanBakar) :
        self._merk = merk
        self._tipe = tipe
        self._kapasitasBBM = kapasitasBBM
        self._jenisBahanBakar = jenisBahanBakar

    def setMerk(self,merk):
        self._merk = merk
    
    def getmerk(self):
        return self._merk

    def setTipe(self,tipe):
        self._tipe = tipe

    def getTipes(self):
        return self._tipe

    def setKapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM
    
    def getKapasitasBBM(self):
        return self._kapasitasBBM
    
    def setJenisBahanBakar(self,JenisBBM):
        self._jenisBahanBakar = JenisBBM
    
    def GetJenisBahanBakar(self):
        return self._jenisBahanBakar

    def printInfo(self):
        print("="*12,"INFO","="*12)
        print(f"Merk                : {self.getmerk()}\n")
        print(f"tipe                : {self.getTipes()}\n")
        print(f"Bahan Bakar         : {self.GetJenisBahanBakar}\n")
        print(f"Kapasitas BBM       : {self.getKapasitasBBM}")

    # def isiBBM(self,total):

    #     print("")

# if __name__ == "__main__":
#     mobil1 = Mobil("Toyota", "Avanza")
#     mobil1.printInfo()
#     mobil2 = Mobil("Nissan", "Grand Livina")
#     mobil2.setJenisBahanBakar("Bensin")
#     mobil2.setKapasitasBBM(20)
#     mobil2.printInfo()
#     mobil1.isiBBM(14500)
#     mobil2.isiBBM(14500)