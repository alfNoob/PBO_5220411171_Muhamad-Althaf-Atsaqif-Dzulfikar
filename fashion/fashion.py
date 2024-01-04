from prettytable import PrettyTable

class Menu_Items:    
    def __init__(self):
        self.jenis_baju =  {
            1: "kaos",
            2: "kemeja batik"
        }

        self.jenis_sablon = {
            1: "Sablon manual plastisol",
            2: "Sablon manual discharge",
            3: "Sablon digital polyflex reflective"
        }

        self.harga_sablon = {
            1: 75000,
            2: 115000,
            3: 100000
        }

        self.motif_batik = {
            1: "Parang",
            2: "Kraton",
            3: "Mega Mendung"
        }

        self.harga_motif_batik = {
            1: 50000,
            2: 60000,
            3: 70000
        }

        self.bahan = {
            1: "Cotton Combed",
            2: "Polyester",
            3: "Rayon"
        }

        self.harga_bahan = {
            1: 40000,
            2: 30000,
            3: 20000
        }

        self.merk = {
            1: "Gucci",
            2: "Hermes",
            3: "Louis Vuitton",
        }        

        self.harga_merk = {
            1: 150000,
            2: 200000,
            3: 250000
        }
    def lihat_motif_baju(self):
        print("== Pilih Motif Baju ==")
        print("1. Putih")
        print("2. Hitam")
        print("3. Batik")

    def tampil_ukuran(self):
        print("\nUkuran (cm): ")
        print("1. S (Small) : 4-7")
        print("2. M (Medium) : 8-11")
        print("3. L (Large) : 12-15")
        print("4. XL (Extra Large) : 16-18")

    def tampilkan_data(self):
        print("\n===== DATA BAJU ======")
        print("1. Kaos sablon")
        print("2. Kaos tidak sablon")
        print("3. Kemeja")

    def tampil_opsi_pakaian(self):
        for key, value in self.jenis_baju.items():
            print(f"{key}.- {value}")

    def tampil_jenis_sablon(self):
        for key, value in self.jenis_sablon.items():
            print(f"{key}.-{value}")

    def tampil_bahan(self):
        for key, value in self.bahan.items():
            print(f"{key}.-{value}")

    def main_menu(self, fashion, data):
        beli = True
        # menu = Menu_Items()
        while beli:
            kaos = Kaos()
            kemeja = Kemeja()
            print("1. admin")
            print("2. pembeli")
            print("3. exit")
            user = input("Siapa Anda?\npilih opsi:   ")
            if user in ["1", "admin"]:
                nama = input("Nama Anda: ")
                status = input("Status Anda: ")
                self.tampilkan_data()
                lihatData = input("Pilih opsi: ")
                if lihatData == '1':
                    data._DataPembelian__show_inventory_kaos_sablon()
                elif lihatData == '2':
                    data._DataPembelian__show_inventory_kaos_tidak_sablon()
                elif lihatData == '3':
                    data._DataPembelian__show_inventory_kemeja()
                else:
                    print("oke")

            elif user in ["2", "pembeli"]:
                baju = Baju()
                self.tampil_opsi_pakaian()
                opsi = input("Pakaian apa yang ingin Anda beli: ")
                jenis_baju= baju.pilih_jenis_baju(opsi)
                ukuran = int(input("Ukuran lengan Anda: "))
                baju.size_of_item(ukuran)
                print(f"Ukuran Anda: {baju.size_of_item(ukuran)}")
                self.tampil_bahan()                
                pilih_bahan = int(input("Pilih bahan kaos: "))
                bahan = self.bahan[pilih_bahan]
                if opsi in ["1", "kaos"] :
                    isSablon = input("\nApakah kaos Anda ingin disablon?(y/n): ")
                    if isSablon == "y".lower():
                        self.tampil_jenis_sablon()
                        harga_bahan = self.harga_bahan[pilih_bahan]
                        numSablon = int(input("\npilih jenis sablon(1/2/3): "))
                        depanBelakang = input("Sablon Depan dan belakang? (y/n): ")
                        sablon = kaos.sablon(numSablon, depanBelakang)
                        jenis_sablon = self.jenis_sablon[numSablon]
                        harga_sablon = 2 * self.harga_sablon[numSablon]
                        harga_total = harga_bahan + harga_sablon
                        # print(f"Anda memilih sablon {jenis_sablon} dengan harga {harga_sablon}\n")
                        pembeli_sablon = Pembeli(jenis_baju, harga_sablon, ukuran, None, bahan, None, jenis_sablon)
                        data.add_inventory(pembeli_sablon)


                    elif isSablon == "n".lower():
                        self.tampil_bahan()
                        pilih_merk = int(input("\nmerk mana yang Anda inginkan:"))
                        merk = self.merk[pilih_merk]
                        harga_merk = self.harga_merk[pilih_merk]
                        print(f"Anda memilih merk {merk} dengan harga Rp{harga_merk}")
                        pembeli_merk = Pembeli(jenis_baju, harga_merk, ukuran, merk, bahan, None, None)
                        data.add_inventory(pembeli_merk)


                elif opsi in ["2", "kemeja"]:
                    pilihMotif = int(input("Pilih motif kemeja: "))
                    motif = kemeja.pilih_motif_kemeja(pilihMotif)
                    motif_batik = motif['kemeja batik']
                    harga_batik = motif['harga kemeja']
                    print(f"Anda memilih batik {motif_batik} dengan harga Rp{harga_batik}\n")
                    pembeli_kemeja = Pembeli(jenis_baju, harga_batik, ukuran, None, None, motif_batik, None)

                else: 
                    print("pilihan tidak ada")



            elif user in ["3", "exit"]:
                sure = input("Apakah Anda yakin?(y/n)\njawab: ")
                if sure == 'y'.lower():
                    print("Terima kasih telah berkunjung!")
                    beli = False
                elif sure == 'n'.lower():
                    beli = True

            else:
                print("Invalid input")

