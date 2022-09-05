# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_filejtaVxw.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.the_main_bloc = QWidget(self.centralwidget)
        self.the_main_bloc.setObjectName(u"the_main_bloc")
        self.the_main_bloc.setMinimumSize(QSize(1280, 720))
        self.gridLayout = QGridLayout(self.the_main_bloc)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QWidget(self.the_main_bloc)
        self.side_bar.setObjectName(u"side_bar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_bar.sizePolicy().hasHeightForWidth())
        self.side_bar.setSizePolicy(sizePolicy1)
        self.side_bar.setMinimumSize(QSize(60, 0))
        self.side_bar.setMaximumSize(QSize(260, 16777215))
        self.side_bar.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.side_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.side_bar)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(60, 0))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_widget = QWidget(self.widget_2)
        self.logo_widget.setObjectName(u"logo_widget")
        self.logo_widget.setMinimumSize(QSize(60, 50))
        self.logo_widget.setMaximumSize(QSize(60, 50))

        self.verticalLayout.addWidget(self.logo_widget)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 10000))
        self.verticalLayout_32 = QVBoxLayout(self.widget)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(60, 0))
        self.widget_11.setMaximumSize(QSize(16777215, 315))
        self.verticalLayout_9 = QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_extend = QPushButton(self.widget_11)
        self.btn_extend.setObjectName(u"btn_extend")
        self.btn_extend.setMinimumSize(QSize(60, 45))
        self.btn_extend.setMaximumSize(QSize(60, 45))
        self.btn_extend.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_9.addWidget(self.btn_extend)

        self.btn_all = QPushButton(self.widget_11)
        self.btn_all.setObjectName(u"btn_all")
        self.btn_all.setEnabled(True)
        self.btn_all.setMinimumSize(QSize(60, 45))
        self.btn_all.setMaximumSize(QSize(60, 45))

        self.verticalLayout_9.addWidget(self.btn_all)

        self.btn_classes = QPushButton(self.widget_11)
        self.btn_classes.setObjectName(u"btn_classes")
        self.btn_classes.setMinimumSize(QSize(60, 45))
        self.btn_classes.setMaximumSize(QSize(60, 45))

        self.verticalLayout_9.addWidget(self.btn_classes)

        self.btn_teachers = QPushButton(self.widget_11)
        self.btn_teachers.setObjectName(u"btn_teachers")
        self.btn_teachers.setMinimumSize(QSize(60, 45))
        self.btn_teachers.setMaximumSize(QSize(60, 45))

        self.verticalLayout_9.addWidget(self.btn_teachers)

        self.btn_edit_teachers = QPushButton(self.widget_11)
        self.btn_edit_teachers.setObjectName(u"btn_edit_teachers")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_edit_teachers.sizePolicy().hasHeightForWidth())
        self.btn_edit_teachers.setSizePolicy(sizePolicy2)
        self.btn_edit_teachers.setMinimumSize(QSize(60, 45))
        self.btn_edit_teachers.setMaximumSize(QSize(60, 45))

        self.verticalLayout_9.addWidget(self.btn_edit_teachers)

        self.btn_save = QPushButton(self.widget_11)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(60, 45))
        self.btn_save.setMaximumSize(QSize(60, 45))
        self.btn_save.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_9.addWidget(self.btn_save)

        self.btn_settings = QPushButton(self.widget_11)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy2.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy2)
        self.btn_settings.setMinimumSize(QSize(60, 45))
        self.btn_settings.setMaximumSize(QSize(60, 45))

        self.verticalLayout_9.addWidget(self.btn_settings)


        self.verticalLayout.addWidget(self.widget_11)

        self.widget1 = QWidget(self.widget_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMaximumSize(QSize(16777215, 1000))
        self.verticalLayout_29 = QVBoxLayout(self.widget1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")

        self.verticalLayout.addWidget(self.widget1)

        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.side_bar, 0, 0, 1, 1)

        self.widget_12 = QWidget(self.the_main_bloc)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_3 = QVBoxLayout(self.widget_12)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QWidget(self.widget_12)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.title_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 0, 1051, 51))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.frame)

        self.widget_6 = QWidget(self.title_bar)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(130, 16777215))
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QPushButton(self.widget_6)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(20, 20))
        self.btn_min.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.widget_6)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(20, 20))
        self.btn_max.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.widget_6)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_close)


        self.horizontalLayout_3.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.title_bar)

        self.main_widget = QWidget(self.widget_12)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_6 = QGridLayout(self.main_widget)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.all_table = QWidget()
        self.all_table.setObjectName(u"all_table")
        self.gridLayout_4 = QGridLayout(self.all_table)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.all_table)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(1150, 600))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_9)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(40, 40, 40, 40)
        self.widget_13 = QWidget(self.frame_9)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_2.setSpacing(32)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.season_selection = QComboBox(self.widget_13)
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.addItem("")
        self.season_selection.setObjectName(u"season_selection")
        self.season_selection.setMinimumSize(QSize(0, 35))
        self.season_selection.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.season_selection)

        self.grade_selection = QComboBox(self.widget_13)
        self.grade_selection.addItem("")
        self.grade_selection.addItem("")
        self.grade_selection.addItem("")
        self.grade_selection.addItem("")
        self.grade_selection.addItem("")
        self.grade_selection.setObjectName(u"grade_selection")
        self.grade_selection.setMinimumSize(QSize(0, 35))
        self.grade_selection.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.grade_selection)


        self.gridLayout_10.addWidget(self.widget_13, 0, 0, 1, 2)

        self.all_table_widget = QWidget(self.frame_9)
        self.all_table_widget.setObjectName(u"all_table_widget")
        self.all_table_widget.setStyleSheet(u"")
        self.gridLayout_11 = QGridLayout(self.all_table_widget)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QWidget(self.all_table_widget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(900, 50))
        self.top_bar.setMaximumSize(QSize(9000, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 17, 0)
        self.pushButton = QPushButton(self.top_bar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_9 = QPushButton(self.top_bar)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.pushButton_9.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.top_bar)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy4.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy4)
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.top_bar)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy4.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy4)
        self.pushButton_11.setMaximumSize(QSize(10000, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.top_bar)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy4.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy4)
        self.pushButton_12.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.top_bar)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.pushButton_13)


        self.gridLayout_11.addWidget(self.top_bar, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.all_table_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1119, 2300))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main_box = QFrame(self.scrollAreaWidgetContents)
        self.main_box.setObjectName(u"main_box")
        self.main_box.setMinimumSize(QSize(900, 2300))
        self.verticalLayout_6 = QVBoxLayout(self.main_box)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.row_1 = QWidget(self.main_box)
        self.row_1.setObjectName(u"row_1")
        self.horizontalLayout_6 = QHBoxLayout(self.row_1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box = QWidget(self.row_1)
        self.time_slot_box.setObjectName(u"time_slot_box")
        self.time_slot_box.setMaximumSize(QSize(2000, 2000))
        self.verticalLayout_11 = QVBoxLayout(self.time_slot_box)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.time_slot_box)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(150, 50))
        self.pushButton_14.setMaximumSize(QSize(500, 50))

        self.verticalLayout_11.addWidget(self.pushButton_14)


        self.horizontalLayout_6.addWidget(self.time_slot_box)

        self.cell_1 = QWidget(self.row_1)
        self.cell_1.setObjectName(u"cell_1")
        self.cell_1.setMaximumSize(QSize(2000, 2000))
        self.verticalLayout_15 = QVBoxLayout(self.cell_1)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.list_1 = QVBoxLayout()
        self.list_1.setSpacing(0)
        self.list_1.setObjectName(u"list_1")
        self.add_cell_1 = QPushButton(self.cell_1)
        self.add_cell_1.setObjectName(u"add_cell_1")
        self.add_cell_1.setMinimumSize(QSize(150, 50))
        self.add_cell_1.setMaximumSize(QSize(500, 50))

        self.list_1.addWidget(self.add_cell_1)


        self.verticalLayout_15.addLayout(self.list_1)


        self.horizontalLayout_6.addWidget(self.cell_1)

        self.cell_2 = QWidget(self.row_1)
        self.cell_2.setObjectName(u"cell_2")
        self.verticalLayout_12 = QVBoxLayout(self.cell_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.list_2 = QVBoxLayout()
        self.list_2.setSpacing(0)
        self.list_2.setObjectName(u"list_2")
        self.add_cell_2 = QPushButton(self.cell_2)
        self.add_cell_2.setObjectName(u"add_cell_2")
        self.add_cell_2.setMinimumSize(QSize(150, 50))
        self.add_cell_2.setMaximumSize(QSize(500, 50))

        self.list_2.addWidget(self.add_cell_2)


        self.verticalLayout_12.addLayout(self.list_2)


        self.horizontalLayout_6.addWidget(self.cell_2)

        self.cell_3 = QWidget(self.row_1)
        self.cell_3.setObjectName(u"cell_3")
        self.cell_3.setMaximumSize(QSize(10000, 2000))
        self.verticalLayout_13 = QVBoxLayout(self.cell_3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.list_3 = QVBoxLayout()
        self.list_3.setObjectName(u"list_3")
        self.add_cell_3 = QPushButton(self.cell_3)
        self.add_cell_3.setObjectName(u"add_cell_3")
        self.add_cell_3.setMinimumSize(QSize(150, 50))
        self.add_cell_3.setMaximumSize(QSize(500, 50))

        self.list_3.addWidget(self.add_cell_3)


        self.verticalLayout_13.addLayout(self.list_3)


        self.horizontalLayout_6.addWidget(self.cell_3)

        self.cell_4 = QWidget(self.row_1)
        self.cell_4.setObjectName(u"cell_4")
        self.cell_4.setMinimumSize(QSize(150, 50))
        self.cell_4.setMaximumSize(QSize(2000, 2000))
        self.verticalLayout_16 = QVBoxLayout(self.cell_4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.list_4 = QVBoxLayout()
        self.list_4.setObjectName(u"list_4")
        self.add_cell_4 = QPushButton(self.cell_4)
        self.add_cell_4.setObjectName(u"add_cell_4")
        self.add_cell_4.setMinimumSize(QSize(150, 50))
        self.add_cell_4.setMaximumSize(QSize(500, 50))

        self.list_4.addWidget(self.add_cell_4)


        self.verticalLayout_16.addLayout(self.list_4)


        self.horizontalLayout_6.addWidget(self.cell_4)

        self.cell_5 = QWidget(self.row_1)
        self.cell_5.setObjectName(u"cell_5")
        self.cell_5.setMaximumSize(QSize(2000, 2000))
        self.verticalLayout_14 = QVBoxLayout(self.cell_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.list_5 = QVBoxLayout()
        self.list_5.setObjectName(u"list_5")
        self.add_cell_5 = QPushButton(self.cell_5)
        self.add_cell_5.setObjectName(u"add_cell_5")
        self.add_cell_5.setMinimumSize(QSize(150, 50))
        self.add_cell_5.setMaximumSize(QSize(500, 50))

        self.list_5.addWidget(self.add_cell_5)


        self.verticalLayout_14.addLayout(self.list_5)


        self.horizontalLayout_6.addWidget(self.cell_5)


        self.verticalLayout_6.addWidget(self.row_1)

        self.this_row = QWidget(self.main_box)
        self.this_row.setObjectName(u"this_row")
        self.horizontalLayout_9 = QHBoxLayout(self.this_row)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_2 = QWidget(self.this_row)
        self.time_slot_box_2.setObjectName(u"time_slot_box_2")
        self.verticalLayout_17 = QVBoxLayout(self.time_slot_box_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_92 = QPushButton(self.time_slot_box_2)
        self.pushButton_92.setObjectName(u"pushButton_92")
        self.pushButton_92.setMinimumSize(QSize(150, 50))
        self.pushButton_92.setMaximumSize(QSize(500, 50))

        self.verticalLayout_17.addWidget(self.pushButton_92)


        self.horizontalLayout_9.addWidget(self.time_slot_box_2)

        self.cell_6 = QWidget(self.this_row)
        self.cell_6.setObjectName(u"cell_6")
        self.cell_6.setMinimumSize(QSize(150, 50))
        self.cell_6.setMaximumSize(QSize(2000, 2000))
        self.verticalLayout_18 = QVBoxLayout(self.cell_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.list_6 = QVBoxLayout()
        self.list_6.setObjectName(u"list_6")
        self.add_cell_6 = QPushButton(self.cell_6)
        self.add_cell_6.setObjectName(u"add_cell_6")
        self.add_cell_6.setMinimumSize(QSize(150, 50))
        self.add_cell_6.setMaximumSize(QSize(500, 50))

        self.list_6.addWidget(self.add_cell_6)


        self.verticalLayout_18.addLayout(self.list_6)


        self.horizontalLayout_9.addWidget(self.cell_6)

        self.cell_7 = QWidget(self.this_row)
        self.cell_7.setObjectName(u"cell_7")
        self.verticalLayout_19 = QVBoxLayout(self.cell_7)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.list_7 = QVBoxLayout()
        self.list_7.setObjectName(u"list_7")
        self.add_cell_7 = QPushButton(self.cell_7)
        self.add_cell_7.setObjectName(u"add_cell_7")
        self.add_cell_7.setMinimumSize(QSize(150, 50))
        self.add_cell_7.setMaximumSize(QSize(500, 50))

        self.list_7.addWidget(self.add_cell_7)


        self.verticalLayout_19.addLayout(self.list_7)


        self.horizontalLayout_9.addWidget(self.cell_7)

        self.cell_8 = QWidget(self.this_row)
        self.cell_8.setObjectName(u"cell_8")
        self.verticalLayout_20 = QVBoxLayout(self.cell_8)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.list_8 = QVBoxLayout()
        self.list_8.setObjectName(u"list_8")
        self.add_cell_8 = QPushButton(self.cell_8)
        self.add_cell_8.setObjectName(u"add_cell_8")
        self.add_cell_8.setMinimumSize(QSize(150, 50))
        self.add_cell_8.setMaximumSize(QSize(500, 50))

        self.list_8.addWidget(self.add_cell_8)


        self.verticalLayout_20.addLayout(self.list_8)


        self.horizontalLayout_9.addWidget(self.cell_8)

        self.cell_9 = QWidget(self.this_row)
        self.cell_9.setObjectName(u"cell_9")
        self.verticalLayout_22 = QVBoxLayout(self.cell_9)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.list_9 = QVBoxLayout()
        self.list_9.setObjectName(u"list_9")
        self.add_cell_9 = QPushButton(self.cell_9)
        self.add_cell_9.setObjectName(u"add_cell_9")
        self.add_cell_9.setMinimumSize(QSize(150, 50))
        self.add_cell_9.setMaximumSize(QSize(500, 50))

        self.list_9.addWidget(self.add_cell_9)


        self.verticalLayout_22.addLayout(self.list_9)


        self.horizontalLayout_9.addWidget(self.cell_9)

        self.cell_10 = QWidget(self.this_row)
        self.cell_10.setObjectName(u"cell_10")
        self.verticalLayout_21 = QVBoxLayout(self.cell_10)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.list_10 = QVBoxLayout()
        self.list_10.setObjectName(u"list_10")
        self.add_cell_10 = QPushButton(self.cell_10)
        self.add_cell_10.setObjectName(u"add_cell_10")
        self.add_cell_10.setMinimumSize(QSize(150, 50))
        self.add_cell_10.setMaximumSize(QSize(500, 50))

        self.list_10.addWidget(self.add_cell_10)


        self.verticalLayout_21.addLayout(self.list_10)


        self.horizontalLayout_9.addWidget(self.cell_10)


        self.verticalLayout_6.addWidget(self.this_row)

        self.widget_21 = QWidget(self.main_box)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_3 = QWidget(self.widget_21)
        self.time_slot_box_3.setObjectName(u"time_slot_box_3")
        self.verticalLayout_23 = QVBoxLayout(self.time_slot_box_3)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pushButton_93 = QPushButton(self.time_slot_box_3)
        self.pushButton_93.setObjectName(u"pushButton_93")
        self.pushButton_93.setMinimumSize(QSize(150, 50))
        self.pushButton_93.setMaximumSize(QSize(200, 50))

        self.verticalLayout_23.addWidget(self.pushButton_93)


        self.horizontalLayout_10.addWidget(self.time_slot_box_3)

        self.cell_11 = QWidget(self.widget_21)
        self.cell_11.setObjectName(u"cell_11")
        self.verticalLayout_24 = QVBoxLayout(self.cell_11)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.list_11 = QVBoxLayout()
        self.list_11.setObjectName(u"list_11")
        self.add_cell_11 = QPushButton(self.cell_11)
        self.add_cell_11.setObjectName(u"add_cell_11")
        self.add_cell_11.setMinimumSize(QSize(150, 50))
        self.add_cell_11.setMaximumSize(QSize(200, 50))

        self.list_11.addWidget(self.add_cell_11)


        self.verticalLayout_24.addLayout(self.list_11)


        self.horizontalLayout_10.addWidget(self.cell_11)

        self.cell_12 = QWidget(self.widget_21)
        self.cell_12.setObjectName(u"cell_12")
        self.verticalLayout_25 = QVBoxLayout(self.cell_12)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.list_12 = QVBoxLayout()
        self.list_12.setObjectName(u"list_12")
        self.add_cell_12 = QPushButton(self.cell_12)
        self.add_cell_12.setObjectName(u"add_cell_12")
        self.add_cell_12.setMinimumSize(QSize(150, 50))
        self.add_cell_12.setMaximumSize(QSize(200, 50))

        self.list_12.addWidget(self.add_cell_12)


        self.verticalLayout_25.addLayout(self.list_12)


        self.horizontalLayout_10.addWidget(self.cell_12)

        self.cell_13 = QWidget(self.widget_21)
        self.cell_13.setObjectName(u"cell_13")
        self.verticalLayout_26 = QVBoxLayout(self.cell_13)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.list_13 = QVBoxLayout()
        self.list_13.setObjectName(u"list_13")
        self.add_cell_13 = QPushButton(self.cell_13)
        self.add_cell_13.setObjectName(u"add_cell_13")
        self.add_cell_13.setMinimumSize(QSize(150, 50))
        self.add_cell_13.setMaximumSize(QSize(200, 50))

        self.list_13.addWidget(self.add_cell_13)


        self.verticalLayout_26.addLayout(self.list_13)


        self.horizontalLayout_10.addWidget(self.cell_13)

        self.cell_14 = QWidget(self.widget_21)
        self.cell_14.setObjectName(u"cell_14")
        self.verticalLayout_27 = QVBoxLayout(self.cell_14)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.list_14 = QVBoxLayout()
        self.list_14.setObjectName(u"list_14")
        self.add_cell_14 = QPushButton(self.cell_14)
        self.add_cell_14.setObjectName(u"add_cell_14")
        self.add_cell_14.setMinimumSize(QSize(150, 50))
        self.add_cell_14.setMaximumSize(QSize(200, 50))

        self.list_14.addWidget(self.add_cell_14)


        self.verticalLayout_27.addLayout(self.list_14)


        self.horizontalLayout_10.addWidget(self.cell_14)

        self.cell_15 = QWidget(self.widget_21)
        self.cell_15.setObjectName(u"cell_15")
        self.verticalLayout_28 = QVBoxLayout(self.cell_15)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.list_15 = QVBoxLayout()
        self.list_15.setObjectName(u"list_15")
        self.add_cell_15 = QPushButton(self.cell_15)
        self.add_cell_15.setObjectName(u"add_cell_15")
        self.add_cell_15.setMinimumSize(QSize(150, 50))
        self.add_cell_15.setMaximumSize(QSize(200, 50))

        self.list_15.addWidget(self.add_cell_15)


        self.verticalLayout_28.addLayout(self.list_15)


        self.horizontalLayout_10.addWidget(self.cell_15)


        self.verticalLayout_6.addWidget(self.widget_21)

        self.widget_3 = QWidget(self.main_box)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_4 = QWidget(self.widget_3)
        self.time_slot_box_4.setObjectName(u"time_slot_box_4")
        self.verticalLayout_53 = QVBoxLayout(self.time_slot_box_4)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.pushButton_123 = QPushButton(self.time_slot_box_4)
        self.pushButton_123.setObjectName(u"pushButton_123")
        self.pushButton_123.setMinimumSize(QSize(150, 50))
        self.pushButton_123.setMaximumSize(QSize(200, 50))

        self.verticalLayout_53.addWidget(self.pushButton_123)


        self.horizontalLayout_11.addWidget(self.time_slot_box_4)

        self.cell_16 = QWidget(self.widget_3)
        self.cell_16.setObjectName(u"cell_16")
        self.verticalLayout_54 = QVBoxLayout(self.cell_16)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.list_16 = QVBoxLayout()
        self.list_16.setObjectName(u"list_16")
        self.add_cell_16 = QPushButton(self.cell_16)
        self.add_cell_16.setObjectName(u"add_cell_16")
        self.add_cell_16.setMinimumSize(QSize(150, 50))
        self.add_cell_16.setMaximumSize(QSize(200, 50))

        self.list_16.addWidget(self.add_cell_16)


        self.verticalLayout_54.addLayout(self.list_16)


        self.horizontalLayout_11.addWidget(self.cell_16)

        self.cell_17 = QWidget(self.widget_3)
        self.cell_17.setObjectName(u"cell_17")
        self.verticalLayout_55 = QVBoxLayout(self.cell_17)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.list_17 = QVBoxLayout()
        self.list_17.setObjectName(u"list_17")
        self.add_cell_17 = QPushButton(self.cell_17)
        self.add_cell_17.setObjectName(u"add_cell_17")
        self.add_cell_17.setMinimumSize(QSize(150, 50))
        self.add_cell_17.setMaximumSize(QSize(200, 50))

        self.list_17.addWidget(self.add_cell_17)


        self.verticalLayout_55.addLayout(self.list_17)


        self.horizontalLayout_11.addWidget(self.cell_17)

        self.cell_18 = QWidget(self.widget_3)
        self.cell_18.setObjectName(u"cell_18")
        self.verticalLayout_56 = QVBoxLayout(self.cell_18)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.list_18 = QVBoxLayout()
        self.list_18.setObjectName(u"list_18")
        self.add_cell_18 = QPushButton(self.cell_18)
        self.add_cell_18.setObjectName(u"add_cell_18")
        self.add_cell_18.setMinimumSize(QSize(150, 50))
        self.add_cell_18.setMaximumSize(QSize(200, 50))

        self.list_18.addWidget(self.add_cell_18)


        self.verticalLayout_56.addLayout(self.list_18)


        self.horizontalLayout_11.addWidget(self.cell_18)

        self.cell_19 = QWidget(self.widget_3)
        self.cell_19.setObjectName(u"cell_19")
        self.verticalLayout_57 = QVBoxLayout(self.cell_19)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.list_19 = QVBoxLayout()
        self.list_19.setObjectName(u"list_19")
        self.add_cell_19 = QPushButton(self.cell_19)
        self.add_cell_19.setObjectName(u"add_cell_19")
        self.add_cell_19.setMinimumSize(QSize(150, 50))
        self.add_cell_19.setMaximumSize(QSize(200, 50))

        self.list_19.addWidget(self.add_cell_19)


        self.verticalLayout_57.addLayout(self.list_19)


        self.horizontalLayout_11.addWidget(self.cell_19)

        self.cell_20 = QWidget(self.widget_3)
        self.cell_20.setObjectName(u"cell_20")
        self.verticalLayout_58 = QVBoxLayout(self.cell_20)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.list_20 = QVBoxLayout()
        self.list_20.setObjectName(u"list_20")
        self.add_cell_20 = QPushButton(self.cell_20)
        self.add_cell_20.setObjectName(u"add_cell_20")
        self.add_cell_20.setMinimumSize(QSize(150, 50))
        self.add_cell_20.setMaximumSize(QSize(200, 50))

        self.list_20.addWidget(self.add_cell_20)


        self.verticalLayout_58.addLayout(self.list_20)


        self.horizontalLayout_11.addWidget(self.cell_20)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.main_box)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_5 = QWidget(self.widget_5)
        self.time_slot_box_5.setObjectName(u"time_slot_box_5")
        self.verticalLayout_59 = QVBoxLayout(self.time_slot_box_5)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.pushButton_129 = QPushButton(self.time_slot_box_5)
        self.pushButton_129.setObjectName(u"pushButton_129")
        self.pushButton_129.setMinimumSize(QSize(150, 50))
        self.pushButton_129.setMaximumSize(QSize(200, 50))

        self.verticalLayout_59.addWidget(self.pushButton_129)


        self.horizontalLayout_12.addWidget(self.time_slot_box_5)

        self.cell_21 = QWidget(self.widget_5)
        self.cell_21.setObjectName(u"cell_21")
        self.verticalLayout_60 = QVBoxLayout(self.cell_21)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.list_21 = QVBoxLayout()
        self.list_21.setObjectName(u"list_21")
        self.add_cell_21 = QPushButton(self.cell_21)
        self.add_cell_21.setObjectName(u"add_cell_21")
        self.add_cell_21.setMinimumSize(QSize(150, 50))
        self.add_cell_21.setMaximumSize(QSize(200, 50))

        self.list_21.addWidget(self.add_cell_21)


        self.verticalLayout_60.addLayout(self.list_21)


        self.horizontalLayout_12.addWidget(self.cell_21)

        self.cell_22 = QWidget(self.widget_5)
        self.cell_22.setObjectName(u"cell_22")
        self.verticalLayout_61 = QVBoxLayout(self.cell_22)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.list_22 = QVBoxLayout()
        self.list_22.setObjectName(u"list_22")
        self.add_cell_22 = QPushButton(self.cell_22)
        self.add_cell_22.setObjectName(u"add_cell_22")
        self.add_cell_22.setMinimumSize(QSize(150, 50))
        self.add_cell_22.setMaximumSize(QSize(200, 50))

        self.list_22.addWidget(self.add_cell_22)


        self.verticalLayout_61.addLayout(self.list_22)


        self.horizontalLayout_12.addWidget(self.cell_22)

        self.cell_23 = QWidget(self.widget_5)
        self.cell_23.setObjectName(u"cell_23")
        self.verticalLayout_62 = QVBoxLayout(self.cell_23)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.list_23 = QVBoxLayout()
        self.list_23.setObjectName(u"list_23")
        self.add_cell_23 = QPushButton(self.cell_23)
        self.add_cell_23.setObjectName(u"add_cell_23")
        self.add_cell_23.setMinimumSize(QSize(150, 50))
        self.add_cell_23.setMaximumSize(QSize(200, 50))

        self.list_23.addWidget(self.add_cell_23)


        self.verticalLayout_62.addLayout(self.list_23)


        self.horizontalLayout_12.addWidget(self.cell_23)

        self.cell_24 = QWidget(self.widget_5)
        self.cell_24.setObjectName(u"cell_24")
        self.verticalLayout_63 = QVBoxLayout(self.cell_24)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.list_24 = QVBoxLayout()
        self.list_24.setObjectName(u"list_24")
        self.add_cell_24 = QPushButton(self.cell_24)
        self.add_cell_24.setObjectName(u"add_cell_24")
        self.add_cell_24.setMinimumSize(QSize(150, 50))
        self.add_cell_24.setMaximumSize(QSize(200, 50))

        self.list_24.addWidget(self.add_cell_24)


        self.verticalLayout_63.addLayout(self.list_24)


        self.horizontalLayout_12.addWidget(self.cell_24)

        self.cell_25 = QWidget(self.widget_5)
        self.cell_25.setObjectName(u"cell_25")
        self.verticalLayout_64 = QVBoxLayout(self.cell_25)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.list_25 = QVBoxLayout()
        self.list_25.setObjectName(u"list_25")
        self.add_cell_25 = QPushButton(self.cell_25)
        self.add_cell_25.setObjectName(u"add_cell_25")
        self.add_cell_25.setMinimumSize(QSize(150, 50))
        self.add_cell_25.setMaximumSize(QSize(200, 50))

        self.list_25.addWidget(self.add_cell_25)


        self.verticalLayout_64.addLayout(self.list_25)


        self.horizontalLayout_12.addWidget(self.cell_25)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.widget_61 = QWidget(self.main_box)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_6 = QWidget(self.widget_61)
        self.time_slot_box_6.setObjectName(u"time_slot_box_6")
        self.verticalLayout_65 = QVBoxLayout(self.time_slot_box_6)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.pushButton_135 = QPushButton(self.time_slot_box_6)
        self.pushButton_135.setObjectName(u"pushButton_135")
        self.pushButton_135.setMinimumSize(QSize(150, 50))
        self.pushButton_135.setMaximumSize(QSize(200, 50))

        self.verticalLayout_65.addWidget(self.pushButton_135)


        self.horizontalLayout_13.addWidget(self.time_slot_box_6)

        self.cell_26 = QWidget(self.widget_61)
        self.cell_26.setObjectName(u"cell_26")
        self.verticalLayout_66 = QVBoxLayout(self.cell_26)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.list_26 = QVBoxLayout()
        self.list_26.setObjectName(u"list_26")
        self.add_cell_26 = QPushButton(self.cell_26)
        self.add_cell_26.setObjectName(u"add_cell_26")
        self.add_cell_26.setMinimumSize(QSize(150, 50))
        self.add_cell_26.setMaximumSize(QSize(200, 50))

        self.list_26.addWidget(self.add_cell_26)


        self.verticalLayout_66.addLayout(self.list_26)


        self.horizontalLayout_13.addWidget(self.cell_26)

        self.cell_27 = QWidget(self.widget_61)
        self.cell_27.setObjectName(u"cell_27")
        self.verticalLayout_67 = QVBoxLayout(self.cell_27)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.list_27 = QVBoxLayout()
        self.list_27.setObjectName(u"list_27")
        self.add_cell_27 = QPushButton(self.cell_27)
        self.add_cell_27.setObjectName(u"add_cell_27")
        self.add_cell_27.setMinimumSize(QSize(150, 50))
        self.add_cell_27.setMaximumSize(QSize(200, 50))

        self.list_27.addWidget(self.add_cell_27)


        self.verticalLayout_67.addLayout(self.list_27)


        self.horizontalLayout_13.addWidget(self.cell_27)

        self.cell_28 = QWidget(self.widget_61)
        self.cell_28.setObjectName(u"cell_28")
        self.verticalLayout_68 = QVBoxLayout(self.cell_28)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.list_28 = QVBoxLayout()
        self.list_28.setObjectName(u"list_28")
        self.add_cell_28 = QPushButton(self.cell_28)
        self.add_cell_28.setObjectName(u"add_cell_28")
        self.add_cell_28.setMinimumSize(QSize(150, 50))
        self.add_cell_28.setMaximumSize(QSize(200, 50))

        self.list_28.addWidget(self.add_cell_28)


        self.verticalLayout_68.addLayout(self.list_28)


        self.horizontalLayout_13.addWidget(self.cell_28)

        self.cell_29 = QWidget(self.widget_61)
        self.cell_29.setObjectName(u"cell_29")
        self.verticalLayout_69 = QVBoxLayout(self.cell_29)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.list_29 = QVBoxLayout()
        self.list_29.setObjectName(u"list_29")
        self.add_cell_29 = QPushButton(self.cell_29)
        self.add_cell_29.setObjectName(u"add_cell_29")
        self.add_cell_29.setMinimumSize(QSize(150, 50))
        self.add_cell_29.setMaximumSize(QSize(200, 50))

        self.list_29.addWidget(self.add_cell_29)


        self.verticalLayout_69.addLayout(self.list_29)


        self.horizontalLayout_13.addWidget(self.cell_29)

        self.cell_30 = QWidget(self.widget_61)
        self.cell_30.setObjectName(u"cell_30")
        self.verticalLayout_70 = QVBoxLayout(self.cell_30)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.list_30 = QVBoxLayout()
        self.list_30.setObjectName(u"list_30")
        self.add_cell_30 = QPushButton(self.cell_30)
        self.add_cell_30.setObjectName(u"add_cell_30")
        self.add_cell_30.setMinimumSize(QSize(150, 50))
        self.add_cell_30.setMaximumSize(QSize(200, 50))

        self.list_30.addWidget(self.add_cell_30)


        self.verticalLayout_70.addLayout(self.list_30)


        self.horizontalLayout_13.addWidget(self.cell_30)


        self.verticalLayout_6.addWidget(self.widget_61)

        self.widget_7 = QWidget(self.main_box)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_7 = QWidget(self.widget_7)
        self.time_slot_box_7.setObjectName(u"time_slot_box_7")
        self.verticalLayout_77 = QVBoxLayout(self.time_slot_box_7)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.pushButton_147 = QPushButton(self.time_slot_box_7)
        self.pushButton_147.setObjectName(u"pushButton_147")
        self.pushButton_147.setMinimumSize(QSize(150, 50))
        self.pushButton_147.setMaximumSize(QSize(200, 50))

        self.verticalLayout_77.addWidget(self.pushButton_147)


        self.horizontalLayout_14.addWidget(self.time_slot_box_7)

        self.cell_31 = QWidget(self.widget_7)
        self.cell_31.setObjectName(u"cell_31")
        self.verticalLayout_78 = QVBoxLayout(self.cell_31)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.list_31 = QVBoxLayout()
        self.list_31.setObjectName(u"list_31")
        self.add_cell_31 = QPushButton(self.cell_31)
        self.add_cell_31.setObjectName(u"add_cell_31")
        self.add_cell_31.setMinimumSize(QSize(150, 50))
        self.add_cell_31.setMaximumSize(QSize(200, 50))

        self.list_31.addWidget(self.add_cell_31)


        self.verticalLayout_78.addLayout(self.list_31)


        self.horizontalLayout_14.addWidget(self.cell_31)

        self.cell_32 = QWidget(self.widget_7)
        self.cell_32.setObjectName(u"cell_32")
        self.verticalLayout_79 = QVBoxLayout(self.cell_32)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.list_32 = QVBoxLayout()
        self.list_32.setObjectName(u"list_32")
        self.add_cell_32 = QPushButton(self.cell_32)
        self.add_cell_32.setObjectName(u"add_cell_32")
        self.add_cell_32.setMinimumSize(QSize(150, 50))
        self.add_cell_32.setMaximumSize(QSize(200, 50))

        self.list_32.addWidget(self.add_cell_32)


        self.verticalLayout_79.addLayout(self.list_32)


        self.horizontalLayout_14.addWidget(self.cell_32)

        self.cell_33 = QWidget(self.widget_7)
        self.cell_33.setObjectName(u"cell_33")
        self.verticalLayout_80 = QVBoxLayout(self.cell_33)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.list_33 = QVBoxLayout()
        self.list_33.setObjectName(u"list_33")
        self.add_cell_33 = QPushButton(self.cell_33)
        self.add_cell_33.setObjectName(u"add_cell_33")
        self.add_cell_33.setMinimumSize(QSize(150, 50))
        self.add_cell_33.setMaximumSize(QSize(200, 50))

        self.list_33.addWidget(self.add_cell_33)


        self.verticalLayout_80.addLayout(self.list_33)


        self.horizontalLayout_14.addWidget(self.cell_33)

        self.cell_34 = QWidget(self.widget_7)
        self.cell_34.setObjectName(u"cell_34")
        self.verticalLayout_81 = QVBoxLayout(self.cell_34)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.list_34 = QVBoxLayout()
        self.list_34.setObjectName(u"list_34")
        self.add_cell_34 = QPushButton(self.cell_34)
        self.add_cell_34.setObjectName(u"add_cell_34")
        self.add_cell_34.setMinimumSize(QSize(150, 50))
        self.add_cell_34.setMaximumSize(QSize(200, 50))

        self.list_34.addWidget(self.add_cell_34)


        self.verticalLayout_81.addLayout(self.list_34)


        self.horizontalLayout_14.addWidget(self.cell_34)

        self.cell_35 = QWidget(self.widget_7)
        self.cell_35.setObjectName(u"cell_35")
        self.verticalLayout_82 = QVBoxLayout(self.cell_35)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.list_35 = QVBoxLayout()
        self.list_35.setObjectName(u"list_35")
        self.add_cell_35 = QPushButton(self.cell_35)
        self.add_cell_35.setObjectName(u"add_cell_35")
        self.add_cell_35.setMinimumSize(QSize(150, 50))
        self.add_cell_35.setMaximumSize(QSize(200, 50))

        self.list_35.addWidget(self.add_cell_35)


        self.verticalLayout_82.addLayout(self.list_35)


        self.horizontalLayout_14.addWidget(self.cell_35)


        self.verticalLayout_6.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.main_box)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_8 = QWidget(self.widget_8)
        self.time_slot_box_8.setObjectName(u"time_slot_box_8")
        self.verticalLayout_71 = QVBoxLayout(self.time_slot_box_8)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.pushButton_141 = QPushButton(self.time_slot_box_8)
        self.pushButton_141.setObjectName(u"pushButton_141")
        self.pushButton_141.setMinimumSize(QSize(150, 50))
        self.pushButton_141.setMaximumSize(QSize(200, 50))

        self.verticalLayout_71.addWidget(self.pushButton_141)


        self.horizontalLayout_33.addWidget(self.time_slot_box_8)

        self.cell_36 = QWidget(self.widget_8)
        self.cell_36.setObjectName(u"cell_36")
        self.verticalLayout_72 = QVBoxLayout(self.cell_36)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.list_36 = QVBoxLayout()
        self.list_36.setObjectName(u"list_36")
        self.add_cell_36 = QPushButton(self.cell_36)
        self.add_cell_36.setObjectName(u"add_cell_36")
        self.add_cell_36.setMinimumSize(QSize(150, 50))
        self.add_cell_36.setMaximumSize(QSize(200, 50))

        self.list_36.addWidget(self.add_cell_36)


        self.verticalLayout_72.addLayout(self.list_36)


        self.horizontalLayout_33.addWidget(self.cell_36)

        self.cell_37 = QWidget(self.widget_8)
        self.cell_37.setObjectName(u"cell_37")
        self.verticalLayout_73 = QVBoxLayout(self.cell_37)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.list_37 = QVBoxLayout()
        self.list_37.setObjectName(u"list_37")
        self.add_cell_37 = QPushButton(self.cell_37)
        self.add_cell_37.setObjectName(u"add_cell_37")
        self.add_cell_37.setMinimumSize(QSize(150, 50))
        self.add_cell_37.setMaximumSize(QSize(200, 50))

        self.list_37.addWidget(self.add_cell_37)


        self.verticalLayout_73.addLayout(self.list_37)


        self.horizontalLayout_33.addWidget(self.cell_37)

        self.cell_38 = QWidget(self.widget_8)
        self.cell_38.setObjectName(u"cell_38")
        self.verticalLayout_74 = QVBoxLayout(self.cell_38)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.list_38 = QVBoxLayout()
        self.list_38.setObjectName(u"list_38")
        self.add_cell_38 = QPushButton(self.cell_38)
        self.add_cell_38.setObjectName(u"add_cell_38")
        self.add_cell_38.setMinimumSize(QSize(150, 50))
        self.add_cell_38.setMaximumSize(QSize(200, 50))

        self.list_38.addWidget(self.add_cell_38)


        self.verticalLayout_74.addLayout(self.list_38)


        self.horizontalLayout_33.addWidget(self.cell_38)

        self.cell_39 = QWidget(self.widget_8)
        self.cell_39.setObjectName(u"cell_39")
        self.verticalLayout_75 = QVBoxLayout(self.cell_39)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.list_39 = QVBoxLayout()
        self.list_39.setObjectName(u"list_39")
        self.add_cell_39 = QPushButton(self.cell_39)
        self.add_cell_39.setObjectName(u"add_cell_39")
        self.add_cell_39.setMinimumSize(QSize(150, 50))
        self.add_cell_39.setMaximumSize(QSize(200, 50))

        self.list_39.addWidget(self.add_cell_39)


        self.verticalLayout_75.addLayout(self.list_39)


        self.horizontalLayout_33.addWidget(self.cell_39)

        self.cell_40 = QWidget(self.widget_8)
        self.cell_40.setObjectName(u"cell_40")
        self.verticalLayout_76 = QVBoxLayout(self.cell_40)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.list_40 = QVBoxLayout()
        self.list_40.setObjectName(u"list_40")
        self.add_cell_40 = QPushButton(self.cell_40)
        self.add_cell_40.setObjectName(u"add_cell_40")
        self.add_cell_40.setMinimumSize(QSize(150, 50))
        self.add_cell_40.setMaximumSize(QSize(200, 50))

        self.list_40.addWidget(self.add_cell_40)


        self.verticalLayout_76.addLayout(self.list_40)


        self.horizontalLayout_33.addWidget(self.cell_40)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.main_box)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.time_slot_box_9 = QWidget(self.widget_9)
        self.time_slot_box_9.setObjectName(u"time_slot_box_9")
        self.verticalLayout_83 = QVBoxLayout(self.time_slot_box_9)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.pushButton_153 = QPushButton(self.time_slot_box_9)
        self.pushButton_153.setObjectName(u"pushButton_153")
        self.pushButton_153.setMinimumSize(QSize(150, 50))
        self.pushButton_153.setMaximumSize(QSize(200, 50))

        self.verticalLayout_83.addWidget(self.pushButton_153)


        self.horizontalLayout_35.addWidget(self.time_slot_box_9)

        self.cell_41 = QWidget(self.widget_9)
        self.cell_41.setObjectName(u"cell_41")
        self.verticalLayout_84 = QVBoxLayout(self.cell_41)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.list_41 = QVBoxLayout()
        self.list_41.setObjectName(u"list_41")
        self.add_cell_41 = QPushButton(self.cell_41)
        self.add_cell_41.setObjectName(u"add_cell_41")
        self.add_cell_41.setMinimumSize(QSize(150, 50))
        self.add_cell_41.setMaximumSize(QSize(200, 50))

        self.list_41.addWidget(self.add_cell_41)


        self.verticalLayout_84.addLayout(self.list_41)


        self.horizontalLayout_35.addWidget(self.cell_41)

        self.cell_42 = QWidget(self.widget_9)
        self.cell_42.setObjectName(u"cell_42")
        self.verticalLayout_85 = QVBoxLayout(self.cell_42)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.list_42 = QVBoxLayout()
        self.list_42.setObjectName(u"list_42")
        self.add_cell_42 = QPushButton(self.cell_42)
        self.add_cell_42.setObjectName(u"add_cell_42")
        self.add_cell_42.setMinimumSize(QSize(150, 50))
        self.add_cell_42.setMaximumSize(QSize(200, 50))

        self.list_42.addWidget(self.add_cell_42)


        self.verticalLayout_85.addLayout(self.list_42)


        self.horizontalLayout_35.addWidget(self.cell_42)

        self.cell_43 = QWidget(self.widget_9)
        self.cell_43.setObjectName(u"cell_43")
        self.verticalLayout_86 = QVBoxLayout(self.cell_43)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.list_43 = QVBoxLayout()
        self.list_43.setObjectName(u"list_43")
        self.add_cell_43 = QPushButton(self.cell_43)
        self.add_cell_43.setObjectName(u"add_cell_43")
        self.add_cell_43.setMinimumSize(QSize(150, 50))
        self.add_cell_43.setMaximumSize(QSize(200, 50))

        self.list_43.addWidget(self.add_cell_43)


        self.verticalLayout_86.addLayout(self.list_43)


        self.horizontalLayout_35.addWidget(self.cell_43)

        self.cell_44 = QWidget(self.widget_9)
        self.cell_44.setObjectName(u"cell_44")
        self.verticalLayout_87 = QVBoxLayout(self.cell_44)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.list_44 = QVBoxLayout()
        self.list_44.setObjectName(u"list_44")
        self.add_cell_44 = QPushButton(self.cell_44)
        self.add_cell_44.setObjectName(u"add_cell_44")
        self.add_cell_44.setMinimumSize(QSize(150, 50))
        self.add_cell_44.setMaximumSize(QSize(200, 50))

        self.list_44.addWidget(self.add_cell_44)


        self.verticalLayout_87.addLayout(self.list_44)


        self.horizontalLayout_35.addWidget(self.cell_44)

        self.cell_45 = QWidget(self.widget_9)
        self.cell_45.setObjectName(u"cell_45")
        self.verticalLayout_88 = QVBoxLayout(self.cell_45)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.list_45 = QVBoxLayout()
        self.list_45.setObjectName(u"list_45")
        self.add_cell_45 = QPushButton(self.cell_45)
        self.add_cell_45.setObjectName(u"add_cell_45")
        self.add_cell_45.setMinimumSize(QSize(150, 50))
        self.add_cell_45.setMaximumSize(QSize(200, 50))

        self.list_45.addWidget(self.add_cell_45)


        self.verticalLayout_88.addLayout(self.list_45)


        self.horizontalLayout_35.addWidget(self.cell_45)


        self.verticalLayout_6.addWidget(self.widget_9)


        self.gridLayout_3.addWidget(self.main_box, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.all_table_widget, 2, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_9, 0, 0, 1, 2)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.all_table)
        self.classes_table = QWidget()
        self.classes_table.setObjectName(u"classes_table")
        self.gridLayout_5 = QGridLayout(self.classes_table)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.classes_table)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(1150, 600))
        self.frame_4.setMaximumSize(QSize(2000, 2000))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_4)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(40, 40, 40, 40)
        self.class_table_widget = QWidget(self.frame_4)
        self.class_table_widget.setObjectName(u"class_table_widget")
        self.gridLayout_13 = QGridLayout(self.class_table_widget)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.table_of_classes = QWidget(self.class_table_widget)
        self.table_of_classes.setObjectName(u"table_of_classes")
        self.verticalLayout_30 = QVBoxLayout(self.table_of_classes)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.pushButton_29 = QPushButton(self.table_of_classes)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy4.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy4)
        self.pushButton_29.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_24.addWidget(self.pushButton_29)

        self.square_1 = QPushButton(self.table_of_classes)
        self.square_1.setObjectName(u"square_1")
        sizePolicy4.setHeightForWidth(self.square_1.sizePolicy().hasHeightForWidth())
        self.square_1.setSizePolicy(sizePolicy4)
        self.square_1.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_24.addWidget(self.square_1)

        self.square_2 = QPushButton(self.table_of_classes)
        self.square_2.setObjectName(u"square_2")
        sizePolicy4.setHeightForWidth(self.square_2.sizePolicy().hasHeightForWidth())
        self.square_2.setSizePolicy(sizePolicy4)
        self.square_2.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_24.addWidget(self.square_2)

        self.square_3 = QPushButton(self.table_of_classes)
        self.square_3.setObjectName(u"square_3")
        sizePolicy4.setHeightForWidth(self.square_3.sizePolicy().hasHeightForWidth())
        self.square_3.setSizePolicy(sizePolicy4)
        self.square_3.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_24.addWidget(self.square_3)

        self.square_4 = QPushButton(self.table_of_classes)
        self.square_4.setObjectName(u"square_4")
        sizePolicy4.setHeightForWidth(self.square_4.sizePolicy().hasHeightForWidth())
        self.square_4.setSizePolicy(sizePolicy4)
        self.square_4.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_24.addWidget(self.square_4)

        self.square_5 = QPushButton(self.table_of_classes)
        self.square_5.setObjectName(u"square_5")
        sizePolicy4.setHeightForWidth(self.square_5.sizePolicy().hasHeightForWidth())
        self.square_5.setSizePolicy(sizePolicy4)
        self.square_5.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_24.addWidget(self.square_5)


        self.verticalLayout_30.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_30 = QPushButton(self.table_of_classes)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy4.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy4)
        self.pushButton_30.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_25.addWidget(self.pushButton_30)

        self.square_6 = QPushButton(self.table_of_classes)
        self.square_6.setObjectName(u"square_6")
        sizePolicy4.setHeightForWidth(self.square_6.sizePolicy().hasHeightForWidth())
        self.square_6.setSizePolicy(sizePolicy4)
        self.square_6.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_25.addWidget(self.square_6)

        self.square_7 = QPushButton(self.table_of_classes)
        self.square_7.setObjectName(u"square_7")
        sizePolicy4.setHeightForWidth(self.square_7.sizePolicy().hasHeightForWidth())
        self.square_7.setSizePolicy(sizePolicy4)
        self.square_7.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_25.addWidget(self.square_7)

        self.square_8 = QPushButton(self.table_of_classes)
        self.square_8.setObjectName(u"square_8")
        sizePolicy4.setHeightForWidth(self.square_8.sizePolicy().hasHeightForWidth())
        self.square_8.setSizePolicy(sizePolicy4)
        self.square_8.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_25.addWidget(self.square_8)

        self.square_9 = QPushButton(self.table_of_classes)
        self.square_9.setObjectName(u"square_9")
        sizePolicy4.setHeightForWidth(self.square_9.sizePolicy().hasHeightForWidth())
        self.square_9.setSizePolicy(sizePolicy4)
        self.square_9.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_25.addWidget(self.square_9)

        self.square_10 = QPushButton(self.table_of_classes)
        self.square_10.setObjectName(u"square_10")
        sizePolicy4.setHeightForWidth(self.square_10.sizePolicy().hasHeightForWidth())
        self.square_10.setSizePolicy(sizePolicy4)
        self.square_10.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_25.addWidget(self.square_10)


        self.verticalLayout_30.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_69 = QPushButton(self.table_of_classes)
        self.pushButton_69.setObjectName(u"pushButton_69")
        sizePolicy4.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy4)
        self.pushButton_69.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_26.addWidget(self.pushButton_69)

        self.square_11 = QPushButton(self.table_of_classes)
        self.square_11.setObjectName(u"square_11")
        sizePolicy4.setHeightForWidth(self.square_11.sizePolicy().hasHeightForWidth())
        self.square_11.setSizePolicy(sizePolicy4)
        self.square_11.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_26.addWidget(self.square_11)

        self.square_12 = QPushButton(self.table_of_classes)
        self.square_12.setObjectName(u"square_12")
        sizePolicy4.setHeightForWidth(self.square_12.sizePolicy().hasHeightForWidth())
        self.square_12.setSizePolicy(sizePolicy4)
        self.square_12.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_26.addWidget(self.square_12)

        self.square_13 = QPushButton(self.table_of_classes)
        self.square_13.setObjectName(u"square_13")
        sizePolicy4.setHeightForWidth(self.square_13.sizePolicy().hasHeightForWidth())
        self.square_13.setSizePolicy(sizePolicy4)
        self.square_13.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_26.addWidget(self.square_13)

        self.square_14 = QPushButton(self.table_of_classes)
        self.square_14.setObjectName(u"square_14")
        sizePolicy4.setHeightForWidth(self.square_14.sizePolicy().hasHeightForWidth())
        self.square_14.setSizePolicy(sizePolicy4)
        self.square_14.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_26.addWidget(self.square_14)

        self.square_15 = QPushButton(self.table_of_classes)
        self.square_15.setObjectName(u"square_15")
        sizePolicy4.setHeightForWidth(self.square_15.sizePolicy().hasHeightForWidth())
        self.square_15.setSizePolicy(sizePolicy4)
        self.square_15.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_26.addWidget(self.square_15)


        self.verticalLayout_30.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pushButton_68 = QPushButton(self.table_of_classes)
        self.pushButton_68.setObjectName(u"pushButton_68")
        sizePolicy4.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy4)
        self.pushButton_68.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_27.addWidget(self.pushButton_68)

        self.square_16 = QPushButton(self.table_of_classes)
        self.square_16.setObjectName(u"square_16")
        sizePolicy4.setHeightForWidth(self.square_16.sizePolicy().hasHeightForWidth())
        self.square_16.setSizePolicy(sizePolicy4)
        self.square_16.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_27.addWidget(self.square_16)

        self.square_17 = QPushButton(self.table_of_classes)
        self.square_17.setObjectName(u"square_17")
        sizePolicy4.setHeightForWidth(self.square_17.sizePolicy().hasHeightForWidth())
        self.square_17.setSizePolicy(sizePolicy4)
        self.square_17.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_27.addWidget(self.square_17)

        self.square_18 = QPushButton(self.table_of_classes)
        self.square_18.setObjectName(u"square_18")
        sizePolicy4.setHeightForWidth(self.square_18.sizePolicy().hasHeightForWidth())
        self.square_18.setSizePolicy(sizePolicy4)
        self.square_18.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_27.addWidget(self.square_18)

        self.square_19 = QPushButton(self.table_of_classes)
        self.square_19.setObjectName(u"square_19")
        sizePolicy4.setHeightForWidth(self.square_19.sizePolicy().hasHeightForWidth())
        self.square_19.setSizePolicy(sizePolicy4)
        self.square_19.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_27.addWidget(self.square_19)

        self.square_20 = QPushButton(self.table_of_classes)
        self.square_20.setObjectName(u"square_20")
        sizePolicy4.setHeightForWidth(self.square_20.sizePolicy().hasHeightForWidth())
        self.square_20.setSizePolicy(sizePolicy4)
        self.square_20.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_27.addWidget(self.square_20)


        self.verticalLayout_30.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_67 = QPushButton(self.table_of_classes)
        self.pushButton_67.setObjectName(u"pushButton_67")
        sizePolicy4.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy4)
        self.pushButton_67.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_28.addWidget(self.pushButton_67)

        self.square_21 = QPushButton(self.table_of_classes)
        self.square_21.setObjectName(u"square_21")
        sizePolicy4.setHeightForWidth(self.square_21.sizePolicy().hasHeightForWidth())
        self.square_21.setSizePolicy(sizePolicy4)
        self.square_21.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_28.addWidget(self.square_21)

        self.square_22 = QPushButton(self.table_of_classes)
        self.square_22.setObjectName(u"square_22")
        sizePolicy4.setHeightForWidth(self.square_22.sizePolicy().hasHeightForWidth())
        self.square_22.setSizePolicy(sizePolicy4)
        self.square_22.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_28.addWidget(self.square_22)

        self.square_23 = QPushButton(self.table_of_classes)
        self.square_23.setObjectName(u"square_23")
        sizePolicy4.setHeightForWidth(self.square_23.sizePolicy().hasHeightForWidth())
        self.square_23.setSizePolicy(sizePolicy4)
        self.square_23.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_28.addWidget(self.square_23)

        self.square_24 = QPushButton(self.table_of_classes)
        self.square_24.setObjectName(u"square_24")
        sizePolicy4.setHeightForWidth(self.square_24.sizePolicy().hasHeightForWidth())
        self.square_24.setSizePolicy(sizePolicy4)
        self.square_24.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_28.addWidget(self.square_24)

        self.square_25 = QPushButton(self.table_of_classes)
        self.square_25.setObjectName(u"square_25")
        sizePolicy4.setHeightForWidth(self.square_25.sizePolicy().hasHeightForWidth())
        self.square_25.setSizePolicy(sizePolicy4)
        self.square_25.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_28.addWidget(self.square_25)


        self.verticalLayout_30.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton_66 = QPushButton(self.table_of_classes)
        self.pushButton_66.setObjectName(u"pushButton_66")
        sizePolicy4.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy4)
        self.pushButton_66.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_29.addWidget(self.pushButton_66)

        self.square_26 = QPushButton(self.table_of_classes)
        self.square_26.setObjectName(u"square_26")
        sizePolicy4.setHeightForWidth(self.square_26.sizePolicy().hasHeightForWidth())
        self.square_26.setSizePolicy(sizePolicy4)
        self.square_26.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_29.addWidget(self.square_26)

        self.square_27 = QPushButton(self.table_of_classes)
        self.square_27.setObjectName(u"square_27")
        sizePolicy4.setHeightForWidth(self.square_27.sizePolicy().hasHeightForWidth())
        self.square_27.setSizePolicy(sizePolicy4)
        self.square_27.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_29.addWidget(self.square_27)

        self.square_28 = QPushButton(self.table_of_classes)
        self.square_28.setObjectName(u"square_28")
        sizePolicy4.setHeightForWidth(self.square_28.sizePolicy().hasHeightForWidth())
        self.square_28.setSizePolicy(sizePolicy4)
        self.square_28.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_29.addWidget(self.square_28)

        self.square_29 = QPushButton(self.table_of_classes)
        self.square_29.setObjectName(u"square_29")
        sizePolicy4.setHeightForWidth(self.square_29.sizePolicy().hasHeightForWidth())
        self.square_29.setSizePolicy(sizePolicy4)
        self.square_29.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_29.addWidget(self.square_29)

        self.square_30 = QPushButton(self.table_of_classes)
        self.square_30.setObjectName(u"square_30")
        sizePolicy4.setHeightForWidth(self.square_30.sizePolicy().hasHeightForWidth())
        self.square_30.setSizePolicy(sizePolicy4)
        self.square_30.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_29.addWidget(self.square_30)


        self.verticalLayout_30.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.pushButton_65 = QPushButton(self.table_of_classes)
        self.pushButton_65.setObjectName(u"pushButton_65")
        sizePolicy4.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy4)
        self.pushButton_65.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_57.addWidget(self.pushButton_65)

        self.square_31 = QPushButton(self.table_of_classes)
        self.square_31.setObjectName(u"square_31")
        sizePolicy4.setHeightForWidth(self.square_31.sizePolicy().hasHeightForWidth())
        self.square_31.setSizePolicy(sizePolicy4)
        self.square_31.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_57.addWidget(self.square_31)

        self.square_32 = QPushButton(self.table_of_classes)
        self.square_32.setObjectName(u"square_32")
        sizePolicy4.setHeightForWidth(self.square_32.sizePolicy().hasHeightForWidth())
        self.square_32.setSizePolicy(sizePolicy4)
        self.square_32.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_57.addWidget(self.square_32)

        self.square_33 = QPushButton(self.table_of_classes)
        self.square_33.setObjectName(u"square_33")
        sizePolicy4.setHeightForWidth(self.square_33.sizePolicy().hasHeightForWidth())
        self.square_33.setSizePolicy(sizePolicy4)
        self.square_33.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_57.addWidget(self.square_33)

        self.square_34 = QPushButton(self.table_of_classes)
        self.square_34.setObjectName(u"square_34")
        sizePolicy4.setHeightForWidth(self.square_34.sizePolicy().hasHeightForWidth())
        self.square_34.setSizePolicy(sizePolicy4)
        self.square_34.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_57.addWidget(self.square_34)

        self.square_35 = QPushButton(self.table_of_classes)
        self.square_35.setObjectName(u"square_35")
        sizePolicy4.setHeightForWidth(self.square_35.sizePolicy().hasHeightForWidth())
        self.square_35.setSizePolicy(sizePolicy4)
        self.square_35.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_57.addWidget(self.square_35)


        self.verticalLayout_30.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_81 = QPushButton(self.table_of_classes)
        self.pushButton_81.setObjectName(u"pushButton_81")
        sizePolicy4.setHeightForWidth(self.pushButton_81.sizePolicy().hasHeightForWidth())
        self.pushButton_81.setSizePolicy(sizePolicy4)
        self.pushButton_81.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_31.addWidget(self.pushButton_81)

        self.square_36 = QPushButton(self.table_of_classes)
        self.square_36.setObjectName(u"square_36")
        sizePolicy4.setHeightForWidth(self.square_36.sizePolicy().hasHeightForWidth())
        self.square_36.setSizePolicy(sizePolicy4)
        self.square_36.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_31.addWidget(self.square_36)

        self.square_37 = QPushButton(self.table_of_classes)
        self.square_37.setObjectName(u"square_37")
        sizePolicy4.setHeightForWidth(self.square_37.sizePolicy().hasHeightForWidth())
        self.square_37.setSizePolicy(sizePolicy4)
        self.square_37.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_31.addWidget(self.square_37)

        self.square_38 = QPushButton(self.table_of_classes)
        self.square_38.setObjectName(u"square_38")
        sizePolicy4.setHeightForWidth(self.square_38.sizePolicy().hasHeightForWidth())
        self.square_38.setSizePolicy(sizePolicy4)
        self.square_38.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_31.addWidget(self.square_38)

        self.square_39 = QPushButton(self.table_of_classes)
        self.square_39.setObjectName(u"square_39")
        sizePolicy4.setHeightForWidth(self.square_39.sizePolicy().hasHeightForWidth())
        self.square_39.setSizePolicy(sizePolicy4)
        self.square_39.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_31.addWidget(self.square_39)

        self.square_40 = QPushButton(self.table_of_classes)
        self.square_40.setObjectName(u"square_40")
        sizePolicy4.setHeightForWidth(self.square_40.sizePolicy().hasHeightForWidth())
        self.square_40.setSizePolicy(sizePolicy4)
        self.square_40.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_31.addWidget(self.square_40)


        self.verticalLayout_30.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_80 = QPushButton(self.table_of_classes)
        self.pushButton_80.setObjectName(u"pushButton_80")
        sizePolicy4.setHeightForWidth(self.pushButton_80.sizePolicy().hasHeightForWidth())
        self.pushButton_80.setSizePolicy(sizePolicy4)
        self.pushButton_80.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_32.addWidget(self.pushButton_80)

        self.square_41 = QPushButton(self.table_of_classes)
        self.square_41.setObjectName(u"square_41")
        sizePolicy4.setHeightForWidth(self.square_41.sizePolicy().hasHeightForWidth())
        self.square_41.setSizePolicy(sizePolicy4)
        self.square_41.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_32.addWidget(self.square_41)

        self.square_42 = QPushButton(self.table_of_classes)
        self.square_42.setObjectName(u"square_42")
        sizePolicy4.setHeightForWidth(self.square_42.sizePolicy().hasHeightForWidth())
        self.square_42.setSizePolicy(sizePolicy4)
        self.square_42.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_32.addWidget(self.square_42)

        self.square_43 = QPushButton(self.table_of_classes)
        self.square_43.setObjectName(u"square_43")
        sizePolicy4.setHeightForWidth(self.square_43.sizePolicy().hasHeightForWidth())
        self.square_43.setSizePolicy(sizePolicy4)
        self.square_43.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_32.addWidget(self.square_43)

        self.square_44 = QPushButton(self.table_of_classes)
        self.square_44.setObjectName(u"square_44")
        sizePolicy4.setHeightForWidth(self.square_44.sizePolicy().hasHeightForWidth())
        self.square_44.setSizePolicy(sizePolicy4)
        self.square_44.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_32.addWidget(self.square_44)

        self.square_45 = QPushButton(self.table_of_classes)
        self.square_45.setObjectName(u"square_45")
        sizePolicy4.setHeightForWidth(self.square_45.sizePolicy().hasHeightForWidth())
        self.square_45.setSizePolicy(sizePolicy4)
        self.square_45.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_32.addWidget(self.square_45)


        self.verticalLayout_30.addLayout(self.horizontalLayout_32)


        self.gridLayout_13.addWidget(self.table_of_classes, 1, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_22 = QPushButton(self.class_table_widget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_23.addWidget(self.pushButton_22)

        self.pushButton_24 = QPushButton(self.class_table_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_23.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.class_table_widget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_23.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.class_table_widget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_23.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.class_table_widget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_23.addWidget(self.pushButton_27)

        self.pushButton_64 = QPushButton(self.class_table_widget)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_23.addWidget(self.pushButton_64)


        self.gridLayout_13.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.class_table_widget, 4, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 3, 0, 1, 2)

        self.widget_14 = QWidget(self.frame_4)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_4.setSpacing(32)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tab3_season_selection = QComboBox(self.widget_14)
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.addItem("")
        self.tab3_season_selection.setObjectName(u"tab3_season_selection")
        self.tab3_season_selection.setMinimumSize(QSize(0, 35))
        self.tab3_season_selection.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.tab3_season_selection)

        self.tab3_yearclass_selection = QComboBox(self.widget_14)
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.addItem("")
        self.tab3_yearclass_selection.setObjectName(u"tab3_yearclass_selection")
        self.tab3_yearclass_selection.setMinimumSize(QSize(0, 35))
        self.tab3_yearclass_selection.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_4.addWidget(self.tab3_yearclass_selection)


        self.gridLayout_12.addWidget(self.widget_14, 0, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)

        self.gridLayout_5.setRowStretch(0, 1)
        self.stackedWidget.addWidget(self.classes_table)
        self.teachers_table = QWidget()
        self.teachers_table.setObjectName(u"teachers_table")
        self.gridLayout_7 = QGridLayout(self.teachers_table)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.teacher_page_frame = QFrame(self.teachers_table)
        self.teacher_page_frame.setObjectName(u"teacher_page_frame")
        self.teacher_page_frame.setMinimumSize(QSize(1150, 600))
        self.teacher_page_frame.setStyleSheet(u"")
        self.teacher_page_frame.setFrameShape(QFrame.StyledPanel)
        self.teacher_page_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.teacher_page_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(40, 40, 40, 40)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 1, 0, 1, 2)

        self.teacher_table_widget = QWidget(self.teacher_page_frame)
        self.teacher_table_widget.setObjectName(u"teacher_table_widget")
        self.teacher_table_widget.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.teacher_table_widget)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.table_of_teacher = QWidget(self.teacher_table_widget)
        self.table_of_teacher.setObjectName(u"table_of_teacher")
        self.verticalLayout_10 = QVBoxLayout(self.table_of_teacher)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_20 = QPushButton(self.table_of_teacher)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy4.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy4)
        self.pushButton_20.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_16.addWidget(self.pushButton_20)

        self.box_1 = QPushButton(self.table_of_teacher)
        self.box_1.setObjectName(u"box_1")
        sizePolicy4.setHeightForWidth(self.box_1.sizePolicy().hasHeightForWidth())
        self.box_1.setSizePolicy(sizePolicy4)
        self.box_1.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_16.addWidget(self.box_1)

        self.box_2 = QPushButton(self.table_of_teacher)
        self.box_2.setObjectName(u"box_2")
        sizePolicy4.setHeightForWidth(self.box_2.sizePolicy().hasHeightForWidth())
        self.box_2.setSizePolicy(sizePolicy4)
        self.box_2.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_16.addWidget(self.box_2)

        self.box_3 = QPushButton(self.table_of_teacher)
        self.box_3.setObjectName(u"box_3")
        sizePolicy4.setHeightForWidth(self.box_3.sizePolicy().hasHeightForWidth())
        self.box_3.setSizePolicy(sizePolicy4)
        self.box_3.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_16.addWidget(self.box_3)

        self.box_4 = QPushButton(self.table_of_teacher)
        self.box_4.setObjectName(u"box_4")
        sizePolicy4.setHeightForWidth(self.box_4.sizePolicy().hasHeightForWidth())
        self.box_4.setSizePolicy(sizePolicy4)
        self.box_4.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_16.addWidget(self.box_4)

        self.box_5 = QPushButton(self.table_of_teacher)
        self.box_5.setObjectName(u"box_5")
        sizePolicy4.setHeightForWidth(self.box_5.sizePolicy().hasHeightForWidth())
        self.box_5.setSizePolicy(sizePolicy4)
        self.box_5.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_16.addWidget(self.box_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_21 = QPushButton(self.table_of_teacher)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy4.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy4)
        self.pushButton_21.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_17.addWidget(self.pushButton_21)

        self.box_6 = QPushButton(self.table_of_teacher)
        self.box_6.setObjectName(u"box_6")
        sizePolicy4.setHeightForWidth(self.box_6.sizePolicy().hasHeightForWidth())
        self.box_6.setSizePolicy(sizePolicy4)
        self.box_6.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_17.addWidget(self.box_6)

        self.box_7 = QPushButton(self.table_of_teacher)
        self.box_7.setObjectName(u"box_7")
        sizePolicy4.setHeightForWidth(self.box_7.sizePolicy().hasHeightForWidth())
        self.box_7.setSizePolicy(sizePolicy4)
        self.box_7.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_17.addWidget(self.box_7)

        self.box_8 = QPushButton(self.table_of_teacher)
        self.box_8.setObjectName(u"box_8")
        sizePolicy4.setHeightForWidth(self.box_8.sizePolicy().hasHeightForWidth())
        self.box_8.setSizePolicy(sizePolicy4)
        self.box_8.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_17.addWidget(self.box_8)

        self.box_9 = QPushButton(self.table_of_teacher)
        self.box_9.setObjectName(u"box_9")
        sizePolicy4.setHeightForWidth(self.box_9.sizePolicy().hasHeightForWidth())
        self.box_9.setSizePolicy(sizePolicy4)
        self.box_9.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_17.addWidget(self.box_9)

        self.box_10 = QPushButton(self.table_of_teacher)
        self.box_10.setObjectName(u"box_10")
        sizePolicy4.setHeightForWidth(self.box_10.sizePolicy().hasHeightForWidth())
        self.box_10.setSizePolicy(sizePolicy4)
        self.box_10.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_17.addWidget(self.box_10)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_23 = QPushButton(self.table_of_teacher)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy4.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy4)
        self.pushButton_23.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_18.addWidget(self.pushButton_23)

        self.box_11 = QPushButton(self.table_of_teacher)
        self.box_11.setObjectName(u"box_11")
        sizePolicy4.setHeightForWidth(self.box_11.sizePolicy().hasHeightForWidth())
        self.box_11.setSizePolicy(sizePolicy4)
        self.box_11.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_18.addWidget(self.box_11)

        self.box_12 = QPushButton(self.table_of_teacher)
        self.box_12.setObjectName(u"box_12")
        sizePolicy4.setHeightForWidth(self.box_12.sizePolicy().hasHeightForWidth())
        self.box_12.setSizePolicy(sizePolicy4)
        self.box_12.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_18.addWidget(self.box_12)

        self.box_13 = QPushButton(self.table_of_teacher)
        self.box_13.setObjectName(u"box_13")
        sizePolicy4.setHeightForWidth(self.box_13.sizePolicy().hasHeightForWidth())
        self.box_13.setSizePolicy(sizePolicy4)
        self.box_13.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_18.addWidget(self.box_13)

        self.box_14 = QPushButton(self.table_of_teacher)
        self.box_14.setObjectName(u"box_14")
        sizePolicy4.setHeightForWidth(self.box_14.sizePolicy().hasHeightForWidth())
        self.box_14.setSizePolicy(sizePolicy4)
        self.box_14.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_18.addWidget(self.box_14)

        self.box_15 = QPushButton(self.table_of_teacher)
        self.box_15.setObjectName(u"box_15")
        sizePolicy4.setHeightForWidth(self.box_15.sizePolicy().hasHeightForWidth())
        self.box_15.setSizePolicy(sizePolicy4)
        self.box_15.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_18.addWidget(self.box_15)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_28 = QPushButton(self.table_of_teacher)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy4.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy4)
        self.pushButton_28.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_19.addWidget(self.pushButton_28)

        self.box_16 = QPushButton(self.table_of_teacher)
        self.box_16.setObjectName(u"box_16")
        sizePolicy4.setHeightForWidth(self.box_16.sizePolicy().hasHeightForWidth())
        self.box_16.setSizePolicy(sizePolicy4)
        self.box_16.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_19.addWidget(self.box_16)

        self.box_17 = QPushButton(self.table_of_teacher)
        self.box_17.setObjectName(u"box_17")
        sizePolicy4.setHeightForWidth(self.box_17.sizePolicy().hasHeightForWidth())
        self.box_17.setSizePolicy(sizePolicy4)
        self.box_17.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_19.addWidget(self.box_17)

        self.box_18 = QPushButton(self.table_of_teacher)
        self.box_18.setObjectName(u"box_18")
        sizePolicy4.setHeightForWidth(self.box_18.sizePolicy().hasHeightForWidth())
        self.box_18.setSizePolicy(sizePolicy4)
        self.box_18.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_19.addWidget(self.box_18)

        self.box_19 = QPushButton(self.table_of_teacher)
        self.box_19.setObjectName(u"box_19")
        sizePolicy4.setHeightForWidth(self.box_19.sizePolicy().hasHeightForWidth())
        self.box_19.setSizePolicy(sizePolicy4)
        self.box_19.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_19.addWidget(self.box_19)

        self.box_20 = QPushButton(self.table_of_teacher)
        self.box_20.setObjectName(u"box_20")
        sizePolicy4.setHeightForWidth(self.box_20.sizePolicy().hasHeightForWidth())
        self.box_20.setSizePolicy(sizePolicy4)
        self.box_20.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_19.addWidget(self.box_20)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_33 = QPushButton(self.table_of_teacher)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy4.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy4)
        self.pushButton_33.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_20.addWidget(self.pushButton_33)

        self.box_21 = QPushButton(self.table_of_teacher)
        self.box_21.setObjectName(u"box_21")
        sizePolicy4.setHeightForWidth(self.box_21.sizePolicy().hasHeightForWidth())
        self.box_21.setSizePolicy(sizePolicy4)
        self.box_21.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_20.addWidget(self.box_21)

        self.box_22 = QPushButton(self.table_of_teacher)
        self.box_22.setObjectName(u"box_22")
        sizePolicy4.setHeightForWidth(self.box_22.sizePolicy().hasHeightForWidth())
        self.box_22.setSizePolicy(sizePolicy4)
        self.box_22.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_20.addWidget(self.box_22)

        self.box_23 = QPushButton(self.table_of_teacher)
        self.box_23.setObjectName(u"box_23")
        sizePolicy4.setHeightForWidth(self.box_23.sizePolicy().hasHeightForWidth())
        self.box_23.setSizePolicy(sizePolicy4)
        self.box_23.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_20.addWidget(self.box_23)

        self.box_24 = QPushButton(self.table_of_teacher)
        self.box_24.setObjectName(u"box_24")
        sizePolicy4.setHeightForWidth(self.box_24.sizePolicy().hasHeightForWidth())
        self.box_24.setSizePolicy(sizePolicy4)
        self.box_24.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_20.addWidget(self.box_24)

        self.box_25 = QPushButton(self.table_of_teacher)
        self.box_25.setObjectName(u"box_25")
        sizePolicy4.setHeightForWidth(self.box_25.sizePolicy().hasHeightForWidth())
        self.box_25.setSizePolicy(sizePolicy4)
        self.box_25.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_20.addWidget(self.box_25)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_53 = QPushButton(self.table_of_teacher)
        self.pushButton_53.setObjectName(u"pushButton_53")
        sizePolicy4.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy4)
        self.pushButton_53.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_21.addWidget(self.pushButton_53)

        self.box_26 = QPushButton(self.table_of_teacher)
        self.box_26.setObjectName(u"box_26")
        sizePolicy4.setHeightForWidth(self.box_26.sizePolicy().hasHeightForWidth())
        self.box_26.setSizePolicy(sizePolicy4)
        self.box_26.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_21.addWidget(self.box_26)

        self.box_27 = QPushButton(self.table_of_teacher)
        self.box_27.setObjectName(u"box_27")
        sizePolicy4.setHeightForWidth(self.box_27.sizePolicy().hasHeightForWidth())
        self.box_27.setSizePolicy(sizePolicy4)
        self.box_27.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_21.addWidget(self.box_27)

        self.box_28 = QPushButton(self.table_of_teacher)
        self.box_28.setObjectName(u"box_28")
        sizePolicy4.setHeightForWidth(self.box_28.sizePolicy().hasHeightForWidth())
        self.box_28.setSizePolicy(sizePolicy4)
        self.box_28.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_21.addWidget(self.box_28)

        self.box_29 = QPushButton(self.table_of_teacher)
        self.box_29.setObjectName(u"box_29")
        sizePolicy4.setHeightForWidth(self.box_29.sizePolicy().hasHeightForWidth())
        self.box_29.setSizePolicy(sizePolicy4)
        self.box_29.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_21.addWidget(self.box_29)

        self.box_30 = QPushButton(self.table_of_teacher)
        self.box_30.setObjectName(u"box_30")
        sizePolicy4.setHeightForWidth(self.box_30.sizePolicy().hasHeightForWidth())
        self.box_30.setSizePolicy(sizePolicy4)
        self.box_30.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_21.addWidget(self.box_30)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_48 = QPushButton(self.table_of_teacher)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy4.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy4)
        self.pushButton_48.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_22.addWidget(self.pushButton_48)

        self.box_31 = QPushButton(self.table_of_teacher)
        self.box_31.setObjectName(u"box_31")
        sizePolicy4.setHeightForWidth(self.box_31.sizePolicy().hasHeightForWidth())
        self.box_31.setSizePolicy(sizePolicy4)
        self.box_31.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_22.addWidget(self.box_31)

        self.box_32 = QPushButton(self.table_of_teacher)
        self.box_32.setObjectName(u"box_32")
        sizePolicy4.setHeightForWidth(self.box_32.sizePolicy().hasHeightForWidth())
        self.box_32.setSizePolicy(sizePolicy4)
        self.box_32.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_22.addWidget(self.box_32)

        self.box_33 = QPushButton(self.table_of_teacher)
        self.box_33.setObjectName(u"box_33")
        sizePolicy4.setHeightForWidth(self.box_33.sizePolicy().hasHeightForWidth())
        self.box_33.setSizePolicy(sizePolicy4)
        self.box_33.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_22.addWidget(self.box_33)

        self.box_34 = QPushButton(self.table_of_teacher)
        self.box_34.setObjectName(u"box_34")
        sizePolicy4.setHeightForWidth(self.box_34.sizePolicy().hasHeightForWidth())
        self.box_34.setSizePolicy(sizePolicy4)
        self.box_34.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_22.addWidget(self.box_34)

        self.box_35 = QPushButton(self.table_of_teacher)
        self.box_35.setObjectName(u"box_35")
        sizePolicy4.setHeightForWidth(self.box_35.sizePolicy().hasHeightForWidth())
        self.box_35.setSizePolicy(sizePolicy4)
        self.box_35.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_22.addWidget(self.box_35)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.pushButton_43 = QPushButton(self.table_of_teacher)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy4.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy4)
        self.pushButton_43.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_37.addWidget(self.pushButton_43)

        self.box_36 = QPushButton(self.table_of_teacher)
        self.box_36.setObjectName(u"box_36")
        sizePolicy4.setHeightForWidth(self.box_36.sizePolicy().hasHeightForWidth())
        self.box_36.setSizePolicy(sizePolicy4)
        self.box_36.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_37.addWidget(self.box_36)

        self.box_37 = QPushButton(self.table_of_teacher)
        self.box_37.setObjectName(u"box_37")
        sizePolicy4.setHeightForWidth(self.box_37.sizePolicy().hasHeightForWidth())
        self.box_37.setSizePolicy(sizePolicy4)
        self.box_37.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_37.addWidget(self.box_37)

        self.box_38 = QPushButton(self.table_of_teacher)
        self.box_38.setObjectName(u"box_38")
        sizePolicy4.setHeightForWidth(self.box_38.sizePolicy().hasHeightForWidth())
        self.box_38.setSizePolicy(sizePolicy4)
        self.box_38.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_37.addWidget(self.box_38)

        self.box_39 = QPushButton(self.table_of_teacher)
        self.box_39.setObjectName(u"box_39")
        sizePolicy4.setHeightForWidth(self.box_39.sizePolicy().hasHeightForWidth())
        self.box_39.setSizePolicy(sizePolicy4)
        self.box_39.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_37.addWidget(self.box_39)

        self.box_40 = QPushButton(self.table_of_teacher)
        self.box_40.setObjectName(u"box_40")
        sizePolicy4.setHeightForWidth(self.box_40.sizePolicy().hasHeightForWidth())
        self.box_40.setSizePolicy(sizePolicy4)
        self.box_40.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_37.addWidget(self.box_40)


        self.verticalLayout_10.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_38 = QPushButton(self.table_of_teacher)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy4.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy4)
        self.pushButton_38.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_38.addWidget(self.pushButton_38)

        self.box_41 = QPushButton(self.table_of_teacher)
        self.box_41.setObjectName(u"box_41")
        sizePolicy4.setHeightForWidth(self.box_41.sizePolicy().hasHeightForWidth())
        self.box_41.setSizePolicy(sizePolicy4)
        self.box_41.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_38.addWidget(self.box_41)

        self.box_42 = QPushButton(self.table_of_teacher)
        self.box_42.setObjectName(u"box_42")
        sizePolicy4.setHeightForWidth(self.box_42.sizePolicy().hasHeightForWidth())
        self.box_42.setSizePolicy(sizePolicy4)
        self.box_42.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_38.addWidget(self.box_42)

        self.box_43 = QPushButton(self.table_of_teacher)
        self.box_43.setObjectName(u"box_43")
        sizePolicy4.setHeightForWidth(self.box_43.sizePolicy().hasHeightForWidth())
        self.box_43.setSizePolicy(sizePolicy4)
        self.box_43.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_38.addWidget(self.box_43)

        self.box_44 = QPushButton(self.table_of_teacher)
        self.box_44.setObjectName(u"box_44")
        sizePolicy4.setHeightForWidth(self.box_44.sizePolicy().hasHeightForWidth())
        self.box_44.setSizePolicy(sizePolicy4)
        self.box_44.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_38.addWidget(self.box_44)

        self.box_45 = QPushButton(self.table_of_teacher)
        self.box_45.setObjectName(u"box_45")
        sizePolicy4.setHeightForWidth(self.box_45.sizePolicy().hasHeightForWidth())
        self.box_45.setSizePolicy(sizePolicy4)
        self.box_45.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_38.addWidget(self.box_45)


        self.verticalLayout_10.addLayout(self.horizontalLayout_38)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 1)
        self.verticalLayout_10.setStretch(3, 1)
        self.verticalLayout_10.setStretch(4, 1)
        self.verticalLayout_10.setStretch(5, 1)
        self.verticalLayout_10.setStretch(6, 1)
        self.verticalLayout_10.setStretch(7, 1)
        self.verticalLayout_10.setStretch(8, 1)

        self.gridLayout_9.addWidget(self.table_of_teacher, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_15 = QPushButton(self.teacher_table_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_15.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.teacher_table_widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_15.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.teacher_table_widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_15.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.teacher_table_widget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_15.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.teacher_table_widget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_15.addWidget(self.pushButton_19)

        self.pushButton_63 = QPushButton(self.teacher_table_widget)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_15.addWidget(self.pushButton_63)


        self.gridLayout_9.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.teacher_table_widget, 4, 0, 1, 2)

        self.widget_15 = QWidget(self.teacher_page_frame)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.widget_15.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_7.setSpacing(32)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tab2_season_selection = QComboBox(self.widget_15)
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.addItem("")
        self.tab2_season_selection.setObjectName(u"tab2_season_selection")
        self.tab2_season_selection.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_7.addWidget(self.tab2_season_selection)

        self.tab2_teacher_selection = QComboBox(self.widget_15)
        self.tab2_teacher_selection.setObjectName(u"tab2_teacher_selection")
        self.tab2_teacher_selection.setMinimumSize(QSize(0, 35))
        self.tab2_teacher_selection.setLayoutDirection(Qt.RightToLeft)
        self.tab2_teacher_selection.setDuplicatesEnabled(False)
        self.tab2_teacher_selection.setFrame(True)

        self.horizontalLayout_7.addWidget(self.tab2_teacher_selection)


        self.gridLayout_8.addWidget(self.widget_15, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.teacher_page_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.teachers_table)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_14 = QGridLayout(self.page)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_2)
        self.gridLayout_16.setSpacing(20)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(40, 40, 40, 40)
        self.widget_16 = QWidget(self.frame_2)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_15 = QGridLayout(self.widget_16)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(10, 10, 10, 10)
        self.horizontalSlider_2 = QSlider(self.widget_16)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.horizontalSlider_2, 3, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.widget_16)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_15.addWidget(self.pushButton_3, 5, 0, 1, 1)

        self.horizontalSlider_3 = QSlider(self.widget_16)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.horizontalSlider_3, 4, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.widget_16)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_15.addWidget(self.pushButton_2, 5, 1, 1, 1)

        self.horizontalSlider = QSlider(self.widget_16)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.widget_16)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_15.addWidget(self.lineEdit_2, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(self.widget_16)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_15.addWidget(self.lineEdit, 0, 0, 1, 2)


        self.gridLayout_16.addWidget(self.widget_16, 0, 1, 1, 1)

        self.widget_17 = QWidget(self.frame_2)
        self.widget_17.setObjectName(u"widget_17")

        self.gridLayout_16.addWidget(self.widget_17, 1, 1, 1, 1)

        self.widget_18 = QWidget(self.frame_2)
        self.widget_18.setObjectName(u"widget_18")
        self.gridLayout_17 = QGridLayout(self.widget_18)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(10, 10, 10, 10)
        self.tableWidget = QTableWidget(self.widget_18)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_17.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_18, 0, 0, 2, 1)

        self.gridLayout_16.setRowStretch(0, 1)
        self.gridLayout_16.setRowStretch(1, 1)
        self.gridLayout_16.setColumnStretch(0, 1)
        self.gridLayout_16.setColumnStretch(1, 1)

        self.gridLayout_14.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.main_widget)

        self.footer = QWidget(self.widget_12)
        self.footer.setObjectName(u"footer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy5)
        self.footer.setMinimumSize(QSize(0, 20))
        self.footer.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_39 = QHBoxLayout(self.footer)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.footer)
        self.widget_4.setObjectName(u"widget_4")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 131, 16))

        self.horizontalLayout_39.addWidget(self.widget_4)

        self.widget_10 = QWidget(self.footer)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_40 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_40.addWidget(self.label_4)

        self.size_grip_widget = QWidget(self.widget_10)
        self.size_grip_widget.setObjectName(u"size_grip_widget")
        self.size_grip_widget.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_40.addWidget(self.size_grip_widget)


        self.horizontalLayout_39.addWidget(self.widget_10)


        self.verticalLayout_3.addWidget(self.footer)


        self.gridLayout.addWidget(self.widget_12, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.the_main_bloc, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_extend.setText("")
        self.btn_all.setText("")
        self.btn_classes.setText("")
        self.btn_teachers.setText("")
        self.btn_edit_teachers.setText("")
        self.btn_save.setText("")
        self.btn_settings.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"class reservation system", None))
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_close.setText("")
        self.season_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"2020 | S1", None))
        self.season_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"2020 | S2", None))
        self.season_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"2020 | S3", None))
        self.season_selection.setItemText(3, QCoreApplication.translate("MainWindow", u"2021 | S1", None))
        self.season_selection.setItemText(4, QCoreApplication.translate("MainWindow", u"2021 | S2", None))
        self.season_selection.setItemText(5, QCoreApplication.translate("MainWindow", u"2021 | S3", None))
        self.season_selection.setItemText(6, QCoreApplication.translate("MainWindow", u"2022 | S1", None))
        self.season_selection.setItemText(7, QCoreApplication.translate("MainWindow", u"2022 | S2", None))
        self.season_selection.setItemText(8, QCoreApplication.translate("MainWindow", u"2022 | S3", None))

        self.grade_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"grade 1", None))
        self.grade_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"grade 2", None))
        self.grade_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"grade 3", None))
        self.grade_selection.setItemText(3, QCoreApplication.translate("MainWindow", u"grade 4", None))
        self.grade_selection.setItemText(4, QCoreApplication.translate("MainWindow", u"grade 5", None))

        self.pushButton.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"sunday", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"monday", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"tuesday", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"wednesday", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"thursday", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"8:00 - 9:00", None))
        self.add_cell_1.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_2.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_3.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_4.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_5.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_92.setText(QCoreApplication.translate("MainWindow", u"9:00 - 10:00", None))
        self.add_cell_6.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_7.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_8.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_9.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_10.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_93.setText(QCoreApplication.translate("MainWindow", u"10:00 - 11:00", None))
        self.add_cell_11.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_12.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_13.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_14.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_15.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_123.setText(QCoreApplication.translate("MainWindow", u"11:00 - 12:00", None))
        self.add_cell_16.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_17.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_18.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_19.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_20.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_129.setText(QCoreApplication.translate("MainWindow", u"BREAK", None))
        self.add_cell_21.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_22.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_23.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_24.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_25.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_135.setText(QCoreApplication.translate("MainWindow", u"13:30 - 14:30", None))
        self.add_cell_26.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_27.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_28.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_29.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_30.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_147.setText(QCoreApplication.translate("MainWindow", u"14:30 - 15:30", None))
        self.add_cell_31.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_32.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_33.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_34.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_35.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_141.setText(QCoreApplication.translate("MainWindow", u"15:30 - 16:30", None))
        self.add_cell_36.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_37.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_38.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_39.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_40.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_153.setText(QCoreApplication.translate("MainWindow", u"14:30 - 17:30", None))
        self.add_cell_41.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_42.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_43.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_44.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.add_cell_45.setText(QCoreApplication.translate("MainWindow", u"add session", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"8:00 - 9:00", None))
        self.square_1.setText("")
        self.square_2.setText("")
        self.square_3.setText("")
        self.square_4.setText("")
        self.square_5.setText("")
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"9:00 - 10:00", None))
        self.square_6.setText("")
        self.square_7.setText("")
        self.square_8.setText("")
        self.square_9.setText("")
        self.square_10.setText("")
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"10:00 - 11:00", None))
        self.square_11.setText("")
        self.square_12.setText("")
        self.square_13.setText("")
        self.square_14.setText("")
        self.square_15.setText("")
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"11:00 - 12:00", None))
        self.square_16.setText("")
        self.square_17.setText("")
        self.square_18.setText("")
        self.square_19.setText("")
        self.square_20.setText("")
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"BREAK", None))
        self.square_21.setText("")
        self.square_22.setText("")
        self.square_23.setText("")
        self.square_24.setText("")
        self.square_25.setText("")
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"13:30 - 14:30", None))
        self.square_26.setText("")
        self.square_27.setText("")
        self.square_28.setText("")
        self.square_29.setText("")
        self.square_30.setText("")
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"14:30 - 15:30", None))
        self.square_31.setText("")
        self.square_32.setText("")
        self.square_33.setText("")
        self.square_34.setText("")
        self.square_35.setText("")
        self.pushButton_81.setText(QCoreApplication.translate("MainWindow", u"15:30 - 16:30", None))
        self.square_36.setText("")
        self.square_37.setText("")
        self.square_38.setText("")
        self.square_39.setText("")
        self.square_40.setText("")
        self.pushButton_80.setText(QCoreApplication.translate("MainWindow", u"14:30 - 17:30", None))
        self.square_41.setText("")
        self.square_42.setText("")
        self.square_43.setText("")
        self.square_44.setText("")
        self.square_45.setText("")
        self.pushButton_22.setText("")
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"sunday", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"monday", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"tuesday", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"wednesday", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"thursday", None))
        self.tab3_season_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"2020 | S1", None))
        self.tab3_season_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"2020 | S2", None))
        self.tab3_season_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"2020 | S3", None))
        self.tab3_season_selection.setItemText(3, QCoreApplication.translate("MainWindow", u"2021 |  S1", None))
        self.tab3_season_selection.setItemText(4, QCoreApplication.translate("MainWindow", u"2021 |  S2", None))
        self.tab3_season_selection.setItemText(5, QCoreApplication.translate("MainWindow", u"2021 |  S3", None))
        self.tab3_season_selection.setItemText(6, QCoreApplication.translate("MainWindow", u"2022 |  S1", None))
        self.tab3_season_selection.setItemText(7, QCoreApplication.translate("MainWindow", u"2022 |  S2", None))
        self.tab3_season_selection.setItemText(8, QCoreApplication.translate("MainWindow", u"2022 |  S3", None))

        self.tab3_yearclass_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"grade 1 | class 1", None))
        self.tab3_yearclass_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"grade 1 | class 2", None))
        self.tab3_yearclass_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"grade 1 | class 3", None))
        self.tab3_yearclass_selection.setItemText(3, QCoreApplication.translate("MainWindow", u"grade 1 | class 4", None))
        self.tab3_yearclass_selection.setItemText(4, QCoreApplication.translate("MainWindow", u"grade 1 | class 5", None))
        self.tab3_yearclass_selection.setItemText(5, QCoreApplication.translate("MainWindow", u"grade 2 | class 1", None))
        self.tab3_yearclass_selection.setItemText(6, QCoreApplication.translate("MainWindow", u"grade 2 | class 2", None))
        self.tab3_yearclass_selection.setItemText(7, QCoreApplication.translate("MainWindow", u"grade 2 | class 3", None))
        self.tab3_yearclass_selection.setItemText(8, QCoreApplication.translate("MainWindow", u"grade 2 | class 4", None))
        self.tab3_yearclass_selection.setItemText(9, QCoreApplication.translate("MainWindow", u"grade 2 | class 5", None))
        self.tab3_yearclass_selection.setItemText(10, QCoreApplication.translate("MainWindow", u"grade 3 | class 1", None))
        self.tab3_yearclass_selection.setItemText(11, QCoreApplication.translate("MainWindow", u"grade 3 | class 2", None))
        self.tab3_yearclass_selection.setItemText(12, QCoreApplication.translate("MainWindow", u"grade 3 | class 3", None))
        self.tab3_yearclass_selection.setItemText(13, QCoreApplication.translate("MainWindow", u"grade 3 | class 4", None))
        self.tab3_yearclass_selection.setItemText(14, QCoreApplication.translate("MainWindow", u"grade 3 | class 5", None))
        self.tab3_yearclass_selection.setItemText(15, QCoreApplication.translate("MainWindow", u"grade 4 | class 1", None))
        self.tab3_yearclass_selection.setItemText(16, QCoreApplication.translate("MainWindow", u"grade 4 | class 2", None))
        self.tab3_yearclass_selection.setItemText(17, QCoreApplication.translate("MainWindow", u"grade 4 | class 3", None))
        self.tab3_yearclass_selection.setItemText(18, QCoreApplication.translate("MainWindow", u"grade 4 | class 4", None))
        self.tab3_yearclass_selection.setItemText(19, QCoreApplication.translate("MainWindow", u"grade 4 | class 5", None))

        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"8:00 - 9:00", None))
        self.box_1.setText("")
        self.box_2.setText("")
        self.box_3.setText("")
        self.box_4.setText("")
        self.box_5.setText("")
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"9:00 - 10:00", None))
        self.box_6.setText("")
        self.box_7.setText("")
        self.box_8.setText("")
        self.box_9.setText("")
        self.box_10.setText("")
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"10:00 - 11:00", None))
        self.box_11.setText("")
        self.box_12.setText("")
        self.box_13.setText("")
        self.box_14.setText("")
        self.box_15.setText("")
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"11:00 - 12:00", None))
        self.box_16.setText("")
        self.box_17.setText("")
        self.box_18.setText("")
        self.box_19.setText("")
        self.box_20.setText("")
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"BREAK", None))
        self.box_21.setText("")
        self.box_22.setText("")
        self.box_23.setText("")
        self.box_24.setText("")
        self.box_25.setText("")
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"13:30 - 14:30", None))
        self.box_26.setText("")
        self.box_27.setText("")
        self.box_28.setText("")
        self.box_29.setText("")
        self.box_30.setText("")
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"14:30 - 15:30", None))
        self.box_31.setText("")
        self.box_32.setText("")
        self.box_33.setText("")
        self.box_34.setText("")
        self.box_35.setText("")
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"15:30 - 16:30", None))
        self.box_36.setText("")
        self.box_37.setText("")
        self.box_38.setText("")
        self.box_39.setText("")
        self.box_40.setText("")
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"14:30 - 17:30", None))
        self.box_41.setText("")
        self.box_42.setText("")
        self.box_43.setText("")
        self.box_44.setText("")
        self.box_45.setText("")
        self.pushButton_15.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"sunday", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"monday", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"tuesday", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"wednesday", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"thursday", None))
        self.tab2_season_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"2020 | S1", None))
        self.tab2_season_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"2020 | S2", None))
        self.tab2_season_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"2020 | S3", None))
        self.tab2_season_selection.setItemText(3, QCoreApplication.translate("MainWindow", u"2021 | S1", None))
        self.tab2_season_selection.setItemText(4, QCoreApplication.translate("MainWindow", u"2021 | S2", None))
        self.tab2_season_selection.setItemText(5, QCoreApplication.translate("MainWindow", u"2021 | S3", None))
        self.tab2_season_selection.setItemText(6, QCoreApplication.translate("MainWindow", u"2022 | S1", None))
        self.tab2_season_selection.setItemText(7, QCoreApplication.translate("MainWindow", u"2021 | S2", None))
        self.tab2_season_selection.setItemText(8, QCoreApplication.translate("MainWindow", u"2021 | S3", None))

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"subject", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"actions", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"   made by ilyes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"             V 1.0.0", None))
    # retranslateUi

