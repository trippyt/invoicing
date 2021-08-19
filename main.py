from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QStandardItemModel, QFontMetrics, QPainter
from PyQt5.QtWidgets import QMessageBox, QDialog, QAbstractItemView, QCalendarWidget
from PyQt5.QtCore import Qt, QDate, QRectF
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery
from loguru import logger as log
from form import Ui_Form
from addContact import Ui_Dialog
from addSubData import Ui_Dialog as subDialog
from addUserData import Ui_Dialog as userDialog
from workDay import Ui_Dialog as workDayWindow
from generateInvoice import Ui_Dialog as genInvoice
# from myCalendar import MyCalendar as mcal
import sys
import atexit
import sqlite3
from xlsxwriter.workbook import Workbook

# python -m PyQt5.uic.pyuic -x form.ui -o form.py
# python -m PyQt5.uic.pyuic -x addContact.ui -o addContact.py
# python -m PyQt5.uic.pyuic -x addSubData.ui -o addSubData.py
# python -m PyQt5.uic.pyuic -x addUserData.ui -o addUserData.py
# python -m PyQt5.uic.pyuic -x workDay.ui -o workDay.py
# python -m PyQt5.uic.pyuic -x generateInvoice.ui -o generateInvoice.py

DB_FILE = "Invoices.sqlite"


class ContactWindow(QDialog):
    def __init__(self, parent=None):
        super(ContactWindow, self).__init__(parent)
        self.ui2 = Ui_Dialog()
        self.ui2.setupUi(self)
        self.ui2.cancelButton.clicked.connect(self.close)
        self.ui2.save_contact_Button.clicked.connect(self.save_contact_info)  # parent.save_contact_info
        self.d = DataBase()
        self.msg = QMessageBox()
        QDialog.setTabOrder(self.ui2.house_name_lineEdit, self.ui2.roadname_lineEdit)
        QDialog.setTabOrder(self.ui2.roadname_lineEdit, self.ui2.areaname_lineEdit)
        QDialog.setTabOrder(self.ui2.areaname_lineEdit, self.ui2.county_lineEdit)
        QDialog.setTabOrder(self.ui2.county_lineEdit, self.ui2.postcode_lineEdit)
        QDialog.setTabOrder(self.ui2.postcode_lineEdit, self.ui2.save_contact_Button)
        QDialog.setTabOrder(self.ui2.save_contact_Button, self.ui2.cancelButton)

        self.parent = parent

    def error_msg(self, msg):
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText(msg)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setWindowTitle("Error!")
        self.msg.exec_()

    def save_contact_info(self):
        contact_data = [self.ui2.house_name_lineEdit.text(), self.ui2.roadname_lineEdit.text(),
                        self.ui2.areaname_lineEdit.text(), self.ui2.county_lineEdit.text(),
                        self.ui2.postcode_lineEdit.text()]
        if len(list(filter(None, contact_data))) == 0:
            log.error("Input Contact Data")
            self.error_msg("Fields are Empty!")
        else:
            name = [contact_data[0]]
            self.d.cur.execute("SELECT house_name FROM Contacts WHERE house_name LIKE ?", name)
            check = self.d.cur.fetchone()
            if check is None:
                log.debug(f"Adding New Contact")
                self.d.cur.execute(
                    '''INSERT INTO Contacts (house_name,road_name,area_name,county_name,postcode)
                     VALUES (?,?,?,?,?)''', contact_data
                )
                self.d.con.commit()
                self.close()

                self.parent.update_model()
            else:
                log.debug(f"Contact Already Exists!")
                log.debug(check)
                self.error_msg("Contact Already Exists!")


