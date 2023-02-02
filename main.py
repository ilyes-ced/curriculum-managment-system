from re import I
import sys
from tokenize import Name
from BlurWindow.blurWindow import blur
from ui_main import Ui_MainWindow
from dia2 import Ui_Dialog
import ctypes
import math
from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QIcon , QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QSizeGrip, QPushButton, QVBoxLayout, QDialogButtonBox, QDialog, QTableWidgetItem
import sqlite3,json
import csv  
import os
from sys import platform

#print(os.path.join(os.path.curdir))
#if platform == "linux" or platform == "linux2":
#    print('linuix')
#elif platform == "darwin":
#    print('mac')
#elif platform == "win32":
#    print('winwi')

#dialogue window
class Popup_window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ff = Ui_Dialog()
        self.ff.setupUi(self)



class MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        #styling  C:\my_projects\python\project1\main
        self.ui.the_main_bloc.setStyleSheet(open(os.path.join(os.path.curdir, 'styles/style.css')).read())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(os.path.join(os.path.curdir,'images/python.svg')))
        #blur effect
        
        #blur(self.winId())
        


        #works for windowss probably but not linux
        #hWnd = self.winId()
        #print(hWnd)
        #blur(hWnd)
        #myappid = 'ilyes.class_managment_system.subproduct.1.0.0' # arbitrary string
        #ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        
        #functions
        #self.ui.btn_extend.clicked.connect(self.side_bar_extend)
        self.ui.season_selection.currentTextChanged.connect(self.changed_selections)
        self.ui.grade_selection.currentTextChanged.connect(self.changed_selections)
        self.ui.tab2_season_selection.currentTextChanged.connect(self.reset_teacher_table)
        self.ui.tab2_teacher_selection.currentTextChanged.connect(self.reset_teacher_table)
        self.ui.tab3_season_selection.currentTextChanged.connect(self.reset_class_table)
        self.ui.tab3_yearclass_selection.currentTextChanged.connect(self.reset_class_table)

        self.sizegrip = QSizeGrip(self.ui.size_grip_widget)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: -1px;")


        for i in range (45):
            exec("self.ui.add_cell_"+str(i+1)+".clicked.connect(self.show_popup)")
       


   


        #for i in range(20):
         #   print("insert into teachers(name,subject,color) values(?,?,?);",(name,subject,color))







        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  
        #self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)

        

        self.ui.btn_all.clicked.connect(self.change_stack)
        self.ui.btn_teachers.clicked.connect(self.change_stack)
        self.ui.btn_classes.clicked.connect(self.change_stack)
        self.ui.btn_edit_teachers.clicked.connect(self.change_stack)

        self.ui.btn_save.clicked.connect(self.create_file)

        self.ui.r_slider.valueChanged.connect(self.rgb_change)
        self.ui.g_slider.valueChanged.connect(self.rgb_change)
        self.ui.b_slider.valueChanged.connect(self.rgb_change)
        self.ui.save_teacher_data.clicked.connect(self.saved_teacher_data)
        self.ui.cancel_teacher_data.clicked.connect(self.canceled_teacher_data)

        #create databse tables in case of new programe
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        tables = con.cursor()
        tables.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='reservations' ''')
        if tables.fetchone()[0]!=1: 
            tables.execute(""" CREATE TABLE "reservations" (
	                        "season"	TEXT,
	                        "grade"	TEXT,
	                        "cell_1"	TEXT,
	                        "cell_2"	TEXT,
	                        "cell_3"	TEXT,
	                        "cell_4"	TEXT,
	                        "cell_5"	TEXT,
	                        "cell_6"	TEXT,
	                        "cell_7"	TEXT,
	                        "cell_8"	TEXT,
	                        "cell_9"	TEXT,
	                        "cell_10"	TEXT,
	                        "cell_11"	TEXT,
	                        "cell_12"	TEXT,
	                        "cell_13"	TEXT,
	                        "cell_14"	TEXT,
	                        "cell_15"	TEXT,
	                        "cell_16"	TEXT,
	                        "cell_17"	TEXT,
	                        "cell_18"	TEXT,
	                        "cell_19"	TEXT,
	                        "cell_20"	TEXT,
	                        "cell_21"	TEXT,
	                        "cell_22"	TEXT,
	                        "cell_23"	TEXT,
	                        "cell_24"	TEXT,
	                        "cell_25"	TEXT,
	                        "cell_26"	TEXT,
	                        "cell_27"	TEXT,
	                        "cell_28"	TEXT,
	                        "cell_29"	TEXT,
	                        "cell_30"	TEXT,
	                        "cell_31"	TEXT,
	                        "cell_32"	TEXT,
	                        "cell_33"	TEXT,
	                        "cell_34"	TEXT,
	                        "cell_35"	TEXT,
	                        "cell_36"	TEXT,
	                        "cell_37"	TEXT,
	                        "cell_38"	TEXT,
	                        "cell_39"	TEXT,
	                        "cell_40"	TEXT,
	                        "cell_41"	TEXT,
	                        "cell_42"	TEXT,
	                        "cell_43"	TEXT,
	                        "cell_44"	TEXT,
	                        "cell_45"	TEXT   ); """)
                            
        tables.execute(""" CREATE TABLE if not exists teachers (
	        id	integer AUTO_INCREMENT,
	        name	TEXT,
	        subject	TEXT,
	        color	TEXT,
	        PRIMARY KEY("id") ); """)
        con.commit()


        #declare comboboxes
        self.season_selection = self.ui.season_selection
        self.grade_selection = self.ui.grade_selection
        self.tab2_teacher_selection = self.ui.tab2_teacher_selection
        self.tab2_season_selection = self.ui.tab2_season_selection
        self.tab3_yearclass_selection = self.ui.tab3_yearclass_selection
        self.tab3_season_selection = self.ui.tab3_season_selection
        
        #fills the tab2 teachers list
        tables.execute("select * from teachers")
        teachers = tables.fetchall()
        for i in (teachers):
            self.tab2_teacher_selection.addItem(i[1])
        self.fill_teacher_table()
        self.fill_class_table()
        
        #declares comboboxes events
        #self.season_selection.currentTextChanged.connect(self.changed_selections)
        #self.grade_selection.currentTextChanged.connect(self.changed_selections)
        #self.tab2_season_selection.currentTextChanged.connect(self.reset_teacher_table)
        #self.tab2_teacher_selection.currentTextChanged.connect(self.reset_teacher_table)
        #self.tab3_season_selection.currentTextChanged.connect(self.reset_class_table)
        #self.tab3_yearclass_selection.currentTextChanged.connect(self.reset_class_table)


        self.max_=False
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_max.clicked.connect(lambda: show_max_normal(self))

        


        self.ui.btn_min.clicked.connect(lambda: self.showMinimized())



        #short for the self.add_cell_1 = self.findChild(QPushButton,"add_cell_1") 1to45
        #short for the self.add_cell_1.clicked.connect(self.add_cell) 1to45
        for i in range(45):
            exec("self.ui.add_cell_"+str(i+1)+".clicked.connect(self.add_cell)")

       
       
        # fills the table for the first time
        self.data_on_start()
        self.fill_teachers_data()







        self.ui.btn_all.setStyleSheet('border-left: 3px solid #04eeff;color: #04eeff;')











        def show_max_normal(self):
            if self.max_==False:
                self.max_=True
                self.showMaximized()
                self.setAttribute(Qt.WA_TranslucentBackground,False)

            else:
                self.max_=False
                self.showNormal()
                self.setAttribute(Qt.WA_TranslucentBackground,True)










    def fill_teachers_data(self):
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        cur.execute('SELECT * from teachers')
        teachers = cur.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for i, teacher in enumerate(teachers):
            rgb = teacher[3].split(',')
            self.ui.tableWidget.insertRow(i)
            
            item1 = QTableWidgetItem(str(teacher[0]))
            item2 = QTableWidgetItem(str(teacher[1]))
            item3 = QTableWidgetItem(str(teacher[2]))
            item4 = QTableWidgetItem(str(teacher[3]))
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            item3.setTextAlignment(Qt.AlignCenter)
            item4.setTextAlignment(Qt.AlignCenter)
            item1.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
            item2.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
            item3.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
            item4.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
            self.ui.tableWidget.setItem(i, 0, item1)
            self.ui.tableWidget.setItem(i, 1, item2)
            self.ui.tableWidget.setItem(i, 2, item3)
            self.ui.tableWidget.setItem(i, 3, item4)
            btn= QPushButton() 
            btn.setObjectName(str(teacher[0]))
            btn.clicked.connect(self.delete_teacher)
            #btn.setObjectName('delete_'+str(teacher[0]))
            btn.setIcon(QIcon( os.path.join(os.path.curdir, 'images/delete.svg' )))
            #exec("self.ui."+'delete_'+str(teacher[0])+".clicked.connect(self.clicked_on_a_reservation)" )
            self.ui.tableWidget.setCellWidget(i, 4, btn)
            self.ui.tableWidget.setRowHeight(i, 35)  

    def delete_teacher(self):
        the_id = self.sender().objectName()
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        cur.execute('delete from teachers where id=?', (the_id,))
        con.commit()


    def side_bar_extend(self):
        width = self.ui.side_bar.width()
        height = self.ui.side_bar.height()
        if(width==60):
            self.ui.side_bar.setMaximumWidth(width+200)
            self.ui.side_bar.resize(width+200, height)
        else:
            self.ui.side_bar.resize(60, height)








    def rgb_change(self):
        if(self.sender().objectName()=='r_slider'):
            self.ui.r_label.setText(str(self.sender().value()))
        elif(self.sender().objectName()=='g_slider'):
            self.ui.g_label.setText(str(self.sender().value()))
        elif(self.sender().objectName()=='b_slider'):
            self.ui.b_label.setText(str(self.sender().value()))

        self.ui.widget_16.setStyleSheet("background-color: rgb("+str(self.ui.r_slider.value())+","+str(self.ui.g_slider.value())+","+str(self.ui.b_slider.value())+")")










    #draggable titlebar
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.max_=False
        self.showNormal()
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)







    #delete reservations
    def clicked_on_a_reservation(self):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            cell = self.findChild(QPushButton,self.sender().objectName()).parent().objectName()
            self.findChild(QPushButton,self.sender().objectName()).hide()
            tt = self.sender().text()
            text = tt.split(' | ')
            con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
            cur = con.cursor()
            cur.execute('SELECT id from teachers where name=?',(text[0],))
            teacher_id = cur.fetchone()[0]
            number = int(''.join(filter(str.isdigit, cell)))
            cur.execute('SELECT cell_'+str(number)+' FROM reservations where season=? AND grade=?',(self.season_selection.currentText(),self.grade_selection.currentText()))
            reses = cur.fetchone()[0]
            ff = json.loads(reses)
            lenght = json.loads(reses)
            second =  json.loads(reses)
            where = reses
            for i in range(len(lenght)):
                if ff[i]['teacher']==teacher_id and ff[i]['subject']==text[1] and ff[i]['class']==text[2]:
                    second.remove(ff[i])
                    sett = json.dumps(second)
                    con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
                    cur = con.cursor()
                    sql = "UPDATE reservations SET cell_"+str(number)+"=? WHERE season=? AND grade=? AND cell_"+str(number)+"=?"
                    cur.execute(sql, (sett,self.season_selection.currentText(),self.grade_selection.currentText(),where))
                    con.commit()
                   
            self.reset_teacher_table()
            self.reset_class_table()
































    def saved_teacher_data(self):
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()

        name = self.ui.teacher_name.text()
        subject = self.ui.teacher_subject.text()
        color = str(self.ui.r_slider.value()) + "," + str(self.ui.g_slider.value()) + "," + str(self.ui.b_slider.value())
        cur.execute("INSERT INTO teachers(name, subject, color) VALUES(?,?,?)",(name,subject,color))
        con.commit()

        cur.execute("select max(id) from teachers")
        id = int(cur.fetchone()[0])+1
        ind = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(ind)
        rgb = color.split(',')
        item1 = QTableWidgetItem(str(id))
        item2 = QTableWidgetItem(str(name))
        item3 = QTableWidgetItem(str(subject))
        item4 = QTableWidgetItem(str(color))
        item1.setTextAlignment(Qt.AlignCenter)
        item2.setTextAlignment(Qt.AlignCenter)
        item3.setTextAlignment(Qt.AlignCenter)
        item4.setTextAlignment(Qt.AlignCenter)
        item1.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
        item2.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
        item3.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
        item4.setBackground(QColor(int(rgb[0]),int(rgb[1]),int(rgb[2])))
        self.ui.tableWidget.setItem(ind, 0, item1)
        self.ui.tableWidget.setItem(ind, 1, item2)
        self.ui.tableWidget.setItem(ind, 2, item3)
        self.ui.tableWidget.setItem(ind, 3, item4)
        btn= QPushButton() 
        btn.setIcon(QIcon(os.path.join(os.path.curdir, 'images/delete.svg')))
        btn.clicked.connect(self.pr)
        self.ui.tableWidget.setCellWidget(ind, 4, btn)
        self.ui.teacher_name.setText('')
        self.ui.teacher_subject.setText('')
        self.ui.r_slider.setValue(0)
        self.ui.g_slider.setValue(0)
        self.ui.b_slider.setValue(0)
    def canceled_teacher_data(self):
        self.ui.teacher_name.setText('')
        self.ui.teacher_subject.setText('')


































    def create_file(self):
        ind = self.ui.stackedWidget.currentIndex()
        
        row_1 = ["","sunday","monday","thlat","arb3a","thuseday"]
        row_2 = ["08:00 - 09:00"]
        row_3 = ["09:00 - 10:00"]
        row_4 = ["10:00 - 11:00"]
        row_5 = ["11:00 - 12:00"]
        row_6 = ["BREAK"]
        row_7 = ["13:30 - 14:30"]
        row_8 = ["14:30 - 15:30"]
        row_9 = ["15:30 - 16:30"]
        row_10 = ["16:30 - 17:30"]

       

        if ind == 1:
            row_0 = [self.ui.tab3_season_selection.currentText(),self.ui.tab3_yearclass_selection.currentText()]
            
            for i in range(1,10):
                for k in range((i*5)-4,(i*5)+1):
                    exec("row_"+str(math.floor((int(k)-1)/5)+1)+".append(self.ui.square_"+str(k)+".text())")

            with open(os.path.join(os.path.curdir, 'my_new_data.csv' ), 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                for i in range(11):
                    exec("print(row_"+str(i)+")")
                    exec("writer.writerow(row_"+str(i)+")")


        elif ind == 2:
            row_0 = [self.ui.tab2_season_selection.currentText(),self.ui.tab2_teacher_selection.currentText()]
            for i in range(1,10):
                for k in range((i*5)-4,(i*5)+1):
                    exec("row_"+str(math.floor((int(k)-1)/5)+1)+".append(self.ui.box_"+str(k)+".text())")

            
            with open(os.path.join(os.path.curdir, 'my_new_data.csv' ), 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                for i in range(11):
                    exec("writer.writerow(row_"+str(i)+")")













    def change_stack(self):
        name = self.sender().objectName()
        if name == 'btn_all':
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.btn_all.setStyleSheet('border-left: 3px solid #04eeff;')
            self.ui.btn_classes.setStyleSheet('border: none;')
            self.ui.btn_teachers.setStyleSheet('border: none;')

        elif name == 'btn_teachers':
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.btn_all.setStyleSheet('border: none;')
            self.ui.btn_classes.setStyleSheet('border: none;')
            self.ui.btn_teachers.setStyleSheet('border-left: 3px solid #04eeff;')
        elif name == 'btn_classes':
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.btn_all.setStyleSheet('border: none;')
            self.ui.btn_classes.setStyleSheet('border-left: 3px solid #04eeff;')
            self.ui.btn_teachers.setStyleSheet('border: none;')
        elif name == 'btn_edit_teachers':
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.btn_all.setStyleSheet('border: none;')
            self.ui.btn_classes.setStyleSheet('border-left: 3px solid #04eeff;')
            self.ui.btn_teachers.setStyleSheet('border: none;')









            
    def fill_class_table(self):
        season = self.ui.tab3_season_selection.currentText()
        year_class = self.ui.tab3_yearclass_selection.currentText()
        year = year_class.split(" | ")[0]
        classe = year_class.split(" | ")[1]
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        cur.execute("select * from reservations where season=? AND grade=? ",(season,year))
        classes = cur.fetchall()
        cur.execute("select * from teachers")
        the_teacher = cur.fetchall()
        for i in classes:
            for j in range(45):
                if i[j+2] != None:
                    var = json.loads(i[j+2])
                    for k in var:
                        if k['class']==classe:
                            for m in the_teacher:
                                if k['teacher'] == m[0]:
                                    tt=m[1]
                            exec("self.ui.square_"+str(j+1)+".setText('"+tt+" "+k['subject']+"')")








    def fill_teacher_table(self):
        season = self.ui.tab2_season_selection.currentText()
        teacher = self.ui.tab2_teacher_selection.currentText()
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        cur.execute("select * from reservations where season='%s'" % season)
        classes = cur.fetchall()
        cur.execute("select * from teachers where name='%s'" % teacher)
        the_teacher = cur.fetchall()
        for i in classes:
            for j in range(45):
                if i[j+2] != None:
                    var = json.loads(i[j+2])
                    for k in var:
                        if k['teacher']==the_teacher[0][0]:
                            #exec("self.ui.box_"+str(j+1)+".setText('"+i[1]+' '+k['class']+"')")
                            exec("self.ui.box_"+str(j+1)+".setText('"+i[1]+"')")








    def reset_teacher_table(self):
        for i in range(45):
            exec("self.ui.box_"+str(i+1)+".setText('')")
        self.fill_teacher_table()
        
    def reset_class_table(self):
        for i in range(45):
            exec("self.ui.square_"+str(i+1)+".setText('')")
        self.fill_class_table()









    def get_teacher(self,id):
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        cur.execute("select * from teachers where id='%s'" % id)
        teacher = cur.fetchone()
        return teacher





    def next_available_cell_name(self):
        bool = True
        i=1
        while bool:
            if(self.findChild(QPushButton,'class_'+str(i))):
                i+=1
            else:
                bool=False
                
        return ('class_'+str(i))























    def changed_selections(self):  
        next_cell = self.next_available_cell_name()
        rang = int(''.join(filter(str.isdigit, next_cell)))
        for i in range(rang-1):
            self.findChild(QPushButton,'class_'+str(i+1)).setParent(None)
            self.findChild(QPushButton,'add_cell_'+str(i+1)).show()

        self.data_on_start()























                        
    def add_cell(self):
        self.add_button = self.sender().objectName()
        self.index = ''.join(filter(str.isdigit, self.sender().objectName()))
        self.cell = self.findChild(QVBoxLayout,"list_"+self.index)
        self.show_popup(self.add_button.split("_")[2])

        







    #shows the dialogue window
    def show_popup(self,cell_number):
        used_teachers = []
        used_classes = []
        cell = self.findChild(QVBoxLayout,"list_"+str(cell_number))
        for k in range(cell.count()):
            mm = cell.itemAt(k).widget()
            if mm.text() != "add session":
                used_teachers.append(mm.text().split(" | ")[0])
                used_classes.append(mm.text().split(" | ")[2])
        self.window = QDialog()
        self.ff = Ui_Dialog()
        self.ff.setupUi(self.window)
        self.window.show()
        ######################
        #self.ui.pushButton_2.clicked.connect(lambda :self.window.hide())
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        cur.execute("select * from teachers")
        teachers = cur.fetchall()
        classes = ['class 1','class 2','class 3','class 4','class 5']
        print('//////////////////////////////////////////////////////////////////')
        print(teachers)
        sql = ("""select cell_"""+cell_number+""" from reservations where season = ?""")
        s = (self.season_selection.currentText())
        cur.execute(sql, (s,))
        reservations = cur.fetchall()
        for i in reservations:
            if i[0] != None:
                data = json.loads(i[0])
                for k in data:
                    used_teachers.append(self.get_teacher(k['teacher'])[1])

        for i in (teachers):
            print(i)
            print('//////////////////////////////////////////////////////////////////')
            if not i[1] in used_teachers:
                self.ff.comboBox.addItem(i[1])




        for i in (classes):
            if not i in used_classes:
                self.ff.comboBox_3.addItem(i)
        cur.execute("select * from teachers")
        subjects = cur.fetchall()
        for i in subjects:
            self.ff.comboBox_2.addItem(i[2])

    
        row = (int(cell_number)-1)/5
        col = int(cell_number)
        while col>5:
            col = col-5
        if col == 1:
            col = 'sunday'
        elif col == 2:
            col = 'monday'
        elif col == 3:
            col = 'tuesday'
        elif col == 4:
            col = 'wednesday'
        elif col == 5:
            col = 'thursday'


        row = math.floor(row)+1
        if row == 1:
            row = '8:00 - 9:00'
        elif row == 2:
            row = '9:00 - 10:00'
        elif row == 3:
            row = '10:00 - 11:00'
        elif row == 4:
            row = '11:00 - 12:00'
        elif row == 5:
            row = 'BREAK'
        elif row == 6:
            row = '13:30 - 14:30'
        elif row == 7:
            row = '14:30 - 15:30'
        elif row == 8:
            row = '15:30 - 16:30'
        elif row == 9:
            row = '14:30 - 17:30'
        self.ff.comboBox.setCurrentIndex(0)
        self.ff.comboBox_2.setCurrentIndex(0)


        self.ff.teacher = self.ff.comboBox.currentText()
        self.ff.subject = self.ff.comboBox_2.currentText()
        self.ff.classe = self.ff.comboBox_3.currentText()

        self.ff.label.setText(self.season_selection.currentText())
        self.ff.label_2.setText(self.grade_selection.currentText())
        self.ff.label_3.setText(col)
        self.ff.label_4.setText(row)

        self.ff.pushButton.clicked.connect(lambda: self.changes(self.ff.teacher,self.ff.subject,self.ff.classe))
       
        cur.execute("select * from teachers")
        sss = cur.fetchall()
        for r in sss:
            if r[1]==self.ff.comboBox.currentText():
                self.ff.comboBox_2.setCurrentText(r[2])


































    #displays the reservations
    def data_on_start(self):
        for i in range (45):
            self.add_button = 'add_cell_'+str(i+1)
            self.cell = self.findChild(QVBoxLayout,"list_"+str(i+1))

            con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
            cur = con.cursor()
       
            sql = ("""select * from reservations where season = ? and grade = ?""")
            s = (self.season_selection.currentText())
            g = (self.grade_selection.currentText())
            cur.execute(sql, (s,g))
            reservations = cur.fetchall()

            if(len(reservations) == 0):
                cur.execute("INSERT INTO reservations(season, grade) VALUES(?,?)",(s,g))
                con.commit()
                sql = ("""select * from reservations where season = ? and grade = ?""")
                s = (self.season_selection.currentText())
                g = (self.grade_selection.currentText())
                cur.execute(sql, (s,g))
                reservations = cur.fetchall()

            
            if(reservations[0][i+2] != None):
                y = json.loads(reservations[0][i+2])
                for x in range(len(y)):
                    cur.execute("select color from teachers where name='%s'" % self.get_teacher(y[x]["teacher"])[1])
                    color=cur.fetchall()
                    ff = self.get_teacher(y[x]["teacher"])[1] + " | " +y[x]["subject"]+" | "+y[x]["class"]
                    if(self.cell.count()<5):
                        self.btn = QPushButton("click")
                        self.btn.setMaximumSize(QSize(500, 50))
                        name=self.next_available_cell_name()
                        self.btn.setObjectName(name)
                        cc = color[0][0].split(',')
                        self.btn.setStyleSheet('background-color:rgba('+cc[0]+','+cc[1]+','+cc[2]+',0.2);border:none;border-left: 2px solid rgb('+cc[0]+','+cc[1]+','+cc[2]+');')
                        self.cell.addWidget(self.btn)
                        self.btn.setText(ff)
                        exec("self."+name+" = self.findChild(QPushButton,'"+name+"')" )
                        exec("self."+name+".clicked.connect(self.clicked_on_a_reservation)" )
                    elif(self.cell.count()==5):
                        self.btn = QPushButton("click")
                        self.btn.setMaximumSize(QSize(500, 50))
                        name=self.next_available_cell_name()
                        self.btn.setObjectName(name)
                        cc = color[0][0].split(',')
                        self.btn.setStyleSheet('background-color:rgba('+cc[0]+','+cc[1]+','+cc[2]+',0.2);border:none;border-left: 2px solid rgb('+cc[0]+','+cc[1]+','+cc[2]+');')
                        self.cell.addWidget(self.btn)
                        self.btn.setText(ff)
                        exec("self."+name+" = self.findChild(QPushButton,'"+name+"')" )
                        exec("self."+name+".clicked.connect(self.clicked_on_a_reservation)" )
                        self.findChild(QPushButton,self.add_button).hide()































    #adds the reservations to DB
    def changes(self,teacher,subject,classe):
        con = sqlite3.connect(os.path.join(os.path.curdir, 'database/db.sqlite'))
        cur = con.cursor()
        sql = ("select cell_"+self.index+" from reservations where season = ? and grade = ?")
        s = (self.season_selection.currentText())
        g = (self.grade_selection.currentText())
        cur.execute(sql, (s,g))
        reservations = cur.fetchall()

        sql = ("select * from teachers where name = ?")
        cur.execute(sql, (teacher,))
        teacher_id=cur.fetchone()[0]
        if(reservations[0][0] != None):
            row_of_reservations =  json.loads(reservations[0][0])
            row_of_reservations.append({"teacher":teacher_id,"subject":subject,"class":classe})
            row_of_reservations=json.dumps(row_of_reservations)
            sql = ("update reservations set cell_"+self.index+" = '"+row_of_reservations+"' where season = ? and grade = ? ")
            cur.execute(sql, (s,g))
            con.commit()
        else:
            res = json.dumps([{"teacher":teacher_id,"subject":subject,"class":classe}])
            sql = ("update reservations set cell_"+self.index+" = '"+res+"' where season = ? and grade = ? ")
            cur.execute(sql, (s,g))
            con.commit()


        cur.execute("select color from teachers where name='%s'" % teacher)
        color=cur.fetchall()

        if(self.cell.count()<5):
            self.btn = QPushButton("click")
            self.btn.setMaximumSize(QSize(500, 50))
            name=self.next_available_cell_name()
            self.btn.setObjectName(name)
            cc = color[0][0].split(',')
            self.btn.setStyleSheet('background-color:rgba('+cc[0]+','+cc[1]+','+cc[2]+',0.2);border:none;border-left: 2px solid rgb('+cc[0]+','+cc[1]+','+cc[2]+');')            
            self.cell.addWidget(self.btn)
            self.btn.setText(teacher+" | "+subject+" | "+classe)
            exec("self."+name+" = self.findChild(QPushButton,'"+name+"')" )
            exec("self."+name+".clicked.connect(self.clicked_on_a_reservation)" )
        elif(self.cell.count()==5):
            self.btn = QPushButton("click")
            self.btn.setMaximumSize(QSize(500, 50))
            name=self.next_available_cell_name()
            self.btn.setObjectName(name)
            cc = color[0][0].split(',')
            self.btn.setStyleSheet('background-color:rgba('+cc[0]+','+cc[1]+','+cc[2]+',0.2);border:none;border-left: 2px solid rgb('+cc[0]+','+cc[1]+','+cc[2]+');')
            self.cell.addWidget(self.btn)
            self.btn.setText(teacher+" | "+subject+" | "+classe)
            exec("self."+name+" = self.findChild(QPushButton,'"+name+"')" )
            exec("self."+name+".clicked.connect(self.clicked_on_a_reservation)" )
            self.findChild(QPushButton,self.add_button).hide()
            # must close the sub window here
            self.ff.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).click()

        #to refill the class and teacher table with the new data
        self.reset_teacher_table()
        self.reset_class_table()
        
        self.ff.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).click()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


