# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.adv

###########################################################################
## Class fitur_login
###########################################################################

class fitur_login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Montserrat Black" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.panel_formlogin = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer57 = wx.BoxSizer( wx.VERTICAL )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_formlogin = wx.StaticText( self.panel_formlogin, wx.ID_ANY, u"Form Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_formlogin.Wrap( -1 )

		self.teks_formlogin.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Black" ) )

		bSizer57.Add( self.teks_formlogin, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer57.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.teks_username = wx.StaticText( self.panel_formlogin, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_username.Wrap( -1 )

		self.teks_username.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer57.Add( self.teks_username, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.form_username = wx.TextCtrl( self.panel_formlogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		bSizer57.Add( self.form_username, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.teks_password = wx.StaticText( self.panel_formlogin, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_password.Wrap( -1 )

		self.teks_password.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer57.Add( self.teks_password, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.form_password = wx.TextCtrl( self.panel_formlogin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), wx.TE_PASSWORD )
		bSizer57.Add( self.form_password, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.btn_login = wx.Button( self.panel_formlogin, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_login.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.btn_login.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.btn_login.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		bSizer57.Add( self.btn_login, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_formlogin.SetSizer( bSizer57 )
		self.panel_formlogin.Layout()
		bSizer57.Fit( self.panel_formlogin )
		bSizer8.Add( self.panel_formlogin, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.teks_username.Bind( wx.EVT_CHAR, self.m_staticText2OnChar )
		self.btn_login.Bind( wx.EVT_BUTTON, self.btn_loginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_staticText2OnChar( self, event ):
		event.Skip()

	def btn_loginOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class listfitur_admin
###########################################################################

class listfitur_admin ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )


		bSizer15.Add( ( 0, 10), 1, 0, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer15.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer15.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_button46 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 450,35 ), 0 )
		bSizer15.Add( self.m_button46, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
		bSizer15.Add( self.m_button42, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button47 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
		bSizer15.Add( self.m_button47, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
		bSizer15.Add( self.m_button43, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class Fiturkaryawan
###########################################################################

class Fiturkaryawan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.panel_fiturkaryawan = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer49 = wx.BoxSizer( wx.VERTICAL )


		bSizer49.Add( ( 0, 0), 1, 0, 5 )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self.panel_fiturkaryawan, wx.ID_ANY, u"Fitur  Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer49.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer49.Add( ( 0, 0), 1, 0, 3 )

		self.btn_barang_karyawan = wx.Button( self.panel_fiturkaryawan, wx.ID_ANY, u"Administrasi Barang", wx.DefaultPosition, wx.Size( 450,35 ), 0 )
		self.btn_barang_karyawan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer49.Add( self.btn_barang_karyawan, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.btn_history_karyawan = wx.Button( self.panel_fiturkaryawan, wx.ID_ANY, u"History Transaksi", wx.DefaultPosition, wx.Size( 450,35 ), 0 )
		self.btn_history_karyawan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer49.Add( self.btn_history_karyawan, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_karyawan_exit = wx.Button( self.panel_fiturkaryawan, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		self.btn_karyawan_exit.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_karyawan_exit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.btn_karyawan_exit.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		bSizer49.Add( self.btn_karyawan_exit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_fiturkaryawan.SetSizer( bSizer49 )
		self.panel_fiturkaryawan.Layout()
		bSizer49.Fit( self.panel_fiturkaryawan )
		bSizer21.Add( self.panel_fiturkaryawan, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		# Connect Events
		self.btn_barang_karyawan.Bind( wx.EVT_BUTTON, self.btn_barang_karyawanOnButtonClick )
		self.btn_history_karyawan.Bind( wx.EVT_BUTTON, self.btn_history_karyawanOnButtonClick )
		self.btn_karyawan_exit.Bind( wx.EVT_BUTTON, self.btn_karyawan_exitOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_barang_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_history_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_karyawan_exitOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Fituradmin
###########################################################################

class Fituradmin ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.panel_fituradmin = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )


		bSizer56.Add( ( 0, 0), 1, 0, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.statis_adminfitur = wx.StaticText( self.panel_fituradmin, wx.ID_ANY, u"Fitur Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statis_adminfitur.Wrap( -1 )

		self.statis_adminfitur.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer56.Add( self.statis_adminfitur, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer56.Add( ( 0, 20), 1, 0, 3 )

		self.btn_admin_kepegawaian = wx.Button( self.panel_fituradmin, wx.ID_ANY, u"Administrasi Kepegawaian", wx.DefaultPosition, wx.Size( 450,35 ), 0 )
		self.btn_admin_kepegawaian.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer56.Add( self.btn_admin_kepegawaian, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.btn_admin_barang = wx.Button( self.panel_fituradmin, wx.ID_ANY, u"Administrasi Barang", wx.DefaultPosition, wx.Size( 450,35 ), 0 )
		self.btn_admin_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer56.Add( self.btn_admin_barang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.btn_admin_history = wx.Button( self.panel_fituradmin, wx.ID_ANY, u"History Transaksi", wx.DefaultPosition, wx.Size( 450,35 ), 0 )
		self.btn_admin_history.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer56.Add( self.btn_admin_history, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_admin_exit = wx.Button( self.panel_fituradmin, wx.ID_ANY, u"EXIT", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		self.btn_admin_exit.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_admin_exit.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_admin_exit.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		bSizer56.Add( self.btn_admin_exit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_fituradmin.SetSizer( bSizer56 )
		self.panel_fituradmin.Layout()
		bSizer56.Fit( self.panel_fituradmin )
		bSizer21.Add( self.panel_fituradmin, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		# Connect Events
		self.btn_admin_kepegawaian.Bind( wx.EVT_BUTTON, self.btn_admin_kepegawaianOnButtonClick )
		self.btn_admin_barang.Bind( wx.EVT_BUTTON, self.btn_admin_barangOnButtonClick )
		self.btn_admin_history.Bind( wx.EVT_BUTTON, self.btn_admin_historyOnButtonClick )
		self.btn_admin_exit.Bind( wx.EVT_BUTTON, self.btn_admin_exitOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_admin_kepegawaianOnButtonClick( self, event ):
		event.Skip()

	def btn_admin_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_admin_historyOnButtonClick( self, event ):
		event.Skip()

	def btn_admin_exitOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_tambah_karyawan
###########################################################################

class form_tambah_karyawan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.panel_tambahpegawai = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel18 = wx.Panel( self.panel_tambahpegawai, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29 = wx.BoxSizer( wx.VERTICAL )


		bSizer29.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"FORM TAMBAH PEGAWAI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer29.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer29.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel18.SetSizer( bSizer29 )
		self.m_panel18.Layout()
		bSizer29.Fit( self.m_panel18 )
		bSizer55.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel6 = wx.Panel( self.panel_tambahpegawai, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_pegawai.Wrap( -1 )

		self.teks_pegawai.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_karyawan, 0, wx.ALL, 5 )

		self.teks_umur_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Umur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_umur_pegawai.Wrap( -1 )

		self.teks_umur_pegawai.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_umur_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_umur_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_umur_karyawan, 0, wx.ALL, 5 )

		self.teks_jeniskelamin_karyawan = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_jeniskelamin_karyawan.Wrap( -1 )

		self.teks_jeniskelamin_karyawan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_jeniskelamin_karyawan, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_jeniskelamin_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_jeniskelamin_karyawan, 0, wx.ALL, 5 )

		self.teks_username_karyawan = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_username_karyawan.Wrap( -1 )

		self.teks_username_karyawan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_username_karyawan, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_username_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_username_karyawan, 0, wx.ALL, 5 )

		self.teks_password_karyawan = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_password_karyawan.Wrap( -1 )

		self.teks_password_karyawan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_password_karyawan, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_password_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		fgSizer5.Add( self.input_password_karyawan, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		self.m_staticText53.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.m_staticText53, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 200,-1 ), wx.FLP_DEFAULT_STYLE|wx.FLP_SAVE )
		fgSizer5.Add( self.m_filePicker2, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.btn_simpan_tambah_karyawan = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_simpan_tambah_karyawan.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.btn_simpan_tambah_karyawan, 0, wx.ALL, 5 )

		self.btn_batal_tambah = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_batal_tambah.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.btn_batal_tambah, 0, wx.ALL, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		fgSizer5.Add( bSizer18, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )


		self.m_panel6.SetSizer( fgSizer5 )
		self.m_panel6.Layout()
		fgSizer5.Fit( self.m_panel6 )
		bSizer55.Add( self.m_panel6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_tambahpegawai.SetSizer( bSizer55 )
		self.panel_tambahpegawai.Layout()
		bSizer55.Fit( self.panel_tambahpegawai )
		bSizer12.Add( self.panel_tambahpegawai, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.m_filePicker2.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker2OnFileChanged )
		self.btn_simpan_tambah_karyawan.Bind( wx.EVT_BUTTON, self.btn_simpan_tambah_karyawanOnButtonClick )
		self.btn_batal_tambah.Bind( wx.EVT_BUTTON, self.btn_batal_tambahOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_filePicker2OnFileChanged( self, event ):
		event.Skip()

	def btn_simpan_tambah_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_batal_tambahOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class tabel_data_karyawan
###########################################################################

class tabel_data_karyawan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		fgSizer10 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.panel_tabelkaryawan = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self.panel_tabelkaryawan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.Colour( 223, 223, 223 ) )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_back_tabel_karyawan = wx.BitmapButton( self.m_panel11, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,35 ), wx.BU_AUTODRAW|0 )

		self.btn_back_tabel_karyawan.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_MENU ) )
		self.btn_back_tabel_karyawan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer26.Add( self.btn_back_tabel_karyawan, 0, wx.ALL, 5 )


		bSizer26.Add( ( 20, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 30, 0), 1, wx.EXPAND, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Tabel Data Pegawai", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText52.Wrap( -1 )

		self.m_staticText52.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer26.Add( self.m_staticText52, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer26.Add( ( 100, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambah_tabelkaryawan = wx.Button( self.m_panel11, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_tambah_tabelkaryawan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_tambah_tabelkaryawan.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_tambah_tabelkaryawan.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		bSizer26.Add( self.btn_tambah_tabelkaryawan, 0, wx.ALL, 5 )

		self.btn_edit_karyawan = wx.Button( self.m_panel11, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_edit_karyawan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_edit_karyawan.SetBackgroundColour( wx.Colour( 242, 242, 0 ) )

		bSizer26.Add( self.btn_edit_karyawan, 0, wx.ALL, 5 )

		self.btn_hapus_karyawan = wx.Button( self.m_panel11, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_hapus_karyawan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_hapus_karyawan.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_hapus_karyawan.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		bSizer26.Add( self.btn_hapus_karyawan, 0, wx.ALL, 5 )


		self.m_panel11.SetSizer( bSizer26 )
		self.m_panel11.Layout()
		bSizer26.Fit( self.m_panel11 )
		bSizer54.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self.panel_tabelkaryawan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.tabel_data_karyawan1 = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 560,-1 ), 0 )

		# Grid
		self.tabel_data_karyawan1.CreateGrid( 200, 6 )
		self.tabel_data_karyawan1.EnableEditing( True )
		self.tabel_data_karyawan1.EnableGridLines( True )
		self.tabel_data_karyawan1.EnableDragGridSize( False )
		self.tabel_data_karyawan1.SetMargins( 0, 0 )

		# Columns
		self.tabel_data_karyawan1.SetColSize( 0, 54 )
		self.tabel_data_karyawan1.SetColSize( 1, 161 )
		self.tabel_data_karyawan1.SetColSize( 2, 50 )
		self.tabel_data_karyawan1.SetColSize( 3, 93 )
		self.tabel_data_karyawan1.SetColSize( 4, 80 )
		self.tabel_data_karyawan1.SetColSize( 5, 80 )
		self.tabel_data_karyawan1.EnableDragColMove( True )
		self.tabel_data_karyawan1.EnableDragColSize( True )
		self.tabel_data_karyawan1.SetColLabelSize( 40 )
		self.tabel_data_karyawan1.SetColLabelValue( 0, u"ID" )
		self.tabel_data_karyawan1.SetColLabelValue( 1, u"Nama Karyawan" )
		self.tabel_data_karyawan1.SetColLabelValue( 2, u"Umur" )
		self.tabel_data_karyawan1.SetColLabelValue( 3, u"Jenis Kelamin" )
		self.tabel_data_karyawan1.SetColLabelValue( 4, u"Username" )
		self.tabel_data_karyawan1.SetColLabelValue( 5, u"Password" )
		self.tabel_data_karyawan1.SetColLabelValue( 6, wx.EmptyString )
		self.tabel_data_karyawan1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_data_karyawan1.EnableDragRowSize( False )
		self.tabel_data_karyawan1.SetRowLabelSize( 20 )
		self.tabel_data_karyawan1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabel_data_karyawan1.SetLabelBackgroundColour( wx.Colour( 106, 188, 255 ) )

		# Cell Defaults
		self.tabel_data_karyawan1.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		bSizer28.Add( self.tabel_data_karyawan1, 0, wx.ALIGN_CENTER, 5 )


		self.m_panel12.SetSizer( bSizer28 )
		self.m_panel12.Layout()
		bSizer28.Fit( self.m_panel12 )
		bSizer54.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.panel_tabelkaryawan.SetSizer( bSizer54 )
		self.panel_tabelkaryawan.Layout()
		bSizer54.Fit( self.panel_tabelkaryawan )
		fgSizer10.Add( self.panel_tabelkaryawan, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()

		# Connect Events
		self.btn_back_tabel_karyawan.Bind( wx.EVT_BUTTON, self.btn_back_tabel_karyawanOnButtonClick )
		self.btn_tambah_tabelkaryawan.Bind( wx.EVT_BUTTON, self.btn_tambah_tabelkaryawanOnButtonClick )
		self.btn_edit_karyawan.Bind( wx.EVT_BUTTON, self.btn_edit_karyawanOnButtonClick )
		self.btn_hapus_karyawan.Bind( wx.EVT_BUTTON, self.btn_hapus_karyawanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_tabel_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_tambah_tabelkaryawanOnButtonClick( self, event ):
		event.Skip()

	def btn_edit_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_hapus_karyawanOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class tabel_data_history
###########################################################################

class tabel_data_history ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		fgSizer10 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.panel_tabelhistory = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer53 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self.panel_tabelhistory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.Colour( 223, 223, 223 ) )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_back_history = wx.BitmapButton( self.m_panel11, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )

		self.btn_back_history.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_BUTTON ) )
		self.btn_back_history.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer26.Add( self.btn_back_history, 0, wx.ALL, 5 )


		bSizer26.Add( ( 10, 0), 1, wx.EXPAND, 5 )

		self.teks_data_history = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Tabel Data History", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.teks_data_history.Wrap( -1 )

		self.teks_data_history.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer26.Add( self.teks_data_history, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer26.Add( ( 100, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_masukin_tabelhistory = wx.Button( self.m_panel11, wx.ID_ANY, u"Masukin", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_masukin_tabelhistory.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_masukin_tabelhistory.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_masukin_tabelhistory.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		bSizer26.Add( self.btn_masukin_tabelhistory, 0, wx.ALL, 5 )

		self.btn_ambil_tabelhistory = wx.Button( self.m_panel11, wx.ID_ANY, u"Ambil", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_ambil_tabelhistory.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.btn_ambil_tabelhistory.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_ambil_tabelhistory.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		bSizer26.Add( self.btn_ambil_tabelhistory, 0, wx.ALL, 5 )


		self.m_panel11.SetSizer( bSizer26 )
		self.m_panel11.Layout()
		bSizer26.Fit( self.m_panel11 )
		bSizer53.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self.panel_tabelhistory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.tabelhistory = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 675,-1 ), 0 )

		# Grid
		self.tabelhistory.CreateGrid( 50, 7 )
		self.tabelhistory.EnableEditing( True )
		self.tabelhistory.EnableGridLines( True )
		self.tabelhistory.EnableDragGridSize( False )
		self.tabelhistory.SetMargins( 0, 0 )

		# Columns
		self.tabelhistory.SetColSize( 0, 57 )
		self.tabelhistory.SetColSize( 1, 88 )
		self.tabelhistory.SetColSize( 2, 94 )
		self.tabelhistory.SetColSize( 3, 114 )
		self.tabelhistory.SetColSize( 4, 115 )
		self.tabelhistory.SetColSize( 5, 80 )
		self.tabelhistory.SetColSize( 6, 80 )
		self.tabelhistory.EnableDragColMove( False )
		self.tabelhistory.EnableDragColSize( True )
		self.tabelhistory.SetColLabelSize( 50 )
		self.tabelhistory.SetColLabelValue( 0, u"ID" )
		self.tabelhistory.SetColLabelValue( 1, u"Id Karyawan" )
		self.tabelhistory.SetColLabelValue( 2, u"Id Barang" )
		self.tabelhistory.SetColLabelValue( 3, u"Keterangan" )
		self.tabelhistory.SetColLabelValue( 4, u"Jumlah" )
		self.tabelhistory.SetColLabelValue( 5, u"Satuan" )
		self.tabelhistory.SetColLabelValue( 6, u"Tanggal" )
		self.tabelhistory.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelhistory.EnableDragRowSize( True )
		self.tabelhistory.SetRowLabelSize( 30 )
		self.tabelhistory.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabelhistory.SetLabelBackgroundColour( wx.Colour( 106, 188, 255 ) )
		self.tabelhistory.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		# Cell Defaults
		self.tabelhistory.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		self.tabelhistory.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer28.Add( self.tabelhistory, 0, wx.ALIGN_CENTER, 5 )


		self.m_panel12.SetSizer( bSizer28 )
		self.m_panel12.Layout()
		bSizer28.Fit( self.m_panel12 )
		bSizer53.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.panel_tabelhistory.SetSizer( bSizer53 )
		self.panel_tabelhistory.Layout()
		bSizer53.Fit( self.panel_tabelhistory )
		fgSizer10.Add( self.panel_tabelhistory, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()

		# Connect Events
		self.btn_back_history.Bind( wx.EVT_BUTTON, self.btn_back_historyOnButtonClick )
		self.btn_masukin_tabelhistory.Bind( wx.EVT_BUTTON, self.btn_masukin_tabelhistoryOnButtonClick )
		self.btn_ambil_tabelhistory.Bind( wx.EVT_BUTTON, self.btn_ambil_tabelhistoryOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_historyOnButtonClick( self, event ):
		event.Skip()

	def btn_masukin_tabelhistoryOnButtonClick( self, event ):
		event.Skip()

	def btn_ambil_tabelhistoryOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class tabel_data_barang
###########################################################################

class tabel_data_barang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		fgSizer10 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.panel_tabelbarang = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self.panel_tabelbarang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.Colour( 223, 223, 223 ) )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_back_tabelbarang = wx.BitmapButton( self.m_panel11, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )

		self.btn_back_tabelbarang.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_BUTTON ) )
		self.btn_back_tabelbarang.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer26.Add( self.btn_back_tabelbarang, 0, wx.ALL, 5 )


		bSizer26.Add( ( 10, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_data_barang = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Tabel Data Barang", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.teks_data_barang.Wrap( -1 )

		self.teks_data_barang.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer26.Add( self.teks_data_barang, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer26.Add( ( 100, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambah_barang = wx.Button( self.m_panel11, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_tambah_barang.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_tambah_barang.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_tambah_barang.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		bSizer26.Add( self.btn_tambah_barang, 0, wx.ALL, 5 )

		self.btn_edit_barang = wx.Button( self.m_panel11, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_edit_barang.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_edit_barang.SetBackgroundColour( wx.Colour( 242, 242, 0 ) )

		bSizer26.Add( self.btn_edit_barang, 0, wx.ALL, 5 )

		self.btn_hapus_barang = wx.Button( self.m_panel11, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_hapus_barang.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_hapus_barang.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_hapus_barang.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		bSizer26.Add( self.btn_hapus_barang, 0, wx.ALL, 5 )


		self.m_panel11.SetSizer( bSizer26 )
		self.m_panel11.Layout()
		bSizer26.Fit( self.m_panel11 )
		bSizer52.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 3 )

		self.m_panel12 = wx.Panel( self.panel_tabelbarang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.tabelbarang = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 650,-1 ), 0 )

		# Grid
		self.tabelbarang.CreateGrid( 200, 7 )
		self.tabelbarang.EnableEditing( True )
		self.tabelbarang.EnableGridLines( True )
		self.tabelbarang.EnableDragGridSize( False )
		self.tabelbarang.SetMargins( 0, 0 )

		# Columns
		self.tabelbarang.SetColSize( 0, 57 )
		self.tabelbarang.SetColSize( 1, 93 )
		self.tabelbarang.SetColSize( 2, 94 )
		self.tabelbarang.SetColSize( 3, 66 )
		self.tabelbarang.SetColSize( 4, 130 )
		self.tabelbarang.SetColSize( 5, 80 )
		self.tabelbarang.SetColSize( 6, 80 )
		self.tabelbarang.EnableDragColMove( False )
		self.tabelbarang.EnableDragColSize( True )
		self.tabelbarang.SetColLabelSize( 30 )
		self.tabelbarang.SetColLabelValue( 0, u"ID" )
		self.tabelbarang.SetColLabelValue( 1, u"Nama Barang" )
		self.tabelbarang.SetColLabelValue( 2, u"Jumlah Barang" )
		self.tabelbarang.SetColLabelValue( 3, u"Satuan" )
		self.tabelbarang.SetColLabelValue( 4, u"tanggal kadaluarsa" )
		self.tabelbarang.SetColLabelValue( 5, u"Password" )
		self.tabelbarang.SetColLabelValue( 6, u"Foto" )
		self.tabelbarang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelbarang.EnableDragRowSize( True )
		self.tabelbarang.SetRowLabelSize( 30 )
		self.tabelbarang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabelbarang.SetLabelBackgroundColour( wx.Colour( 106, 188, 255 ) )

		# Cell Defaults
		self.tabelbarang.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		self.tabelbarang.SetBackgroundColour( wx.Colour( 223, 223, 223 ) )

		bSizer28.Add( self.tabelbarang, 0, wx.ALIGN_CENTER, 5 )


		self.m_panel12.SetSizer( bSizer28 )
		self.m_panel12.Layout()
		bSizer28.Fit( self.m_panel12 )
		bSizer52.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.panel_tabelbarang.SetSizer( bSizer52 )
		self.panel_tabelbarang.Layout()
		bSizer52.Fit( self.panel_tabelbarang )
		fgSizer10.Add( self.panel_tabelbarang, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()

		# Connect Events
		self.btn_back_tabelbarang.Bind( wx.EVT_BUTTON, self.btn_back_tabelbarangOnButtonClick )
		self.btn_tambah_barang.Bind( wx.EVT_BUTTON, self.btn_tambah_karyawanOnButtonClick )
		self.btn_edit_barang.Bind( wx.EVT_BUTTON, self.btn_edit_pegawaiOnButtonClick )
		self.btn_hapus_barang.Bind( wx.EVT_BUTTON, self.btn_hapus_pegawaiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_tabelbarangOnButtonClick( self, event ):
		event.Skip()

	def btn_tambah_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_edit_pegawaiOnButtonClick( self, event ):
		event.Skip()

	def btn_hapus_pegawaiOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_tambah_history
###########################################################################

class form_tambah_history ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.panel_tambahstory = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer50 = wx.BoxSizer( wx.VERTICAL )


		bSizer50.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel27 = wx.Panel( self.panel_tambahstory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.teks_tambah_history = wx.StaticText( self.m_panel27, wx.ID_ANY, u"Form Tambah history", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambah_history.Wrap( -1 )

		self.teks_tambah_history.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer48.Add( self.teks_tambah_history, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel27.SetSizer( bSizer48 )
		self.m_panel27.Layout()
		bSizer48.Fit( self.m_panel27 )
		bSizer50.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self.panel_tambahstory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_idkaryawan_history = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Id Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_idkaryawan_history.Wrap( -1 )

		self.teks_idkaryawan_history.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_idkaryawan_history, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_idkaryawan_history = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		fgSizer5.Add( self.input_idkaryawan_history, 0, wx.ALL, 5 )

		self.teks_idbarang_history = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Id Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_idbarang_history.Wrap( -1 )

		self.teks_idbarang_history.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_idbarang_history, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_idbarang_history = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		fgSizer5.Add( self.input_idbarang_history, 0, wx.ALL, 5 )

		self.teks_keterangan_history = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Keterangan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_keterangan_history.Wrap( -1 )

		self.teks_keterangan_history.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_keterangan_history, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		input_keterangan_historyChoices = [ u"Ambil Barang", u"Tambah Barang" ]
		self.input_keterangan_history = wx.ComboBox( self.m_panel6, wx.ID_ANY, u"Ambil Barang", wx.DefaultPosition, wx.Size( 200,25 ), input_keterangan_historyChoices, 0 )
		self.input_keterangan_history.SetSelection( 0 )
		fgSizer5.Add( self.input_keterangan_history, 0, wx.ALL, 5 )

		self.teks_satuan_history = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Satuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_satuan_history.Wrap( -1 )

		self.teks_satuan_history.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_satuan_history, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_satuan_history = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		fgSizer5.Add( self.input_satuan_history, 0, wx.ALL, 5 )

		self.teks_tanggal_history = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tanggal_history.Wrap( -1 )

		self.teks_tanggal_history.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_tanggal_history, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_tanggal_history = wx.adv.DatePickerCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,25 ), wx.adv.DP_DEFAULT )
		fgSizer5.Add( self.input_tanggal_history, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_simpan_tambah_history = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		fgSizer5.Add( self.btn_simpan_tambah_history, 0, wx.ALL, 5 )

		self.btn_batal_tambah_history = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		fgSizer5.Add( self.btn_batal_tambah_history, 0, wx.ALL, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		fgSizer5.Add( bSizer18, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )


		self.m_panel6.SetSizer( fgSizer5 )
		self.m_panel6.Layout()
		fgSizer5.Fit( self.m_panel6 )
		bSizer50.Add( self.m_panel6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer50.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_tambahstory.SetSizer( bSizer50 )
		self.panel_tambahstory.Layout()
		bSizer50.Fit( self.panel_tambahstory )
		bSizer12.Add( self.panel_tambahstory, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.btn_simpan_tambah_history.Bind( wx.EVT_BUTTON, self.btn_simpan_tambah_historyOnButtonClick )
		self.btn_batal_tambah_history.Bind( wx.EVT_BUTTON, self.btn_batal_tambah_historyOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan_tambah_historyOnButtonClick( self, event ):
		event.Skip()

	def btn_batal_tambah_historyOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_tambah_barang
###########################################################################

class form_tambah_barang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.panel_tambahbarang = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_tambah_barang = wx.StaticText( self.panel_tambahbarang, wx.ID_ANY, u"Form Tambah Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambah_barang.Wrap( -1 )

		self.teks_tambah_barang.SetFont( wx.Font( 28, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer51.Add( self.teks_tambah_barang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self.panel_tambahbarang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_pegawai.Wrap( -1 )

		self.teks_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_namabarang_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_namabarang_barang, 0, wx.ALL, 5 )

		self.teks_umur_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Stock Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_umur_pegawai.Wrap( -1 )

		self.teks_umur_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_umur_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_stockbarang_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_stockbarang_barang, 0, wx.ALL, 5 )

		self.teks_satuan_barang = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Satuan Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_satuan_barang.Wrap( -1 )

		self.teks_satuan_barang.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_satuan_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_satuanbarang_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_satuanbarang_barang, 0, wx.ALL, 5 )

		self.teks_tahunkadaluarsa_barang = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tahun Kadaluarsa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tahunkadaluarsa_barang.Wrap( -1 )

		self.teks_tahunkadaluarsa_barang.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_tahunkadaluarsa_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_tahunkadaluarsa_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_tahunkadaluarsa_barang, 0, wx.ALL, 5 )

		self.teks_bulan_Kadaluarsa = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Bulan Kadaluarsa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_bulan_Kadaluarsa.Wrap( -1 )

		self.teks_bulan_Kadaluarsa.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_bulan_Kadaluarsa, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_bulankadaluarsa_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_bulankadaluarsa_barang, 0, wx.ALL, 5 )

		self.teks_tanggal_kadaluarsa = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tanggal Kadaluarsa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tanggal_kadaluarsa.Wrap( -1 )

		self.teks_tanggal_kadaluarsa.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_tanggal_kadaluarsa, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_tanggalkadaluarsa_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.input_tanggalkadaluarsa_barang.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.input_tanggalkadaluarsa_barang, 0, wx.ALL, 5 )

		self.teks_foto_barang = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_foto_barang.Wrap( -1 )

		self.teks_foto_barang.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_foto_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_filePicker3 = wx.FilePickerCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 200,-1 ), wx.FLP_DEFAULT_STYLE )
		fgSizer5.Add( self.m_filePicker3, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 15), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.btn_simpan_tambah_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		fgSizer5.Add( self.btn_simpan_tambah_barang, 0, wx.ALL, 5 )

		self.btn_batal_tambah_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		fgSizer5.Add( self.btn_batal_tambah_barang, 0, wx.ALL, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		fgSizer5.Add( bSizer18, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )


		self.m_panel6.SetSizer( fgSizer5 )
		self.m_panel6.Layout()
		fgSizer5.Fit( self.m_panel6 )
		bSizer51.Add( self.m_panel6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_tambahbarang.SetSizer( bSizer51 )
		self.panel_tambahbarang.Layout()
		bSizer51.Fit( self.panel_tambahbarang )
		bSizer12.Add( self.panel_tambahbarang, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.m_filePicker3.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker3OnFileChanged )
		self.btn_simpan_tambah_barang.Bind( wx.EVT_BUTTON, self.btn_simpan_tambah_barangOnButtonClick )
		self.btn_batal_tambah_barang.Bind( wx.EVT_BUTTON, self.btn_batal_tambah_barangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_filePicker3OnFileChanged( self, event ):
		event.Skip()

	def btn_simpan_tambah_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_batal_tambah_barangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class panel_ambil_history
###########################################################################

class panel_ambil_history ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 279,208 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel36 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer59 = wx.BoxSizer( wx.VERTICAL )


		bSizer59.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Form_ambil_history = wx.StaticText( self.m_panel36, wx.ID_ANY, u"Form Ambil/Tambah Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Form_ambil_history.Wrap( -1 )

		self.Form_ambil_history.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer59.Add( self.Form_ambil_history, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.teks_ambil_idkaryawan = wx.StaticText( self.m_panel36, wx.ID_ANY, u"Id Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_ambil_idkaryawan.Wrap( -1 )

		self.teks_ambil_idkaryawan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer59.Add( self.teks_ambil_idkaryawan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.input_ambil_idbarang = wx.TextCtrl( self.m_panel36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer59.Add( self.input_ambil_idbarang, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Teks_ambil_jumlah = wx.StaticText( self.m_panel36, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Teks_ambil_jumlah.Wrap( -1 )

		self.Teks_ambil_jumlah.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer59.Add( self.Teks_ambil_jumlah, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.input_ambil_idjumlah = wx.TextCtrl( self.m_panel36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer59.Add( self.input_ambil_idjumlah, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer59.Add( ( 0, 5), 1, 0, 5 )

		self.btn_ok_ambilbarang = wx.Button( self.m_panel36, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_ok_ambilbarang.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		bSizer59.Add( self.btn_ok_ambilbarang, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel36.SetSizer( bSizer59 )
		self.m_panel36.Layout()
		bSizer59.Fit( self.m_panel36 )
		bSizer58.Add( self.m_panel36, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer58 )
		self.Layout()

		# Connect Events
		self.btn_ok_ambilbarang.Bind( wx.EVT_BUTTON, self.btn_ok_ambilbarangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_ok_ambilbarangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 240,167 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.teks_id_edittambah = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_id_edittambah.Wrap( -1 )

		bSizer27.Add( self.teks_id_edittambah, 0, wx.ALL, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText51 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer12.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_textCtrl35 = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_textCtrl35, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer12.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.m_textCtrl36 = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_textCtrl36, 0, wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 75,50 ), 0 )
		bSizer30.Add( self.m_button51, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Hapus_karyawan
###########################################################################

class Hapus_karyawan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 240,146 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.teks_id_edittambah = wx.StaticText( self, wx.ID_ANY, u"Hapus Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_id_edittambah.Wrap( -1 )

		self.teks_id_edittambah.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer27.Add( self.teks_id_edittambah, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText51 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Id Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer12.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.input_id_hapus_pegawai = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		fgSizer12.Add( self.input_id_hapus_pegawai, 0, wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.btn_hapus_karyawan = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_hapus_karyawan, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_hapus_karyawan.Bind( wx.EVT_BUTTON, self.btn_hapus_karyawanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_hapus_karyawanOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahkaryawan_sukses
###########################################################################

class notif_tambahkaryawan_sukses ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 240,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahkaryawan_sukses = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Karyawan Berhasil Ditambahkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahkaryawan_sukses.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahkaryawan_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahkaryawan_sukses = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahkaryawan_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahkaryawan_sukses.Bind( wx.EVT_BUTTON, self.btn_tambahkaryawan_suksesOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahkaryawan_suksesOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahkaryawan_batal
###########################################################################

class notif_tambahkaryawan_batal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 240,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahkaryawan_batal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Penambahan Data Karyawan Dibatalkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahkaryawan_batal.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahkaryawan_batal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahkaryawan_batal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahkaryawan_batal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahkaryawan_batal.Bind( wx.EVT_BUTTON, self.btn_tambahkaryawan_batalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahkaryawan_batalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahkaryawan_gagal
###########################################################################

class notif_tambahkaryawan_gagal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 240,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahkaryawan_gagal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Karyawan Gagal Ditambahkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahkaryawan_gagal.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahkaryawan_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahkaryawan_gagal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahkaryawan_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahkaryawan_gagal.Bind( wx.EVT_BUTTON, self.btn_tambahkaryawan_gagalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahkaryawan_gagalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_editkaryawan_sukses
###########################################################################

class notif_editkaryawan_sukses ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 226,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_editkaryawan_sukses = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Karyawan Berhasil Diupdate!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_editkaryawan_sukses.Wrap( -1 )

		fgSizer12.Add( self.teks_editkaryawan_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_editkaryawan_sukses = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_editkaryawan_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_editkaryawan_sukses.Bind( wx.EVT_BUTTON, self.btn_editkaryawan_suksesOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_editkaryawan_suksesOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_editkaryawan_gagal
###########################################################################

class notif_editkaryawan_gagal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 226,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_editkaryawan_gagal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Karyawan Gagal Diupdate!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_editkaryawan_gagal.Wrap( -1 )

		fgSizer12.Add( self.teks_editkaryawan_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_editkaryawan_gagal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_editkaryawan_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_editkaryawan_gagal.Bind( wx.EVT_BUTTON, self.btn_editkaryawan_gagalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_editkaryawan_gagalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_hapuskaryawan_sukses
###########################################################################

class notif_hapuskaryawan_sukses ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 226,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_hapuskaryawan_sukses = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Karyawan Berhasil DiHapus!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_hapuskaryawan_sukses.Wrap( -1 )

		fgSizer12.Add( self.teks_hapuskaryawan_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_hapuskaryawan_sukses = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_hapuskaryawan_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_hapuskaryawan_sukses.Bind( wx.EVT_BUTTON, self.btn_hapuskaryawan_suksesOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_hapuskaryawan_suksesOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_hapuskaryawan_gagal
###########################################################################

class notif_hapuskaryawan_gagal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 226,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer12.Add( ( 15, 0), 1, wx.EXPAND, 5 )

		self.teks_hapuskaryawan_gagal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Karyawan Gagal Dihapus!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_hapuskaryawan_gagal.Wrap( -1 )

		fgSizer12.Add( self.teks_hapuskaryawan_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_hapuskaryawan_gagal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_hapuskaryawan_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_hapuskaryawan_gagal.Bind( wx.EVT_BUTTON, self.btn_hapuskaryawan_gagalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_hapuskaryawan_gagalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahbarang_sukses
###########################################################################

class notif_tambahbarang_sukses ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 227,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahbarang_berhasil = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Barang Berhasil Ditambahkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahbarang_berhasil.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahbarang_berhasil, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahbarang_sukses = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahbarang_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahbarang_sukses.Bind( wx.EVT_BUTTON, self.btn_tambahbarang_suksesOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahbarang_suksesOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahbarang_batal
###########################################################################

class notif_tambahbarang_batal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 240,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahkaryawan_batal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Penambahan Data Barang Dibatalkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahkaryawan_batal.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahkaryawan_batal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahbarang_batal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahbarang_batal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahbarang_batal.Bind( wx.EVT_BUTTON, self.btn_tambahbarang_batalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahbarang_batalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahbarang_gagal
###########################################################################

class notif_tambahbarang_gagal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 214,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahkaryawan_gagal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data Barang Gagal Ditambahkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahkaryawan_gagal.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahkaryawan_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahbarang_gagal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahbarang_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahbarang_gagal.Bind( wx.EVT_BUTTON, self.btn_tambahbarang_gagalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahbarang_gagalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahhistory_sukses
###########################################################################

class notif_tambahhistory_sukses ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 214,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahhistory_sukses = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data History  Berhasil Ditambahkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahhistory_sukses.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahhistory_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahhistory_sukses = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahhistory_sukses, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahhistory_sukses.Bind( wx.EVT_BUTTON, self.btn_tambahhistory_suksesOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahhistory_suksesOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahhistory_batal
###########################################################################

class notif_tambahhistory_batal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 214,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahhistory_batal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data History  Batal Ditambahkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahhistory_batal.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahhistory_batal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahhistory_batal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahhistory_batal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahhistory_batal.Bind( wx.EVT_BUTTON, self.btn_tambahhistory_batalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahhistory_batalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class notif_tambahhistory_gagal
###########################################################################

class notif_tambahhistory_gagal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 214,119 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_tambahhistory_gagal = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Data History  Gagal Ditambahkan!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambahhistory_gagal.Wrap( -1 )

		fgSizer12.Add( self.teks_tambahhistory_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel17.SetSizer( fgSizer12 )
		self.m_panel17.Layout()
		fgSizer12.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )


		bSizer30.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_tambahhistory_gagal = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer30.Add( self.btn_tambahhistory_gagal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_tambahhistory_gagal.Bind( wx.EVT_BUTTON, self.btn_tambahhistory_gagalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_tambahhistory_gagalOnButtonClick( self, event ):
		event.Skip()


