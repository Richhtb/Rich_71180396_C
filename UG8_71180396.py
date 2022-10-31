class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
        self._data = [None] * Kasir.DEFAULT_CAPACITY
        self._size = 0
       
    def __len__(self): #mengembalikan ukuran Queue
        return self._size

    def is_empty(self): 
        return self._size == 0

    def dequeue(self): #menghapus data paling depan (front)
        if self.is_empty():
            print('Empty')
        
        for i in range(len(self._data)):
            if i == len(self._data) - 1:
                break
            self._data[i] = self._data[i+1]
        self._size -= 1

    def enqueue(self, namaPelanggan): #menambah data ke list
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        
        avail = 0
        for i in range(len(self._data)):
            if self._data[i] is None:
                avail = i
                break

        self._data[avail] = NodePelanggan(namaPelanggan)
        self._size += 1

    def resize(self, cap): #mengubah ukuran queue pada list
        old = self._data
        self._data = [None] * cap
        for i in range(self._size):
            self._data[i] = old[i]
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        print('=== Kasir ===')
        for i in range(len(self._data)):
            try:
                print(f'{i+1} {self._data[i].getNamaPelanggan()}')
            except AttributeError as atr:
                print(f'{i+1} None')
        print()
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()
