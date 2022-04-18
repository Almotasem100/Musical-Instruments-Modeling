# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.slider = QtWidgets.QSlider(self.frame_4)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.verticalLayout_3.addWidget(self.slider)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.piano = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.piano.setFont(font)
        self.piano.setObjectName("piano")
        self.verticalLayout.addWidget(self.piano)
        self.guitar = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guitar.setFont(font)
        self.guitar.setObjectName("guitar")
        self.verticalLayout.addWidget(self.guitar)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.frame_3)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.csharp = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csharp.sizePolicy().hasHeightForWidth())
        self.csharp.setSizePolicy(sizePolicy)
        self.csharp.setMinimumSize(QtCore.QSize(0, 0))
        self.csharp.setMaximumSize(QtCore.QSize(60, 250))
        self.csharp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.csharp.setObjectName("csharp")
        self.horizontalLayout_2.addWidget(self.csharp)
        self.eflat = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eflat.sizePolicy().hasHeightForWidth())
        self.eflat.setSizePolicy(sizePolicy)
        self.eflat.setMinimumSize(QtCore.QSize(0, 0))
        self.eflat.setMaximumSize(QtCore.QSize(60, 250))
        self.eflat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.eflat.setObjectName("eflat")
        self.horizontalLayout_2.addWidget(self.eflat)
        spacerItem4 = QtWidgets.QSpacerItem(80, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.fsharp = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fsharp.sizePolicy().hasHeightForWidth())
        self.fsharp.setSizePolicy(sizePolicy)
        self.fsharp.setMinimumSize(QtCore.QSize(0, 0))
        self.fsharp.setMaximumSize(QtCore.QSize(60, 250))
        self.fsharp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.fsharp.setObjectName("fsharp")
        self.horizontalLayout_2.addWidget(self.fsharp)
        self.aflat = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aflat.sizePolicy().hasHeightForWidth())
        self.aflat.setSizePolicy(sizePolicy)
        self.aflat.setMinimumSize(QtCore.QSize(0, 0))
        self.aflat.setMaximumSize(QtCore.QSize(60, 250))
        self.aflat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.aflat.setObjectName("aflat")
        self.horizontalLayout_2.addWidget(self.aflat)
        self.bflat = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bflat.sizePolicy().hasHeightForWidth())
        self.bflat.setSizePolicy(sizePolicy)
        self.bflat.setMinimumSize(QtCore.QSize(0, 0))
        self.bflat.setMaximumSize(QtCore.QSize(60, 250))
        self.bflat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.bflat.setObjectName("bflat")
        self.horizontalLayout_2.addWidget(self.bflat)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.horizontalFrame_2)
        self.horizontalFrame = QtWidgets.QFrame(self.frame_3)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.c_note = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_note.sizePolicy().hasHeightForWidth())
        self.c_note.setSizePolicy(sizePolicy)
        self.c_note.setMinimumSize(QtCore.QSize(0, 0))
        self.c_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_note.setObjectName("c_note")
        self.horizontalLayout.addWidget(self.c_note)
        self.d_note = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_note.sizePolicy().hasHeightForWidth())
        self.d_note.setSizePolicy(sizePolicy)
        self.d_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.d_note.setObjectName("d_note")
        self.horizontalLayout.addWidget(self.d_note)
        self.e_note = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e_note.sizePolicy().hasHeightForWidth())
        self.e_note.setSizePolicy(sizePolicy)
        self.e_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_note.setObjectName("e_note")
        self.horizontalLayout.addWidget(self.e_note)
        self.f_note = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_note.sizePolicy().hasHeightForWidth())
        self.f_note.setSizePolicy(sizePolicy)
        self.f_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.f_note.setObjectName("f_note")
        self.horizontalLayout.addWidget(self.f_note)
        self.g_note = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_note.sizePolicy().hasHeightForWidth())
        self.g_note.setSizePolicy(sizePolicy)
        self.g_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.g_note.setObjectName("g_note")
        self.horizontalLayout.addWidget(self.g_note)
        self.a_note = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_note.sizePolicy().hasHeightForWidth())
        self.a_note.setSizePolicy(sizePolicy)
        self.a_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a_note.setObjectName("a_note")
        self.horizontalLayout.addWidget(self.a_note)
        self.b_note = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_note.sizePolicy().hasHeightForWidth())
        self.b_note.setSizePolicy(sizePolicy)
        self.b_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.b_note.setObjectName("b_note")
        self.horizontalLayout.addWidget(self.b_note)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sustain Effect"))
        self.piano.setText(_translate("MainWindow", "Piano"))
        self.guitar.setText(_translate("MainWindow", "Guitar"))
        self.csharp.setText(_translate("MainWindow", "C#"))
        self.eflat.setText(_translate("MainWindow", "Eb"))
        self.fsharp.setText(_translate("MainWindow", "F#"))
        self.aflat.setText(_translate("MainWindow", "Ab"))
        self.bflat.setText(_translate("MainWindow", "Bb"))
        self.c_note.setText(_translate("MainWindow", "C"))
        self.d_note.setText(_translate("MainWindow", "D"))
        self.e_note.setText(_translate("MainWindow", "E"))
        self.f_note.setText(_translate("MainWindow", "F"))
        self.g_note.setText(_translate("MainWindow", "G"))
        self.a_note.setText(_translate("MainWindow", "A"))
        self.b_note.setText(_translate("MainWindow", "B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())