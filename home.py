import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class UiForm(object):
    def setup_Ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(741, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/tasque.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.background_frame = QtWidgets.QFrame(Form)
        self.background_frame.setGeometry(QtCore.QRect(0, 0, 741, 571))
        self.background_frame.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame.setObjectName("background_frame")
        self.heading_label = QtWidgets.QLabel(self.background_frame)
        self.heading_label.setGeometry(QtCore.QRect(160, 20, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.heading_label.setFont(font)
        self.heading_label.setObjectName("heading_label")
        self.hz_line = QtWidgets.QFrame(self.background_frame)
        self.hz_line.setGeometry(QtCore.QRect(90, 100, 581, 20))
        self.hz_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.hz_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hz_line.setObjectName("hz_line")
        self.getPlayer_list = QtWidgets.QListView(self.background_frame)
        self.getPlayer_list.setGeometry(QtCore.QRect(110, 160, 256, 351))
        self.getPlayer_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.getPlayer_list.setObjectName("getPlayer_list")
        self.getpoint_list = QtWidgets.QListView(self.background_frame)
        self.getpoint_list.setGeometry(QtCore.QRect(400, 160, 256, 351))
        self.getpoint_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.getpoint_list.setObjectName("getpoint_list")
        self.calculate_btn = QtWidgets.QPushButton(self.background_frame)
        self.calculate_btn.setGeometry(QtCore.QRect(330, 520, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculate_btn.setFont(font)
        self.calculate_btn.setObjectName("calculate_btn")
        self.players_label = QtWidgets.QLabel(self.background_frame)
        self.players_label.setGeometry(QtCore.QRect(110, 135, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.players_label.setFont(font)
        self.players_label.setObjectName("players_label")
        self.point_label = QtWidgets.QLabel(self.background_frame)
        self.point_label.setGeometry(QtCore.QRect(400, 136, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.point_label.setFont(font)
        self.point_label.setObjectName("point_label")
        self.gettotal_label = QtWidgets.QLabel(self.background_frame)
        self.gettotal_label.setGeometry(QtCore.QRect(460, 140, 61, 20))
        self.gettotal_label.setText("")
        self.gettotal_label.setObjectName("gettotal_label")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.background_frame)
        self.verticalScrollBar.setGeometry(QtCore.QRect(350, 160, 16, 351))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.background_frame)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(640, 160, 16, 351))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.team_combobox = QtWidgets.QComboBox(self.background_frame)
        self.team_combobox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team_combobox.setGeometry(QtCore.QRect(140, 60, 191, 22))
        self.team_combobox.setObjectName("team_combobox")
        self.team_combobox.addItem("")
        self.team_combobox.addItem("")
        self.team_combobox.addItem("")
        self.team_combobox.addItem("")
        self.team_combobox.addItem("")
        self.team_combobox.addItem("")
        self.team_combobox.addItem("")
        self.matches_combobox = QtWidgets.QComboBox(self.background_frame)
        self.matches_combobox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.matches_combobox.setGeometry(QtCore.QRect(410, 60, 191, 21))
        self.matches_combobox.setObjectName("matches_combobox")
        self.matches_combobox.addItem("")
        self.matches_combobox.addItem("")
        self.matches_combobox.addItem("")
        self.matches_combobox.addItem("")
        self.matches_combobox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate"))
        self.heading_label.setText(_translate("Form", "Evaluate the Performance of Your Fantasy Team"))
        self.calculate_btn.setText(_translate("Form", "Calculate Score"))
        self.players_label.setText(_translate("Form", "Players"))
        self.point_label.setText(_translate("Form", "Points"))
        self.team_combobox.setItemText(0, _translate("Form", "internshala"))
        self.team_combobox.setItemText(1, _translate("Form", "python"))
        self.team_combobox.setItemText(2, _translate("Form", "java"))
        self.team_combobox.setItemText(3, _translate("Form", "c"))
        self.team_combobox.setItemText(4, _translate("Form", "c++"))
        self.team_combobox.setItemText(5, _translate("Form", "django"))
        self.team_combobox.setItemText(6, _translate("Form", "angular"))
        self.matches_combobox.setItemText(0, _translate("Form", "match1"))
        self.matches_combobox.setItemText(1, _translate("Form", "match2"))
        self.matches_combobox.setItemText(2, _translate("Form", "match3"))
        self.matches_combobox.setItemText(3, _translate("Form", "match4"))
        self.matches_combobox.setItemText(4, _translate("Form", "match5"))

#this class for main window

class Ui_MainWindow(object):
    a=UiForm()

    start_bat = 0
    start_bow = 0
    start_ar = 0
    start_wk = 0
    totalpoint = 1000
    pointused = 0

    def fetchvalue(self):



        try:
            conn = sqlite3.connect("players.db")
            cur = conn.cursor()
            cur.execute("select value from stats where")
            record = cur.fetchall()
            for row in record:
                print(row)
        except Exception:
            print("Error")
    def savedata(self):
        pass


    def first(self):
        self.getbat_label.setNum(self.start_bat)
        self.getbow_label.setNum(self.start_bow)
        self.getar_label.setNum(self.start_ar)
        self.getwk_label.setNum(self.start_wk)
        self.getpoint_label.setNum(self.totalpoint)
        self.getpoint_label_2.setNum(self.pointused)

        self.bat_radiobtn.toggled.connect(self.checkstate)
        self.bow_radiobtn.toggled.connect(self.checkstate)
        self.ar_radiobtn.toggled.connect(self.checkstate)
        self.wk_radiobtn.toggled.connect(self.checkstate)

        self.getplayer_list.itemDoubleClicked.connect(self.removeplayerlist)
        self.getplayerafter_list.itemDoubleClicked.connect(self.removeplayerafterlist)

        self.getteamname_label.setText("Internshala11")


        try:
            conn = sqlite3.connect("players.db")
            cur = conn.cursor()
            cur.execute("select name from teams ")
            record = cur.fetchall()
            for row in record:
                print(row)
        except Exception:
            print("Error")

    

    def checkstate(self):

        if self.bat_radiobtn.isChecked() == True:
            try:
                category="BAT"
                conn = sqlite3.connect("players.db")
                cur = conn.cursor()
                cur.execute("select player from stats where ctg = ?",(category,))
                record = cur.fetchall()
                self.getplayer_list.clear()
                for i in range(len(record)):
                    item = QtWidgets.QListWidgetItem(record[i][0])
                    self.getplayer_list.addItem(item.text())



            except Exception:
                print("Error")

        if self.bow_radiobtn.isChecked() == True:
            try:
                category="BWL"
                conn = sqlite3.connect("players.db")
                cur = conn.cursor()
                cur.execute("select player from stats where ctg = ?",(category,))
                record = cur.fetchall()
                self.getplayer_list.clear()
                for i in range(len(record)):
                    item = QtWidgets.QListWidgetItem(record[i][0])
                    self.getplayer_list.addItem(item.text())

            except Exception:
                print("Error")

        if self.ar_radiobtn.isChecked() == True:
            try:
                category="AR"
                conn = sqlite3.connect("players.db")
                cur = conn.cursor()
                cur.execute("select player from stats where ctg = ?",(category,))
                record = cur.fetchall()
                self.getplayer_list.clear()
                for i in range(len(record)):
                    item = QtWidgets.QListWidgetItem(record[i][0])
                    self.getplayer_list.addItem(item.text())

            except Exception:
                print("Error")

        if self.wk_radiobtn.isChecked() == True:
            try:
                category="WK"
                conn = sqlite3.connect("players.db")
                cur = conn.cursor()
                cur.execute("select player from stats where ctg= ?",(category,))
                record = cur.fetchall()
                self.getplayer_list.clear()
                for i in range(len(record)):
                    item = QtWidgets.QListWidgetItem(record[i][0])
                    self.getplayer_list.addItem(item.text())

            except Exception:
                print("Error")




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 661)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/gnujump.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setIconSize(QtCore.QSize(20, 15))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_frame = QtWidgets.QFrame(self.centralwidget)
        self.background_frame.setGeometry(QtCore.QRect(-1, -1, 901, 631))
        self.background_frame.setStyleSheet("")
        self.background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame.setObjectName("background_frame")
        self.selection_frame = QtWidgets.QFrame(self.background_frame)
        self.selection_frame.setGeometry(QtCore.QRect(40, 30, 811, 81))
        self.selection_frame.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.selection_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selection_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selection_frame.setObjectName("selection_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.selection_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bat_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bat_label.setFont(font)
        self.bat_label.setObjectName("bat_label")
        self.horizontalLayout.addWidget(self.bat_label)
        self.getbat_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getbat_label.setFont(font)
        self.getbat_label.setText("")
        self.getbat_label.setObjectName("getbat_label")
        self.getbat_label.setStyleSheet("color:blue;")
        self.horizontalLayout.addWidget(self.getbat_label)
        self.bow_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bow_label.setFont(font)
        self.bow_label.setObjectName("bow_label")
        self.horizontalLayout.addWidget(self.bow_label)
        self.getbow_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getbow_label.setFont(font)
        self.getbow_label.setText("")
        self.getbow_label.setObjectName("getbow_label")
        self.getbow_label.setStyleSheet("color:blue;")
        self.horizontalLayout.addWidget(self.getbow_label)
        self.ar_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ar_label.setFont(font)
        self.ar_label.setObjectName("ar_label")
        self.horizontalLayout.addWidget(self.ar_label)
        self.getar_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getar_label.setFont(font)
        self.getar_label.setText("")
        self.getar_label.setObjectName("getar_label")
        self.getar_label.setStyleSheet("color:blue;")
        self.horizontalLayout.addWidget(self.getar_label)
        self.wk_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wk_label.setFont(font)
        self.wk_label.setObjectName("wk_label")
        self.horizontalLayout.addWidget(self.wk_label)
        self.getwk_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getwk_label.setFont(font)
        self.getwk_label.setText("")
        self.getwk_label.setObjectName("getwk_label")
        self.getwk_label.setStyleSheet("color:blue;")
        self.horizontalLayout.addWidget(self.getwk_label)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.yourselection_label = QtWidgets.QLabel(self.selection_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yourselection_label.setFont(font)
        self.yourselection_label.setObjectName("yourselection_label")
        self.gridLayout.addWidget(self.yourselection_label, 0, 0, 1, 1)
        self.list_frame = QtWidgets.QFrame(self.background_frame)
        self.list_frame.setGeometry(QtCore.QRect(40, 120, 811, 461))
        self.list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_frame.setObjectName("list_frame")
        self.getplayer_list = QtWidgets.QListWidget(self.list_frame)
        self.getplayer_list.setGeometry(QtCore.QRect(31, 73, 331, 380))
        self.getplayer_list.setObjectName("getplayer_list")
        self.getplayer_list.setStyleSheet("color:blue;")

        self.getplayerafter_list = QtWidgets.QListWidget(self.list_frame)
        self.getplayerafter_list.setGeometry(QtCore.QRect(439, 73, 341, 380))
        self.getplayerafter_list.setObjectName("getplayerafter_list")
        self.getplayerafter_list.setStyleSheet("color:blue;")
        self.points_label = QtWidgets.QLabel(self.list_frame)
        self.points_label.setGeometry(QtCore.QRect(30, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.points_label.setFont(font)
        self.points_label.setObjectName("points_label")
        self.usedpoint_label = QtWidgets.QLabel(self.list_frame)
        self.usedpoint_label.setGeometry(QtCore.QRect(440, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usedpoint_label.setFont(font)
        self.usedpoint_label.setObjectName("usedpoint_label")
        self.getpoint_label = QtWidgets.QLabel(self.list_frame)
        self.getpoint_label.setGeometry(QtCore.QRect(130, 20, 91, 21))
        self.getpoint_label.setStyleSheet("color:blue;")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getpoint_label.setFont(font)
        self.getpoint_label.setText("")
        self.getpoint_label.setObjectName("getpoint_label")
        self.getpoint_label_2 = QtWidgets.QLabel(self.list_frame)
        self.getpoint_label_2.setGeometry(QtCore.QRect(520, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getpoint_label_2.setFont(font)
        self.getpoint_label_2.setText("")
        self.getpoint_label_2.setObjectName("getpoint_label_2")
        self.getpoint_label_2.setStyleSheet("color:blue;")
        self.layoutWidget = QtWidgets.QWidget(self.list_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 50, 261, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.teamname_layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.teamname_layout.setContentsMargins(0, 0, 0, 0)
        self.teamname_layout.setObjectName("teamname_layout")
        self.teamname_label = QtWidgets.QLabel(self.layoutWidget)
        self.teamname_label.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.teamname_label.setFont(font)
        self.teamname_label.setObjectName("teamname_label")
        self.teamname_layout.addWidget(self.teamname_label)
        self.getteamname_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getteamname_label.setFont(font)
        self.getteamname_label.setText("")
        self.getteamname_label.setObjectName("getteamname_label")
        self.getteamname_label.setStyleSheet("color:blue;")
        self.teamname_layout.addWidget(self.getteamname_label)
        self.layoutWidget1 = QtWidgets.QWidget(self.list_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 50, 321, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.radio_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.radio_layout.setContentsMargins(0, 0, 0, 0)
        self.radio_layout.setObjectName("radio_layout")
        self.bat_radiobtn = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bat_radiobtn.setFont(font)
        self.bat_radiobtn.setObjectName("bat_radiobtn")
        self.radio_layout.addWidget(self.bat_radiobtn)
        self.bow_radiobtn = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bow_radiobtn.setFont(font)
        self.bow_radiobtn.setObjectName("bow_radiobtn")
        self.radio_layout.addWidget(self.bow_radiobtn)
        self.ar_radiobtn = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ar_radiobtn.setFont(font)
        self.ar_radiobtn.setObjectName("ar_radiobtn")
        self.radio_layout.addWidget(self.ar_radiobtn)
        self.wk_radiobtn = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wk_radiobtn.setFont(font)
        self.wk_radiobtn.setObjectName("wk_radiobtn")
        self.radio_layout.addWidget(self.wk_radiobtn)
        self.bat_radiobtn.raise_()
        self.ar_radiobtn.raise_()
        self.wk_radiobtn.raise_()
        self.bow_radiobtn.raise_()
        self.gt_label = QtWidgets.QLabel(self.list_frame)
        self.gt_label.setGeometry(QtCore.QRect(400, 230, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gt_label.setFont(font)
        self.gt_label.setObjectName("gt_label")
        MainWindow.setCentralWidget(self.centralwidget)

        #menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 110, 21))
        self.menubar.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("\n""background-color: rgb(166, 166, 166);")
        self.menubar.setObjectName("menubar")
        self.menu_manage = QtWidgets.QMenu(self.menubar)
        self.menu_manage.setObjectName("menu_manage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_new = QtWidgets.QAction(MainWindow)
        self.menu_new.setObjectName("menu_new")

        self.menu_new.triggered.connect(self.first)

        self.menu_open = QtWidgets.QAction(MainWindow)
        self.menu_open.setObjectName("menu_open")
        self.menu_save = QtWidgets.QAction(MainWindow)
        self.menu_save.setObjectName("menu_save")

        self.menu_save.triggered.connect(self.savedata)

        self.menu_evaluate = QtWidgets.QAction(MainWindow)
        self.menu_evaluate.setObjectName("menu_evaluate")

        #evaluate connected to popup
        self.menu_evaluate.triggered.connect(self.evaluate)

        self.menu_manage.addAction(self.menu_new)
        self.menu_manage.addAction(self.menu_open)
        self.menu_manage.addAction(self.menu_save)
        self.menu_manage.addAction(self.menu_evaluate)
        self.menubar.addAction(self.menu_manage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def removeplayerlist(self, item):
        self.getplayer_list.takeItem(self.getplayer_list.row(item))
        self.getplayerafter_list.addItem(item.text())

    def removeplayerafterlist(self, item):
        self.getplayerafter_list.takeItem(self.getplayerafter_list.row(item))
        self.getplayer_list.addItem(item.text())




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy_Cricket"))
        self.bat_label.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.bow_label.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.ar_label.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.wk_label.setText(_translate("MainWindow", "Wicket-Keeper (WK)"))
        self.yourselection_label.setText(_translate("MainWindow", "Your Selections"))
        self.points_label.setText(_translate("MainWindow", "Points Available"))
        self.usedpoint_label.setText(_translate("MainWindow", "Points Used"))
        self.teamname_label.setText(_translate("MainWindow", "Team Name"))
        self.bat_radiobtn.setText(_translate("MainWindow", "BAT"))
        self.bow_radiobtn.setText(_translate("MainWindow", "BOW"))
        self.ar_radiobtn.setText(_translate("MainWindow", "AR"))
        self.wk_radiobtn.setText(_translate("MainWindow", "WK"))
        self.gt_label.setText(_translate("MainWindow", ">"))
        self.menu_manage.setTitle(_translate("MainWindow", "Manage Teams"))
        self.menu_new.setText(_translate("MainWindow", "NEW Team"))
        self.menu_open.setText(_translate("MainWindow", "OPEN Team"))
        self.menu_save.setText(_translate("MainWindow", "SAVE Team"))
        self.menu_evaluate.setText(_translate("MainWindow", "EVALUATE Team"))

    def evaluate(self):
        self.win=QtWidgets.QMainWindow()
        self.ui=UiForm()
        self.ui.setup_Ui(self.win)
        self.win.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())