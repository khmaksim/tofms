from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel, QGroupBox, QGridLayout, QVBoxLayout, QHBoxLayout, QSizePolicy, QDateEdit
import PyQt5.QtCore
import sys
import sqlite3

class InputDialog(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setWindowTitle('Ввод данных')
		
		self.typePageLabel = QLabel("Тип листка:")
		self.typePageLineEdit = QLineEdit()
		self.surnameLabel = QLabel("Фамилия:")
		self.surnameLineEdit = QLineEdit()
		self.nameLabel = QLabel("Имя:")
		self.nameLineEdit = QLineEdit()
		self.patronymicLabel = QLabel("Отчество:")
		self.patronymicLineEdit = QLineEdit()
		
		self.personLayout = QGridLayout()
		self.personLayout.addWidget(self.typePageLabel, 0, 0)
		self.personLayout.addWidget(self.typePageLineEdit, 0, 1)
		self.personLayout.addWidget(self.surnameLabel, 0, 2)
		self.personLayout.addWidget(self.surnameLineEdit, 0, 3)
		self.personLayout.addWidget(self.nameLabel, 0, 4)
		self.personLayout.addWidget(self.nameLineEdit, 0, 5)
		self.personLayout.addWidget(self.patronymicLabel, 0, 6)
		self.personLayout.addWidget(self.patronymicLineEdit, 0, 7)
		self.personGroupBox = QGroupBox("ФИО")
		self.personGroupBox.setLayout(self.personLayout)
						
		self.birthdayLabel = QLabel("Дата:")
		self.birthdayLineEdit = QLineEdit()
		self.countryLabel = QLabel("Государство:")
		self.countryLineEdit = QLineEdit()
		self.regionLabel = QLabel("Область:")
		self.regionLineEdit = QLineEdit()
		self.cityLabel = QLabel("Город:")
		self.cityLineEdit = QLineEdit()
		self.districtLabel = QLabel("Район:")
		self.districtLineEdit = QLineEdit()
		self.localityLabel = QLabel("Населенный пункт:")
		self.localityLineEdit = QLineEdit()
		
		self.birthLayout = QGridLayout()
		self.birthLayout.addWidget(self.birthdayLabel, 0, 0)
		self.birthLayout.addWidget(self.birthdayLineEdit, 0, 1)
		self.birthLayout.addWidget(self.countryLabel, 1, 0)
		self.birthLayout.addWidget(self.countryLineEdit, 1, 1)
		self.birthLayout.addWidget(self.regionLabel, 1, 2)
		self.birthLayout.addWidget(self.regionLineEdit, 1, 3)
		self.birthLayout.addWidget(self.cityLabel, 1, 4)
		self.birthLayout.addWidget(self.cityLineEdit, 1, 5)
		self.birthLayout.addWidget(self.districtLabel, 4, 0)
		self.birthLayout.addWidget(self.districtLineEdit, 4, 1)
		self.birthLayout.addWidget(self.localityLabel, 4, 2)
		self.birthLayout.addWidget(self.localityLineEdit, 4, 3)
		self.birthGroupBox = QGroupBox("Рождение")
		self.birthGroupBox.setLayout(self.birthLayout)
	
		self.countryResidenceLabel = QLabel("Государство:")
		self.countryResidenceLineEdit = QLineEdit()
		self.regionResidenceLabel = QLabel("Область:")
		self.regionResidenceLineEdit = QLineEdit()
		self.cityResidenceLabel = QLabel("Город:")
		self.cityResidenceLineEdit = QLineEdit()
		self.districtResidenceLabel = QLabel("Район:")
		self.districtResidenceLineEdit = QLineEdit()
		self.localityResidenceLabel = QLabel("Населенный пункт:")
		self.localityResidenceLineEdit = QLineEdit()
		self.streetResidenceLabel = QLabel("Улица:")
		self.streetResidenceLineEdit = QLineEdit()
		self.houseResidenceLabel = QLabel("Дом:")
		self.houseResidenceLineEdit = QLineEdit()
		self.caseResidenceLabel = QLabel("Корпус:")
		self.caseResidenceLineEdit = QLineEdit()
		self.apartmentResidenceLabel = QLabel("Квартира:")
		self.apartmentResidenceLineEdit = QLineEdit()
		
		self.residenceLayout = QGridLayout()
		self.residenceLayout.addWidget(self.countryResidenceLabel, 0, 0)
		self.residenceLayout.addWidget(self.countryResidenceLineEdit, 0, 1)
		self.residenceLayout.addWidget(self.regionResidenceLabel, 0, 2)
		self.residenceLayout.addWidget(self.regionResidenceLineEdit, 0, 3)
		self.residenceLayout.addWidget(self.cityResidenceLabel, 0, 4)
		self.residenceLayout.addWidget(self.cityResidenceLineEdit, 0, 5)
		self.residenceLayout.addWidget(self.districtResidenceLabel, 1, 0)
		self.residenceLayout.addWidget(self.districtResidenceLineEdit, 1, 1)
		self.residenceLayout.addWidget(self.localityResidenceLabel, 1, 2)
		self.residenceLayout.addWidget(self.localityResidenceLineEdit, 1, 3)
		self.residenceLayout.addWidget(self.streetResidenceLabel, 2, 0)
		self.residenceLayout.addWidget(self.streetResidenceLineEdit, 2, 1)
		self.residenceLayout.addWidget(self.houseResidenceLabel, 2, 2)
		self.residenceLayout.addWidget(self.houseResidenceLineEdit, 2, 3)
		self.residenceLayout.addWidget(self.caseResidenceLabel, 2, 4)
		self.residenceLayout.addWidget(self.caseResidenceLineEdit, 2, 5)
		self.residenceLayout.addWidget(self.apartmentResidenceLabel, 2, 6)
		self.residenceLayout.addWidget(self.apartmentResidenceLineEdit, 2, 7)
		self.residenceGroupBox = QGroupBox("Адрес места жительства")
		self.residenceGroupBox.setLayout(self.residenceLayout)
		
		self.documentLabel = QLabel("Вид документа:")
		self.documentLineEdit = QLineEdit()
		self.seriesLabel = QLabel("Серия:")
		self.seriesLineEdit = QLineEdit()
		self.numberLabel = QLabel("Номер:")
		self.numberLineEdit = QLineEdit()
		self.dateIssueLabel = QLabel("Дата выдачи:")
		self.dateIssueLineEdit = QLineEdit()
		self.issuedLabel = QLabel("Кем выдан:")
		self.issuedLineEdit = QLineEdit()
		
		self.documentLayout = QGridLayout()
		self.documentLayout.addWidget(self.documentLabel, 0, 0)
		self.documentLayout.addWidget(self.documentLineEdit, 0, 1)
		self.documentLayout.addWidget(self.seriesLabel, 1, 0)
		self.documentLayout.addWidget(self.seriesLineEdit, 1, 1)
		self.documentLayout.addWidget(self.numberLabel, 1, 2)
		self.documentLayout.addWidget(self.numberLineEdit, 1, 3)
		self.documentLayout.addWidget(self.dateIssueLabel, 1, 4)
		self.documentLayout.addWidget(self.dateIssueLineEdit, 1, 5)
		self.documentLayout.addWidget(self.issuedLabel, 2, 0)
		self.documentLayout.addWidget(self.issuedLineEdit, 2, 1, 1, 5)
		self.documentGroupBox = QGroupBox("Документ")
		self.documentGroupBox.setLayout(self.documentLayout)
		
		self.dateArrivalLabel = QLabel("Дата прибытия:")
		self.dateArrivalDateEdit = QDateEdit()
		self.dateRetirementLabel = QLabel("Дата выбытия:")
		self.dateRetirementDateEdit = QDateEdit()
		self.nameHotelLabel = QLabel("Название гостиницы:")
		self.nameHotelLineEdit = QLineEdit()
		self.structureLabel = QLabel("Строение/Корпус/Сектор:")
		self.structureLineEdit = QLineEdit()
		self.roomLabel = QLabel("Комната:")
		self.roomLineEdit = QLineEdit()
		
		self.checkLayout = QGridLayout()
		self.checkLayout.addWidget(self.dateArrivalLabel, 0, 0)
		self.checkLayout.addWidget(self.dateArrivalDateEdit, 0, 1)
		self.checkLayout.addWidget(self.dateRetirementLabel, 0, 2)
		self.checkLayout.addWidget(self.dateRetirementDateEdit, 0, 3)
		self.checkLayout.addWidget(self.nameHotelLabel, 2, 0)
		self.checkLayout.addWidget(self.nameHotelLineEdit, 2, 1)
		self.checkLayout.addWidget(self.structureLabel, 2, 2)
		self.checkLayout.addWidget(self.structureLineEdit, 2, 3)
		self.checkLayout.addWidget(self.roomLabel, 2, 4)
		self.checkLayout.addWidget(self.roomLineEdit, 2, 5)
		self.checkGroupBox = QGroupBox("Регистрация")
		self.checkGroupBox.setLayout(self.checkLayout)
		
		self.saveButton = QPushButton("Сохранить")
		self.cancelButton = QPushButton("Отмена")
		
		self.bottomLayout = QHBoxLayout()
		self.bottomLayout.addStretch()
		self.bottomLayout.addWidget(self.saveButton)
		self.bottomLayout.addWidget(self.cancelButton)
		
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.personGroupBox)
		self.layout.addWidget(self.birthGroupBox)
		self.layout.addWidget(self.residenceGroupBox)
		self.layout.addWidget(self.documentGroupBox)
		self.layout.addWidget(self.checkGroupBox)
		self.layout.addLayout(self.bottomLayout)
		
		self.setLayout(self.layout)
		
		self.saveButton.clicked.connect(self.save_data)
		self.cancelButton.clicked.connect(self.cancel)
		
		self.connect = self.connect_database()
		
	def connect_database(self):
		return sqlite3.connect('fms.db')
			
	def save_data(self):
		cursor = self.connect.cursor()
		cursor.execute("INSERT INTO profile(type_page, surname, name, patronymic, birthday, country, region, city, district, "
						"locality, country_residence, region_residence, city_residence, district_residence, locality_residence, "
						"street_residence, house_residence, case_residence, apartment_residence, document, series, number, date_issue, "
						"issued, date_arrival_str, date_retirement_str, name_hotel, structure, room, date_arrival, date_retirement) "
						"VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
						(self.typePageLineEdit.text(), self.surnameLineEdit.text(),	self.nameLineEdit.text(), 
						self.patronymicLineEdit.text(), self.birthdayLineEdit.text(), self.countryLineEdit.text(), 
						self.regionLineEdit.text(), self.cityLineEdit.text(), self.districtLineEdit.text(), 
						self.localityLineEdit.text(), self.countryResidenceLineEdit.text(), self.regionResidenceLineEdit.text(), 
						self.cityResidenceLineEdit.text(), self.districtResidenceLineEdit.text(), self.localityResidenceLineEdit.text(), 
						self.streetResidenceLineEdit.text(), self.houseResidenceLineEdit.text(), self.caseResidenceLineEdit.text(), 
						self.apartmentResidenceLineEdit.text(), self.documentLineEdit.text(), self.seriesLineEdit.text(), 
						self.numberLineEdit.text(), self.dateIssueLineEdit.text(), self.issuedLineEdit.text(), self.dateArrivalDateEdit.date().toString("dd.MM.yyyy"), 
						self.dateRetirementDateEdit.date().toString("dd.MM.yyyy"), self.nameHotelLineEdit.text(), self.structureLineEdit.text(), self.roomLineEdit.text(), 
						self.dateArrivalDateEdit.date().toString("yyyy-MM-dd"), self.dateRetirementDateEdit.date().toString("yyyy-MM-dd")))
		self.connect.commit()
		cursor.close()
		self.connect.close()
		self.accept()
		
	def cancel(self):
		self.connect.close()
		self.reject()
