import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.sentences = []
        self.sentences_2 = []
        self.fluents = []
        self.actions = []
        self.agents = []
        self.query = []

        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1147, 834)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1141, 801))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayoutWidget = QWidget(self.page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1141, 791))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_3, 6, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_6, 7, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayoutWidget_1 = QWidget(self.page_1)
        self.gridLayoutWidget_1.setObjectName(u"gridLayoutWidget_1")
        self.gridLayoutWidget_1.setGeometry(QRect(0, 0, 1141, 801))
        self.gridLayout_1 = QGridLayout(self.gridLayoutWidget_1)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        font1 = QFont()
        font1.setPointSize(12)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_6, 5, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.gridLayout_1.addWidget(self.label_14, 1, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gridLayout_1.addItem(self.verticalSpacer_14, 2, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.gridLayout_1.addWidget(self.label_11, 3, 1, 1, 1)

        self.LineEdit_1 = QLineEdit(self.gridLayoutWidget_1)
        self.LineEdit_1.setObjectName(u"LineEdit_1")
        self.gridLayout_1.addWidget(self.LineEdit_1, 4, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_1)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.gridLayout_1.addWidget(self.pushButton_11, 5, 1, 1, 1)

        self.textBrowser_5 = QListWidget(self.gridLayoutWidget_1)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.gridLayout_1.addWidget(self.textBrowser_5, 6, 1, 1, 1)

        self.pushButton_21 = QPushButton(self.gridLayoutWidget_1)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.gridLayout_1.addWidget(self.pushButton_21, 7, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gridLayout_1.addItem(self.verticalSpacer_11, 8, 1, 1, 1)


        self.label_12 = QLabel(self.gridLayoutWidget_1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.gridLayout_1.addWidget(self.label_12, 9, 1, 1, 1)

        self.LineEdit_2 = QLineEdit(self.gridLayoutWidget_1)
        self.LineEdit_2.setObjectName(u"LineEdit_2")
        self.gridLayout_1.addWidget(self.LineEdit_2, 10, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget_1)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.gridLayout_1.addWidget(self.pushButton_12, 11, 1, 1, 1)

        self.textBrowser_6 = QListWidget(self.gridLayoutWidget_1)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.gridLayout_1.addWidget(self.textBrowser_6, 12, 1, 1, 1)
    
        self.pushButton_22 = QPushButton(self.gridLayoutWidget_1)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.gridLayout_1.addWidget(self.pushButton_22, 13, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gridLayout_1.addItem(self.verticalSpacer_12, 14, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.gridLayout_1.addWidget(self.label_13, 15, 1, 1, 1)

        self.LineEdit_3 = QLineEdit(self.gridLayoutWidget_1)
        self.LineEdit_3.setObjectName(u"LineEdit_3")
        self.gridLayout_1.addWidget(self.LineEdit_3, 16, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget_1)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.gridLayout_1.addWidget(self.pushButton_13, 17, 1, 1, 1)

        self.textBrowser_7 = QListWidget(self.gridLayoutWidget_1)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.gridLayout_1.addWidget(self.textBrowser_7, 18, 1, 1, 1)

        self.pushButton_23 = QPushButton(self.gridLayoutWidget_1)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.gridLayout_1.addWidget(self.pushButton_23, 19, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gridLayout_1.addItem(self.verticalSpacer_13, 20, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget_1)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.gridLayout_1.addWidget(self.pushButton_10, 21, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayoutWidget_2 = QWidget(self.page_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1141, 801))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 4, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 0, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 14, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 8, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.fields_container = QWidget(self.gridLayoutWidget_2)
        self.fields_container.setObjectName(u"fields_container")

        self.fields_layout = QFormLayout()
        self.fields_container.setLayout(self.fields_layout)

        self.gridLayout_2.addWidget(self.fields_container, 6, 1, 1, 1)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 7, 1, 1, 1)


        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 5, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 13, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 9, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 12, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 11, 1, 1, 1)

        self.textBrowser = QListWidget(self.gridLayoutWidget_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 10, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayoutWidget_3 = QWidget(self.page_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 1141, 761))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_13, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_3.addWidget(self.pushButton_6, 21, 1, 1, 1)


        self.comboBox_2 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 5, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_3.addWidget(self.comboBox_4, 10, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_3.addWidget(self.pushButton_7, 8, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)


        self.fields_container_2 = QWidget(self.gridLayoutWidget_3)
        self.fields_container_2.setObjectName(u"fields_container_2")
        self.fields_layout_2 = QFormLayout()

        self.fields_container_2.setLayout(self.fields_layout_2)
        self.gridLayout_3.addWidget(self.fields_container_2, 6, 1, 1, 1)

        self.textBrowser_3 = QLineEdit(self.gridLayoutWidget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.gridLayout_3.addWidget(self.textBrowser_3, 7, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_3.addWidget(self.label_10, 9, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_3.addWidget(self.pushButton_8, 13, 1, 1, 1)

        self.fields_container_3 = QWidget(self.gridLayoutWidget_3)
        self.fields_container_3.setObjectName(u"fields_container_3")
        self.fields_layout_3 = QFormLayout()

        self.fields_container_3.setLayout(self.fields_layout_3)
        self.gridLayout_3.addWidget(self.fields_container_3, 11, 1, 1, 1)

        self.textBrowser_2 = QListWidget(self.gridLayoutWidget_3)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.gridLayout_3.addWidget(self.textBrowser_2, 16, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_3.addWidget(self.pushButton_9, 17, 1, 1, 1)


        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_12, 3, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_3.addWidget(self.label_9, 4, 1, 1, 1)


        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayoutWidget_4 = QWidget(self.page_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 1141, 801))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        font1 = QFont()
        font1.setPointSize(12)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_20, 1, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 1, 1, 1, 1)


        self.label_20 = QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_20, 2, 1, 1, 1)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 3, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.gridLayout_4.addWidget(self.label_21, 4, 1, 1, 1)


        self.textBrowser_world = QListWidget(self.gridLayoutWidget_4)
        self.textBrowser_world.setObjectName(u"textBrowser_world")
        self.gridLayout_4.addWidget(self.textBrowser_world, 6, 1, 1, 1)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 7, 1, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.gridLayout_4.addWidget(self.label_22, 8, 1, 1, 1)


        self.textBrowser_program = QListWidget(self.gridLayoutWidget_4)
        self.textBrowser_program.setObjectName(u"textBrowser_program")
        self.gridLayout_4.addWidget(self.textBrowser_program, 10, 1, 1, 1)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 11, 1, 1, 1)


        self.label_23 = QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_4.addWidget(self.label_23, 12, 1, 1, 1)


        self.textBrowser_query = QLineEdit(self.gridLayoutWidget_4)
        self.textBrowser_query.setObjectName(u"textBrowser_query")
        self.gridLayout_4.addWidget(self.textBrowser_query, 14, 1, 1, 1)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 15, 1, 1, 1)


        self.label_24 = QLabel(self.gridLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.gridLayout_4.addWidget(self.label_24, 16, 1, 1, 1)


        self.textBrowser_result = QLineEdit(self.gridLayoutWidget_4)
        self.textBrowser_result.setObjectName(u"textBrowser_result")
        self.gridLayout_4.addWidget(self.textBrowser_result, 18, 1, 1, 1)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 19, 1, 1, 1)


        self.pushButton_20 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_4.addWidget(self.pushButton_20, 20, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1147, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

        #Value statement
        ##1
        self.comboBox.addItem("[fluent1] [linking] [fluent2] after [action1]")
        ##2
        self.comboBox.addItem("observable [fluent1] [linking] [fluent2] after [action1]")
        ##3
        self.comboBox.addItem("initially [fluent1] [linking] [fluent2]")

        #Effect statement
        ##1
        self.comboBox.addItem("[action] by [agent] causes [fluent1] [linking] [fluent2] if [fluent3] [linking2] [fluent4]")
        ##2
        self.comboBox.addItem("[action] by [agent] causes [fluent1] [linking] [fluent2]")
        ##3
        self.comboBox.addItem("impossible [action] by [agent] if [fluent1] [linking] [fluent2]")


        #Release statement
        ##1
        self.comboBox.addItem("[action] by [agent] releases [fluent1] if [fluent3] [linking2] [fluent4]")
        ##2
        self.comboBox.addItem("[action] by [agent] releases [fluent1]")
        #Constraint statement
        ##1
        self.comboBox.addItem("always [fluent1] [linking1] [fluent2]")

        # self.comboBox.addItem("[formula] after [action,action...]")
        self.comboBox.currentIndexChanged.connect(self.update_template)
        self.comboBox.setCurrentIndex(-1)
        self.empty_fields = []
        self.field_names = []

        #Value query
        self.comboBox_2.addItem("necessary [fluent1] [linking1] [fluent2] after program")
        self.comboBox_2.addItem("possibly [fluent1] [linking1] [fluent2] after program")
        #Realizability query
        self.comboBox_2.addItem("program realizable always")
        self.comboBox_2.addItem("program realizable ever")
        #Activity query
        self.comboBox_2.addItem("active [agent] in program ")
 
        self.comboBox_2.currentIndexChanged.connect(self.update_template_2)
        self.comboBox_2.setCurrentIndex(-1)
        self.empty_fields_2 = []
        self.field_names_2 = []

        self.comboBox_4.addItem("[agent] [action]")
        self.comboBox_4.setCurrentIndex(-1)
        self.comboBox_4.currentIndexChanged.connect(self.update_template_3)
        self.empty_fields_3 = []
        self.field_names_3 = []


        self.pushButton.clicked.connect(self.clicked_switch_to_initial_page)
        self.pushButton_5.clicked.connect(self.clicked_add_sentence)
        self.pushButton_2.clicked.connect(self.clicked_remove_sentence)
        self.pushButton_4.clicked.connect(self.clicked_switch_to_query_page)
        self.pushButton_7.clicked.connect(self.clicked_add_sentence_2)
        self.pushButton_8.clicked.connect(self.clicked_add_sentence_3)
        self.pushButton_3.clicked.connect(self.clicked_exit_app)
        self.pushButton_6.clicked.connect(self.clicked_switch_to_results_page)
        self.pushButton_9.clicked.connect(self.clicked_remove_sentence_2)
        self.pushButton_10.clicked.connect(self.clicked_switch_to_add_world_definition)
        self.pushButton_11.clicked.connect(self.clicked_add_sentence_4)
        self.pushButton_12.clicked.connect(self.clicked_add_sentence_5)
        self.pushButton_13.clicked.connect(self.clicked_add_sentence_6)
        self.pushButton_6.clicked.connect(self.clicked_query_results)
        self.pushButton_20.clicked.connect(self.clicked_exit_app)
        self.pushButton_21.clicked.connect(self.clicked_remove_fluent)
        self.pushButton_22.clicked.connect(self.clicked_remove_agent)
        self.pushButton_23.clicked.connect(self.clicked_remove_action)


    def clicked_switch_to_add_world_definition(self):
        self.stackedWidget.setCurrentIndex(2)


    def clicked_switch_to_results_page(self):

        self.textBrowser_world.addItems(self.sentences)
        self.textBrowser_program.addItems(self.sentences_2)
        self.textBrowser_query.setText(str(self.query[-1]))
        

        self.stackedWidget.setCurrentIndex(4)

    def clicked_exit_app(self):
        app.quit()
    
    def clicked_exit_app(self):
        app.quit()

    def clicked_remove_sentence(self):
        selected_item = self.textBrowser.currentItem()
        if selected_item:
            sentence = selected_item.text()
            self.sentences.remove(sentence)
            self.textBrowser.takeItem(self.textBrowser.row(selected_item))
    
    def clicked_remove_sentence_2(self):
        selected_item = self.textBrowser_2.currentItem()
        if selected_item:
            sentence = selected_item.text()
            self.sentences_2.remove(sentence)
            self.textBrowser_2.takeItem(self.textBrowser_2.row(selected_item))

    def clicked_switch_to_query_page(self):
        self.stackedWidget.setCurrentIndex(3)
        import copy
                        #{0 : [[strzelba_naladowana,kurczak_zyje], [strzelba_naladowana,!kurczak_zyje]],
                        # 1: [[strzelba_naladowana,kurczak_zyje], [strzelba_naladowana,!kurczak_zyje]]}
        states = {0:[[]]} # [[strzelba_naladowana,kurczak_zyje], [strzelba_naladowana,!kurczak_zyje]]
        # fluents = ["strzelba_naladowana", "kurczak_zyje", "slonce_swieci"]
        fluents = self.fluents
        agents = self.agents
        agents_actions = {}
        actions_conditions = {}#klucz: agent,akcja value: [precon, postcon]
                                #agents_actions = {"strzelec":["laduje","strzela"]}
                                #actions_conditions = {(strzelec,strzela,): [[["!strzelba_naladowana"],["ma dodatkowe ammo"]],["stzelba_naladowana"]],
                                                    #"strzelec_strzela": [["strzelba_naladowana"],["!kurczak_zyje"]]}
        agents_actions_impossible = {}
        actions_conditions_impossible = {}
        agents_actions_releases = {}
        actions_conditions_releases = {}
        after_sequences={}#(A1,A2,A3):[[formula, fromula1], [formula,formula2]],(A1,A2,A4):[formula]
        after_observable_sequences = {}
        statments = {"initial_fluents":[[]], #["kurczak_zyje", "strzelba_naladowana"],["!kurczak_zyje","strzelba_naladowana"],[]
                    "always":[[]]}

        # sequences = ["initially kurczak_zyje",
        #              "initially slonce_swieci",
        #               "strzal by strzelec releases !kurczak_zyje if kurczak_zyje",
        #               "strzal by strzelec causes !strzelba_naladowana if kurczak_zyje",
        #               "impossible strzal by strzelec if !strzelba_naladowana",
        #               "przeladowanie by strzelec causes strzelba_naladowana if !strzelba_naladowana",
        #             #   "always kurczak_zyje",
        #              "!slonce_swieci after strzal, przeladowanie, strzal"
        #               ]

        sequences = self.sentences

        for j,i in enumerate(fluents):
            i = i.replace("  "," ")
            i = i.replace("  "," ")
            if i[-1]==" ":
                i = i[:-1]
            fluents[j] = i

        for j,i in enumerate(sequences):
            i = i.replace("  "," ")
            print(i)
            i = i.replace("  "," ")
            print(i)
            if i[-1]==" ":
                i = i[:-1]
            sequences[j] = i
            print(sequences[j])

        self.historical_actions =[]

        for seq in sequences:
            if "initially" in seq:#done
                seq = seq[len("initially")+1:]
                if "or" in seq:
                    seq1, seq2 = seq.split(" or ")
                    copied = copy.deepcopy(statments["initial_fluents"])
                    statments["initial_fluents"] = statments["initial_fluents"] + copied
                    for i in range(len(statments["initial_fluents"])):
                        if i<len(copied):
                            statments["initial_fluents"][i].append(seq1)
                        else:
                            statments["initial_fluents"][i].append(seq2)
                elif "and" in seq:
                    seq1, seq2 = seq.split(" and ")
                    for i in range(len(statments["initial_fluents"])):  
                        statments["initial_fluents"][i].append(seq1)
                        statments["initial_fluents"][i].append(seq2)
                else:
                    for i in range(len(statments["initial_fluents"])):  
                        statments["initial_fluents"][i].append(seq)

            elif "observable" in seq:
                seq = seq[len("observable")+1:]
                seq1, seq2 = seq.split(" after ")
                actions_ = tuple(seq2.split(", "))
                if not actions_ in after_observable_sequences.keys():
                    after_observable_sequences[actions_] = [[]]
                if "or" in seq1:
                    seq11, seq21 = seq1.split(" or ")
                    copied = copy.deepcopy(after_observable_sequences[actions_])
                    after_observable_sequences[actions_] = after_observable_sequences[actions_] + copied
                    for i in range(len(after_observable_sequences[actions_])):
                        if i<len(copied):
                            after_observable_sequences[actions_][i].append(seq11)
                        else:
                            after_observable_sequences[actions_][i].append(seq21)
                elif "and" in seq1:
                    seq11, seq21 = seq1.split(" and ")
                    for i in range(len(after_observable_sequences[actions_])):  
                        after_observable_sequences[actions_][i].append(seq11)
                        after_observable_sequences[actions_][i].append(seq21)
                else:
                    for i in range(len(after_observable_sequences[actions_])):  
                        after_observable_sequences[actions_][i].append(seq1)    
            elif "after" in seq:
                seq1, seq2 = seq.split(" after ")
                actions_ = tuple(seq2.split(", "))
                if not actions_ in after_sequences.keys():
                    after_sequences[actions_] = [[]]
                if "or" in seq1:
                    seq11, seq21 = seq1.split(" or ")
                    copied = copy.deepcopy(after_sequences[actions_])
                    after_sequences[actions_] = after_sequences[actions_] + copied
                    for i in range(len(after_sequences[actions_])):
                        if i<len(copied):
                            after_sequences[actions_][i].append(seq11)
                        else:
                            after_sequences[actions_][i].append(seq21)
                elif "and" in seq1:
                    seq11, seq21 = seq1.split(" and ")
                    for i in range(len(after_sequences[actions_])):  
                        after_sequences[actions_][i].append(seq11)
                        after_sequences[actions_][i].append(seq21)
                else:
                    for i in range(len(after_sequences[actions_])):  
                        after_sequences[actions_][i].append(seq1)    
            elif "causes" in seq:
                seq4 = None
                seq1, seqrest = seq.split(" by ")
                seq2, seqrest = seqrest.split(" causes ")
                if "if" in seqrest:
                    seq3,seq4 = seqrest.split(" if ")
                else:
                    seq3 = seqrest
                if not (seq2,seq1) in agents_actions.keys():
                    agents_actions[seq2] = []
                    actions_conditions[(seq2,seq1)] = [[[]],[[]]]
                agents_actions[seq2].append(seq1)
                #actions_conditions[(seq2,seq1)]
                
                #done
                if "or" in seq3:
                    seq31, seq32 = seq3.split(" or ")
                    copied = copy.deepcopy(actions_conditions[(seq2,seq1)][1])
                    actions_conditions[(seq2,seq1)][1] = actions_conditions[(seq2,seq1)][1] + copied
                    for i in range(len(actions_conditions[(seq2,seq1)][1])):
                        if i<len(copied):
                            actions_conditions[(seq2,seq1)][1][i].append(seq31)
                        else:
                            actions_conditions[(seq2,seq1)][1][i].append(seq32)
                elif "and" in seq3:
                    seq31, seq32 = seq3.split(" and ")
                    for i in range(len(actions_conditions[(seq2,seq1)][1])):  
                        actions_conditions[(seq2,seq1)][1][i].append(seq31)
                        actions_conditions[(seq2,seq1)][1][i].append(seq32)
                else:
                    for i in range(len(actions_conditions[(seq2,seq1)][1])):  
                        actions_conditions[(seq2,seq1)][1][i].append(seq3)

                if not seq4==None:
                    if "or" in seq4:
                        seq41, seq42 = seq4.split(" or ")
                        copied = copy.deepcopy(actions_conditions[(seq2,seq1)][0])
                        actions_conditions[(seq2,seq1)][0] = actions_conditions[(seq2,seq1)][0] + copied
                        for i in range(len(actions_conditions[(seq2,seq1)][0])):
                            if i<len(copied):
                                actions_conditions[(seq2,seq1)][0][i].append(seq41)
                            else:
                                actions_conditions[(seq2,seq1)][0][i].append(seq42)
                    elif "and" in seq4:
                        seq41, seq42 = seq4.split(" and ")
                        for i in range(len(actions_conditions[(seq2,seq1)][0])):  
                            actions_conditions[(seq2,seq1)][0][i].append(seq41)
                            actions_conditions[(seq2,seq1)][0][i].append(seq42)
                    else:
                        for i in range(len(actions_conditions[(seq2,seq1)][0])):  
                            actions_conditions[(seq2,seq1)][0][i].append(seq4)

            elif "impossible" in seq:
                seq = seq.split("impossible ")[1]
                seq1, seqrest = seq.split(" by ")
                seq2, seq3 = seqrest.split(" if ")
                if not (seq2,seq1) in agents_actions_impossible.keys():
                    agents_actions_impossible[seq2] = []
                    actions_conditions_impossible[(seq2,seq1)] = [[[]],[[]]]
                agents_actions_impossible[seq2].append(seq1)
                
                #done
                if "or" in seq3:
                    seq31, seq32 = seq3.split(" or ")
                    copied = copy.deepcopy(actions_conditions_impossible[(seq2,seq1)][0])
                    actions_conditions_impossible[(seq2,seq1)][0] = actions_conditions_impossible[(seq2,seq1)][0] + copied
                    for i in range(len(actions_conditions_impossible[(seq2,seq1)][0])):
                        if i<len(copied):
                            actions_conditions_impossible[(seq2,seq1)][0][i].append(seq31)
                        else:
                            actions_conditions_impossible[(seq2,seq1)][0][i].append(seq32)
                elif "and" in seq3:
                    seq31, seq32 = seq3.split(" and ")
                    for i in range(len(actions_conditions_impossible[(seq2,seq1)][0])):  
                        actions_conditions_impossible[(seq2,seq1)][0][i].append(seq31)
                        actions_conditions_impossible[(seq2,seq1)][0][i].append(seq32)
                else:
                    for i in range(len(actions_conditions_impossible[(seq2,seq1)][0])):  
                        actions_conditions_impossible[(seq2,seq1)][0][i].append(seq3)

                
            elif "releases" in seq:
                seq4 = None
                seq1, seqrest = seq.split(" by ")
                seq2, seqrest = seqrest.split(" releases ")
                if "if" in seqrest:
                    seq3,seq4 = seqrest.split(" if ")
                else:
                    seq3 = seqrest
                if not (seq2,seq1) in agents_actions_releases.keys():
                    agents_actions_releases[seq2] = []
                    actions_conditions_releases[(seq2,seq1)] = [[[]],[[]]]
                agents_actions_releases[seq2].append(seq1)
                #actions_conditions[(seq2,seq1)]
                
                #done
                for i in range(len(actions_conditions_releases[(seq2,seq1)][1])):  
                    actions_conditions_releases[(seq2,seq1)][1][i].append(seq3)

                if not seq4==None:
                    if "or" in seq4:
                        seq41, seq42 = seq4.split(" or ")
                        copied = copy.deepcopy(actions_conditions_releases[(seq2,seq1)][0])
                        actions_conditions_releases[(seq2,seq1)][0] = actions_conditions_releases[(seq2,seq1)][0] + copied
                        for i in range(len(actions_conditions_releases[(seq2,seq1)][0])):
                            if i<len(copied):
                                actions_conditions_releases[(seq2,seq1)][0][i].append(seq41)
                            else:
                                actions_conditions_releases[(seq2,seq1)][0][i].append(seq42)
                    elif "and" in seq4:
                        seq41, seq42 = seq4.split(" and ")
                        for i in range(len(actions_conditions_releases[(seq2,seq1)][0])):  
                            actions_conditions_releases[(seq2,seq1)][0][i].append(seq41)
                            actions_conditions_releases[(seq2,seq1)][0][i].append(seq42)
                    else:
                        for i in range(len(actions_conditions_releases[(seq2,seq1)][0])):  
                            actions_conditions_releases[(seq2,seq1)][0][i].append(seq4)
            elif "always" in seq:
                seq = seq[len("always")+1:]
                if "or" in seq:
                    seq1, seq2 = seq.split(" or ")
                    copied = copy.deepcopy(statments["always"])
                    statments["always"] = statments["always"] + copied
                    for i in range(len(statments["always"])):
                        if i<len(copied):
                            statments["always"][i].append(seq1)
                        else:
                            statments["always"][i].append(seq2)
                elif "and" in seq:
                    seq1, seq2 = seq.split(" and ")
                    for i in range(len(statments["always"])):  
                        statments["always"][i].append(seq1)
                        statments["always"][i].append(seq2)
                else:
                    for i in range(len(statments["always"])):  
                        statments["always"][i].append(seq)
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! blad")
        self.statments = statments
        self.after_sequences = after_sequences
        self.after_observable_sequences = after_observable_sequences
        self.actions_conditions = actions_conditions
        self.actions_conditions_impossible = actions_conditions_impossible
        self.actions_conditions_releases = actions_conditions_releases
        self.agents_actions_impossible = agents_actions_impossible
        self.agents_actions_releases = agents_actions_releases

        print(f"Initial fluents :{statments['initial_fluents']}")
        print(f"After sequences :{after_sequences}")
        print(f"After observable sequences :{after_observable_sequences}")
        print(f"actions_conditions :{actions_conditions}")
        print(f"actions_conditions_impossible :{actions_conditions_impossible}")
        print(f"actions_conditions_releases :{actions_conditions_releases}")
        print(f"always :{statments['always']}")




        initial_fluents = copy.deepcopy(statments["initial_fluents"])
        for f in fluents:
            new_statements = []
            
            for l in initial_fluents:
                #print(f"l {l}")
                if "!" + f in l or f in l:
                    #print(f"in if 1 ")
                    new_statements.append(l)
                    continue
                else:
                    l_copy_1 = copy.deepcopy(l)
                    l_copy_1.append(f)
                    new_statements.append(l_copy_1)
                    l_copy_2 = copy.deepcopy(l)
                    l_copy_2.append("!" + f)
                    new_statements.append(l_copy_2)
            new_statements = [list(x) for x in set(tuple(sorted(x)) for x in new_statements)]        

            initial_fluents = new_statements
        states[0] = initial_fluents

        print(f"states0 {states}")

        new_statements = []
        for states_model in states[0]:
            for posibility2 in statments["always"]:
                boolean = True
                for fluent in posibility2:
                    if not fluent in states_model:
                        boolean = False
                        break
                if boolean:
                    break
            if boolean:                   
                new_statements.append(states_model)
        states[0] = new_statements        


        print(f"states1 {states}")
        print(f"statments[initial_fluents] {statments['initial_fluents']}")
        self.states = states 

                    

    def clicked_switch_to_initial_page(self):
        self.stackedWidget.setCurrentIndex(1)


    def update_template(self, index):
        # Usunięcie istniejących pól edycyjnych
        while self.fields_layout.rowCount() > 0:
            self.fields_layout.removeRow(0)

        selected_template = self.comboBox.currentText()
        
        #Value statement
        ##1
        if selected_template == "[fluent1] [linking] [fluent2] after [action1]":
            self.field_names = ["fluent1","linking","fluent2", "action1"]
        ##2
        elif selected_template == "observable [fluent1] [linking] [fluent2] after [action1]":
            self.field_names = ["fluent1","linking","fluent2","action1"]
        ##3
        elif selected_template == "initially [fluent1] [linking] [fluent2]":
            self.field_names = ["fluent1","linking", "fluent2"]
            
        #Effect statement
        ##1
        elif selected_template == "[action] by [agent] causes [fluent1] [linking] [fluent2] if [fluent3] [linking2] [fluent4]":
            self.field_names = ["action","agent","fluent1","linking","fluent2","fluent3","linking2","fluent4"]
        ##2
        elif selected_template == "[action] by [agent] causes [fluent1] [linking] [fluent2]":
            self.field_names = ["action","agent","fluent1","linking","fluent2"]

        ##3
        elif selected_template == "impossible [action] by [agent] if [fluent1] [linking] [fluent2]":
            self.field_names = ["action","agent","fluent1","linking","fluent2"]


        #Release statement
        ##1
        elif selected_template == "[action] by [agent] releases [fluent1] if [fluent3] [linking2] [fluent4]":
            self.field_names = ["action","agent","fluent1","fluent3","linking2","fluent4"]
        ##2
        elif selected_template == "[action] by [agent] releases [fluent1]":
            self.field_names = ["action","agent","fluent1"]
        #Constraint statement
        ##1
        elif selected_template == "always [fluent1] [linking1] [fluent2]":
            self.field_names = ["fluent1","linking1","fluent2"]







        self.fields = []
        for i, field_name in enumerate(self.field_names):
            if field_name == "linking" or field_name == "linking1" or field_name == "linking2":
                self.drop_down = QComboBox()
                self.drop_down.addItem("or")
                self.drop_down.addItem("and")
                self.drop_down.setCurrentIndex(-1)
                self.fields.append(self.drop_down)
            elif field_name == "action" or field_name== "action1":
                self.drop_down_action = QComboBox()
                self.drop_down_action.addItems(self.actions)
                self.drop_down_action.setCurrentIndex(-1)
                self.fields.append(self.drop_down_action)
            elif field_name == "agent" or field_name == "agent1":
                self.drop_down_agent = QComboBox()
                self.drop_down_agent.addItems(self.agents)
                self.drop_down_agent.setCurrentIndex(-1)
                self.fields.append(self.drop_down_agent)
            else:
                self.drop_down_fluents = QComboBox()
                self.drop_down_fluents.addItems(self.fluents)
                for f in self.fluents:
                    self.drop_down_fluents.addItem(f"!{f}")
                self.drop_down_fluents.setCurrentIndex(-1)
                self.fields.append(self.drop_down_fluents)
                
            self.fields_layout.addRow(field_name, self.fields[i])

    def clicked_add_sentence(self):
        combined_text = self.comboBox.currentText()

        for field, field_name in zip(self.fields, self.field_names):
            field_value = str(field.currentText())
                        
            combined_text = combined_text.replace(f"[{field_name}]", field_value)

        self.textBrowser.addItem(combined_text)

        while self.fields_layout.rowCount() > 0:
            self.fields_layout.removeRow(0)

        self.comboBox.setCurrentIndex(-1)

        self.sentences.append(combined_text)
        print(self.sentences)


    def update_template_2(self, index):
        # Usunięcie istniejących pól edycyjnych
        while self.fields_layout_2.rowCount() > 0:
            self.fields_layout_2.removeRow(0)

        selected_template = self.comboBox_2.currentText()

        #Value query
        if selected_template == "necessary [fluent1] [linking1] [fluent2] after program":
            self.field_names_2 = ["fluent1","linking1","fluent2"]

        elif selected_template == "possibly [fluent1] [linking1] [fluent2] after program":
            self.field_names_2 = ["fluent1","linking1","fluent2"]
        #Realizability query
        elif selected_template == "program realizable always":
            self.field_names_2 = []

        elif selected_template == "program realizable ever":
            self.field_names_2 = []
        #Activity query
        elif selected_template == "active [agent] in program ":
             self.field_names_2 = ["agent"]

        self.fields_2 = []
        for i, field_name in enumerate(self.field_names_2):
            if field_name == "linking" or field_name == "linking1" or field_name == "linking2":
                self.drop_down = QComboBox()
                self.drop_down.addItem("or")
                self.drop_down.addItem("and")
                self.drop_down.setCurrentIndex(-1)
                self.fields_2.append(self.drop_down)
            elif field_name == "action" or field_name== "action1":
                self.drop_down_action = QComboBox()
                self.drop_down_action.addItems(self.actions)
                self.drop_down_action.setCurrentIndex(-1)
                self.fields_2.append(self.drop_down_action)
            elif field_name == "agent" or field_name == "agent1":
                self.drop_down_agent = QComboBox()
                self.drop_down_agent.addItems(self.agents)
                self.drop_down_agent.setCurrentIndex(-1)
                self.fields_2.append(self.drop_down_agent)
            else:
                self.drop_down_fluents = QComboBox()
                self.drop_down_fluents.addItems(self.fluents)
                for f in self.fluents:
                    self.drop_down_fluents.addItem(f"!{f}")
                self.drop_down_fluents.setCurrentIndex(-1)
                self.fields_2.append(self.drop_down_fluents)
            self.fields_layout_2.addRow(field_name, self.fields_2[i])

    def update_template_3(self):
        
        while self.fields_layout_3.rowCount() > 0:
            self.fields_layout_3.removeRow(0)

        
        self.field_names_3 = ['action','agent']
        self.fields_3 = []
        for i, field_name in enumerate(self.field_names_3):
            if field_name == "action":
                self.drop_down_action = QComboBox()
                self.drop_down_action.addItems(self.actions)
                self.drop_down_action.setCurrentIndex(-1)
                self.fields_3.append(self.drop_down_action)
            elif field_name == "agent" or field_name == "agent1":
                self.drop_down_agent = QComboBox()
                self.drop_down_agent.addItems(self.agents)
                self.drop_down_agent.setCurrentIndex(-1)
                self.fields_3.append(self.drop_down_agent)
            self.fields_layout_3.addRow(field_name, self.fields_3[i])


    def clicked_add_sentence_2(self):
        combined_text = self.comboBox_2.currentText()

        for field, field_name in zip(self.fields_2, self.field_names_2):
            field_value = str(field.currentText())
            
            combined_text = combined_text.replace(f"[{field_name}]", field_value)

        self.textBrowser_3.setText(f"{combined_text}")

        while self.fields_layout_2.rowCount() > 0:
            self.fields_layout_2.removeRow(0)

        self.comboBox_2.setCurrentIndex(-1)
        self.query.append(combined_text)
        print(self.query)

    def clicked_add_sentence_3(self):
        
        combined_text = '[agent] [action]'
        for field, field_name in zip(self.fields_3, self.field_names_3):
            field_value = str(field.currentText())
            combined_text = combined_text.replace(f"[{field_name}]", field_value)

        self.textBrowser_2.addItem(f"{combined_text}")
        
        while self.fields_layout_3.rowCount() > 0:
            self.fields_layout_3.removeRow(0)
            
        self.comboBox_4.setCurrentIndex(-1)
        self.sentences_2.append(combined_text)
        print(self.sentences_2)

    def clicked_add_sentence_4(self):
        
        field_value = self.LineEdit_1.text()
    
        self.textBrowser_5.addItem(f"{field_value}")

        self.fluents.append(field_value)
        self.LineEdit_1.clear()

    def clicked_add_sentence_5(self):
        
        field_value = self.LineEdit_2.text()
    
        self.textBrowser_6.addItem(f"{field_value}")

        self.agents.append(field_value)
        self.LineEdit_2.clear()

    def clicked_add_sentence_6(self):
        
        field_value = self.LineEdit_3.text()
    
        self.textBrowser_7.addItem(f"{field_value}")

        self.actions.append(field_value)
        self.LineEdit_3.clear()

    def clicked_remove_fluent(self):
        selected_item = self.textBrowser_5.currentItem()
        if selected_item:
            fluent = selected_item.text()
            self.fluents.remove(fluent)
            self.textBrowser_5.takeItem(self.textBrowser_5.row(selected_item))

    def clicked_remove_agent(self):
        selected_item = self.textBrowser_6.currentItem()
        if selected_item:
            agent = selected_item.text()
            self.agents.remove(agent)
            self.textBrowser_6.takeItem(self.textBrowser_6.row(selected_item))

    def clicked_remove_action(self):
        selected_item = self.textBrowser_7.currentItem()
        if selected_item:
            action = selected_item.text()
            self.actions.remove(action)
            self.textBrowser_7.takeItem(self.textBrowser_7.row(selected_item))

    def clicked_query_results(self):
        import copy
        actions_conditions = self.actions_conditions
        agents_actions_impossible = self.agents_actions_impossible
        actions_conditions_impossible = self.actions_conditions_impossible
        agents_actions_releases = self.agents_actions_releases
        actions_conditions_releases = self.actions_conditions_releases
        after_sequences=self.after_sequences
        after_observable_sequences = self.after_observable_sequences
        statments = self.statments
        states = copy.deepcopy(self.states)
        historical_actions = copy.deepcopy(self.historical_actions)


        program = self.sentences_2

        parsed_program = []
        for p in program:
            a,b = p.split(" ")
            parsed_program.append((a,b))
        # query = ["necessary !kurczak_zyje after"]
        query = [self.query[-1]]
        print(query)
        for j,i in enumerate(query):
            i = i.replace("  "," ")
            i = i.replace("  "," ")
            if i[-1]==" ":
                i = i[:-1]
            query[j] = i


        def value_query_necessary():
            for i,(agent, action) in enumerate(parsed_program):
                states[i+1]=[]
                historical_actions.append(action)  
                for state in states[i]:
                    boolean_always = True 
                    #impossible
                    if (agent, action) in actions_conditions_impossible.keys():
                        for posibility in actions_conditions_impossible[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break                         
                        if  boolean==True:
                            return False
                            continue                             
                    #causes
                    states_or =[]
                    if (agent, action) in actions_conditions.keys():
                        for posibility in actions_conditions[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    boolean_always = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            boolean_always = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    # states[i+1].append(state_copied)
                                    # state = state_copied
                                    states_or.append(state_copied)
                                    print(f"states_or {states_or}")
                        else:
                            states[i+1].append(state)
                    #release
                    if (agent, action) in actions_conditions_releases.keys():
                        for posibility in actions_conditions_releases[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            for posibility in actions_conditions_releases[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    states[i+1].append(state_copied)
                        #else:
                        states[i+1].append(state)
                    if boolean_always:
                        #states[i+1].append(state)
                        for state_or in states_or:
                            states[i+1].append(state_or) 
                                        
                states[i+1] = [list(x) for x in set(tuple(x) for x in states[i+1])]
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for state in states[i+1]:
                            state_copied = copy.deepcopy(state)
                            for formula in formulas:
                                for fluent in formula:
                                    if fluent in state_copied:
                                        continue
                                    elif "!" in postcondtion:
                                        state_copied.remove(fluent[1:])
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                                    else:
                                        state_copied.remove("!"+fluent)
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                        states[i+1] = state_new
            if len(states[len(states)-1]) == 0:
                return False 
            for state in states[len(states)-1]:
                formula = query[0].split("necessary ")[1].split(" after")[0]
                formula2 = None
                if "or" in formula:
                    formula, formula2 = formula.split(" or ")
                    if not formula in state and not formula2 in state:
                        return False
                elif "and" in formula:
                    formula, formula2 = formula.split(" and ")
                    if not formula in state or not formula2 in state:
                        return False
                else:
                    if not formula in state:
                        return False
            return True

                        
                        
                    


        def value_query_possibly():
            states_models = []
            for state in states[0]:
                states_models.append({0:[state]})
            for i,(agent, action) in enumerate(parsed_program):
                for states_model in states_models:
                    states_model[i+1]=[]
                historical_actions.append(action)  
                for states_model in states_models:
                    for state in states_model[i]:
                        boolean_always = True
                        #impossible
                        if (agent, action) in actions_conditions_impossible.keys():
                            for posibility in actions_conditions_impossible[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break                         
                            if  boolean==True:
                                continue                             
                        #causes
                        states_or =[]
                        if (agent, action) in actions_conditions.keys():
                            for posibility in actions_conditions[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            print(f"boolean {boolean}")    
                            if boolean:
                                
                                for posibility in actions_conditions[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    print(f"posibility {posibility}")
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                            print(f"state_copied {state_copied}")
                                        else:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                            print(f"state_copied {state_copied}")
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        boolean_always = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                boolean_always = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        # states[i+1].append(state_copied)
                                        # state = state_copied
                                        states_or.append(state_copied)
                                        print(f"states_or {states_or}")
                                    
                            else:
                                states_model[i+1].append(state)
                        #release
                        if (agent, action) in actions_conditions_releases.keys():
                            print(f"releases (agent, action) {(agent, action)}")
                            for posibility in actions_conditions_releases[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            if boolean:
                                
                                for posibility in actions_conditions_releases[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                        else:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        states_model[i+1].append(state_copied)
                                        # states_model[i+1].append(state) # TODO
                            # else:
                            states_model[i+1].append(state)
                        if boolean_always:                
                            # states_model[i+1].append(state) 
                            for state_or in states_or:
                                states_model[i+1].append(state_or) 

                for states_model in states_models: #remve the same states in model                         
                    states_model[i+1] = [list(x) for x in set(tuple(x) for x in states_model[i+1])]  
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for states_model in states_models:
                            for state in states_model[i+1]:
                                state_copied = copy.deepcopy(state)
                                for formula in formulas:
                                    for fluent in formula:
                                        if fluent in state_copied:
                                            continue
                                        elif "!" in postcondtion:
                                            state_copied.remove(fluent[1:])
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)
                                        else:
                                            state_copied.remove("!"+fluent)
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)                
                            states_model[i+1] = state_new
            print(f"states_models {states_models}")

            for states_model in states_models:
                print(f"states_model[len(states_model)-1] {states_model[len(states_model)-1]}")
                if len(states_model[len(states_model)-1]) == 0:
                    return False 
                state_possibly_true_tab =[]
                for state in states_model[len(states_model)-1]:
                    print(f"sate {state}")
                    formula = query[0].split("possibly ")[1].split(" after")[0]
                    formula2 = None
                    if "or" in formula:
                        formula, formula2 = formula.split(" or ")
                        if formula in state or formula2 in state:
                            # break
                            state_possibly_true_tab.append(True)
                    elif "and" in formula:
                        formula, formula2 = formula.split(" and ")
                        if formula in state and formula2 in state:
                            #break
                            state_possibly_true_tab.append(True)
                    # else:
                    #     if formula in state:
                    elif formula in state:
                            # break
                            state_possibly_true_tab.append(True)
                    #return False  
                    else:
                        state_possibly_true_tab.append(False)
                print(f"state_possibly_true_tab {state_possibly_true_tab}")
                if True in state_possibly_true_tab:
                    continue
                else:
                    return False        
            return True
        
            #         for iter,states_model in enumerate(states_models):
            #     print(f"iter {iter}")
            #     print(f"states_model[len(states_model)-1] {states_model[len(states_model)-1]}")
            #     if len(states_model[len(states_model)-1]) == 0:
            #         return False 
            #     states_combine = []
            #     for state in states_model[len(states_model)-1]:
            #         states_combine += state
            #     print(f"states_combine {states_combine}")    
                
            #     formula = query[0].split("possibly ")[1].split(" after")[0]
            #     formula2 = None
            #     if "or" in formula:
            #         formula, formula2 = formula.split(" or ")
            #         if formula in state or formula2 in state:
            #             break
            #     elif "and" in formula:
            #         formula, formula2 = formula.split(" and ")
            #         if formula in state and formula2 in state:
            #             break
            #     else:
            #         if formula in state:
            #             break
            #     return False    
            # return True        

                                
                                
        def activity_query():
            formula_agent = query[0].split("active ")[1].split(" in ")[0]
            boolean_agent = False
            for (agent, action) in parsed_program:
                if agent == formula_agent:
                    boolean_agent=True
            if not  boolean_agent:
                return False        
            for i,(agent, action) in enumerate(parsed_program):
                states[i+1]=[]
                historical_actions.append(action)  
                for state in states[i]:
                    boolean_always = True
                    #impossible
                    if (agent, action) in actions_conditions_impossible.keys():
                        for posibility in actions_conditions_impossible[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break                         
                        if  boolean==True:
                            if agent ==formula_agent:
                                return False
                            continue                             
                    #causes
                    states_or =[]
                    if (agent, action) in actions_conditions.keys():
                        for posibility in actions_conditions[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            for posibility in actions_conditions[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    boolean_always = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            boolean_always = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    # states[i+1].append(state_copied)
                                    if formula_agent == agent:
                                        if state==state_copied:
                                            return False
                                    states_or.append(state_copied)
                                    print(f"states_or {states_or}")

                                else:
                                    if formula_agent == agent:
                                        return False
                        else:
                            if formula_agent == agent:
                                return False
                            states[i+1].append(state)

                    if boolean_always:
                        # states[i+1].append(state) 
                        for state_or in states_or:
                            states[i+1].append(state_or) 
                    #release
                    if (agent, action) in actions_conditions_releases.keys():
                        if formula_agent == agent:
                            return False
                        for posibility in actions_conditions_releases[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions_releases[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    states[i+1].append(state_copied)
                        # else:
                        states[i+1].append(state)
                    
                                        
                states[i+1] = [list(x) for x in set(tuple(x) for x in states[i+1])]
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for state in states[i+1]:
                            state_copied = copy.deepcopy(state)
                            for formula in formulas:
                                for fluent in formula:
                                    if fluent in state_copied:
                                        continue
                                    elif "!" in postcondtion:
                                        state_copied.remove(fluent[1:])
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                                    else:
                                        state_copied.remove("!"+fluent)
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                        states[i+1] = state_new

            return True            
                        

        def realizability_query_always():
            for i,(agent, action) in enumerate(parsed_program):
                states[i+1]=[]
                historical_actions.append(action)  
                for state in states[i]:
                    boolean_always  = True
                    #impossible
                    if (agent, action) in actions_conditions_impossible.keys():
                        for posibility in actions_conditions_impossible[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break                         
                        if  boolean==True:
                            return False
                            continue                             
                    #causes
                    states_or =[]
                    if (agent, action) in actions_conditions.keys():
                        for posibility in actions_conditions[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    boolean_always = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            boolean_always = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    # states[i+1].append(state_copied)
                                    # state = state_copied
                                    states_or.append(state_copied)
                                    print(f"states_or {states_or}")
                                else:
                                    return False    
                        else:
                            states[i+1].append(state)
                    #release
                    if (agent, action) in actions_conditions_releases.keys():
                        for posibility in actions_conditions_releases[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions_releases[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    states[i+1].append(state_copied)
                                else:
                                    return False

                        # else:
                        states[i+1].append(state)   
                    if boolean_always:             
                        # states[i+1].append(state) 
                        for state_or in states_or:
                            states[i+1].append(state_or) 
                                        
                states[i+1] = [list(x) for x in set(tuple(x) for x in states[i+1])]
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for state in states[i+1]:
                            state_copied = copy.deepcopy(state)
                            for formula in formulas:
                                for fluent in formula:
                                    if fluent in state_copied:
                                        continue
                                    elif "!" in postcondtion:
                                        state_copied.remove(fluent[1:])
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                                    else:
                                        state_copied.remove("!"+fluent)
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                        states[i+1] = state_new
            return True



        def realizability_query_ever():
            states_models = []
            for state in states[0]:
                states_models.append({0:[state]})
            for i,(agent, action) in enumerate(parsed_program):
                for states_model in states_models:
                    states_model[i+1]=[]
                historical_actions.append(action)  
                for states_model in states_models:
                    for state in states_model[i]:
                        boolean_always = True 
                        #impossible
                        if (agent, action) in actions_conditions_impossible.keys():
                            for posibility in actions_conditions_impossible[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break                         
                            if  boolean==True:
                                continue                             
                        #causes
                        states_or =[]
                        if (agent, action) in actions_conditions.keys():
                            for posibility in actions_conditions[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            if boolean:
                                
                                for posibility in actions_conditions[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                        else:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        boolean_always = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                boolean_always = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        # states[i+1].append(state_copied)
                                        # state = state_copied
                                        states_or.append(state_copied)
                                        print(f"states_or {states_or}")
                            else:
                                states_model[i+1].append(state)
                        #release
                        if (agent, action) in actions_conditions_releases.keys():
                            for posibility in actions_conditions_releases[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            if boolean:
                                for posibility in actions_conditions_releases[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                        else:
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        states_model[i+1].append(state_copied)
                            # else:
                            states_model[i+1].append(state)
                        if boolean_always:
                            # states_model[i+1].append(state) 
                            for state_or in states_or:
                                states_model[i+1].append(state_or) 

                for states_model in states_models: #remve the same states in model                         
                    states_model[i+1] = [list(x) for x in set(tuple(x) for x in states_model[i+1])]  
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for states_model in states_models:
                            for state in states_model[i+1]:
                                state_copied = copy.deepcopy(state)
                                for formula in formulas:
                                    for fluent in formula:
                                        if fluent in state_copied:
                                            continue
                                        elif "!" in postcondtion:
                                            state_copied.remove(fluent[1:])
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)
                                        else:
                                            state_copied.remove("!"+fluent)
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)                
                            states_model[i+1] = state_new

            for states_model in states_models:
                state_tab = states_model[len(states_model)-1]
                if len(state_tab)==0:
                    return False
            return True                    
                            

        if "active" in query[-1]:
            self.answer = activity_query()
            print(self.answer)
            self.textBrowser_result.setText(str(self.answer))
        elif "necessary" in query[-1]:
            self.answer = value_query_necessary()
            print(self.answer)
            self.textBrowser_result.setText(str(self.answer))
        elif "possibly" in query[-1]:
            self.answer = value_query_possibly()
            print(self.answer)
            self.textBrowser_result.setText(str(self.answer))
        elif "always" in query[-1]:
            self.answer = realizability_query_always()
            print(self.answer)
            self.textBrowser_result.setText(str(self.answer))
        elif "ever" in query[-1]:
            self.answer = realizability_query_ever()
            print(self.answer)
            self.textBrowser_result.setText(str(self.answer))
        else:
            print("blad")
        
  

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Knowledge reasoning and representation ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add fluent, agents, actions", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add new sentence", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Definition of world", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Added sentences", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Choose template:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Close app", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Choose template:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Query", None))
        
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Add program", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Add fluent", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Add agent", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Add action", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Fluents, Agents, Actions", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"World definition", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Program", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Query", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Query results", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
    