class FashionShop:
    def __init__(self, bahan=None):
        self.bahan = bahan

    def set_bahan(self, bahan):
        self.bahan = bahan


class Baju(FashionShop):
    def __init__(self, bahan=None):
        super().__init__(bahan=None)
        self.jenis = None
        self.ukuran_baju = None

    def set_bahan(self, bahan):
        return f"Bahan : {super().set_bahan(bahan)}"

    def size_of_item(self, size):
        sizes = ["S", "M", "L", "XL"]
        if 4 <= size <= 7:
            return sizes[0]
        elif 8 <= size <= 11:
            return sizes[1]
        elif 12 <= size <= 15:
            return sizes[2]
        elif 16 <= size <= 18:
            return sizes[3]
        else:
            return "Ukuran tidak tersedia!"

    def pilih_jenis_baju(self, opsi):
        menu = Menu_Items()
        if opsi in ["1", "kaos"]:
            return menu.jenis_baju[1]

        elif opsi in ["2", "kemeja"]:
            return menu.jenis_baju[2]

        

class Kaos(Baju):
    def __init__(self, bahan=None):
        super().__init__(bahan=None)

    def set_bahan(self, bahan):
        super().set_bahan(bahan)

    def sablon(self, sablon, depanBelakang=None):
        if depanBelakang == "y":
            return f"Sablon {menu.jenis_sablon[sablon]} depan dan belakang", 2 * menu.harga_sablon[sablon]
        elif depanBelakang == "n":
            return f"Sablon {sablon}", self.harga_sablon(sablon)
        else:
            print("Pilihan tidak tersedia")
            return None, None


class Kemeja(Baju):
    def __init__(self, bahan=None):
        super().__init__(bahan=None)

    def pilih_motif_kemeja(self, kemeja):
        return {
            "kemeja batik": menu.motif_batik[kemeja],
            "harga kemeja": menu.harga_motif_batik[kemeja]
        }

# class untuk meletakkan data pembeli 
class Pembeli:
    def __init__(self, jenis, harga, ukuran, merk=None, bahan=None, motif=None, jenis_sablon=None):
        self.jenis = jenis
        self.harga = harga
        self.ukuran = ukuran
        self.merk = merk
        self.bahan = bahan
        self.motif = motif
        self.jenis_sablon = jenis_sablon


class DataPembelian(Pembeli):
    def __init__(self, jenis, harga, ukuran, merk=None, bahan=None, motif=None, jenis_sablon=None):
        super().__init__(jenis, harga, ukuran, merk=None, bahan=None, motif=None, jenis_sablon=None)
        self.inventory = []

    def add_inventory(self, item=None):
        if item is not None:
            self.inventory.append(item)
        else:
            print("Belum ada data")

    def __show_inventory_kaos_sablon(self):
        table = PrettyTable()
        table.field_names = ["No", "Jenis", "Harga", "Ukuran", "Bahan", "Jenis Sablon"]

        for index, item in enumerate(self.inventory, start=1):
            if item.jenis_sablon is not None:
                table.add_row([index, item.jenis, f"Rp{item.harga}", item.ukuran, item.bahan, item.jenis_sablon])

        print(table)

    def __show_inventory_kaos_tidak_sablon(self):
        table = PrettyTable()
        table.field_names = ["No", "Jenis", "Harga", "Ukuran", "Bahan", "Merk"]

        for index, item in enumerate(self.inventory, start=1):
            if item.merk is not None:
                table.add_row([index, item.jenis, f"Rp{item.harga}", item.ukuran, item.bahan, item.merk])

        print(table)

    def __show_inventory_kemeja(self):
        table = PrettyTable()
        table.field_names = ["No", "Jenis", "Harga", "Ukuran", "Motif"]

        for index, item in enumerate(self.inventory, start=1):
            if item.motif is not None:
                table.add_row([index, item.jenis, f"Rp{item.harga}", item.ukuran, item.motif])

        print(table)
                

if __name__ == "__main__":
    menu = Menu_Items()
    fashion = FashionShop()
    data = DataPembelian()
    menu.main_menu(fashion, data)    
         