class AddUserWindow(QDialog):
    def __init__(self, parent=None):
        super(AddUserWindow, self).__init__(parent)
        self.addUserUi = userDialog()
        self.addUserUi.setupUi(self)
        self.addUserUi.cancelButton.clicked.connect(self.close)
        self.addUserUi.settingSave_Button.clicked.connect(self.saveUserData)
        self.d = DataBase()
        self.parent2 = parent
        QDialog.setTabOrder(self.addUserUi.settingUserName_lineEdit, self.addUserUi.settingUserHouse_lineEdit)
        QDialog.setTabOrder(self.addUserUi.settingUserHouse_lineEdit, self.addUserUi.settingUserRoad_lineEdit)
        QDialog.setTabOrder(self.addUserUi.settingUserRoad_lineEdit, self.addUserUi.settingUserArea_lineEdit)
        QDialog.setTabOrder(self.addUserUi.settingUserArea_lineEdit, self.addUserUi.settingUserCounty_lineEdit)
        QDialog.setTabOrder(self.addUserUi.settingUserCounty_lineEdit, self.addUserUi.settingUserPostcode_lineEdit)
        QDialog.setTabOrder(self.addUserUi.settingUserPostcode_lineEdit, self.addUserUi.settingUserEmail_lineEdit)
        QDialog.setTabOrder(self.addUserUi.settingUserEmail_lineEdit, self.addUserUi.settingSave_Button)
        QDialog.setTabOrder(self.addUserUi.settingSave_Button, self.addUserUi.cancelButton)

    def saveUserData(self):
        userData = ["user", self.addUserUi.settingUserName_lineEdit.text(),
                    self.addUserUi.settingUserEmail_lineEdit.text(), self.addUserUi.settingUserHouse_lineEdit.text(),
                    self.addUserUi.settingUserRoad_lineEdit.text(), self.addUserUi.settingUserArea_lineEdit.text(),
                    self.addUserUi.settingUserCounty_lineEdit.text(),
                    self.addUserUi.settingUserPostcode_lineEdit.text()]
        self.d.cur.execute('''INSERT INTO Config (type,name,email,houseName,roadName,areaName,countyName,
                        postcode) VALUES (?,?,?,?,?,?,?,?)''', userData)
        self.d.con.commit()
        self.parent2.update_configModel()
        self.close()


class AddSubWindow(QDialog):
    def __init__(self, parent=None):
        super(AddSubWindow, self).__init__(parent)
        self.addSubUi = subDialog()
        self.addSubUi.setupUi(self)
        self.addSubUi.cancelButton.clicked.connect(self.close)
        self.addSubUi.settingSave_Button.clicked.connect(self.saveSubData)
        self.d = DataBase()
        QDialog.setTabOrder(self.addSubUi.settingSubName_lineEdit, self.addSubUi.settingSubHouse_lineEdit)
        QDialog.setTabOrder(self.addSubUi.settingSubHouse_lineEdit, self.addSubUi.settingSubRoad_lineEdit)
        QDialog.setTabOrder(self.addSubUi.settingSubRoad_lineEdit, self.addSubUi.settingSubArea_lineEdit)
        QDialog.setTabOrder(self.addSubUi.settingSubArea_lineEdit, self.addSubUi.settingSubCounty_lineEdit)
        QDialog.setTabOrder(self.addSubUi.settingSubCounty_lineEdit, self.addSubUi.settingSubPostcode_lineEdit)
        QDialog.setTabOrder(self.addSubUi.settingSubPostcode_lineEdit, self.addSubUi.settingSubEmail_lineEdit)
        QDialog.setTabOrder(self.addSubUi.settingSubEmail_lineEdit, self.addSubUi.settingSave_Button)
        QDialog.setTabOrder(self.addSubUi.settingSave_Button, self.addSubUi.cancelButton)
        self.parent = parent

    def saveSubData(self):
        subData = ["sub contractor", self.addSubUi.settingSubName_lineEdit.text(),
                   self.addSubUi.settingSubEmail_lineEdit.text(), self.addSubUi.settingSubHouse_lineEdit.text(),
                   self.addSubUi.settingSubRoad_lineEdit.text(), self.addSubUi.settingSubArea_lineEdit.text(),
                   self.addSubUi.settingSubCounty_lineEdit.text(),
                   self.addSubUi.settingSubPostcode_lineEdit.text()]
        self.d.cur.execute('''INSERT INTO Config (type,name,email,houseName,roadName,areaName,countyName,
                        postcode) VALUES (?,?,?,?,?,?,?,?)''', subData)
        self.d.con.commit()
        self.parent.update_configModel()
        self.close()


