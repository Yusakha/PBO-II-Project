import wx, ui
from sql import connection

class sub(connection, ui.fitur_login):
    def __init__(self, parent):
        super().__init__()
        ui.fitur_login.__init__(self, parent)

    def btn_loginOnButtonClick( self, event ):
        self.username = self.form_username.GetValue().lower()
        self.password = self.form_password.GetValue()
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
        for i in range(len(tempUsername)):
            if self.username == tempUsername[i] and self.password == tempPassword[i]:
                self.namaUser = tempNama[i]
                self.UserID = tempUserID[i]
                print("Login Sucsess\n")
                if tempRole[i] == "Owner":
                    resp = wx.MessageBox('Login Sukses. Klik OK untuk melanjutkan,', 'Login Sukses', wx.OK | wx.ICON_WARNING)
                    # self.ownerMenu()
                else:
                    resp = wx.MessageBox('Login Sukses. Klik OK untuk melanjutkan,', 'Login Sukses', wx.OK | wx.ICON_WARNING)
                    # self.karyawanMenu()
            else:
                tempJ += 1
                if tempJ != len(tempUsername):
                    pass
                else :
                    pass
                    # y = input("Login Failed. Silahkan coba lagi\nKetik 'exit' untuk exit : ").lower()
                    resp = wx.MessageBox('Login Failed. Silahkan coba lagi?', 'Login Gagal', wx.OK | wx.ICON_ERROR)

if __name__ == '__main__':
    app = wx.App()
    frame = sub(parent=None)
    frame.Show()
    app.MainLoop()