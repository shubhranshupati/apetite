# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Subhranshu\OneDrive\Desktop\python project\Add files via upload · jincy-p-janardhanan_Fantasy-Cricket-Game@f7424a1_files\game.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetNameDialog(object):
    def setupUi(self, GetNameDialog):
        GetNameDialog.setObjectName("GetNameDialog")
        GetNameDialog.resize(565, 171)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GetNameDialog.sizePolicy().hasHeightForWidth())
        GetNameDialog.setSizePolicy(sizePolicy)
        GetNameDialog.setMinimumSize(QtCore.QSize(565, 171))
        GetNameDialog.setMaximumSize(QtCore.QSize(565, 171))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Subhranshu\\OneDrive\\Desktop\\python project\\Add files via upload · jincy-p-janardhanan_Fantasy-Cricket-Game@f7424a1_files\\IMAGES/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GetNameDialog.setWindowIcon(icon)
        GetNameDialog.setModal(True)
        self.GetTeamNameButtons = QtWidgets.QDialogButtonBox(GetNameDialog)
        self.GetTeamNameButtons.setGeometry(QtCore.QRect(460, 50, 81, 61))
        self.GetTeamNameButtons.setOrientation(QtCore.Qt.Vertical)
        self.GetTeamNameButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.GetTeamNameButtons.setCenterButtons(True)
        self.GetTeamNameButtons.setObjectName("GetTeamNameButtons")
        self.BackgroundLbl = QtWidgets.QLabel(GetNameDialog)
        self.BackgroundLbl.setGeometry(QtCore.QRect(0, -20, 571, 251))
        self.BackgroundLbl.setText("")
        self.BackgroundLbl.setPixmap(QtGui.QPixmap("c:\\Users\\Subhranshu\\OneDrive\\Desktop\\python project\\Add files via upload · jincy-p-janardhanan_Fantasy-Cricket-Game@f7424a1_files\\IMAGES/ground2.jpg"))
        self.BackgroundLbl.setScaledContents(True)
        self.BackgroundLbl.setObjectName("BackgroundLbl")
        self.TeamNameLine = QtWidgets.QLineEdit(GetNameDialog)
        self.TeamNameLine.setGeometry(QtCore.QRect(110, 70, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TeamNameLine.setFont(font)
        self.TeamNameLine.setObjectName("TeamNameLine")
        self.CricketerImageLbl = QtWidgets.QLabel(GetNameDialog)
        self.CricketerImageLbl.setGeometry(QtCore.QRect(0, 0, 111, 171))
        self.CricketerImageLbl.setText("")
        self.CricketerImageLbl.setPixmap(QtGui.QPixmap("c:\\Users\\Subhranshu\\OneDrive\\Desktop\\python project\\Add files via upload · jincy-p-janardhanan_Fantasy-Cricket-Game@f7424a1_files\\IMAGES/logo.png"))
        self.CricketerImageLbl.setScaledContents(True)
        self.CricketerImageLbl.setObjectName("CricketerImageLbl")
        self.EnterTeamNameLbl = QtWidgets.QLabel(GetNameDialog)
        self.EnterTeamNameLbl.setGeometry(QtCore.QRect(110, 40, 321, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(253, 253, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 253, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.EnterTeamNameLbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(12)
        self.EnterTeamNameLbl.setFont(font)
        self.EnterTeamNameLbl.setWordWrap(True)
        self.EnterTeamNameLbl.setObjectName("EnterTeamNameLbl")
        self.BackgroundLbl.raise_()
        self.GetTeamNameButtons.raise_()
        self.TeamNameLine.raise_()
        self.CricketerImageLbl.raise_()
        self.EnterTeamNameLbl.raise_()

        self.retranslateUi(GetNameDialog)
        self.GetTeamNameButtons.accepted.connect(GetNameDialog.accept) # type: ignore
        self.GetTeamNameButtons.rejected.connect(GetNameDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(GetNameDialog)

    def retranslateUi(self, GetNameDialog):
        _translate = QtCore.QCoreApplication.translate
        GetNameDialog.setWindowTitle(_translate("GetNameDialog", "Fantasy Cricket"))
        self.TeamNameLine.setPlaceholderText(_translate("GetNameDialog", "Ex. My Team"))
        self.EnterTeamNameLbl.setText(_translate("GetNameDialog", "Enter Your Team Name Here"))
