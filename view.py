import wx
class messages:
    def __init__(self, parent, message, title, icon):
        self.message = message
        self.title = title.capitalize()
        if icon == 'S':
            self.icon = wx.ICON_INFORMATION
        else:
            self.icon = wx.ICON_ERROR
    def basic(self):
        wx.MessageBox(self.message, self.title, wx.OK | self.icon)
    def login(self):
        if self.icon == 2048:
            self.messages = f"Login Sukses!\nSelamat datang {self.message}.\nKlik OK untuk melanjutkan."
            self.message = self.messages
        else:
            self.message = "Login Gagal!\nSilahkan coba login kembali."
        self.basic()
    def exit(self):
        self.message = "Berhasil keluar dari aplikasi."
        self.basic()
    def kosong(self):
        self.messages = f"Harap masukkan {self.message} pada kolom.\n{self.message.capitalize()} tidak boleh kosong!"
        self.message = self.messages
        self.basic()
    def date(self):
        self.messages = f"Harap masukkan {self.message} kadaluarsa dengan benar!"
        self.message = self.messages
        self.basic()
    def unknown(self):
        self.messages = f"Mohon maaf!\n{self.message} tidak tersedia!"
        self.message = self.messages
        self.basic()
    def used(self):
        self.messages = f"{self.message.capitalize()} telah digunakan.\nGunakan {self.message} yang lain."
        self.message = self.messages
        self.basic()
    def value(self):
        self.messages = f"Harap masukkan angka pada kolom {self.message.lower()}!"
        self.message = self.messages
        self.basic()
    def gender(self):
        self.message = f"Harap masukkan L/P pada jenis kelamin."
        self.basic()
    def invalid(self):
        self.messages = f"Ada yang error saat {self.message} data ke dalam database."
        self.message = self.messages
        self.basic()
    def sukses(self):
        self.messages = f"{self.message.capitalize()} telah berhasil!\nKlik OK untuk melanjutkan."
        self.message = self.messages
        self.basic()
    def batal(self):
        self.messages = f"{self.message.capitalize()} telah dibatalkan!\nKlik OK untuk melanjutkan."
        self.message = self.messages
        self.basic()
    def hapus(self):
        self.messages = f"Berhasil menghapus {self.message}!\nKlik OK untuk melanjutkan."
        self.message = self.messages
        self.basic()
    def zero(self):
        self.messages = f"{self.message.capitalize()} tidak boleh kurang dari 0!"
        self.message = self.messages
        self.basic()
    def overload(self):
        self.messages = f"{self.message.capitalize()} tidak boleh melebihi stock awal!"
        self.message = self.messages
        self.basic()