class WorkDayWindow(QDialog):
    def __init__(self, parent=None):
        super(WorkDayWindow, self).__init__(parent)
        self.workDay = workDayWindow()
        self.workDay.setupUi(self)
        self.p = parent
        self.d = DataBase()
        self.selectedDate = self.p.ui.calendarWidget.selectedDate()
        self.workDay.cancel_Button.clicked.connect(self.close)
        self.workDay.dateEdit.setDate(self.selectedDate)
        self.workDay.extras_checkBox.clicked.connect(self.extrasCheck)
        self.workDay.comboBox.addItems(self.clientList())
        self.workDay.ok_Button.clicked.connect(self.save)
        # self.workDay.comboBox.adjustSize()
        self.dropDownSize()
        self.extrasCheck()
        self.dataExists()

    def dataExists(self):
        data = list(self.d.cur.execute("SELECT date FROM Days"))
        a = QtCore.QDate.toString(self.selectedDate, "yyyy-MM-dd")
        log.debug(f"selected {a}")

        for i in [row[0] for row in data]:
            log.debug(i)
            if QtCore.QDate.toString(self.selectedDate, "yyyy-MM-dd") in i:
                log.warning("data Exists")
                loaded = list(self.d.cur.execute("SELECT * FROM Days WHERE date=?", [a])).pop()
                # b = [row for row in loaded]
                log.success(loaded)
                self.workDay.comboBox.setCurrentText(loaded[2])
                self.workDay.dayRate_SpinBox.setValue(float(loaded[3]))
                self.workDay.notes_textEdit.setText(loaded[4])
                if loaded[5]:
                    self.workDay.tabWidget.setTabEnabled(1, True)
                    self.workDay.extras_checkBox.setChecked(1)
                    self.workDay.extras_textEdit.setText(loaded[5])

    def clientList(self):
        clients = list(self.d.cur.execute("SELECT house_name FROM Contacts"))
        log.debug(clients)
        return [row[0] for row in clients]

    def extrasCheck(self):
        if self.workDay.extras_checkBox.checkState():
            self.workDay.tabWidget.setTabEnabled(1, True)
        else:
            self.workDay.tabWidget.setTabEnabled(1, False)

    def dropDownSize(self):
        fm = QFontMetrics(self.workDay.comboBox.font())
        maxWidth = max([fm.width(self.workDay.comboBox.itemText(i)) for i in range(self.workDay.comboBox.count())]) + 10
        styleSheet = "QComboBox QAbstractItemView { min-width: %s;}"
        self.workDay.comboBox.setStyleSheet(styleSheet % maxWidth)

    def save(self):
        data = [self.workDay.dateEdit.date().toPyDate(), self.workDay.comboBox.currentText(),
                self.workDay.dayRate_SpinBox.text(), self.workDay.notes_textEdit.toPlainText(),
                self.workDay.extras_textEdit.toPlainText()]
        # self.d.cur.execute('''IF NOT ALREADY EXISTS INSERT INTO Days (date,client,rate,notes,extras)
        # VALUES (?,?,?,?,?)''', data)
        self.d.cur.execute(
            '''INSERT OR IGNORE INTO Days (date,client,rate,notes,extras) VALUES (?,?,?,?,?)''', data)
        self.d.con.commit()

        self.close()


