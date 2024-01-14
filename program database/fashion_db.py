from prettytable import PrettyTable
from mysql.connector import connect, Error
import os

def pause():
    os.system("pause")

class Database:
    
    def connect_db(self):
        try:
            db = connect(
                host="localhost",
                user="root",
                password="",
                database="fashion_5220411171"
            )

            if db.is_connected():
                print("Berhasil Terhubung")
                return db

        except Error as e:
            print(e)

    def create_database(self, db):
        cursor = db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS fashion_5220411171"
        cursor.execute(sql)
        print("Database berhasil dibuat!")

    def __display_all_data(self, db, table_name):
        cursor = db.cursor()

        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows:
            table = PrettyTable()
            table.field_names = [i[0] for i in cursor.description]

            for row in rows:
                table.add_row(row)

            print(table)
        else:
            print("Belum ada data")

    def __delete(self, db, table_name, record_id):
        cursor = db.cursor()

        try:
            sql = f"DELETE FROM {table_name} WHERE id = %s"
            
            cursor.execute(sql, (record_id,))
            
            db.commit()

            print(f"Pembeli dengan id {record_id} telah berhasil dihapus.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def get_data_by_id(self, db, table_name, record_id):
        cursor = db.cursor()

        try:
            sql = None
            if table_name == "kaos_sablon":
                sql = f"SELECT * FROM {table_name} WHERE id_sablon = %s"
            elif table_name == "kaos_tidak_sablon":
                sql = f"SELECT * FROM {table_name} WHERE id__tidaksablon = %s"
            elif table_name == "kemeja":
                sql = f"SELECT * FROM {table_name} WHERE id_kemeja = %s"
            cursor.execute(sql, (record_id,))
            row = cursor.fetchone()

            if row:
                table = PrettyTable()
                table.field_names = [i[0] for i in cursor.description]
                table.add_row(row)
                print(table)
            else:
                print(f"Tidak ada data dengan id {record_id}")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()


class db_KaosSablon(Database):
    
    def connect_db(self):
        super().connect_db()

    def create_table_kaos_sablon(self, db):
        cursor = db.cursor()
        # "id_sablon", "Jenis", "Harga", "Ukuran", "Bahan", "Jenis Sablon"
        sql = """
        CREATE TABLE IF NOT EXISTS kaos_sablon(
            id_sablon INT PRIMARY KEY,
            jenis VARCHAR(30),
            harga int,
            ukuran int,
            bahan VARCHAR(30),
            jns_sablon VARCHAR(30)
        )
        """

        cursor.execute(sql)
        print("Table kaos sablon berhasil dibuat")

    def insert_data_kaos_sablon(self, db, jenis, harga, ukuran, bahan, jns_sablon):
        cursor = db.cursor()
        
        cursor.execute("SELECT MAX(id_sablon) FROM kaos_sablon")
        last_id = cursor.fetchone()[0]
        if last_id is None:
            next_id = 1
        else:
            next_id = last_id + 1

        sql = """
        INSERT INTO kaos_sablon (id_sablon, jenis, harga, ukuran, bahan, jns_sablon)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (next_id, jenis, harga, ukuran, bahan, jns_sablon))
        db.commit()
        print(f"Data baru berhasil ditambahkan dengan id_sablon: {next_id}")

    def __delete_sablon(self, db, record_id):
        cursor = db.cursor()

        try:
            sql = f"DELETE FROM kaos_sablon WHERE id_sablon = %s"
            
            cursor.execute(sql, (record_id,))
            
            db.commit()

            print(f"Pembeli kaos sablon dengan id_sablon {record_id} telah berhasil dihapus.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def __update_data_kaos_sablon(self, db, record_id, new_jenis, new_harga, new_ukuran, new_bahan, new_jns_sablon):
        cursor = db.cursor()

        try:
            sql = """
            UPDATE kaos_sablon
            SET jenis = %s, harga = %s, ukuran = %s, bahan = %s, jns_sablon = %s
            WHERE id_sablon = %s
            """

            cursor.execute(sql, (new_jenis, new_harga, new_ukuran, new_bahan, new_jns_sablon, record_id))
            db.commit()

            print(f"Data dengan id_sablon {record_id} berhasil diperbarui.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

class db_KaosTidakSablon(Database):

    def connect_db(self):
        super().connect_db()

    def create_table_kaos_tidak_sablon(self, db):
        # "id_tidak_sablon", "Jenis", "Harga", "Ukuran", "Bahan", "Merk"
        cursor = db.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS kaos_tidak_sablon(
            id_tidak_sablon INT PRIMARY KEY,
            jenis VARCHAR(30),
            harga int,
            ukuran int,
            bahan VARCHAR(30),
            merk VARCHAR(30)
        )
        """

        cursor.execute(sql)
        print("Table kaos tidak sablon berhasil dibuat")

    def insert_data_kaos_tidak_sablon( db, jenis, harga, ukuran, bahan, merk):
        cursor = db.cursor()
        
        cursor.execute("SELECT MAX(id_tidak_sablon) FROM kaos_tidak_sablon")
        last_id = cursor.fetchone()[0]
        if last_id is None:
            next_id = 1
        else:
            next_id = last_id + 1

        sql = """
        INSERT INTO kaos_tidak_sablon (id_tidak_sablon, jenis, harga, ukuran, bahan, merk)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (next_id, jenis, harga, ukuran, bahan, merk))
        db.commit()
        print(f"Data baru berhasil ditambahkan dengan id_tidak_sablon: {next_id}")

    def __delete_tidak_sablon(self, db, record_id):
        cursor = db.cursor()

        try:
            sql = f"DELETE FROM kaos_tidak_sablon WHERE id_tidak_sablon = %s"
            
            cursor.execute(sql, (record_id,))
            
            db.commit()

            print(f"Pembeli kaos tidak sablon dengan id_tidak_sablon {record_id} telah berhasil dihapus.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def __update_data_kaos_tidak_sablon(self, db, record_id, new_jenis, new_harga, new_ukuran, new_bahan, new_merk):
        cursor = db.cursor()

        try:
            sql = """
            UPDATE kaos_tidak_sablon
            SET jenis = %s, harga = %s, ukuran = %s, bahan = %s, merk = %s
            WHERE id_tidak_sablon = %s
            """

            cursor.execute(sql, (new_jenis, new_harga, new_ukuran, new_bahan, new_merk, record_id))
            db.commit()

            print(f"Data dengan id_tidak_sablon {record_id} berhasil diperbarui.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

class db_Kemeja(Database):

    def connect_db(self):
        super().connect_db()

    def create_table_kemeja(self, db):
        # "id_kemeja", "Jenis", "Harga", "Ukuran", "Motif"
        cursor = db.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS kemeja(
            id_kemeja INT PRIMARY KEY,
            jenis VARCHAR(30),
            harga int,
            ukuran int,
            motif VARCHAR(30)
        )
        """
        cursor.execute(sql)
        print("Table kemeja berhasil dibuat")

    def insert_data_kemeja(self ,db, jenis, harga, ukuran, motif):
        cursor = db.cursor()
        
        cursor.execute("SELECT MAX(id_kemeja) FROM kemeja")
        last_id = cursor.fetchone()[0]
        if last_id is None:
            next_id = 1
        else:
            next_id = last_id + 1

        sql = """
        INSERT INTO kemeja (id_kemeja, jenis, harga, ukuran, motif)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (next_id, jenis, harga, ukuran, motif))
        db.commit()
        print(f"Data baru berhasil ditambahkan dengan id_kemeja: {next_id}")

    def __delete_kemeja(self, db, record_id):
        cursor = db.cursor()

        try:
            sql = f"DELETE FROM kemeja WHERE id_kemeja = %s"
            
            cursor.execute(sql, (record_id,))
            
            db.commit()

            print(f"Pembeli kemeja sablon dengan id_kemeja {record_id} telah berhasil dihapus.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def __update_data_kemeja(self, db, record_id, new_jenis, new_harga, new_ukuran, new_motif):
        cursor = db.cursor()

        try:
            sql = """
            UPDATE kemeja
            SET jenis = %s, harga = %s, ukuran = %s, motif = %s
            WHERE id_kemeja = %s
            """

            cursor.execute(sql, (new_jenis, new_harga, new_ukuran, new_motif, record_id))
            db.commit()

            print(f"Data dengan id_kemeja {record_id} berhasil diperbarui.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()



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
        i = 1
        for key, value in self.motif_batik.items():
            print(f"{key}.- {value}: Rp{self.harga_motif_batik[i]}")
            i += 1

    def tampil_ukuran(self):
        print("\nUkuran (cm): ")
        print("S (Small) : 4-7")
        print("M (Medium) : 8-11")
        print("L (Large) : 12-15")
        print("XL (Extra Large) : 16-18")

    def tampilkan_data(self):
        print("\n===== LIHAT DATA BAJU ======")
        print("1. Kaos sablon")
        print("2. Kaos tidak sablon")
        print("3. Kemeja")

    def tampil_opsi_pakaian(self):
        for key, value in self.jenis_baju.items():
            print(f"{key}.- {value}")

    def tampil_jenis_sablon(self):
        i = 1
        for key, value in self.jenis_sablon.items():
            print(f"{key}.-{value}: Rp{self.harga_sablon[i]}")
            i += 1

    def tampil_bahan(self):
        i = 1
        for key, value in self.bahan.items():
            print(f"{key}.-{value}: Rp{self.harga_bahan[i]}")
            i += 1

    def tampil_merk(self):
        i = 1
        for key, value in self.merk.items():
            print(f"{key}.-{value}: Rp{self.harga_merk[i]}")
            i += 1

    def main_menu(self, fashion, data):
        beli = True
        while beli:
            kaos = Kaos()
            kemeja = Kemeja()
            print("1. admin")
            print("2. pembeli")
            print("3. exit")
            user = input("Siapa Anda?\npilih opsi:   ")
            if user in ["1", "admin"]:
                print("\n== Kelola Data ==")
                print("1. Read/Show Data")
                print("2. Delete Data")
                print("3. Update Data")
                show = input("Apa yang ingin Anda lakukan?(1/2): ")
                if show in ["1", "tampil data"]:
                    self.tampilkan_data()
                    lihatData = input("Pilih opsi: ")
                    if lihatData == '1':
                        db._Database__display_all_data(db_con, "kaos_sablon")
                    elif lihatData == '2':
                        db._Database__display_all_data(db_con, "kaos_tidak_sablon")
                    elif lihatData == '3':
                        db._Database__display_all_data(db_con, "kemeja")
                    else:
                        print("oke")

                elif show in ["2", "hapus data"]:
                    print("\n== Pilih table==")
                    print("1. delete data kaos sablon")
                    print("2. delete data kaos tidak sablon")
                    print("3. delete data kemeja")
                    table_name = input("Tabel mana yang ingin anda tuju? (1/2/3): ")
                    id_delete = int(input("Masukkan ID yang akan dihapus: ")) 
                    if table_name in ["1", "kaos sablon"]:
                        db_sablon._db_KaosSablon__delete_sablon(db_con, id_delete)
                
                    elif table_name in ["2", "kaos tidak sablon"]:
                        db_tidak_sablon._db_KaosTidakSablon__delete_tidak_sablon(db_con, id_delete)
                
                    elif table_name in ["3", "kemeja"]:
                        db_kemeja._db_Kemeja__delete_kemeja(db_con, id_delete)

                elif show in ["3", "update data"]:
                    print("== Pilih table==")
                    print("1. update data kaos sablon")
                    print("2. update data kaos tidak sablon")
                    print("3. update data kemeja")
                    table_name = input("Tabel mana yang ingin anda tuju? (1/2/3): ")
                    if table_name in ["1", "kaos sablon", 'sablon']:
                        id_update = int(input("Id sablon yang ingin di-update: "))
                        db.get_data_by_id(db_con, "kaos_sablon", id_update)
                        menu.tampil_jenis_sablon()
                        numSablon = int(input("\npilih jenis sablon(1/2/3): "))
                        menu.tampil_ukuran()
                        ukuran = int(input("Masukkan ukuran Anda: "))
                        menu.tampil_bahan()
                        numbahan = int(input("Pilih bahan kaos(1/2/3):"))
                        bahan = menu.bahan[numbahan]
                        harga_bahan = menu.harga_bahan[numbahan]
                        depanBelakang = input("Sablon Depan dan belakang? (y/n): ")
                        sablon = kaos.sablon(numSablon, depanBelakang)
                        jenis_sablon = menu.jenis_sablon[numSablon]
                        if depanBelakang.lower() == 'y':
                            harga_sablon = 2 * self.harga_sablon[numSablon]
                            harga_total_sablon_1 = harga_bahan + harga_sablon
                            db_sablon._db_KaosSablon__update_data_kaos_sablon(db_con, id_update, "kaos", harga_total_sablon_1, ukuran, bahan, jenis_sablon)
                        elif depanBelakang.lower() == 'n':
                            harga_sablon = self.harga_sablon[numSablon]
                            harga_total_sablon_2 = harga_bahan + harga_sablon
                            db_sablon._db_KaosSablon__update_data_kaos_sablon(db_con, id_update, "kaos", harga_total_sablon_2, ukuran, bahan, jenis_sablon)


                    elif table_name in ["2", "kaos tidak sablon", 'tidak sablon']:
                        id_tdk_sablon = int(input("Id Kaos Tidak Sablon yang ingin di-updat: e"))
                        db.get_data_by_id(db_con, "kaos_tidak_sablon", id_tdk_sablon)
                        menu.tampil_ukuran()
                        ukuran = int(input("Masukkan ukuran Anda: "))
                        menu.tampil_bahan()
                        numbahan = int(input("Pilih bahan kaos(1/2/3):"))
                        bahan = menu.bahan[numbahan]
                        harga_bahan = menu.harga_bahan[numbahan]
                        menu.tampil_merk()
                        pilih_merk = int(input("\nmerk mana yang Anda inginkan:"))
                        merk = self.merk[pilih_merk]
                        harga_merk = self.harga_merk[pilih_merk]
                        harga_total = harga_bahan + harga_merk

                        db_tidak_sablon._db_KaosTidakSablon__update_data_kaos_tidak_sablon(db_con, id_tdk_sablon, "kaos", harga_total, ukuran, bahan, merk)

                    elif table_name in ["3", "kemeja", "kemeja batik"]:
                        id_kemeja = int(input("masukkan Id Kemeja yang ingin di-update: "))
                        db.get_data_by_id(db_con, "kemeja", id_kemeja)
                        menu.tampil_ukuran()
                        ukuran = int(input("Masukkan ukuran Anda: "))
                        menu.lihat_motif_baju()
                        numkemeja = int(input("Pilih motif kemeja(1/2/3): "))
                        motif = kemeja.pilih_motif_kemeja(numkemeja)
                        motif_batik = motif['kemeja batik']
                        harga_batik = motif['harga kemeja']

                        db_kemeja._db_Kemeja__update_data_kemeja(db_con, id_kemeja, "kemeja", harga_batik, ukuran, motif_batik)

                    

            elif user in ["2", "pembeli"]:
                baju = Baju()
                self.tampil_opsi_pakaian()
                opsi = input("Pakaian apa yang ingin Anda beli: ")
                jenis_baju= baju.pilih_jenis_baju(opsi)
                self.tampil_ukuran()
                ukuran = int(input("Ukuran lengan Anda: "))
                if ukuran > 18:
                    print("Ukuran Tidak Tersedia")
                else: 
                    baju.size_of_item(ukuran)
                    print(f"Ukuran Anda: {baju.size_of_item(ukuran)}")
                    if opsi in ["1", "kaos"] :
                        self.tampil_bahan()                
                        pilih_bahan = int(input("Pilih bahan kaos: "))
                        bahan = self.bahan[pilih_bahan]
                        harga_bahan = self.harga_bahan[pilih_bahan]
                        isSablon = input("\nApakah kaos Anda ingin disablon?(y/n): ")
                        if isSablon == "y".lower():
                            self.tampil_jenis_sablon()
                            numSablon = int(input("\npilih jenis sablon(1/2/3): "))
                            depanBelakang = input("Sablon Depan dan belakang? (y/n): ")
                            sablon = kaos.sablon(numSablon, depanBelakang)
                            jenis_sablon = self.jenis_sablon[numSablon]
                            if depanBelakang.lower() == 'y':
                                harga_sablon = 2 * self.harga_sablon[numSablon]
                                harga_total = harga_bahan + harga_sablon
                                pembeli_sablon = Pembeli(jenis_baju, harga_sablon, ukuran, None, bahan, None, jenis_sablon)
                                data.add_inventory(pembeli_sablon)
                                db_sablon.insert_data_kaos_sablon(db_con, jenis_baju, harga_total, ukuran, bahan, jenis_sablon)

                            elif depanBelakang.lower() == 'n':
                                harga_sablon = self.harga_sablon[numSablon]
                                harga_total = harga_bahan + harga_sablon
                                pembeli_sablon = Pembeli(jenis_baju, harga_total, ukuran, None, bahan, None, jenis_sablon)
                                data.add_inventory(pembeli_sablon)
                                db_sablon.insert_data_kaos_sablon(db_con, "kemeja", harga_total, ukuran, bahan, jenis_sablon)

                            

                        elif isSablon == "n".lower():
                            self.tampil_merk()
                            pilih_merk = int(input("\nmerk mana yang Anda inginkan:"))
                            merk = self.merk[pilih_merk]
                            harga_merk = self.harga_merk[pilih_merk]
                            harga_total = harga_bahan + harga_merk
                            print(f"Anda memilih merk {merk} dengan harga Rp{harga_merk} sehingga totalnya menjadi Rp{harga_total}")
                            pembeli_merk = Pembeli(jenis_baju, harga_total, ukuran, merk, bahan, None, None)
                            data.add_inventory(pembeli_merk)
                            db_KaosTidakSablon.insert_data_kaos_tidak_sablon(db_con, jenis_baju, harga_total, ukuran, bahan, merk)


                    elif opsi in ["2", "kemeja"]:
                        menu.lihat_motif_baju()
                        pilihMotif = int(input("Pilih motif kemeja: "))
                        motif = kemeja.pilih_motif_kemeja(pilihMotif)
                        motif_batik = motif['kemeja batik']
                        harga_batik = motif['harga kemeja']
                        print(f"Anda memilih batik {motif_batik} dengan harga Rp{harga_batik}\n")
                        pembeli_kemeja = Pembeli(jenis_baju, harga_batik, ukuran, None, None, motif_batik, None)
                        data.add_inventory(pembeli_kemeja)
                        db_kemeja.insert_data_kemeja(db_con ,jenis_baju, harga_batik, ukuran, motif_batik)

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
            return f"Sablon {sablon}", menu.harga_sablon[sablon], menu.harga_bahan[1]
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
    def __init__(self, jenis=None, harga=None, ukuran=None, merk=None, bahan=None, motif=None, jenis_sablon=None):
        super().__init__(jenis, harga, ukuran, merk=None, bahan=None, motif=None, jenis_sablon=None)
        self.inventory = []

    def add_inventory(self, item=None):
        if item is not None:
            self.inventory.append(item)
        else:
            print("\nBelum ada data\n")
        
                

if __name__ == "__main__":
    # membuat objek dari kelas Database
    db = Database()
    db_con = db.connect_db()
    db_sablon = db_KaosSablon()
    db_tidak_sablon = db_KaosTidakSablon()
    db_kemeja = db_Kemeja()

    # membuat objek dari class laiinnya
    menu = Menu_Items()
    fashion = FashionShop()
    data = DataPembelian()

    # membuat table dan database
    db.create_database(db_con)
    db_sablon.create_table_kaos_sablon(db_con)
    db_tidak_sablon.create_table_kaos_tidak_sablon(db_con)
    db_kemeja.create_table_kemeja(db_con)
    pause()
    os.system("cls")

    
    # menjalankan program
    menu.main_menu(fashion, data)    
         
