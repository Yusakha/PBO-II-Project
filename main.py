import wx, ui
from sql import connection
from datetime import datetime
from view import messages

class login(connection, ui.fitur_login):
    def __init__(self, parent):
        ui.fitur_login.__init__(self, parent)
        super().__init__()

    def btn_loginOnButtonClick( self, event ):
        self.username = self.form_username.GetValue().lower()
        self.password = self.form_password.GetValue()
        self.title = 'Login'
        tempNama = []
        tempUsername = []
        tempPassword = []
        tempRole = []
        tempUserID = []
        tempJ = 0
        query = ('SELECT ID_Person, Nama, username, password, role FROM person')
        for x in self.fetch_all(query):
            tempUserID.append(x[0])
            tempNama.append(x[1])
            tempUsername.append(x[2])
            tempPassword.append(x[3])
            tempRole.append(x[4])
        if len(self.username) == 0:
            messages(self, 'username', self.title, 'E').kosong()
        else:
            if len(self.password) == 0:
                messages(self, 'password', self.title, 'E').kosong()
            else:
                for i in range(len(tempUsername)):
                    if self.username == tempUsername[i] and self.password == tempPassword[i]:
                        self.namaUser = tempNama[i]
                        self.UserID = tempUserID[i]
                        if tempRole[i] == "Owner":
                            messages(self, self.namaUser, self.title, 'S').login()
                            mod = "Owner"
                            self.panel_formlogin.Show(False)
                            admin(self, mod, self.UserID).Show(True)
                        else:
                            messages(self, self.namaUser, self.title, 'S').login()
                            mod = "Karyawan"
                            self.panel_formlogin.Show(False)
                            karyawan(self, mod, self.UserID).Show(True)
                    else:
                        tempJ += 1
                        if tempJ != len(tempUsername):
                            pass
                        else :
                            messages(self, '', self.title, 'E').login()

class karyawan(connection, ui.Fiturkaryawan):
    def __init__(self, parent, mod, user):
        ui.Fiturkaryawan.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.title = 'Exit'
    def btn_barang_karyawanOnButtonClick( self, event ):
        self.panel_fiturkaryawan.Show(False)
        dataBarang(self, self.mod, self.user).Show(True)
    def btn_history_karyawanOnButtonClick( self, event ):
        self.panel_fiturkaryawan.Show(False)
        dataHistory(self, self.mod, self.user).Show(True)
    def btn_karyawan_exitOnButtonClick( self, event ):
        self.close()
        messages(self, '', self.title, 'S').exit()
        exit()

class admin(connection, ui.Fituradmin):
    def __init__(self, parent, mod, user):
        ui.Fituradmin.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.title = 'Exit'
    def btn_admin_kepegawaianOnButtonClick( self, event ):
        self.panel_fituradmin.Show(False)
        dataKaryawan(self, self.mod, self.user).Show(True)
    def btn_admin_barangOnButtonClick( self, event ):
        self.panel_fituradmin.Show(False)
        dataBarang(self, self.mod, self.user).Show(True)
    def btn_admin_historyOnButtonClick( self, event ):
        self.panel_fituradmin.Show(False)
        dataHistory(self, self.mod, self.user).Show(True)
    def btn_admin_exitOnButtonClick( self, event ):
        self.close()
        messages(self, '', self.title, 'S').exit()
        exit()

class dataKaryawan(connection, ui.tabel_data_karyawan):
    def __init__(self, parent, mod, user):
        ui.tabel_data_karyawan.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.select()
    def select(self):
        query = "SELECT ID_Person,Nama,Umur,Jenis_Kelamin,username,password FROM person WHERE Role='Karyawan'"
        result = self.fetch_all(query)
        for row in range(len(result)):
            for col in range(6):
                self.tabel_data_karyawan1.SetCellValue(row, col, f"{result[row][col]}")
    def btn_back_tabel_karyawanOnButtonClick( self, event ):
        self.panel_tabelkaryawan.Show(False)
        if (self.mod == "Owner"):
            admin(self, self.mod, self.user).Show(True)
        else:
            karyawan(self, self.mod, self.user).Show(True)
    def btn_tambah_tabelkaryawanOnButtonClick( self, event ):
        tambahKaryawan(self, self.mod, self.user).Show(True)
        self.panel_tabelkaryawan.Show(False)
    def btn_edit_karyawanOnButtonClick( self, event ):
        idKaryawan(self, self.mod, self.user).Show(True)
        self.panel_tabelkaryawan.Show(False)

