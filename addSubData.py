# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSubData.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(198, 267)
        self.settingSave_Button = QtWidgets.QPushButton(Dialog)
        self.settingSave_Button.setGeometry(QtCore.QRect(10, 230, 101, 31))
        self.settingSave_Button.setObjectName("settingSave_Button")
        self.settingSubRoad_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.settingSubRoad_lineEdit.setGeometry(QtCore.QRect(80, 70, 113, 21))
        self.settingSubRoad_lineEdit.setText("")
        self.settingSubRoad_lineEdit.setObjectName("settingSubRoad_lineEdit")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(4, 40, 71, 20))
        self.label_17.setObjectName("label_17")
        self.settingSubName_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.settingSubName_lineEdit.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.settingSubName_lineEdit.setText("")
        self.settingSubName_lineEdit.setObjectName("settingSubName_lineEdit")
        self.settingSubEmail_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.settingSubEmail_lineEdit.setGeometry(QtCore.QRect(80, 200, 113, 21))
        self.settingSubEmail_lineEdit.setObjectName("settingSubEmail_lineEdit")
        self.settingSubCounty_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.settingSubCounty_lineEdit.setGeometry(QtCore.QRect(80, 130, 113, 21))
        self.settingSubCounty_lineEdit.setText("")
        self.settingSubCounty_lineEdit.setObjectName("settingSubCounty_lineEdit")
        self.settingSubArea_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.settingSubArea_lineEdit.setGeometry(QtCore.QRect(80, 100, 113, 21))
        self.settingSubArea_lineEdit.setText("")
        self.settingSubArea_lineEdit.setObjectName("settingSubArea_lineEdit")
        self.settingSubPostcode_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.settingSubPostcode_lineEdit.setGeometry(QtCore.QRect(80, 160, 113, 21))
        self.settingSubPostcode_lineEdit.setText("")
        self.settingSubPostcode_lineEdit.setObjectName("settingSubPostcode_lineEdit")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.label_18.setObjectName("label_18")
        self.settingSubHouse_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.settingSubHouse_lineEdit.setGeometry(QtCore.QRect(80, 40, 113, 21))
        self.settingSubHouse_lineEdit.setText("")
        self.settingSubHouse_lineEdit.setObjectName("settingSubHouse_lineEdit")
        self.label_57 = QtWidgets.QLabel(Dialog)
        self.label_57.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_57.setObjectName("label_57")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(4, 200, 71, 20))
        self.label_21.setObjectName("label_21")
        self.label_58 = QtWidgets.QLabel(Dialog)
        self.label_58.setGeometry(QtCore.QRect(4, 70, 81, 20))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(Dialog)
        self.label_59.setGeometry(QtCore.QRect(30, 100, 41, 20))
        self.label_59.setObjectName("label_59")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(10, 160, 61, 21))
        self.label_19.setObjectName("label_19")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(120, 230, 71, 31))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Sub Contractor"))
        self.settingSave_Button.setText(_translate("Dialog", "Update Settings"))
        self.label_17.setText(_translate("Dialog", "Sub  House:"))
        self.label_18.setText(_translate("Dialog", "Sub Name:"))
        self.label_57.setText(_translate("Dialog", "County :"))
        self.label_21.setText(_translate("Dialog", "Sub Email :"))
        self.label_58.setText(_translate("Dialog", "Road Name:"))
        self.label_59.setText(_translate("Dialog", "Area  :"))
        self.label_19.setText(_translate("Dialog", "Postcode :"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
