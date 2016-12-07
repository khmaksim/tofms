from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel, QGroupBox, QGridLayout, QVBoxLayout, QHBoxLayout, QSizePolicy, QDateEdit
from input_dialog import UpperSimplifiedLineEdit
import PyQt5.QtCore
import sys
import sqlite3
import os
import datetime

class ReportDialog(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setWindowTitle('Отчет')
		
		self.dateFromLabel = QLabel("Дата с:")
		self.dateFromDateEdit = QDateEdit()
		self.dateToLabel = QLabel("Дата по:")
		self.dateToDateEdit = QDateEdit()
		self.numberHotelLabel = QLabel("Код гостиницы:")
		self.numberHotelLineEdit = UpperSimplifiedLineEdit()
		self.numberHotelLineEdit.setInputMask("999;_")
		self.numberStructureLabel = QLabel("Код строения:")
		self.numberStructureLineEdit = UpperSimplifiedLineEdit()
		self.numberStructureLineEdit.setInputMask("99;_")
		self.postLabel = QLabel("Должность приславшего:")
		self.postLineEdit = UpperSimplifiedLineEdit()
		self.nameLabel = QLabel("ФИО:")
		self.nameLineEdit = UpperSimplifiedLineEdit()
				
		self.layout = QGridLayout()
		self.layout.addWidget(self.dateFromLabel, 0, 0)
		self.layout.addWidget(self.dateFromDateEdit, 0, 1)
		self.layout.addWidget(self.dateToLabel, 1, 0)
		self.layout.addWidget(self.dateToDateEdit, 1, 1)
		self.layout.addWidget(self.numberHotelLabel, 2, 0)
		self.layout.addWidget(self.numberHotelLineEdit, 2, 1)
		self.layout.addWidget(self.numberStructureLabel, 3, 0)
		self.layout.addWidget(self.numberStructureLineEdit, 3, 1)
		self.layout.addWidget(self.postLabel, 4, 0)
		self.layout.addWidget(self.postLineEdit, 4, 1)
		self.layout.addWidget(self.nameLabel, 5, 0)
		self.layout.addWidget(self.nameLineEdit, 5, 1)
								
		self.saveButton = QPushButton("Сохранить")
		self.cancelButton = QPushButton("Отмена")
		
		self.bottomLayout = QHBoxLayout()
		self.bottomLayout.addStretch()
		self.bottomLayout.addWidget(self.saveButton)
		self.bottomLayout.addWidget(self.cancelButton)
		
		self.layout.addLayout(self.bottomLayout, 6, 0, 1, 2)
		
		self.setLayout(self.layout)
		
		self.saveButton.clicked.connect(self.save_data)
		self.cancelButton.clicked.connect(self.cancel)
		
		self.connect = self.connect_database()
		
	def get_serial_number(self):
		cursor = self.connect.cursor()
		cursor.execute("SELECT serial_number FROM journal ORDER BY id DESC LIMIT 1")
		row = cursor.fetchone()
		if row is not None:
			if row[0] == '999':
				return '001'
			return str(int(row[0]) + 1).zfill(3)
		return '001'
		
	def connect_database(self):
		return sqlite3.connect('fms.db')
			
	def save_data(self):
		# create directory for current report
		save_dir = datetime.datetime.now().strftime("%d%m%Y_%I%M%S")
		if not os.path.exists(save_dir):
			os.mkdir(save_dir)
					
		serial_number = self.get_serial_number()		# get serial number report
				
		name_txt_file = "%s%s%s.txt" % (self.numberHotelLineEdit.text(), self.numberStructureLineEdit.text(), serial_number)
		report_file = open((save_dir + "/" + name_txt_file), "wb")
				
		cursor = self.connect.cursor()
		cursor.execute("SELECT type_page, surname, name, patronymic, birthday, country, region, city, district, "
						"locality, country_residence, region_residence, city_residence, district_residence, locality_residence, "
						"street_residence, house_residence, case_residence, apartment_residence, document, series, number, date_issue, "
						"issued, date_arrival_str, date_retirement_str, name_hotel, structure, room "
						"FROM profile WHERE date_arrival >= ? AND date_retirement <= ?",
			(self.dateFromDateEdit.date().toString("yyyy-MM-dd"), self.dateToDateEdit.date().toString("yyyy-MM-dd")))
		count = 0
		for row in cursor:
			row_str = ''
			for cell in row:
				row_str += ("\"%s\"" % cell)
				row_str += ","
			report_file.write(row_str.rstrip(",").encode('utf-8'))
			report_file.write("\r\n".encode('utf-8'))
			count += 1
		report_file.close()
		
		self.add_journal(count, serial_number)		# add record journal database
		
		name_psm_file = "%s%s%s.psm" % (self.numberHotelLineEdit.text(), self.numberStructureLineEdit.text(), serial_number)
		cover_file = open((save_dir + "/" + name_psm_file), "wb")
		row_str = ("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"" % 
			(name_txt_file, self.dateFromDateEdit.date().toString("ddMMyy"), self.dateToDateEdit.date().toString("ddMMyy"), str(count), "0", 
			self.postLineEdit.text(), self.nameLineEdit.text()))
		cover_file.write(row_str.encode('utf-8'))
		cover_file.close()
		
		cursor.close()
		self.connect.close()
		self.accept()
		
	def add_journal(self, number_records, serial_number):
		cursor = self.connect.cursor()
		cursor.execute("INSERT INTO journal(date_from, date_to, number_records, post, name, serial_number) VALUES(?, ?, ?, ?, ?, ?)", 
			(self.dateFromDateEdit.date().toString("yyyy-MM-dd"), self.dateToDateEdit.date().toString("yyyy-MM-dd"), 
			number_records, self.postLineEdit.text(), self.nameLineEdit.text(), serial_number))
		self.connect.commit()
		cursor.close()
		
	def cancel(self):
		self.connect.close()
		self.reject()
