from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pymongo
from bson.objectid import ObjectId

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.record_btn = QtWidgets.QPushButton(self.centralwidget)
        self.record_btn.setGeometry(QtCore.QRect(230, 330, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.record_btn.setFont(font)
        self.record_btn.setObjectName("record_btn")
        self.save_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_all_btn.setGeometry(QtCore.QRect(580, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_all_btn.setFont(font)
        self.save_all_btn.setObjectName("save_all_btn")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(580, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(580, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(580, 260, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(670, 510, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 90, 381, 221))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.id_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.id_lbl.setFont(font)
        self.id_lbl.setObjectName("id_lbl")
        self.verticalLayout.addWidget(self.id_lbl)
        self.last_name_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_name_lbl.setFont(font)
        self.last_name_lbl.setObjectName("last_name_lbl")
        self.verticalLayout.addWidget(self.last_name_lbl)
        self.first_name_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.first_name_lbl.setFont(font)
        self.first_name_lbl.setObjectName("first_name_lbl")
        self.verticalLayout.addWidget(self.first_name_lbl)
        self.subject_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_lbl.setFont(font)
        self.subject_lbl.setObjectName("subject_lbl")
        self.verticalLayout.addWidget(self.subject_lbl)
        self.points_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.points_lbl.setFont(font)
        self.points_lbl.setObjectName("points_lbl")
        self.verticalLayout.addWidget(self.points_lbl)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.id_txt = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_txt.setFont(font)
        self.id_txt.setObjectName("id_txt")
        self.verticalLayout_2.addWidget(self.id_txt)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.last_name_txt = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_name_txt.setFont(font)
        self.last_name_txt.setObjectName("last_name_txt")
        self.verticalLayout_2.addWidget(self.last_name_txt)
        self.first_name_txt = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.first_name_txt.setFont(font)
        self.first_name_txt.setObjectName("first_name_txt")
        self.verticalLayout_2.addWidget(self.first_name_txt)
        self.subject_txt = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_txt.setFont(font)
        self.subject_txt.setObjectName("subject_txt")
        self.verticalLayout_2.addWidget(self.subject_txt)
        self.points_txt = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.points_txt.setFont(font)
        self.points_txt.setObjectName("points_txt")
        self.verticalLayout_2.addWidget(self.points_txt)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #### My Code starts here #####
        self.close_btn.clicked.connect(self.close_program)
        self.search_btn.clicked.connect(self.search)
        self.update_btn.clicked.connect(self.update)
        self.delete_btn.clicked.connect(self.delete)


    def delete(self):
        myquery = {}
        if(len(self.first_name_txt.toPlainText()) > 0) :
            myquery['first name'] = str(self.first_name_txt.toPlainText())

        if(len(self.last_name_txt.toPlainText()) > 0) :
            myquery['last name'] = str(self.last_name_txt.toPlainText())

        if(len(self.subject_txt.toPlainText()) > 0) :
            myquery['subject'] = str(self.subject_txt.toPlainText())

        if(len(self.points_txt.toPlainText()) > 0) :
            myquery['points'] = str(self.points_txt.toPlainText())

        mycol.delete_many(myquery)
    def update(self):
        try:
            object_id = ObjectId(self.id_txt.toPlainText())
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Invalid ObjectId: {e}")
            return

        myquery = {'_id': object_id}
        new_val = {
            "$set": {
                'first name': self.first_name_txt.toPlainText(),
                'last name': self.last_name_txt.toPlainText(),
                'subject': self.subject_txt.toPlainText(),
                'points': int(self.points_txt.toPlainText())  # Assuming points should be an integer
            }
        }
        
        mycol.update_one(myquery, new_val)
        

    def search(self):
        myquery = {}
        # x = self.first_name_txt.toPlainText()
        # if len(self.id_txt.toPlainText()) > 0:
        #     myquery['id'] = int(self.id_txt.toPlainText())

        if(len(self.first_name_txt.toPlainText()) > 0) :
            myquery['first name'] = str(self.first_name_txt.toPlainText())

        if(len(self.last_name_txt.toPlainText()) > 0) :
            myquery['last name'] = str(self.last_name_txt.toPlainText())

        if(len(self.subject_txt.toPlainText()) > 0) :
            myquery['subject'] = str(self.subject_txt.toPlainText())

        if(len(self.points_txt.toPlainText()) > 0) :
            myquery['points'] = str(self.points_txt.toPlainText())

        print(myquery)

        x = mycol.find(myquery)

        for i in x:
            print(i)


    def save_all(self, data):
        for i in data:
            x = i.split()
            my_dict = {"last name" : x[0], 'first name' : x[1], 'subject' : x[2], 'points' : x[3]}
            mycol.insert_one(my_dict)
        
    def close_program(self):
        sys.exit(app.exec_())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.record_btn.setText(_translate("MainWindow", "ჩაწერა"))
        self.save_all_btn.setText(_translate("MainWindow", "ყველა ჩანაწერის გაკეთება"))
        self.search_btn.setText(_translate("MainWindow", "ძებნა"))
        self.update_btn.setText(_translate("MainWindow", "განახლება"))
        self.delete_btn.setText(_translate("MainWindow", "წაშლა"))
        self.close_btn.setText(_translate("MainWindow", "Close"))
        self.id_lbl.setText(_translate("MainWindow", "ID"))
        self.last_name_lbl.setText(_translate("MainWindow", "Last Name"))
        self.first_name_lbl.setText(_translate("MainWindow", "First Name"))
        self.subject_lbl.setText(_translate("MainWindow", "Subject"))
        self.points_lbl.setText(_translate("MainWindow", "Points"))


LNames = ['აბაშიძე', 'გიგაური', 'არჩვაძე', 'ახალაია', 'ბაძაღუა', 'ბერიანიძე', 'ბერიშვილი', 'გვენცაძე', 'დალაქიშვილი',
'ანთიძე', 'გიორგაძე', 'გოგალაძე', 'გოცირიძე', 'ვარდიძე', 'ზარანდია', 'თადუმაძე', 'ლაბაძე', 'კვარაცხელია',
'კუსრაძე', 'კვესელავა', 'კაპანაძე', 'კასრაძე', 'კვინიკაძე', 'კოპაძე', 'კანკია', 'კორძაია', 'მიქავა', 'მელია',
'მონიავა', 'ნიაური', 'ლაცაბიძე', 'მიქაძე', 'ნემსიწვერიძე', 'მაისურაძე', 'მაცაბერიძე', 'მჟავია', 'მაჩალაძე',
'ოდიშარია', 'მეტრეველი', 'ნეფარიძე', 'მოდებაძე', 'მარჯანიძე', 'მუმლაძე', 'ნასრაშვილი', 'ჯანჯღავა', 'მოსია',
'ნოზაძე', 'ნუცუბიძე', 'ონიანი', 'ოქრუაშვილი', 'პერტია', 'რაზმაძე', 'რევაზაშვილი', 'საგანელიძე', 'ჯახაია',
'სალუქვაძე', 'სამსონაშვილი', 'სამხარაძე', 'სარალიძე', 'სართანია', 'სარიშვილი', 'სიმონიშვილი', 'სხილაძე',
'ხურციძე', 'სიხარულიძე', 'ტაბატაძე', 'ფაცაცია', 'ფილაური', 'ფუხაშვილი', 'ქობალია', 'ყიფშიძე', 'შაინიძე',
'ფიფია', 'შენგელია', 'შეროზია', 'შველიძე', 'ჩხეიძე', 'ჩადუნელი', 'ჩიკვაშვილი', 'ცქიტიშვილი', 'ჩოკორაია',
'ცაგურია', 'ცერცვაძე', 'ცუხიშვილი', 'ძინძიბაძე', 'წერეთელი', 'წიკლაური', 'ჭავჭანიძე', 'ჩირაძე', 'ჭელიძე',
'ჭანტურია', 'სირაძე', 'შონია', 'ხანჯალაძე', 'ხარაზიშვილი', 'ხელაძე', 'ხვინგია', 'ხუციშვილი', 'ჯანელიძე',
'ჯოხაძე']

FNames = ['ანა', 'ანუკი', 'ბარბარე', 'გვანცა', 'დიანა', 'ეკა', 'ელენე', 'ვერონიკა', 'ვიქტორია', 'თათია', 'ლამზირა',
'თეა', 'თეკლე', 'თინიკო', 'თამარი', 'იზაბელა', 'ია', 'იამზე', 'ლია', 'ლიკა', 'ლანა', 'მარიკა', 'მანანა',
'მაია', 'მაკა', 'მარიამი', 'ნანა', 'ნანი', 'ნატა', 'ნატო', 'ნინო', 'ნონა', 'ოლიკო', 'ქეთევანი', 'სალომე',
'სოფიკო', 'ნია', 'ქრისტინე', 'შორენა', 'ხატია', 'ალეკო', 'ალიკა', 'ამირან', 'ანდრია', 'არჩილი', 'ასლანი',
'ბაჩუკი', 'ბექა', 'გიგა', 'გიორგი', 'დავითი',
'გიგი', 'გოგა', 'დათა', 'ერეკლე', 'თემური', 'იაკობ', 'ილია', 'ირაკლი', 'ლადო', 'ლაშა', 'მიხეილ',
'ნიკა', 'ოთარი', 'პაატა', 'რამაზ', 'რამინი', 'რატი', 'რაული', 'რევაზი', 'რომა', 'რომანი', 'სანდრო',
'საბა', 'სერგი', 'სიმონ', 'შალვა', 'შოთა', 'ცოტნე', 'ჯაბა']

Subject = ['პროგრამირების_საფუძვლები', 'კალკულუსი II', 'შესავალი_ფიზიკაში', 'კომპიუტერული_უნარჩვევები',
'ქიმიის_შესავალი', 'ბიოლოგიის_შესავალი', 'ალგორითმები_I', 'შესავალი_ელექტრონიკაში',
'მონაცემთა_სტრუქტურები', 'ალგორითმები_II']


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    point = [str(i) for i in range(101)]
    ch = random.choice
    stud_recs = [' '.join([ch(LNames), ch(FNames), ch(Subject), ch(point)]) for _ in range(5)]
    #print(Stud_recs)

    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = my_client["StudentsDB"]
    mycol = mydb["Students"]
    
    ui.save_all_btn.clicked.connect(lambda: ui.save_all(stud_recs))    

    sys.exit(app.exec_())