class GenerateInvoiceWindow(QDialog):
    def __init__(self, parent=None):
        super(GenerateInvoiceWindow, self).__init__(parent)
        self.gen = genInvoice()
        self.gen.setupUi(self)
        self.d = DataBase()
        self.gen.cancelButton.clicked.connect(self.closeWindow)  # clear_selection
        self.gen.from_comboBox.addItems(self.userList())
        self.gen.billTo_comboBox.addItems(self.contractorList())

        self.dropDownSize2()
        self.parent = parent
        qsql_db = self.parent.qsql_db
        self.invoiceModel_days = QSqlTableModel(None, qsql_db)  # pretty sure its here - qsql_db -
        # self.invoiceModel_days = QSqlTableModel(None, self.daysSelected) # thats what im trying to achieve
        self.invoiceModel_days.setTable("Days")
        self.invoiceModel_days.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.gen.genInvoice_tableView.resizeColumnsToContents()
        self.invoiceModel_days.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.invoiceModel_days.setHeaderData(1, QtCore.Qt.Horizontal, "Date")
        self.invoiceModel_days.setHeaderData(2, QtCore.Qt.Horizontal, "Client")
        self.invoiceModel_days.setHeaderData(3, QtCore.Qt.Horizontal, "Rate")
        self.invoiceModel_days.setHeaderData(4, QtCore.Qt.Horizontal, "Notes")
        self.invoiceModel_days.setHeaderData(5, QtCore.Qt.Horizontal, "Extras")

        self.days = self.parent.ui.calendarWidget.selected_dates
        self.dates = []
        for date in self.days:
            self.dates.append(date.toString("yyyy-MM-dd"))
        self.dates_string = str(tuple(self.dates)).replace(',)', ')')
        log.debug(self.dates)

        self.invoiceModel_days.setFilter(f"date IN {tuple(self.dates_string)}")
        self.gen.genInvoice_tableView.setModel(self.invoiceModel_days)
        self.updateInvoiceTable()
        self.gen.generateButton.clicked.connect(self.createInvoice)
        # self.daysSelected(days=self.parent.ui.calendarWidget.selected_dates)
        self.fillWorkSheet()

    def fillWorkSheet(self):
        userIdx = self.gen.from_comboBox.currentIndex()
        user = self.gen.from_comboBox.itemText(userIdx)
        userdata = list(self.d.cur.execute("SELECT * FROM Config WHERE name=?", [user]))
        log.debug(f"User Data: {userdata}")
        for i in [row for row in userdata]:
            log.info(i)
        # Bill Form
        userAddress = {
            'userName': i[1],
            'userHouse': i[3],
            'userRoad': i[4],
            'userArea': i[5],
            'userCounty': i[6],
            'userPostcode': i[7],
            'userEmail': i[2]
        }
        log.debug(f"User: {userAddress}")

        contractorIdx = self.gen.billTo_comboBox.currentIndex()
        contractor = self.gen.billTo_comboBox.itemText(contractorIdx)
        contractordata = list(self.d.cur.execute("SELECT * FROM Config WHERE name=?", [contractor]))
        log.debug(f"Contractor Data: {contractordata}")
        for j in [row for row in contractordata]:
            log.info(j)
        # Bill To
        contractorAddress = {
            'contractorName': j[1],
            'contractorHouse': j[3],
            'contractorRoad': j[4],
            'contractorArea': j[5],
            'contractorCounty': j[6],
            'contractorPostcode': j[7],
            'contractorEmail': j[2]
        }
        log.debug(f"Contractor: {contractorAddress}")
        workbook = Workbook(f'{"test1"}.xlsx')
        worksheet = workbook.add_worksheet()
        # Username Cell
        usernameCellFormat = workbook.add_format({'bold': True, 'font_size': 11, 'align': 'bottom-left',
                                                  'font_name': 'Arial'})
        worksheet.set_column_pixels(3, 3, 210)
        worksheet.set_row_pixels(0, 40)

        worksheet.write(0, 3, userAddress.get('userName'), usernameCellFormat)
        userAddressFormat = workbook.add_format({'align': 'bottom', 'font_name': 'Arial', 'font_size': 10})
        userEmailFormat = workbook.add_format({'align': 'bottom', 'font_name': 'Arial', 'bold': True, 'italic': True,
                                               'font_size': 11})
        worksheet.write(1, 3, f"{userAddress.get('userHouse')}, {userAddress.get('userRoad')}", userAddressFormat)
        worksheet.write(2, 3, f"{userAddress.get('userArea')}, {userAddress.get('userPostcode')}", userAddressFormat)
        worksheet.write(3, 3, userAddress.get('userEmail'), userEmailFormat)

        billToCellFormat = workbook.add_format({'bold': True, 'font_size': 11, 'align': 'bottom-left',
                                                'font_name': 'Arial'})
        contractorAddressFormat = workbook.add_format({'align': 'bottom', 'font_name': 'Arial', 'font_size': 10})
        worksheet.write(5, 3, "Bill To:", billToCellFormat)
        worksheet.write(6, 3, contractorAddress.get('contractorName'), contractorAddressFormat)
        worksheet.write(7, 3, contractorAddress.get('contractorHouse'), contractorAddressFormat)
        worksheet.write(8, 3, contractorAddress.get('contractorRoad'), contractorAddressFormat)
        worksheet.write(9, 3, contractorAddress.get('contractorArea'), contractorAddressFormat)
        worksheet.write(10, 3, contractorAddress.get('contractorPostcode'), contractorAddressFormat)
        worksheet.write(11, 3, contractorAddress.get('contractorEmail'), contractorAddressFormat)
        invoiceHeaderFormat = workbook.add_format({'bold': True, 'font_size': 18, 'align': 'bottom-left',
                                                   'font_name': 'Arial'})
        worksheet.write(0, 6, "Invoice", invoiceHeaderFormat)
        infoBoxFormat = workbook.add_format({'bold': True, 'font_size': 11, 'align': 'bottom',
                                             'font_name': 'Arial', 'border': 1})
        worksheet.set_column_pixels(6, 6, 100)
        worksheet.write(2, 6, "Date:", infoBoxFormat)
        worksheet.write(3, 6, "Week #", infoBoxFormat)
        worksheet.write(4, 6, "Invoice #", infoBoxFormat)
        worksheet.write(5, 6, "For:", infoBoxFormat)

        # Find the very next Friday after the last work day
        last_date = max(self.days)
        log.debug(f"Date Before: {last_date}")
        #log.debug(f"Date After: {QDate.}")
        try:
            while last_date.dayOfWeek() != 5:   # 5 - Friday
                last_date = last_date.addDays(1)
            log.debug(f'FRIDAY AFTER: {last_date}') # 239
        except Exception as e:
            log.exception(e)

        """mostRecentDate = max(self.dates)
        rd = QDate.fromString(mostRecentDate, Qt.ISODate).dayOfYear()
        date = QDate.
        log.debug(rd)
        log.debug(f"Recent Date: {mostRecentDate}")
        log.debug(f"Today: {today}")
        friday = rd - today + 5
        log.success(f"Next Friday: {friday}")
        day = QDate.daysTo()"""


        """for entry in userAddress:
            worksheet.write(row, col + 1, userAddress[entry])
            row += 1"""
        workbook.close()

    def createInvoice(self):
        workbook = Workbook(f'{"test1"}.xlsx')
        worksheet = workbook.add_worksheet()

        model = self.invoiceModel_days
        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                index = model.index(row, column)
                log.info(worksheet.write(row, column, model.data(index)))

        workbook.close()

    def invoiceNumber(self):
        self.d.cur.execute("SELECT max(id) FROM Days")  # TODO change to invoice table
        invoiceId = self.d.cur.fetchone()[0] + 1
        self.gen.invoiceNo_lineEdit.setText(str(invoiceId))
        log.success(invoiceId)

    def weekNumber(self, date):
        a = QDate.fromString(date, Qt.ISODate).weekNumber()
        return a[0]

    def updateInvoiceTable(self):
        self.invoiceNumber()
        if len(self.dates) < 2:
            for i in self.dates:
                log.debug(i)
                weekNumber = self.weekNumber(i)
                self.gen.weekNo_lineEdit.setText(str(weekNumber))
        self.invoiceModel_days.setFilter(f"date IN {self.dates_string}")
        self.invoiceModel_days.select()

    def daysSelected(self, days):  # daysToInvoice
        dates = []
        for date in days:
            dates.append(date.toString("yyyy-MM-dd"))
        dates = str(tuple(self.dates)).replace(',)', ')')
        log.debug(f"{dates}")
        self.chosenDays = self.d.cur.execute(f"SELECT * FROM Days WHERE date IN {dates}")
        log.debug(f"Days Selected: {list(self.chosenDays)}")
        self.updateInvoiceTable()
        return self.chosenDays

    def closeWindow(self):
        self.parent.ui.calendarWidget.clear_selection()  # need myCalendar.clear...
        self.close()

    def dropDownSize2(self):
        fm = QFontMetrics(self.gen.from_comboBox.font())
        maxWidth = max(
            [fm.width(self.gen.from_comboBox.itemText(i)) for i in range(self.gen.from_comboBox.count())]) + 10
        styleSheet = "QComboBox QAbstractItemView { min-width: %s;}"
        self.gen.from_comboBox.setStyleSheet(styleSheet % maxWidth)

        fm2 = QFontMetrics(self.gen.billTo_comboBox.font())
        maxWidth = max(
            [fm2.width(self.gen.billTo_comboBox.itemText(i)) for i in range(self.gen.billTo_comboBox.count())]) + 10
        styleSheet = "QComboBox QAbstractItemView { min-width: %s;}"
        self.gen.billTo_comboBox.setStyleSheet(styleSheet % maxWidth)

    def userList(self):
        users = list(self.d.cur.execute("SELECT name FROM Config WHERE type=?", ["user"]))
        log.debug(users)
        return [row[0] for row in users]

    def contractorList(self):
        contractor = list(self.d.cur.execute("SELECT name FROM Config WHERE type=?", ["sub contractor"]))
        log.debug(contractor)
        return [row[0] for row in contractor]