class idKaryawan(connection, ui.form_id_karyawan):
    def __init__(self, parent, mod, user):
        ui.form_id_karyawan.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.title = 'ID karyawan'
        self.select()
    def select(self):
        query = "SELECT ID_Person,Nama FROM person WHERE Role='Karyawan'"
        result = self.fetch_all(query)
        for row in range(len(result)):
            for col in range(2):
                self.tabel_edit_karyawan.SetCellValue(row, col, f"{result[row][col]}")
    def check(self, karyawanID):
        query = f"SELECT Nama FROM person WHERE Role='Karyawan' AND ID_Person ='{karyawanID}'"
        result = self.fetch_all(query)
        if len(result) == 1:
            return True
        else:
            return False
    def btn_OKOnButtonClick( self, event ):
        self.id = self.input_id_karyawan.GetValue()
        try:
            int(self.input_id_karyawan.GetValue())
            if self.check(self.id):
                editKaryawan(self, self.mod, self.user, self.id).Show(True)
                self.panel_tabelkaryawan.Show(False)
            else:
                messages(self, 'ID karyawan', self.title, 'E').unknown()
        except ValueError:
            messages(self, 'Stock', self.title, 'E').value()
    def btn_back_tabel_karyawanOnButtonClick( self, event ):
        self.panel_tabelkaryawan.Show(False)
        dataKaryawan(self, self.mod, self.user).Show(True)

class tambahKaryawan(connection, ui.form_tambah_karyawan):
    def __init__(self, parent, mod, user):
        ui.form_tambah_karyawan.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.title = 'Tambah karyawan'
    def checkUsername(self,username):
        query = f"SELECT username FROM person WHERE username = '{username}'"
        result = self.fetch_all(query)
        return result
    def btn_simpan_tambah_karyawanOnButtonClick( self, event ):
        self.nama = self.input_karyawan.GetValue()
        self.umur = self.input_umur_karyawan.GetValue()
        self.jenisKelamin = self.input_jeniskelamin_karyawan.GetValue().upper()
        self.username = self.input_username_karyawan.GetValue().lower()
        self.role = "Karyawan"
        self.password = self.input_password_karyawan.GetValue()
        try:
            if len(self.nama) == 0:
                messages(self, 'nama karyawan', self.title, 'E').kosong()
            else:
                if len(self.umur) == 0:
                    messages(self, 'umur', self.title, 'E').kosong()
                else:
                    try:
                        int(self.umur)
                        if len(self.jenisKelamin) == 0:
                            messages(self, 'jenis kelamin', self.title, 'E').kosong()
                        elif self.jenisKelamin == 'L' or self.jenisKelamin == 'P':
                            if len(self.username) == 0:
                                messages(self, 'username', self.title, 'E').kosong()
                            else:
                                if (len(self.checkUsername(self.username))==0):
                                    if len(self.password) == 0:
                                        messages(self, 'password', self.title, 'E').kosong()
                                    else:
                                        self.created = datetime.now()
                                        sql = "INSERT INTO person (Nama, Umur, Jenis_Kelamin, Role, username, password, created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                        val = (self.nama, self.umur, self.jenisKelamin, self.role, self.username, self.password, self.created)
                                        self.commit(sql, val)
                                        messages(self, 'menambahkan karyawan', self.title, 'S').sukses()
                                        self.panel_tambahpegawai.Show(False)
                                        dataKaryawan(self, self.mod, self.user).Show(True)
                                else:
                                    messages(self, 'username', self.title, 'E').used()
                        else:
                            messages(self, 'jenis kelamin', self.title, 'E').gender()
                    except ValueError:
                        messages(self, 'umur', self.title, 'E').value()
        except:
            messages(self, 'menambahkan', self.title, 'E').invalid()
    def btn_batal_tambahOnButtonClick( self, event ):
        messages(self, 'menambahkan karyawan', self.title, 'E').batal()
        self.panel_tambahpegawai.Show(False)
        dataKaryawan(self, self.mod, self.user).Show(True)

