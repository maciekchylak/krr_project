import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


from sentence_processing import sentence_tagging

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.sentences = []

        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1158, 832)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1131, 801))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayoutWidget = QWidget(self.page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1131, 751))
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
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayoutWidget_2 = QWidget(self.page_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1151, 801))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 14, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.fields_container = QWidget(self.gridLayoutWidget_2)
        self.fields_container.setObjectName(u"fields_container")

        self.fields_layout = QFormLayout()
        self.fields_container.setLayout(self.fields_layout)

        self.gridLayout_2.addWidget(self.fields_container, 6, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 12, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 8, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 5, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 13, 1, 1, 1)

        self.textBrowser = QListWidget(self.gridLayoutWidget_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 10, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 11, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 5, 1, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 4, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 7, 1, 1, 1)

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

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayoutWidget_3 = QWidget(self.page_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 1131, 761))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_12, 3, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 5, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_13, 0, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 4, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.gridLayoutWidget_3)

        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_3.addWidget(self.textBrowser_2, 8, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_3.addWidget(self.pushButton_6, 10, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_15, 9, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_16, 11, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 7, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_14, 6, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_3.addWidget(self.pushButton_7, 5, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1158, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.addItem("initially [fluents]")
        self.comboBox.addItem("observable [fluents1] after [fluents2]")
        self.comboBox.currentIndexChanged.connect(self.update_template)
        self.comboBox.setCurrentIndex(-1)

        self.empty_fields = []

        self.pushButton.clicked.connect(self.clicked_switch_to_add_world_definition)
        self.pushButton_5.clicked.connect(self.clicked_add_sentence)
        self.pushButton_2.clicked.connect(self.clicked_remove_sentence)
        self.pushButton_4.clicked.connect(self.clicked_switch_to_query_page)
        self.pushButton_7.clicked.connect(self.clicked_query_results)
        
        self.pushButton_3.clicked.connect(self.clicked_exit_app)
        self.pushButton_6.clicked.connect(self.clicked_exit_app)

    def clicked_switch_to_add_world_definition(self):
        self.stackedWidget.setCurrentIndex(1)

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

    def clicked_switch_to_query_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def clicked_query_results(self):
        output_query = "Output z query"
        self.textBrowser_2.append(f"{self.lineEdit_2.text()}: {output_query}")
        self.lineEdit_2.clear()

    def update_template(self, index):
        # Usunięcie istniejących pól edycyjnych
        while self.fields_layout.rowCount() > 0:
            self.fields_layout.removeRow(0)

        selected_template = self.comboBox.currentText()
        
        if selected_template == "initially [fluents]":
            self.field_names = ["fluents"]
            
        elif selected_template == "observable [fluents1] after [fluents2]":
            self.field_names = ["fluents1", "fluents2"]


        self.fields = []
        for i, field_name in enumerate(self.field_names):
            self.fields.append(QLineEdit())
            self.fields_layout.addRow(field_name, self.fields[i])
        # ...

    def clicked_add_sentence(self):
        combined_text = self.comboBox.currentText()

        for field, field_name in zip(self.fields, self.field_names):
            field_value = field.text()
            
            combined_text = combined_text.replace(f"[{field_name}]", field_value)

        self.textBrowser.addItem(combined_text)

        while self.fields_layout.rowCount() > 0:
            self.fields_layout.removeRow(0)

        self.comboBox.setCurrentIndex(-1)

        self.sentences.append(combined_text)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Knowledge reasoning and representation ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add word definition", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add new sentence", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Definition of world", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Added sentences", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Choose template:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add new sentence", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Query", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Close app", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Query result", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"OK", None))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