class DataBase:
    def __init__(self):
        self.ui = Ui_Form()
        self.con = sqlite3.connect(DB_FILE)
        self.con.set_trace_callback(print)
        self.cur = self.con.cursor()

        # Setup the DB
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Contacts
                    (id INTEGER PRIMARY KEY, house_name text, road_name text, area_name text, county_name text, 
                    postcode text)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Invoices
                    (id INTEGER PRIMARY KEY, invoice_number INTEGER, contact_id INTEGER, date text, rate real,
                    extras text, payment bool)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Config
                    (type text, name text, email text, houseName text, roadName text, areaName text, 
                    countyName text, postcode text,
                    UNIQUE (name, email)
                    )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Days
        (id INTEGER PRIMARY KEY, date text, client text, rate text, notes text, extras text)''')

        # Save (commit) the changes
        self.con.commit()

        atexit.register(self.teardown)

    def update(self):
        pass

    def teardown(self):
        self.con.close()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.d = DataBase()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.add_contact_Button1.clicked.connect(self.show_contact_dialog)
        self.ui.add_contact_Button.clicked.connect(self.show_contact_dialog)
        self.ui.settingAddUser_Button.clicked.connect(self.showAddUserWindow)
        self.ui.settingAddSubC_Button.clicked.connect(self.showAddSubWindow)
        self.ui.delete_contact_Button.clicked.connect(self.delete_contact_data)
        self.ui.settingDelete_Button.clicked.connect(self.delete_configContact)
        self.ui.calendarWidget.clicked.connect(self.ui.calendarWidget.date_is_clicked)
        # self.ui.calendarWidget.selectionChanged.connect(self.setDate) Todo Delete
        # self.ui.dateEdit.setDate(QDate.currentDate()) Todo Delete
        self.ui.calendarWidget.setSelectedDate(QDate.currentDate())
        self.ui.calendarWidget.activated.connect(self.showWorkDayWindow)
        #self.ui.calendarWidget.
        self.ui.genInvoice_Button.clicked.connect(self.generateInvoiceWindow)

        self.qsql_db = QSqlDatabase.addDatabase("QSQLITE")
        self.qsql_db.setDatabaseName("Invoices.sqlite")
        self.qsql_db.open()

        self.model = QSqlTableModel(None, self.qsql_db)
        self.model.setTable("Contacts")  # its the same db but different table
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.ui.tableView.resizeColumnsToContents()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "House Name/No.")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Road")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Area")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "County")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Post Code")
        self.ui.tableView.setModel(self.model)

        self.ui.contacts_listView.setModel(self.model)
        self.ui.contacts_listView.setModelColumn(1)
        self.ui.contacts_listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.update_model()

        self.configModel = QSqlTableModel(None, self.qsql_db)
        self.configModel.setTable("Config")
        self.configModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.ui.setting_tableView.resizeColumnsToContents()

        self.configModel.setHeaderData(0, QtCore.Qt.Horizontal, "Type")
        self.configModel.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.configModel.setHeaderData(2, QtCore.Qt.Horizontal, "Email")
        self.configModel.setHeaderData(3, QtCore.Qt.Horizontal, "House Name")
        self.configModel.setHeaderData(4, QtCore.Qt.Horizontal, "Road Name")
        self.configModel.setHeaderData(5, QtCore.Qt.Horizontal, "Area Name")
        self.configModel.setHeaderData(6, QtCore.Qt.Horizontal, "County")
        self.configModel.setHeaderData(7, QtCore.Qt.Horizontal, "Postcode")
        self.ui.setting_tableView.setModel(self.configModel)
        self.update_configModel()
        self.calendarRefresh()
        self.msg_homePage = QMessageBox()

    # def todayDate(self):
    #    return QDate.currentDate().toString(Qt.ISODate)

    def calendarRefresh(self):
        self.ui.calendarWidget.daysWorked = self.daysWorked()

    def daysWorked(self):
        self.d.cur.execute("SELECT date FROM Days")
        row = self.d.cur.fetchall()
        itr = [row[0] for row in row]
        # dates = [QtCore.QDate.fromString(row[0], "yy/mm/dd") for row in row]
        log.debug(f"Stored days: {len(itr)}")
        dates = []
        for date in itr:
            # log.debug(f"date: {date}")
            # log.debug(QtCore.QDate.fromString(date, Qt.ISODate))
            dates.append(QtCore.QDate.fromString(date, Qt.ISODate))
        # log.debug(f"dates: {dates}")
        return dates

    def selectedDate(self):  # function i want to call
        date = self.ui.calendarWidget.selectedDate()
        if date is not None:
            return date

    def update_model(self):
        self.model.select()

    def update_configModel(self):
        self.configModel.select()

    def delete_configContact(self):
        contactIndex = self.ui.setting_tableView.currentIndex()
        name = self.ui.setting_tableView.model().data(self.ui.setting_tableView.model().index(contactIndex.row(), 1))
        result = self.contactDelete_msg(name)
        if result:
            self.d.cur.execute("DELETE FROM Config WHERE name=?", [name])
            self.d.con.commit()
            self.update_configModel()
            log.success(f"{name} Deleted")

    def delete_contact_data(self):
        tableIndex = self.ui.tableView.currentIndex()
        name = self.ui.tableView.model().data(self.ui.tableView.model().index(tableIndex.row(), 1))
        result = self.contactDelete_msg(name)
        if result:
            self.d.cur.execute("DELETE FROM Contacts WHERE house_name=?", [name])
            self.d.con.commit()
            self.update_model()
            log.success(f"{name} Deleted")

    def contactDelete_msg(self, name):
        self.msg_homePage.setIcon(QMessageBox.Warning)
        self.msg_homePage.setText(f"Are you sure you want to delete {name}")
        self.msg_homePage.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg_homePage.setWindowTitle("Warning!")
        returnValue = self.msg_homePage.exec_()
        if returnValue == QMessageBox.Ok:
            log.critical(f"Contact {name} Deleted")
            return True

    def DataBaseWarning_msg(self, msg):
        self.msg_homePage.setIcon(QMessageBox.Warning)
        self.msg_homePage.setText(msg)
        self.msg_homePage.setStandardButtons(QMessageBox.Ok)
        self.msg_homePage.setWindowTitle("Warning!")
        returnValue = self.msg_homePage.exec_()
        if returnValue == QMessageBox.Ok:
            log.critical(msg)
            return True

    def show_contact_dialog(self):
        ContactWindow(self).exec_()

    def showAddUserWindow(self):
        AddUserWindow(self).exec_()

    def showAddSubWindow(self):
        AddSubWindow(self).exec_()

    def showWorkDayWindow(self):
        WorkDayWindow(self).exec_()
        self.calendarRefresh()

    def generateInvoiceWindow(self):
        try:
            user = list(self.d.cur.execute("SELECT * FROM Config WHERE type LIKE 'user'"))
            sub = list(self.d.cur.execute("SELECT * FROM Config WHERE type LIKE 'sub contractor'"))
            log.success(f"Users:{len(user)}")
            log.success(f"Contractors:{len(sub)}")
            log.success("1")
            if len(user) and len(sub):  # both
                log.success("2")
                GenerateInvoiceWindow(self).exec_()
            elif len(user) and not len(sub):  # user only
                log.success("3")
                msg = f"Database Missing Sub-Contractor Data"
                self.DataBaseWarning_msg(msg)
            elif not len(user) and len(sub):  # sub only
                log.success("4")
                msg = f"Database Missing User Data"
                self.DataBaseWarning_msg(msg)
            else:  # neither
                log.success("5")
                msg = f"Database Missing User & Sub-Contractor Data"
                self.DataBaseWarning_msg(msg)
        except Exception as e:
            log.error(e)

    def setDate(self): # Todo Delete
        date = self.ui.calendarWidget.selectedDate()
        if date is not None:
            self.ui.dateEdit.setDate(date)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.setWindowTitle("Invoicing")
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