class editKaryawan(connection, ui.form_edit_karyawan):
    def __init__(self, parent, mod, user, idKaryawan):
        ui.form_edit_karyawan.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.id = idKaryawan
        self.title = "Edit karyawan"
        self.select(self.id)
    def checkUsername(self,username):
        query = f"SELECT username FROM person WHERE username = '{username}' EXCEPT SELECT username FROM person WHERE ID_Person = '{self.id}'"
        result = self.fetch_all(query)
        return result
    def select(self, idKaryawan):
        query = f"SELECT Nama,Umur,Jenis_Kelamin,username,password FROM person WHERE Role='Karyawan' AND ID_Person ='{idKaryawan}'"
        result = self.fetch_all(query)
        self.nama = result[0][0]
        self.umur = result[0][1]
        self.jenisKelamin = result[0][2]
        self.username = result[0][3]
        self.password = result[0][4]
        self.input_edit_karyawan.SetValue(self.nama)
        self.input_edit_umur_karyawan.SetValue(str(self.umur))
        self.input_edit_jeniskelamin_karyawan.SetValue(self.jenisKelamin)
        self.input_edit_username_karyawan.SetValue(self.username)
        self.input_edit_password_karyawan.SetValue(self.password)
    def btn_edit_simpan_karyawanOnButtonClick( self, event ):
        self.nama = self.input_edit_karyawan.GetValue()
        self.umur = self.input_edit_umur_karyawan.GetValue()
        self.jenisKelamin = self.input_edit_jeniskelamin_karyawan.GetValue().upper()
        self.username = self.input_edit_username_karyawan.GetValue().lower()
        self.password = self.input_edit_password_karyawan.GetValue()
        try:
            if len(self.nama) == 0:
                messages(self, 'nama karyawan', self.title, 'E').kosong()
            else:
                if len(self.umur) == 0:
                    messages(self, 'umur', self.title, 'E').kosong()
                else:
                    try:
                        int(self.umur)
                        if len(self.jenisKelamin) == 0:
                            messages(self, 'jenis kelamin', self.title, 'E').kosong()
                        elif self.jenisKelamin == 'L' or self.jenisKelamin == 'P':
                            if len(self.username) == 0:
                                messages(self, 'username', self.title, 'E').kosong()
                            else:
                                if (len(self.checkUsername(self.username))==0):
                                    if len(self.password) == 0:
                                        messages(self, 'password', self.title, 'E').kosong()
                                    else:
                                        query = f"UPDATE person SET Nama = '{self.nama}', Umur = '{self.umur}', Jenis_Kelamin = '{self.jenisKelamin}', username = '{self.username}', password ='{self.password}' WHERE ID_Person = '{self.id}'"
                                        self.fetch_one(query)
                                        messages(self, 'mengedit karyawan', self.title, 'S').sukses()
                                        self.panel_tambahpegawai.Show(False)
                                        dataKaryawan(self, self.mod, self.user).Show(True)
                                else:
                                    messages(self, 'username', self.title, 'E').used()
                        else:
                            messages(self, '', self.title, 'E').gender()
                    except ValueError:
                        messages(self, 'umur', self.title, 'E').value()
        except:
            messages(self, 'mengedit', self.title, 'E').invalid()
    def btn_edit_batal_karyawanOnButtonClick( self, event ):
        messages(self, 'mengedit karyawan', self.title, 'E').batal()
        self.panel_tambahpegawai.Show(False)
        dataKaryawan(self, self.mod, self.user).Show(True)
    def btn_hapus_karyawanOnButtonClick( self, event ):
        try:
            query = f"DELETE FROM person WHERE ID_Person = {self.id}"
            self.fetch_one(query)
            messages(self, 'karyawan', self.title, 'S').hapus()
            self.panel_tambahpegawai.Show(False)
            dataKaryawan(self, self.mod, self.user).Show(True)
        except:
            messages(self, 'menghapus', self.title, 'E').invalid()

