# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'param.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(446, 189)
        Dialog.setMinimumSize(QtCore.QSize(446, 189))
        Dialog.setMaximumSize(QtCore.QSize(446, 189))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setMinimum(1024)
        self.spinBox.setMaximum(4096)
        self.spinBox.setSingleStep(1024)
        self.spinBox.setProperty("value", 1024)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setMinimum(8000)
        self.spinBox_2.setMaximum(44100)
        self.spinBox_2.setSingleStep(1000)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_3 = QtGui.QSpinBox(Dialog)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(2)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.horizontalLayout_4.addWidget(self.spinBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.Button_Path = QtGui.QPushButton(Dialog)
        self.Button_Path.setObjectName(_fromUtf8("Button_Path"))
        self.verticalLayout.addWidget(self.Button_Path)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Button_Path, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.CheminDEnregistrementClick)
        QtCore.QObject.connect(self.spinBox_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.SetChannel)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.SetRate)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.SetChunk)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Karaoké - Paramètre", None))
        self.label.setText(_translate("Dialog", "Taille de tableau", None))
        self.label_2.setText(_translate("Dialog", "Fréquence d\'échantillonnage", None))
        self.label_3.setText(_translate("Dialog", "Canaux", None))
        self.Button_Path.setText(_translate("Dialog", "Chemin d\'enregistrement", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

