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

###########################################################################
## Class fitur_login
###########################################################################

class fitur_login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistem Managemen Gudang Barang", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Montserrat Black" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.panel_formlogin = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_formlogin.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )


		bSizer57.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_formlogin = wx.StaticText( self.panel_formlogin, wx.ID_ANY, u"Form Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_formlogin.Wrap( -1 )

		self.teks_formlogin.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Black" ) )

		bSizer57.Add( self.teks_formlogin, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.teks_penjelasan = wx.StaticText( self.panel_formlogin, wx.ID_ANY, u"Sistem Manajemen Gudang Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_penjelasan.Wrap( -1 )

		self.teks_penjelasan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat SemiBold" ) )

		bSizer57.Add( self.teks_penjelasan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self.panel_formlogin, wx.ID_ANY, wx.Bitmap( u"logo - Copy.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 70,70 ), 0 )
		bSizer57.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

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

		self.statis_adminfitur.SetFont( wx.Font( 20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

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
		self.btn_admin_exit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
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


		self.m_panel11.SetSizer( bSizer26 )
		self.m_panel11.Layout()
		bSizer26.Fit( self.m_panel11 )
		bSizer54.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self.panel_tabelkaryawan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.tabel_data_karyawan1 = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,500 ), 0 )

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
		self.tabel_data_karyawan1.SetColSize( 4, 133 )
		self.tabel_data_karyawan1.SetColSize( 5, 145 )
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

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_tabel_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_tambah_tabelkaryawanOnButtonClick( self, event ):
		event.Skip()

	def btn_edit_karyawanOnButtonClick( self, event ):
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


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_data_history = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Tabel Data History", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.teks_data_history.Wrap( -1 )

		self.teks_data_history.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer26.Add( self.teks_data_history, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer26.Add( ( 400, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )


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
		self.tabelhistory.SetColSize( 0, 42 )
		self.tabelhistory.SetColSize( 1, 85 )
		self.tabelhistory.SetColSize( 2, 73 )
		self.tabelhistory.SetColSize( 3, 86 )
		self.tabelhistory.SetColSize( 4, 115 )
		self.tabelhistory.SetColSize( 5, 80 )
		self.tabelhistory.SetColSize( 6, 142 )
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

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_historyOnButtonClick( self, event ):
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


		self.m_panel11.SetSizer( bSizer26 )
		self.m_panel11.Layout()
		bSizer26.Fit( self.m_panel11 )
		bSizer52.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 3 )

		self.m_panel12 = wx.Panel( self.panel_tabelbarang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.tabelbarang = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 650,-1 ), 0 )

		# Grid
		self.tabelbarang.CreateGrid( 200, 5 )
		self.tabelbarang.EnableEditing( True )
		self.tabelbarang.EnableGridLines( True )
		self.tabelbarang.EnableDragGridSize( False )
		self.tabelbarang.SetMargins( 0, 0 )

		# Columns
		self.tabelbarang.SetColSize( 0, 57 )
		self.tabelbarang.SetColSize( 1, 173 )
		self.tabelbarang.SetColSize( 2, 103 )
		self.tabelbarang.SetColSize( 3, 89 )
		self.tabelbarang.SetColSize( 4, 190 )
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
		self.btn_tambah_barang.Bind( wx.EVT_BUTTON, self.btn_tambah_barangOnButtonClick )
		self.btn_edit_barang.Bind( wx.EVT_BUTTON, self.btn_edit_barangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_tabelbarangOnButtonClick( self, event ):
		event.Skip()

	def btn_tambah_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_edit_barangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_id_karyawan
###########################################################################

class form_id_karyawan ( wx.Panel ):

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

		self.m_staticText52 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Tabel Edit Pegawai", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText52.Wrap( -1 )

		self.m_staticText52.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer26.Add( self.m_staticText52, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer26.Add( ( 100, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel11.SetSizer( bSizer26 )
		self.m_panel11.Layout()
		bSizer26.Fit( self.m_panel11 )
		bSizer54.Add( self.m_panel11, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel12 = wx.Panel( self.panel_tabelkaryawan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel32 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		self.tabel_edit_karyawan = wx.grid.Grid( self.m_panel32, wx.ID_ANY, wx.DefaultPosition, wx.Size( 255,500 ), 0 )

		# Grid
		self.tabel_edit_karyawan.CreateGrid( 200, 2 )
		self.tabel_edit_karyawan.EnableEditing( True )
		self.tabel_edit_karyawan.EnableGridLines( True )
		self.tabel_edit_karyawan.EnableDragGridSize( False )
		self.tabel_edit_karyawan.SetMargins( 0, 0 )

		# Columns
		self.tabel_edit_karyawan.SetColSize( 0, 54 )
		self.tabel_edit_karyawan.SetColSize( 1, 161 )
		self.tabel_edit_karyawan.EnableDragColMove( True )
		self.tabel_edit_karyawan.EnableDragColSize( True )
		self.tabel_edit_karyawan.SetColLabelSize( 40 )
		self.tabel_edit_karyawan.SetColLabelValue( 0, u"ID" )
		self.tabel_edit_karyawan.SetColLabelValue( 1, u"Nama Karyawan" )
		self.tabel_edit_karyawan.SetColLabelValue( 2, wx.EmptyString )
		self.tabel_edit_karyawan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_edit_karyawan.EnableDragRowSize( False )
		self.tabel_edit_karyawan.SetRowLabelSize( 20 )
		self.tabel_edit_karyawan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabel_edit_karyawan.SetLabelBackgroundColour( wx.Colour( 106, 188, 255 ) )

		# Cell Defaults
		self.tabel_edit_karyawan.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		bSizer38.Add( self.tabel_edit_karyawan, 0, wx.EXPAND, 5 )

		self.panel_input_idkaryawan = wx.Panel( self.m_panel32, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer40 = wx.BoxSizer( wx.VERTICAL )


		bSizer40.Add( ( 0, 0), 1, 0, 5 )

		self.teks_id = wx.StaticText( self.panel_input_idkaryawan, wx.ID_ANY, u"Masukkan ID Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_id.Wrap( -1 )

		self.teks_id.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer40.Add( self.teks_id, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.input_id_karyawan = wx.TextCtrl( self.panel_input_idkaryawan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer40.Add( self.input_id_karyawan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.btn_OK = wx.Button( self.panel_input_idkaryawan, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_OK.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )
		self.btn_OK.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		bSizer40.Add( self.btn_OK, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer40.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_input_idkaryawan.SetSizer( bSizer40 )
		self.panel_input_idkaryawan.Layout()
		bSizer40.Fit( self.panel_input_idkaryawan )
		bSizer38.Add( self.panel_input_idkaryawan, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel32.SetSizer( bSizer38 )
		self.m_panel32.Layout()
		bSizer38.Fit( self.m_panel32 )
		bSizer28.Add( self.m_panel32, 1, wx.EXPAND |wx.ALL, 5 )


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
		self.btn_OK.Bind( wx.EVT_BUTTON, self.btn_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_tabel_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_OKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_id_barang
###########################################################################

class form_id_barang ( wx.Panel ):

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

		self.teks_data_barang = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Tabel Edit Barang", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.teks_data_barang.Wrap( -1 )

		self.teks_data_barang.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer26.Add( self.teks_data_barang, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer26.Add( ( 100, 0), 1, wx.EXPAND, 5 )


		bSizer26.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel11.SetSizer( bSizer26 )
		self.m_panel11.Layout()
		bSizer26.Fit( self.m_panel11 )
		bSizer52.Add( self.m_panel11, 1, wx.ALL|wx.EXPAND, 3 )

		self.m_panel12 = wx.Panel( self.panel_tabelbarang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.tabel_edit_barang = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,420 ), 0 )

		# Grid
		self.tabel_edit_barang.CreateGrid( 200, 2 )
		self.tabel_edit_barang.EnableEditing( True )
		self.tabel_edit_barang.EnableGridLines( True )
		self.tabel_edit_barang.EnableDragGridSize( False )
		self.tabel_edit_barang.SetMargins( 0, 0 )

		# Columns
		self.tabel_edit_barang.SetColSize( 0, 57 )
		self.tabel_edit_barang.SetColSize( 1, 195 )
		self.tabel_edit_barang.EnableDragColMove( False )
		self.tabel_edit_barang.EnableDragColSize( True )
		self.tabel_edit_barang.SetColLabelSize( 30 )
		self.tabel_edit_barang.SetColLabelValue( 0, u"ID" )
		self.tabel_edit_barang.SetColLabelValue( 1, u"Nama Barang" )
		self.tabel_edit_barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_edit_barang.EnableDragRowSize( True )
		self.tabel_edit_barang.SetRowLabelSize( 30 )
		self.tabel_edit_barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabel_edit_barang.SetLabelBackgroundColour( wx.Colour( 106, 188, 255 ) )

		# Cell Defaults
		self.tabel_edit_barang.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		self.tabel_edit_barang.SetBackgroundColour( wx.Colour( 223, 223, 223 ) )

		bSizer28.Add( self.tabel_edit_barang, 0, 0, 5 )

		self.Panel_input_idbarang = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer521 = wx.BoxSizer( wx.VERTICAL )


		bSizer521.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_id_barang = wx.StaticText( self.Panel_input_idbarang, wx.ID_ANY, u"Masukkan ID Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.input_id_barang.Wrap( -1 )

		self.input_id_barang.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer521.Add( self.input_id_barang, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.input_id_barang = wx.TextCtrl( self.Panel_input_idbarang, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer521.Add( self.input_id_barang, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.btn_OK = wx.Button( self.Panel_input_idbarang, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_OK.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )
		self.btn_OK.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		bSizer521.Add( self.btn_OK, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer521.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.Panel_input_idbarang.SetSizer( bSizer521 )
		self.Panel_input_idbarang.Layout()
		bSizer521.Fit( self.Panel_input_idbarang )
		bSizer28.Add( self.Panel_input_idbarang, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer28 )
		self.m_panel12.Layout()
		bSizer28.Fit( self.m_panel12 )
		bSizer52.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.panel_tabelbarang.SetSizer( bSizer52 )
		self.panel_tabelbarang.Layout()
		bSizer52.Fit( self.panel_tabelbarang )
		fgSizer10.Add( self.panel_tabelbarang, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer10 )
		self.Layout()

		# Connect Events
		self.btn_back_tabelbarang.Bind( wx.EVT_BUTTON, self.btn_back_tabelbarangOnButtonClick )
		self.btn_OK.Bind( wx.EVT_BUTTON, self.btn_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back_tabelbarangOnButtonClick( self, event ):
		event.Skip()

	def btn_OKOnButtonClick( self, event ):
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

		self.m_staticText22 = wx.StaticText( self.panel_tambahpegawai, wx.ID_ANY, u"TAMBAH PEGAWAI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer55.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


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

		self.teks_jeniskelamin_karyawan = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Jenis Kelamin (L/P)", wx.DefaultPosition, wx.DefaultSize, 0 )
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


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 20), 1, wx.EXPAND, 5 )

		self.btn_simpan_tambah_karyawan = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_simpan_tambah_karyawan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_simpan_tambah_karyawan.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		fgSizer5.Add( self.btn_simpan_tambah_karyawan, 0, wx.ALL, 5 )

		self.btn_batal_tambah = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_batal_tambah.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_batal_tambah.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		fgSizer5.Add( self.btn_batal_tambah, 0, wx.ALL, 5 )


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
		self.btn_simpan_tambah_karyawan.Bind( wx.EVT_BUTTON, self.btn_simpan_tambah_karyawanOnButtonClick )
		self.btn_batal_tambah.Bind( wx.EVT_BUTTON, self.btn_batal_tambahOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan_tambah_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_batal_tambahOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_edit_karyawan
###########################################################################

class form_edit_karyawan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 238, 242, 245 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.panel_tambahpegawai = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_edit_pegawai = wx.StaticText( self.panel_tambahpegawai, wx.ID_ANY, u"EDIT PEGAWAI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_pegawai.Wrap( -1 )

		self.teks_edit_pegawai.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )

		bSizer55.Add( self.teks_edit_pegawai, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel6 = wx.Panel( self.panel_tambahpegawai, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_edit_nama_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_nama_pegawai.Wrap( -1 )

		self.teks_edit_nama_pegawai.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_nama_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_karyawan, 0, wx.ALL, 5 )

		self.teks_edit_umur_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Umur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_umur_pegawai.Wrap( -1 )

		self.teks_edit_umur_pegawai.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_umur_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_umur_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_umur_karyawan, 0, wx.ALL, 5 )

		self.teks_jeniskelamin_karyawan = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_jeniskelamin_karyawan.Wrap( -1 )

		self.teks_jeniskelamin_karyawan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_jeniskelamin_karyawan, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_jeniskelamin_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_jeniskelamin_karyawan, 0, wx.ALL, 5 )

		self.teks_username_karyawan = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_username_karyawan.Wrap( -1 )

		self.teks_username_karyawan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_username_karyawan, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_username_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_username_karyawan, 0, wx.ALL, 5 )

		self.teks_password_karyawan = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_password_karyawan.Wrap( -1 )

		self.teks_password_karyawan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_password_karyawan, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_password_karyawan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		fgSizer5.Add( self.input_edit_password_karyawan, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.btn_edit_simpan_karyawan = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_edit_simpan_karyawan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_edit_simpan_karyawan.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		fgSizer5.Add( self.btn_edit_simpan_karyawan, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.btn_edit_batal_karyawan = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_edit_batal_karyawan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_edit_batal_karyawan.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		fgSizer5.Add( self.btn_edit_batal_karyawan, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.btn_hapus_karyawan = wx.Button( self.m_panel6, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_hapus_karyawan.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )
		self.btn_hapus_karyawan.SetBackgroundColour( wx.Colour( 242, 242, 0 ) )

		fgSizer5.Add( self.btn_hapus_karyawan, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


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
		self.btn_edit_simpan_karyawan.Bind( wx.EVT_BUTTON, self.btn_edit_simpan_karyawanOnButtonClick )
		self.btn_edit_batal_karyawan.Bind( wx.EVT_BUTTON, self.btn_edit_batal_karyawanOnButtonClick )
		self.btn_hapus_karyawan.Bind( wx.EVT_BUTTON, self.btn_hapus_karyawanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_edit_simpan_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_edit_batal_karyawanOnButtonClick( self, event ):
		event.Skip()

	def btn_hapus_karyawanOnButtonClick( self, event ):
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


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_tambah_barang = wx.StaticText( self.panel_tambahbarang, wx.ID_ANY, u"TAMBAH BARANG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tambah_barang.Wrap( -1 )

		self.teks_tambah_barang.SetFont( wx.Font( 28, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer51.Add( self.teks_tambah_barang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

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

		self.input_nama_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_nama_barang, 0, wx.ALL, 5 )

		self.teks_umur_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Stock Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_umur_pegawai.Wrap( -1 )

		self.teks_umur_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_umur_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_stock_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_stock_barang, 0, wx.ALL, 5 )

		self.teks_satuan_barang = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Satuan Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_satuan_barang.Wrap( -1 )

		self.teks_satuan_barang.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_satuan_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_satuan_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_satuan_barang, 0, wx.ALL, 5 )

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


		fgSizer5.Add( ( 0, 15), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.btn_simpan_tambah_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_simpan_tambah_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_simpan_tambah_barang.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		fgSizer5.Add( self.btn_simpan_tambah_barang, 0, wx.ALL, 5 )

		self.btn_batal_tambah_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_batal_tambah_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_batal_tambah_barang.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		fgSizer5.Add( self.btn_batal_tambah_barang, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( fgSizer5 )
		self.m_panel6.Layout()
		fgSizer5.Fit( self.m_panel6 )
		bSizer51.Add( self.m_panel6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_tambahbarang.SetSizer( bSizer51 )
		self.panel_tambahbarang.Layout()
		bSizer51.Fit( self.panel_tambahbarang )
		bSizer12.Add( self.panel_tambahbarang, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.btn_simpan_tambah_barang.Bind( wx.EVT_BUTTON, self.btn_simpan_tambah_barangOnButtonClick )
		self.btn_batal_tambah_barang.Bind( wx.EVT_BUTTON, self.btn_batal_tambah_barangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan_tambah_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_batal_tambah_barangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_edit_barang
###########################################################################

class form_edit_barang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.panel_editbarang = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_edit_barang = wx.StaticText( self.panel_editbarang, wx.ID_ANY, u"EDIT BARANG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_barang.Wrap( -1 )

		self.teks_edit_barang.SetFont( wx.Font( 28, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer51.Add( self.teks_edit_barang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer51.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_panel6 = wx.Panel( self.panel_editbarang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_edit_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_pegawai.Wrap( -1 )

		self.teks_edit_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_namabarang_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_namabarang_barang, 0, wx.ALL, 5 )

		self.teks_edit_umur_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Stock Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_umur_pegawai.Wrap( -1 )

		self.teks_edit_umur_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_umur_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_stockbarang_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_stockbarang_barang, 0, wx.ALL, 5 )

		self.teks_satuan_barang = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Satuan Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_satuan_barang.Wrap( -1 )

		self.teks_satuan_barang.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_satuan_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_satuanbarang_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_satuanbarang_barang, 0, wx.ALL, 5 )

		self.teks_tahunkadaluarsa_barang = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tahun Kadaluarsa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_tahunkadaluarsa_barang.Wrap( -1 )

		self.teks_tahunkadaluarsa_barang.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_tahunkadaluarsa_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_tahunkadaluarsa_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_tahunkadaluarsa_barang, 0, wx.ALL, 5 )

		self.teks_edit_bulan_Kadaluarsa = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Bulan Kadaluarsa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_bulan_Kadaluarsa.Wrap( -1 )

		self.teks_edit_bulan_Kadaluarsa.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_bulan_Kadaluarsa, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_bulankadaluarsa_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_edit_bulankadaluarsa_barang, 0, wx.ALL, 5 )

		self.teks_edit_tanggal_kadaluarsa = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tanggal Kadaluarsa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_tanggal_kadaluarsa.Wrap( -1 )

		self.teks_edit_tanggal_kadaluarsa.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_tanggal_kadaluarsa, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_edit_tanggalkadaluarsa_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.input_edit_tanggalkadaluarsa_barang.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.input_edit_tanggalkadaluarsa_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_edit_simpan_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_edit_simpan_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_edit_simpan_barang.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		fgSizer5.Add( self.btn_edit_simpan_barang, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.btn_edit_batal_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_edit_batal_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_edit_batal_barang.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		fgSizer5.Add( self.btn_edit_batal_barang, 0, wx.ALL, 5 )

		self.btn_hapus_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_hapus_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )
		self.btn_hapus_barang.SetBackgroundColour( wx.Colour( 242, 242, 0 ) )

		fgSizer5.Add( self.btn_hapus_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_input_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Input", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_input_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )
		self.btn_input_barang.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer5.Add( self.btn_input_barang, 0, wx.ALL, 5 )

		self.btn_ambil_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Ambil", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_ambil_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat ExtraBold" ) )
		self.btn_ambil_barang.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		fgSizer5.Add( self.btn_ambil_barang, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( fgSizer5 )
		self.m_panel6.Layout()
		fgSizer5.Fit( self.m_panel6 )
		bSizer51.Add( self.m_panel6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_editbarang.SetSizer( bSizer51 )
		self.panel_editbarang.Layout()
		bSizer51.Fit( self.panel_editbarang )
		bSizer12.Add( self.panel_editbarang, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.btn_edit_simpan_barang.Bind( wx.EVT_BUTTON, self.btn_edit_simpan_barangOnButtonClick )
		self.btn_edit_batal_barang.Bind( wx.EVT_BUTTON, self.btn_edit_batal_barangOnButtonClick )
		self.btn_hapus_barang.Bind( wx.EVT_BUTTON, self.btn_hapus_barangOnButtonClick )
		self.btn_input_barang.Bind( wx.EVT_BUTTON, self.btn_input_barangOnButtonClick )
		self.btn_ambil_barang.Bind( wx.EVT_BUTTON, self.btn_ambil_barangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_edit_simpan_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_edit_batal_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_hapus_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_input_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_ambil_barangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_ambil_barang
###########################################################################

class form_ambil_barang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.panel_ambil_barang = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_ambil_barang = wx.StaticText( self.panel_ambil_barang, wx.ID_ANY, u"AMBIL BARANG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_ambil_barang.Wrap( -1 )

		self.teks_ambil_barang.SetFont( wx.Font( 28, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer51.Add( self.teks_ambil_barang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer51.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_panel6 = wx.Panel( self.panel_ambil_barang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_edit_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_pegawai.Wrap( -1 )

		self.teks_edit_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.read_nama_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer5.Add( self.read_nama_barang, 0, wx.ALL, 5 )

		self.teks_edit_umur_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Stock Awal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_umur_pegawai.Wrap( -1 )

		self.teks_edit_umur_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_umur_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.read_stock_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer5.Add( self.read_stock_barang, 0, wx.ALL, 5 )

		self.teks_edit_bulan_Kadaluarsa = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Stock Yang Ingin Diambil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_bulan_Kadaluarsa.Wrap( -1 )

		self.teks_edit_bulan_Kadaluarsa.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_bulan_Kadaluarsa, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_ambil_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_ambil_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_simpan_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_simpan_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_simpan_barang.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		fgSizer5.Add( self.btn_simpan_barang, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.btn_batal_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_batal_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_batal_barang.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		fgSizer5.Add( self.btn_batal_barang, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( fgSizer5 )
		self.m_panel6.Layout()
		fgSizer5.Fit( self.m_panel6 )
		bSizer51.Add( self.m_panel6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_ambil_barang.SetSizer( bSizer51 )
		self.panel_ambil_barang.Layout()
		bSizer51.Fit( self.panel_ambil_barang )
		bSizer12.Add( self.panel_ambil_barang, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.btn_simpan_barang.Bind( wx.EVT_BUTTON, self.btn_simpan_barangOnButtonClick )
		self.btn_batal_barang.Bind( wx.EVT_BUTTON, self.btn_batal_barangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_batal_barangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class form_input_barang
###########################################################################

class form_input_barang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.panel_input_barang = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.teks_input_barang = wx.StaticText( self.panel_input_barang, wx.ID_ANY, u"INPUT BARANG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_input_barang.Wrap( -1 )

		self.teks_input_barang.SetFont( wx.Font( 28, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer51.Add( self.teks_input_barang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer51.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_panel6 = wx.Panel( self.panel_input_barang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.teks_edit_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_pegawai.Wrap( -1 )

		self.teks_edit_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.read_nama_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer5.Add( self.read_nama_barang, 0, wx.ALL, 5 )

		self.teks_edit_umur_pegawai = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Stock Awal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_umur_pegawai.Wrap( -1 )

		self.teks_edit_umur_pegawai.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_umur_pegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.read_stock_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer5.Add( self.read_stock_barang, 0, wx.ALL, 5 )

		self.teks_edit_bulan_Kadaluarsa = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Stock Yang Ingin Diambil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teks_edit_bulan_Kadaluarsa.Wrap( -1 )

		self.teks_edit_bulan_Kadaluarsa.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer5.Add( self.teks_edit_bulan_Kadaluarsa, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_input_barang = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.input_input_barang, 0, wx.ALL, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_simpan_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_simpan_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_simpan_barang.SetBackgroundColour( wx.Colour( 0, 206, 0 ) )

		fgSizer5.Add( self.btn_simpan_barang, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.btn_batal_barang = wx.Button( self.m_panel6, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.btn_batal_barang.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )
		self.btn_batal_barang.SetBackgroundColour( wx.Colour( 246, 69, 70 ) )

		fgSizer5.Add( self.btn_batal_barang, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( fgSizer5 )
		self.m_panel6.Layout()
		fgSizer5.Fit( self.m_panel6 )
		bSizer51.Add( self.m_panel6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_input_barang.SetSizer( bSizer51 )
		self.panel_input_barang.Layout()
		bSizer51.Fit( self.panel_input_barang )
		bSizer12.Add( self.panel_input_barang, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.btn_simpan_barang.Bind( wx.EVT_BUTTON, self.btn_simpan_barangOnButtonClick )
		self.btn_batal_barang.Bind( wx.EVT_BUTTON, self.btn_batal_barangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan_barangOnButtonClick( self, event ):
		event.Skip()

	def btn_batal_barangOnButtonClick( self, event ):
		event.Skip()