class dataBarang(connection, ui.tabel_data_barang):
    def __init__(self, parent, mod, user):
        ui.tabel_data_barang.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.select()
    def select(self):
        query = "SELECT * FROM barang"
        result = self.fetch_all(query)
        for row in range(len(result)):
            for col in range(5):
                self.tabelbarang.SetCellValue(row, col, f"{result[row][col]}")
    def btn_tambah_barangOnButtonClick( self, event ):
        tambahBarang(self, self.mod, self.user).Show(True)
        self.panel_tabelbarang.Show(False)
    def btn_edit_barangOnButtonClick( self, event ):
        idBarang(self, self.mod, self.user).Show(True)
        self.panel_tabelbarang.Show(False)
    def btn_back_tabelbarangOnButtonClick( self, event ):
        self.panel_tabelbarang.Show(False)
        if (self.mod == "Owner"):
            admin(self, self.mod, self.user).Show(True)
        else:
            karyawan(self, self.mod, self.user).Show(True)

class tambahBarang(connection, ui.form_tambah_barang):
    def __init__(self, parent, mod, user):
        ui.form_tambah_barang.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.title = "Tambah barang"
    def checkNama(self,nama):
        query = f"SELECT Nama_Barang FROM barang WHERE Nama_Barang = '{nama}'"
        result = self.fetch_all(query)
        return result
    def btn_simpan_tambah_barangOnButtonClick( self, event ):
        self.nama = self.input_nama_barang.GetValue()
        self.stok = self.input_stock_barang.GetValue()
        self.satuan = self.input_satuan_barang.GetValue().lower()
        self.tahun = self.input_tahunkadaluarsa_barang.GetValue()
        self.bulan = self.input_bulankadaluarsa_barang.GetValue()
        self.hari = self.input_tanggalkadaluarsa_barang.GetValue()
        try:
            if len(self.nama) == 0:
                messages(self, 'nama barang', self.title, 'E').kosong()
            else:
                if (len(self.checkNama(self.nama))==0):
                    if len(self.stok) == 0:
                        messages(self, 'stock', self.title, 'E').kosong()
                    else:
                        try:
                            int(self.stok)
                            if len(self.satuan) == 0:
                                messages(self, 'satuan', self.title, 'E').kosong()
                            else:
                                if len(self.tahun) == 0:
                                    messages(self, 'tahun', self.title, 'E').kosong()
                                else:
                                    try:
                                        int(self.tahun)
                                        if len(str(self.tahun)) != 4 or int(self.tahun) > 9999 or int(self.tahun) < int(datetime.now().strftime("%Y")):
                                            messages(self, 'tahun', self.title, 'E').date()
                                        else:
                                            if len(self.bulan) == 0:
                                                messages(self, 'bulan', self.title, 'E').kosong()
                                            else:
                                                try:
                                                    int(self.bulan)
                                                    if int(self.bulan) > 12 or int(self.bulan) < 1:
                                                        messages(self, 'bulan', self.title, 'E').date()
                                                    else:
                                                        if len(self.hari) == 0:
                                                            messages(self, 'tanggal', self.title, 'E').kosong()
                                                        elif int(self.hari) > 32 or int(self.hari) < 1:
                                                            messages(self, 'tanggal', self.title, 'E').date()
                                                        else:
                                                            try:
                                                                int(self.hari)
                                                                self.tanggal = f"{self.tahun}-{self.bulan}-{self.hari}"
                                                                sql = "INSERT INTO barang (Nama_Barang , Jumlah_Barang , Satuan, Tanggal_Kadaluarsa) VALUES (%s, %s, %s, %s)"
                                                                val = (self.nama, self.stok, self.satuan, self.tanggal)
                                                                self.commit(sql, val)
                                                                sql =  "SELECT ID_Barang FROM barang WHERE Nama_Barang = '{}'".format(self.nama)
                                                                res = self.fetch_one(sql)
                                                                for x in res :
                                                                    self.barangID = x
                                                                sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
                                                                val = (self.user, self.barangID, "Input", self.stok, self.satuan, datetime.now())
                                                                self.commit(sql, val)                                  
                                                                messages(self, 'menambahkan barang', self.title, 'S').sukses()
                                                                self.panel_tambahbarang.Show(False)
                                                                dataBarang(self, self.mod, self.user).Show(True)
                                                            except ValueError:
                                                                messages(self, 'hari kadaluarsa', self.title, 'E').value()
                                                except ValueError:
                                                    messages(self, 'bulan kadaluarsa', self.title, 'E').value()
                                    except ValueError:
                                        messages(self, 'tahun kadaluarsa', self.title, 'E').value()
                        except ValueError:
                                messages(self, 'stock', self.title, 'E').value()
                else:
                    messages(self, 'nama barang', self.title, 'E').used()
        except:
            messages(self, 'menambahkan ', self.title, 'E').invalid()
    def btn_batal_tambah_barangOnButtonClick( self, event ):
        messages(self, 'menambahkan barang', self.title, 'E').batal()
        self.panel_tambahbarang.Show(False)
        dataBarang(self, self.mod, self.user).Show(True)

