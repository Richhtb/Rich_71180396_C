class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
class tabungan:     
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self._size == 0

    def insert_head(self,no_rek,nama,saldo):
        self._norek = no_rek
        self._nama = nama
        self._saldo= saldo
        rek_baru = NodeTabungan(no_rek,nama,saldo,None)
        if self.isEmpty() == True:
            self._head =rek_baru
            self._tail =rek_baru
            self._tail.next= None
        else:
            rek_baru.next = self._head
            self._head = rek_baru
        self.size += 1