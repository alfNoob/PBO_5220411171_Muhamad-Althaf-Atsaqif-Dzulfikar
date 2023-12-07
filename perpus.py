from dataclasses import dataclass
from typing import Optional, List
import os

@dataclass
class PerpusItem:
    judul: str
    subjek: str

    def lokasiPenyimpanan(self, lokasi) :
        ruang = {
            1: "Rak 1",
            2: "Rak 2",
            3: "Rak 3"
        }
        
        while True :
            try:
                if not(lokasi in ruang):
                    print("Masukkan angka yang benar!")
                else : 
                    # return f"\nlokasi {type(self).className(self)} ada di {ruang[lokasi]}\n"
                    return f"Lokasi Penyimpanan: {ruang[lokasi]}"
            except ValueError :
                print("Angka tidak valid. Masukkan angka.")
                return None

    def info(self):
        if type(self) == Buku:
            print(f"Judul buku: {self.judul}\nSubjek: {self.subjek}\nNo. ISBN: {self.ISBN}\nNama Pengarang: {self.Pengarang}\nJumlah Halaman: {self.jmlHal}\nUkuran buku: {self.ukuran}")
        elif type(self) == Majalah:
            print(f"Judul buku: {self.judul}\nSubjek: {self.subjek}\nIssue: {self.issue}\nVolume: {self.volume}")
        elif type(self) == DVD:
            print(f"Judul buku: {self.judul}\nSubjek: {self.subjek}\naktor: {self.aktor}\ngenre: {self.genre}")
        print("\n")

@dataclass
class Katalog(PerpusItem):
    items: List[PerpusItem] = None
    judul: str = "Karya Tulis"
    subjek: str = "Perpus UTY"

    def __init__(self):
        self.items = []

    def tambahItem(self, item):
        self.items.append(item)

    def tampilkan_katalog(self):
        if self.items:
            count = 0
            print("\n")
            for item in self.items:
                print(f"{count+1} - {item.className()}")
                item.info()
            
        else:
            print("Katalog Kosong")


@dataclass
class Buku(PerpusItem):
    ISBN: str
    Pengarang: str
    jmlHal: int
    ukuran: int
    

    def lokasiPenyimpanan(self, lokasi):
        super().lokasiPenyimpanan(lokasi)

    def info(self):
        super().info()

    def className(self):
        return f"{Buku.__name__}"

@dataclass
class Pengarang(Buku):
    def info(self):
        print(f"Nama Pengarang: {self.Pengarang}")

    def cari(self, nama_pengarang):
        if self.Pengarang.lower() == nama_pengarang.lower():
            return True
        return False

@dataclass
class Majalah(PerpusItem):
    volume: int
    issue: str

    def lokasiPenyimpanan(self, lokasi):
        return super().lokasiPenyimpanan(lokasi)

    def info(self):
        super().info()
        

    def className(self):
        return f"{Majalah.__name__}"

@dataclass
class DVD(PerpusItem):
    aktor: str
    genre: str

    def lokasiPenyimpanan(self, lokasi):
        super().lokasiPenyimpanan(lokasi)

    def info(self):
        super().info()

    def className(self):
        return f"{DVD.__name__}"

def clear():
    os.system('cls')

def pause():
    os.system('pause')

def main():
    katalog = Katalog()

    while True:
        opsi_1 = input("1. Buku\n2. Majalah\n3. DVD\n4. Katalog\nPilih item: ")

        if opsi_1 in ['1', 'Buku']:
            try: 
                judul = input("Judul Buku: ")
                subjek = input("Isi Bahasan Buku: ")
                ISBN = input("No. ISBN: ")
                pengarang = input("Nama Pengarang: ")
                halaman = int(input("Jumlah Halaman: "))
                ukuran = int(input("Ukuran Buku: "))
                lokasi = int(input("Lokasi item: "))    
                            
                if type(halaman) != int and type(ukuran) != int:
                    raise ValueError("Halaman dan Ukuran harus berupa angka!")
                else: 
                    buku = Buku(judul, subjek, ISBN, pengarang, halaman, ukuran)
                    katalog.tambahItem(buku)
                    print(buku.lokasiPenyimpanan(lokasi))
                    print("Data berhasil di masukkan")
                    pause()
                    clear()
            except ValueError:
                print("\033[91mGagal!\033[0m Masukkan Angka.")
                    
        elif opsi_1 in ['2', "Majalah"]: 
            try: 
                judul = input("Judul Majalah: ")
                subjek = input("Isi Bahasan Majalah: ")
                volume = int(input("Volume Majalah: "))
                issue = input("Issue: ")
                lokasi = int(input("Lokasi item: "))
                
                if type(volume) != int :
                    raise ValueError("Halaman dan Ukuran harus berupa angka!")
                else: 
                    majalah = Majalah(judul, subjek, volume, issue)
                    katalog.tambahItem(majalah)
                    print(majalah.lokasiPenyimpanan(lokasi))
                    print("Data berhasil di masukkan")
                    pause()
                    clear()
                    
            except ValueError:
                print("\033[91mGagal!\033[0m Masukkan Angka.")

        elif opsi_1 in ['3', "DVD"]:
            try: 
                judul = input("Judul Majalah: ")
                subjek = input("Isi Bahasan Majalah: ")
                aktor = input("Aktor Film: ")
                genre = input("Genre Film: ")                
                dvd = DVD(judul, subjek, aktor, genre)
                lokasi = int(input("Lokasi item: "))
                katalog.tambahItem(dvd)
                print(majalah.lokasiPenyimpanan(lokasi))
                print("Data berhasil di masukkan")
                pause()
                clear()
            except ValueError:
                print("\033[91mGagal!\033[0m Masukkan huruf.")


        elif opsi_1 in ["4", "Katalog"]:
            katalog.tampilkan_katalog()
            pause()
            clear()

        else:
            print("Invalid Input")


if __name__ == "__main__" :
    main()