class idBarang(connection, ui.form_id_barang):
    def __init__(self, parent, mod, user):
        ui.form_id_barang.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.title = 'ID barang'
        self.select()
    def select(self):
        query = "SELECT ID_Barang,Nama_Barang FROM barang"
        result = self.fetch_all(query)
        for row in range(len(result)):
            for col in range(2):
                self.tabel_edit_barang.SetCellValue(row, col, f"{result[row][col]}")
    def check(self, barangID):
        query = f"SELECT Nama_Barang FROM barang WHERE ID_Barang ='{barangID}'"
        result = self.fetch_all(query)
        if len(result) == 1:
            return True
        else:
            return False
    def btn_OKOnButtonClick( self, event ):
        self.id = self.input_id_barang.GetValue()
        try:
            int(self.input_id_barang.GetValue())
            if self.check(self.id):
                editBarang(self, self.mod, self.user, self.id).Show(True)
                self.panel_tabelbarang.Show(False)
            else:
                messages(self, self.title, self.title, 'E').unknown()
        except ValueError:
            messages(self, self.title, self.title, 'E').value()
    def btn_back_tabelbarangOnButtonClick( self, event ):
        self.panel_tabelbarang.Show(False)
        dataBarang(self, self.mod, self.user).Show(True)

class editBarang(connection, ui.form_edit_barang):
    def __init__(self, parent, mod, user, idBarang):
        ui.form_edit_barang.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.id = idBarang
        self.title = 'Edit barang'
        self.select(self.id)
    def checkNamaBarang(self,nama):
        query = f"SELECT Nama_Barang FROM barang WHERE Nama_Barang = '{nama}' EXCEPT SELECT Nama_Barang FROM barang WHERE ID_Barang = {self.id}"
        result = self.fetch_all(query)
        return result
    def select(self, barangID):
        query = f"SELECT Nama_Barang,Jumlah_Barang,Satuan,Tanggal_Kadaluarsa FROM barang WHERE ID_Barang ='{barangID}'"
        result = self.fetch_all(query)
        self.nama = result[0][0]
        self.jumlah = result[0][1]
        self.satuan = result[0][2]
        self.tanggal = result[0][3]
        self.tahun = result[0][3].strftime("%Y")
        self.bulan = result[0][3].strftime("%m")
        self.hari = result[0][3].strftime("%d")
        self.input_edit_namabarang_barang.SetValue(self.nama)
        self.input_edit_stockbarang_barang.SetValue(str(self.jumlah))
        self.input_edit_satuanbarang_barang.SetValue(self.satuan)
        self.input_edit_tahunkadaluarsa_barang.SetValue(self.tahun)
        self.input_edit_bulankadaluarsa_barang.SetValue(self.bulan)
        self.input_edit_tanggalkadaluarsa_barang.SetValue(self.hari)
    def btn_edit_simpan_barangOnButtonClick( self, event ):
        self.nama = self.input_edit_namabarang_barang.GetValue()
        self.stok = self.input_edit_stockbarang_barang.GetValue()
        self.satuan = self.input_edit_satuanbarang_barang.GetValue().lower()
        self.tahun = self.input_edit_tahunkadaluarsa_barang.GetValue()
        self.bulan = self.input_edit_bulankadaluarsa_barang.GetValue()
        self.hari = self.input_edit_tanggalkadaluarsa_barang.GetValue()
        try:
            if len(self.nama) == 0:
                messages(self, 'nama barang', self.title, 'E').kosong()
            else:
                if (len(self.checkNamaBarang(self.nama))==0):
                    if len(self.stok) == 0:
                        messages(self, 'stock', self.title, 'E').kosong()
                    else:
                        try:
                            int(self.stok)
                            if len(self.satuan) == 0:
                                messages(self, 'satuan', self.title, 'E').kosong()
                            else:
                                if len(self.tahun) == 0:
                                    messages(self, 'tahun kadaluarsa', self.title, 'E').kosong()
                                else:
                                    try:
                                        int(self.tahun)
                                        if len(str(self.tahun)) != 4 or int(self.tahun) > 9999 or int(self.tahun) < int(datetime.now().strftime("%Y")):
                                            messages(self, 'tahun', self.title, 'E').date()
                                        else:
                                            if len(self.bulan) == 0:
                                                messages(self, 'tahun kadaluarsa', self.title, 'E').kosong()
                                            else:
                                                try:
                                                    int(self.bulan)
                                                    if int(self.bulan) > 12 or int(self.bulan) < 1:
                                                        messages(self, 'bulan', self.title, 'E').date()
                                                    else:
                                                        if len(self.hari) == 0:
                                                            messages(self, 'tanggal kadaluarsa', self.title, 'E').kosong()
                                                        elif len(str(self.hari)) > 2 or len(str(self.hari)) < 0 or int(self.hari) > 32 or int(self.hari) < 1:
                                                            messages(self, 'tanggal', self.title, 'E').date()
                                                        else:
                                                            try:
                                                                int(self.hari)
                                                                self.tanggal = f"{self.tahun}-{self.bulan}-{self.hari}"
                                                                sql = "UPDATE barang SET Nama_Barang ='{}', Jumlah_Barang ='{}', Satuan='{}', Tanggal_Kadaluarsa='{}' WHERE ID_barang='{}'".format(self.nama, self.stok, self.satuan, self.tanggal, self.id)
                                                                self.fetch_one(sql)
                                                                sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
                                                                val = (self.user, self.id, "Adjust", self.stok, self.satuan, datetime.now())
                                                                self.commit(sql, val)
                                                                messages(self, 'edit barang', self.title, 'S').sukses()
                                                                self.panel_editbarang.Show(False)
                                                                dataBarang(self, self.mod, self.user).Show(True)
                                                            except ValueError:
                                                                messages(self, 'tanggal', self.title, 'E').value()
                                                except ValueError:
                                                    messages(self, 'bulan', self.title, 'E').value()
                                    except ValueError:
                                        messages(self, 'tahun', self.title, 'E').value()
                        except ValueError:
                                messages(self, 'stock', self.title, 'E').value()
                else:
                    messages(self, 'nama barang', self.title, 'E').used()
        except:
            messages(self, 'mengedit', self.title, 'E').invalid()
    def btn_edit_batal_barangOnButtonClick( self, event ):
        messages(self, 'mengedit karyawan', self.title, 'E').batal()
        self.panel_editbarang.Show(False)
        dataBarang(self, self.mod, self.user).Show(True)
    def btn_hapus_barangOnButtonClick( self, event ):
        try:
            query = f"DELETE FROM barang WHERE ID_Barang = {self.id}"
            self.fetch_one(query)
            messages(self, 'barang', self.title, 'S').hapus()
            self.panel_editbarang.Show(False)
            dataBarang(self, self.mod, self.user).Show(True)
        except:
            messages(self, 'menghapus', self.title, 'E').invalid()
    def btn_input_barangOnButtonClick( self, event ):
        self.panel_editbarang.Show(False)
        inputBarang(self, self.mod, self.user, self.id).Show(True)
    def btn_ambil_barangOnButtonClick( self, event ):
        self.panel_editbarang.Show(False)
        ambilBarang(self, self.mod, self.user, self.id).Show(True)

