# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(947, 467)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 941, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.calendarWidget = MyCalendar(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 0, 401, 201))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Saturday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.invoice_scrollArea = QtWidgets.QScrollArea(self.tab)
        self.invoice_scrollArea.setGeometry(QtCore.QRect(470, 0, 461, 281))
        self.invoice_scrollArea.setWidgetResizable(True)
        self.invoice_scrollArea.setObjectName("invoice_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.invoice_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 210, 341, 221))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.invoice_number_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.invoice_number_lineEdit.setGeometry(QtCore.QRect(70, 50, 61, 21))
        self.invoice_number_lineEdit.setObjectName("invoice_number_lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(8, 50, 61, 20))
        self.label_2.setObjectName("label_2")
        self.payment_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.payment_comboBox.setGeometry(QtCore.QRect(10, 140, 72, 22))
        self.payment_comboBox.setObjectName("payment_comboBox")
        self.payment_comboBox.addItem("")
        self.payment_comboBox.addItem("")
        self.add_contact_Button1 = QtWidgets.QPushButton(self.groupBox)
        self.add_contact_Button1.setGeometry(QtCore.QRect(210, 160, 91, 21))
        self.add_contact_Button1.setObjectName("add_contact_Button1")
        self.genInvoice_Button = QtWidgets.QPushButton(self.groupBox)
        self.genInvoice_Button.setGeometry(QtCore.QRect(200, 190, 111, 21))
        self.genInvoice_Button.setObjectName("genInvoice_Button")
        self.contacts_listView = QtWidgets.QListView(self.groupBox)
        self.contacts_listView.setGeometry(QtCore.QRect(180, 0, 161, 151))
        self.contacts_listView.setObjectName("contacts_listView")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(650, 300, 281, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(350, 300, 291, 131))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(480, 280, 47, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(780, 280, 47, 13))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(35, 21, 871, 311))
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.add_contact_Button = QtWidgets.QPushButton(self.tab_2)
        self.add_contact_Button.setGeometry(QtCore.QRect(50, 350, 80, 21))
        self.add_contact_Button.setObjectName("add_contact_Button")
        self.delete_contact_Button = QtWidgets.QPushButton(self.tab_2)
        self.delete_contact_Button.setGeometry(QtCore.QRect(150, 350, 80, 21))
        self.delete_contact_Button.setObjectName("delete_contact_Button")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.settingAddUser_Button = QtWidgets.QPushButton(self.tab_4)
        self.settingAddUser_Button.setGeometry(QtCore.QRect(10, 230, 91, 21))
        self.settingAddUser_Button.setObjectName("settingAddUser_Button")
        self.setting_tableView = QtWidgets.QTableView(self.tab_4)
        self.setting_tableView.setGeometry(QtCore.QRect(10, 10, 921, 211))
        self.setting_tableView.setObjectName("setting_tableView")
        self.settingDelete_Button = QtWidgets.QPushButton(self.tab_4)
        self.settingDelete_Button.setGeometry(QtCore.QRect(110, 250, 80, 21))
        self.settingDelete_Button.setObjectName("settingDelete_Button")
        self.settingAddSubC_Button = QtWidgets.QPushButton(self.tab_4)
        self.settingAddSubC_Button.setGeometry(QtCore.QRect(10, 260, 91, 21))
        self.settingAddSubC_Button.setObjectName("settingAddSubC_Button")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Invoicing"))
        self.label_2.setText(_translate("Form", "Invoice No."))
        self.payment_comboBox.setItemText(0, _translate("Form", "Bank"))
        self.payment_comboBox.setItemText(1, _translate("Form", "Cash"))
        self.add_contact_Button1.setText(_translate("Form", "Add Contact"))
        self.genInvoice_Button.setText(_translate("Form", "Generate Invoice"))
        self.label_9.setText(_translate("Form", "Notes"))
        self.label_10.setText(_translate("Form", "Extras"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Invoicing"))
        self.add_contact_Button.setText(_translate("Form", "Add Contact"))
        self.delete_contact_Button.setText(_translate("Form", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Contacts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Sent"))
        self.settingAddUser_Button.setText(_translate("Form", "Add User"))
        self.settingDelete_Button.setText(_translate("Form", "Delete"))
        self.settingAddSubC_Button.setText(_translate("Form", "Add Sub C."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Settings"))
from myCalendar import MyCalendar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
