# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_view3dpoints.ui'
#
# Created: Thu Feb  6 21:58:18 2014
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_view3Dpoints(object):
    def setupUi(self, view3Dpoints):
        view3Dpoints.setObjectName(_fromUtf8("view3Dpoints"))
        view3Dpoints.resize(355, 90)
        self.verticalLayout = QtGui.QVBoxLayout(view3Dpoints)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(view3Dpoints)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.zCB = QtGui.QComboBox(self.splitter)
        self.zCB.setObjectName(_fromUtf8("zCB"))
        self.zCB.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(view3Dpoints)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(view3Dpoints)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), view3Dpoints.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), view3Dpoints.reject)
        QtCore.QMetaObject.connectSlotsByName(view3Dpoints)

    def retranslateUi(self, view3Dpoints):
        view3Dpoints.setWindowTitle(_translate("view3Dpoints", "view3Dpoints", None))
        self.label.setText(_translate("view3Dpoints", "Z field", None))
        self.zCB.setItemText(0, _translate("view3Dpoints", "Z Value", None))