class inputBarang(connection, ui.form_input_barang):
    def __init__(self, parent, mod, user, barangID):
        ui.form_input_barang.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.id = barangID
        self.title = "input barang"
        self.awal = self.select(self.id)
    def select(self, barangID):
        query = f"SELECT Nama_Barang,Jumlah_Barang FROM barang WHERE ID_Barang ='{self.id}'"
        result = self.fetch_all(query)
        self.nama = result[0][0]
        self.jumlah = result[0][1]
        self.read_nama_barang.SetValue(self.nama)
        self.read_stock_barang.SetValue(str(self.jumlah))
        return self.jumlah
    def btn_simpan_barangOnButtonClick( self, event ):
        self.input = self.input_input_barang.GetValue()
        try:
            if len(self.input) == 0:
                messages(self, 'stock', self.title, 'E').kosong()
            else:
                int(self.input)
                if int(self.input) < 1:
                    messages(self, 'stock', self.title, 'E').zero()
                else:
                    self.total = int(self.awal) + int(self.input)
                    sql = "UPDATE barang SET Jumlah_Barang = {} WHERE ID_Barang = {}".format(self.total,self.id)
                    self.fetch_one(sql)

                    sql =  "SELECT Satuan FROM barang WHERE ID_Barang = {}".format(self.id)
                    res = self.fetch_one(sql)
                    self.satuan = res[0][0]

                    sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (self.user, self.id, "Input", self.input, self.satuan, datetime.now())
                    self.commit(sql, val)

                    messages(self, 'input barang', self.title, 'S').sukses()
                    self.panel_input_barang.Show(False)
                    dataBarang(self, self.mod, self.user).Show(True)
        except ValueError:
            messages(self, 'stock', self.title, 'E').value()
    def btn_batal_barangOnButtonClick( self, event ):
        messages(self, 'menambahkan stock barang', self.title, 'E').batal()
        self.panel_input_barang.Show(False)
        dataBarang(self, self.mod, self.user).Show(True)

