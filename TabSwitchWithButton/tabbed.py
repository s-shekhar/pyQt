# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabbed = QtGui.QTabWidget(self.centralwidget)
        self.tabbed.setEnabled(True)
        self.tabbed.setTabPosition(QtGui.QTabWidget.West)
        self.tabbed.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabbed.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabbed.setTabsClosable(False)
        self.tabbed.setObjectName(_fromUtf8("tabbed"))
        #self.tabbed.setStyleSheet("QTabWidget::tab::disabled{width: 0; height: 0; margin: 0; padding: 0; border: none;}")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(390, 280, 65, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabbed.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(210, 190, 65, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabbed.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabbed)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #code for calling function for switching tab based on index value
        self.pushButton.clicked.connect(self.handleButton,0)
        self.pushButton_2.clicked.connect(self.handleButton_2,1)

        self.retranslateUi(MainWindow)
        #self.tabbed.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def handleButton(self):
        self.tabbed.setCurrentIndex(0)


    def handleButton_2(self):
        self.tabbed.setCurrentIndex(1)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "VMWARE", None))
        self.tabbed.setTabText(self.tabbed.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.label.setText(_translate("MainWindow", "CITRIX", None))
        self.tabbed.setTabText(self.tabbed.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.pushButton_2.setText(_translate("MainWindow", "CITRIX", None))
        self.pushButton.setText(_translate("MainWindow", "VMWARE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
