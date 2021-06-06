from cursor import connection

class model(connection):
    def __init__(self):
        super().__init__()

    def login(self):
        query = ('SELECT ID_Person, Nama, username, password, role FROM person')
        return self.fetch_all(query)

    def dataKaryawan(self):
        query = "SELECT ID_Person,Nama,Umur,Jenis_Kelamin,username,password FROM person WHERE Role='Karyawan'"
        return self.fetch_all(query)

    def select_idKaryawan(self):
        query = "SELECT ID_Person,Nama FROM person WHERE Role='Karyawan'"
        return self.fetch_all(query)

    def check_idKaryawan(self, karyawanID):
        query = f"SELECT Nama FROM person WHERE Role='Karyawan' AND ID_Person ='{karyawanID}'"
        return self.fetch_all(query)

    def check_tambahKaryawan(self, username):
        query = f"SELECT username FROM person WHERE username = '{username}'"
        return self.fetch_all(query)

    def tambahKaryawan(self, nama, umur, jenisKelamin, role, username, password, created):
        sql = "INSERT INTO person (Nama, Umur, Jenis_Kelamin, Role, username, password, created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (nama, umur, jenisKelamin, role, username, password, created)
        return self.commit(sql, val)

    def check_editKaryawan(self, username, ids):
        query = f"SELECT username FROM person WHERE username = '{username}' EXCEPT SELECT username FROM person WHERE ID_Person = '{ids}'"
        return self.fetch_all(query)

    def select_editKaryawan(self, idKaryawan):
        query = f"SELECT Nama,Umur,Jenis_Kelamin,username,password FROM person WHERE Role='Karyawan' AND ID_Person ='{idKaryawan}'"
        return self.fetch_all(query)

    def editKaryawan(self, nama, umur, jenisKelamin, username, password, ids):
        query = f"UPDATE person SET Nama = '{nama}', Umur = '{umur}', Jenis_Kelamin = '{jenisKelamin}', username = '{username}', password ='{password}' WHERE ID_Person = '{ids}'"
        return self.fetch_one(query)
    
    def hapus_editKaryawan(self, ids):
        query = f"DELETE FROM person WHERE ID_Person = {ids}"
        return self.fetch_one(query)
    
    def select_dataBarang(self):
        query = "SELECT * FROM barang"
        return self.fetch_all(query)

    def check_tambahBarang(self, nama):
        query = f"SELECT Nama_Barang FROM barang WHERE Nama_Barang = '{nama}'"
        return self.fetch_all(query)

    def tambahBarang(self, nama, stok, satuan, tanggal, user, date):
        sql = "INSERT INTO barang (Nama_Barang , Jumlah_Barang , Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s)"
        val = (nama, stok, satuan, tanggal)
        self.commit(sql, val)
        sql =  f"SELECT ID_Barang FROM barang WHERE Nama_Barang = '{nama}'"
        res = self.fetch_one(sql)
        for x in res :
            barangID = x
        sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (user, barangID, "Input", stok, satuan, date)
        self.commit(sql, val)
        return

    def select_idBarang(self):
        query = "SELECT ID_Barang,Nama_Barang FROM barang"
        return self.fetch_all(query)

    def check_idBarang(self,barangID):
        query = f"SELECT Nama_Barang FROM barang WHERE ID_Barang ='{barangID}'"
        return self.fetch_all(query)

    def check_editBarang(self, nama, ids):
        query = f"SELECT Nama_Barang FROM barang WHERE Nama_Barang = '{nama}' EXCEPT SELECT Nama_Barang FROM barang WHERE ID_Barang = {ids}"
        return self.fetch_all(query)

    def select_editBarang(self, barangID):
        query = f"SELECT Nama_Barang,Jumlah_Barang,Satuan,Tanggal_Kadaluarsa FROM barang WHERE ID_Barang ='{barangID}'"
        return self.fetch_all(query)
    
    def editBarang(self, nama, stok, satuan, tanggal, ids, user, date):
        sql = "UPDATE barang SET Nama_Barang ='{}', Jumlah_Barang ='{}', Satuan='{}', Tanggal_Kadaluarsa='{}' WHERE ID_barang='{}'".format(nama, stok, satuan, tanggal, ids)
        self.fetch_one(sql)
        sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (user, ids, "Adjust", stok, satuan, date)
        self.commit(sql, val)
        return
    
    def hapus_editBarang(self, ids):
        query = f"DELETE FROM barang WHERE ID_Barang = {ids}"
        return self.fetch_one(query)

    def select_inputBarang(self, ids):
        query = f"SELECT Nama_Barang,Jumlah_Barang FROM barang WHERE ID_Barang ='{ids}'"
        return self.fetch_all(query)

    def inputBarang(self, total, ids, user, inputs, date):
        sql = "UPDATE barang SET Jumlah_Barang = {} WHERE ID_Barang = {}".format(total, ids)
        self.fetch_one(sql)
        sql =  "SELECT Satuan FROM barang WHERE ID_Barang = {}".format(ids)
        res = self.fetch_one(sql)
        satuan = res[0]
        sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (user, ids, "Input", inputs, satuan, date)
        self.commit(sql, val)
        return

    def select_ambilBarang(self,ids):
        query = f"SELECT Nama_Barang,Jumlah_Barang FROM barang WHERE ID_Barang ='{ids}'"
        return self.fetch_all(query)

    def ambil_ambilBarang(self, total, ids, user, ambil, date):
        sql = "UPDATE barang SET Jumlah_Barang = {} WHERE ID_Barang = {}".format(total,ids)
        self.fetch_one(sql)
        sql =  "SELECT Satuan FROM barang WHERE ID_Barang = {}".format(ids)
        res = self.fetch_one(sql)
        satuan = res[0]
        sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (user, ids, "Output", ambil, satuan, date)
        self.commit(sql, val)
        return