class ambilBarang(connection, ui.form_ambil_barang):
    def __init__(self, parent, mod, user, barangID):
        ui.form_ambil_barang.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.id = barangID
        self.title = "ambil barang"
        self.awal = self.select(self.id)
    def select(self, barangID):
        query = f"SELECT Nama_Barang,Jumlah_Barang FROM barang WHERE ID_Barang ='{self.id}'"
        result = self.fetch_all(query)
        self.nama = result[0][0]
        self.jumlah = result[0][1]
        self.read_nama_barang.SetValue(self.nama)
        self.read_stock_barang.SetValue(str(self.jumlah))
        return self.jumlah
    def btn_simpan_barangOnButtonClick( self, event ):
        self.ambil = self.input_ambil_barang.GetValue()
        try:
            if len(self.ambil) == 0:
                messages(self, 'stock', self.title, 'E').kosong()
            else:
                int(self.ambil)
                if int(self.ambil) < 1:
                    messages(self, 'stock', self.title, 'E').zero()
                else:
                    if int(self.ambil) > int(self.awal):
                        messages(self, 'stock barang', self.title, 'E').overload()
                    else:
                        self.total = int(self.awal) - int(self.ambil)
                        sql = "UPDATE barang SET Jumlah_Barang = {} WHERE ID_Barang = {}".format(self.total,self.id)
                        self.fetch_one(sql)

                        sql =  "SELECT Satuan FROM barang WHERE ID_Barang = {}".format(self.id)
                        res = self.fetch_one(sql)
                        self.satuan = res[0][0]

                        sql = "INSERT INTO history (PersonID, BarangID, Keterangan, Jumlah, Satuan, Tanggal) VALUES (%s, %s, %s, %s, %s, %s)"
                        val = (self.user, self.id, "Output", self.ambil, self.satuan, datetime.now())
                        self.commit(sql, val)

                        messages(self, 'mengambil barang', self.title, 'S').sukses()
                        self.panel_ambil_barang.Show(False)
                        dataBarang(self, self.mod, self.user).Show(True)
        except ValueError:
            messages(self, 'stock', self.title, 'E').value()
    def btn_batal_barangOnButtonClick( self, event ):
        messages(self, 'ambil barang', self.title, 'E').batal()
        self.panel_ambil_barang.Show(False)
        dataBarang(self, self.mod, self.user).Show(True)

class dataHistory(connection, ui.tabel_data_history):
    def __init__(self, parent, mod, user):
        ui.tabel_data_history.__init__(self, parent)
        super().__init__()
        self.mod = mod
        self.user = user
        self.select()
    def select(self):
        query = "SELECT * FROM history"
        result = self.fetch_all(query)
        for row in range(len(result)):
            for col in range(7):
                self.tabelhistory.SetCellValue(row, col, f"{result[row][col]}")
    def btn_back_historyOnButtonClick( self, event ):
        self.panel_tabelhistory.Show(False)
        if (self.mod == "Owner"):
            admin(self, self.mod, self.user).Show(True)
        else:
            karyawan(self, self.mod, self.user).Show(True)

if __name__ == '__main__':
    mod = ""
    app = wx.App()
    frame = login(parent=None)
    frame.SetIcon(wx.Icon("logo.png"))
    frame.Show(True)
    app.MainLoop()