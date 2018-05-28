# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
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
        Dialog.resize(445, 414)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 75))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 75))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.dockWidget = QtGui.QDockWidget(Dialog)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.verticalLayout.addWidget(self.dockWidget)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Button_Listen = QtGui.QPushButton(Dialog)
        self.Button_Listen.setObjectName(_fromUtf8("Button_Listen"))
        self.horizontalLayout.addWidget(self.Button_Listen)
        self.Button_Play = QtGui.QPushButton(Dialog)
        self.Button_Play.setObjectName(_fromUtf8("Button_Play"))
        self.horizontalLayout.addWidget(self.Button_Play)
        self.Button_Parametre = QtGui.QPushButton(Dialog)
        self.Button_Parametre.setObjectName(_fromUtf8("Button_Parametre"))
        self.horizontalLayout.addWidget(self.Button_Parametre)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Button_Listen, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.ecouterClick)
        QtCore.QObject.connect(self.Button_Play, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.jouerClick)
        QtCore.QObject.connect(self.Button_Parametre, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.parametreClick)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textBrowser, self.Button_Listen)
        Dialog.setTabOrder(self.Button_Listen, self.Button_Play)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Karaoké", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bienvenue</p></body></html>", None))
        self.Button_Listen.setText(_translate("Dialog", "Ecouter", None))
        self.Button_Play.setText(_translate("Dialog", "Jouer", None))
        self.Button_Parametre.setText(_translate("Dialog", "Paramètre", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

