# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QTabWidget,
    QTextEdit,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QSize(600, 400))
        MainWindow.setMaximumSize(QSize(600, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(-1, 0, 603, 400))
        self.tab_7 = QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayoutWidget_6 = QWidget(self.tab_7)
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 110, 591, 91))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_6)
        self.label_8.setObjectName("label_8")

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_6)
        self.label_9.setObjectName("label_9")

        self.gridLayout_6.addWidget(self.label_9, 1, 0, 1, 1)

        self.lne_api_hash = QLineEdit(self.gridLayoutWidget_6)
        self.lne_api_hash.setObjectName("lne_api_hash")

        self.gridLayout_6.addWidget(self.lne_api_hash, 0, 1, 1, 1)

        self.lne_api_id = QLineEdit(self.gridLayoutWidget_6)
        self.lne_api_id.setObjectName("lne_api_id")

        self.gridLayout_6.addWidget(self.lne_api_id, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 600, 375))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget = QWidget(self.tab_4)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 591, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_open_links = QPushButton(self.gridLayoutWidget)
        self.btn_open_links.setObjectName("btn_open_links")
        self.btn_open_links.setEnabled(True)

        self.gridLayout.addWidget(self.btn_open_links, 2, 3, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setEnabled(True)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.btn_chat_action = QPushButton(self.gridLayoutWidget)
        self.btn_chat_action.setObjectName("btn_chat_action")

        self.gridLayout.addWidget(self.btn_chat_action, 6, 0, 1, 4)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setEnabled(True)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.sb_join_delay = QSpinBox(self.gridLayoutWidget)
        self.sb_join_delay.setObjectName("sb_join_delay")
        self.sb_join_delay.setEnabled(True)
        self.sb_join_delay.setMaximum(999999999)
        self.sb_join_delay.setValue(500)

        self.gridLayout.addWidget(self.sb_join_delay, 3, 1, 1, 3)

        self.rd_join_chat = QRadioButton(self.gridLayoutWidget)
        self.rd_join_chat.setObjectName("rd_join_chat")
        self.rd_join_chat.setChecked(True)

        self.gridLayout.addWidget(self.rd_join_chat, 0, 0, 1, 1)

        self.lne_chat_links = QLineEdit(self.gridLayoutWidget)
        self.lne_chat_links.setObjectName("lne_chat_links")
        self.lne_chat_links.setEnabled(True)
        self.lne_chat_links.setReadOnly(True)

        self.gridLayout.addWidget(self.lne_chat_links, 2, 1, 1, 2)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.chat_action_progress = QProgressBar(self.gridLayoutWidget)
        self.chat_action_progress.setObjectName("chat_action_progress")
        self.chat_action_progress.setValue(0)

        self.gridLayout.addWidget(self.chat_action_progress, 4, 1, 1, 3)

        self.rd_exit_from_chats = QRadioButton(self.gridLayoutWidget)
        self.rd_exit_from_chats.setObjectName("rd_exit_from_chats")

        self.gridLayout.addWidget(self.rd_exit_from_chats, 0, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayoutWidget_8 = QWidget(self.tab_9)
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(0, 0, 591, 341))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.gridLayoutWidget_8)
        self.label_17.setObjectName("label_17")

        self.gridLayout_8.addWidget(self.label_17, 1, 0, 1, 1)

        self.btn_chat_spam = QPushButton(self.gridLayoutWidget_8)
        self.btn_chat_spam.setObjectName("btn_chat_spam")

        self.gridLayout_8.addWidget(self.btn_chat_spam, 4, 0, 1, 3)

        self.sb_chat_spam_repeats = QSpinBox(self.gridLayoutWidget_8)
        self.sb_chat_spam_repeats.setObjectName("sb_chat_spam_repeats")
        self.sb_chat_spam_repeats.setMinimum(1)
        self.sb_chat_spam_repeats.setMaximum(999999999)

        self.gridLayout_8.addWidget(self.sb_chat_spam_repeats, 1, 1, 1, 2)

        self.chat_spam_progress = QProgressBar(self.gridLayoutWidget_8)
        self.chat_spam_progress.setObjectName("chat_spam_progress")
        self.chat_spam_progress.setValue(0)

        self.gridLayout_8.addWidget(self.chat_spam_progress, 2, 1, 1, 2)

        self.label_20 = QLabel(self.gridLayoutWidget_8)
        self.label_20.setObjectName("label_20")

        self.gridLayout_8.addWidget(self.label_20, 2, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayoutWidget_5 = QWidget(self.tab_5)
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 591, 341))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_5)
        self.label_4.setObjectName("label_4")

        self.gridLayout_5.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.label_7.setEnabled(False)

        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)

        self.sb_spam_user_count = QSpinBox(self.gridLayoutWidget_5)
        self.sb_spam_user_count.setObjectName("sb_spam_user_count")
        self.sb_spam_user_count.setMaximum(999999999)

        self.gridLayout_5.addWidget(self.sb_spam_user_count, 3, 1, 1, 2)

        self.lne_phones_path = QLineEdit(self.gridLayoutWidget_5)
        self.lne_phones_path.setObjectName("lne_phones_path")
        self.lne_phones_path.setEnabled(False)
        self.lne_phones_path.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lne_phones_path, 2, 1, 1, 1)

        self.btn_open_phones = QPushButton(self.gridLayoutWidget_5)
        self.btn_open_phones.setObjectName("btn_open_phones")
        self.btn_open_phones.setEnabled(False)

        self.gridLayout_5.addWidget(self.btn_open_phones, 2, 2, 1, 1)

        self.btn_private_spam = QPushButton(self.gridLayoutWidget_5)
        self.btn_private_spam.setObjectName("btn_private_spam")

        self.gridLayout_5.addWidget(self.btn_private_spam, 6, 0, 1, 3)

        self.private_spam_progress = QProgressBar(self.gridLayoutWidget_5)
        self.private_spam_progress.setObjectName("private_spam_progress")
        self.private_spam_progress.setValue(0)

        self.gridLayout_5.addWidget(self.private_spam_progress, 4, 1, 1, 2)

        self.label_13 = QLabel(self.gridLayoutWidget_5)
        self.label_13.setObjectName("label_13")

        self.gridLayout_5.addWidget(self.label_13, 4, 0, 1, 1)

        self.rd_list_spam = QRadioButton(self.gridLayoutWidget_5)
        self.rd_list_spam.setObjectName("rd_list_spam")

        self.gridLayout_5.addWidget(self.rd_list_spam, 0, 1, 1, 1)

        self.rd_db_spam = QRadioButton(self.gridLayoutWidget_5)
        self.rd_db_spam.setObjectName("rd_db_spam")
        self.rd_db_spam.setChecked(True)

        self.gridLayout_5.addWidget(self.rd_db_spam, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayoutWidget_4 = QWidget(self.tab_6)
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 591, 341))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName("label_6")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_4)
        self.label_3.setObjectName("label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 2)

        self.lne_photo_path = QLineEdit(self.gridLayoutWidget_4)
        self.lne_photo_path.setObjectName("lne_photo_path")
        self.lne_photo_path.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lne_photo_path, 3, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_4)
        self.label_5.setObjectName("label_5")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.btn_open_photo = QPushButton(self.gridLayoutWidget_4)
        self.btn_open_photo.setObjectName("btn_open_photo")

        self.gridLayout_4.addWidget(self.btn_open_photo, 3, 2, 1, 1)

        self.t_edit_message = QTextEdit(self.gridLayoutWidget_4)
        self.t_edit_message.setObjectName("t_edit_message")

        self.gridLayout_4.addWidget(self.t_edit_message, 1, 0, 1, 3)

        self.sb_message_delay = QSpinBox(self.gridLayoutWidget_4)
        self.sb_message_delay.setObjectName("sb_message_delay")
        self.sb_message_delay.setMaximum(999999999)
        self.sb_message_delay.setValue(500)

        self.gridLayout_4.addWidget(self.sb_message_delay, 4, 1, 1, 2)

        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 591, 371))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rd_db_invite = QRadioButton(self.gridLayoutWidget_2)
        self.rd_db_invite.setObjectName("rd_db_invite")
        self.rd_db_invite.setChecked(True)

        self.gridLayout_2.addWidget(self.rd_db_invite, 0, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.label_10.setEnabled(False)

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.rd_list_invite = QRadioButton(self.gridLayoutWidget_2)
        self.rd_list_invite.setObjectName("rd_list_invite")

        self.gridLayout_2.addWidget(self.rd_list_invite, 0, 1, 1, 1)

        self.btn_start_invite = QPushButton(self.gridLayoutWidget_2)
        self.btn_start_invite.setObjectName("btn_start_invite")

        self.gridLayout_2.addWidget(self.btn_start_invite, 7, 0, 1, 3)

        self.btn_open_phones_2 = QPushButton(self.gridLayoutWidget_2)
        self.btn_open_phones_2.setObjectName("btn_open_phones_2")
        self.btn_open_phones_2.setEnabled(False)

        self.gridLayout_2.addWidget(self.btn_open_phones_2, 3, 2, 1, 1)

        self.sb_invite_user_count = QSpinBox(self.gridLayoutWidget_2)
        self.sb_invite_user_count.setObjectName("sb_invite_user_count")
        self.sb_invite_user_count.setMaximum(999999999)

        self.gridLayout_2.addWidget(self.sb_invite_user_count, 4, 1, 1, 2)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")

        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)

        self.lne_phones_path_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lne_phones_path_2.setObjectName("lne_phones_path_2")
        self.lne_phones_path_2.setEnabled(False)

        self.gridLayout_2.addWidget(self.lne_phones_path_2, 3, 1, 1, 1)

        self.invite_progress = QProgressBar(self.gridLayoutWidget_2)
        self.invite_progress.setObjectName("invite_progress")
        self.invite_progress.setValue(0)

        self.gridLayout_2.addWidget(self.invite_progress, 5, 1, 1, 2)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")

        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 591, 371))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")

        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_6.setMaximum(999999999)

        self.gridLayout_3.addWidget(self.spinBox_6, 0, 1, 1, 1)

        self.btn_start_dump = QPushButton(self.gridLayoutWidget_3)
        self.btn_start_dump.setObjectName("btn_start_dump")

        self.gridLayout_3.addWidget(self.btn_start_dump, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayoutWidget_7 = QWidget(self.tab_8)
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(2, 0, 591, 371))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 10)
        self.label_16 = QLabel(self.gridLayoutWidget_7)
        self.label_16.setObjectName("label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_16, 0, 1, 1, 1)

        self.log = QPlainTextEdit(self.gridLayoutWidget_7)
        self.log.setObjectName("log")
        self.log.setReadOnly(True)

        self.gridLayout_7.addWidget(self.log, 2, 0, 1, 3)

        self.tabWidget.addTab(self.tab_8, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Spamer & Inviter", None)
        )
        self.label_8.setText(QCoreApplication.translate("MainWindow", "Api hash", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Api id", None))
        self.lne_api_hash.setInputMask("")
        self.lne_api_hash.setText("")
        self.lne_api_hash.setPlaceholderText("")
        self.lne_api_id.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_7),
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.btn_open_links.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0424\u043e\u0440\u043c\u0430\u0442 \u0441\u0441\u044b\u043b\u043a\u0438:</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_open_links.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0424\u0430\u0439\u043b \u0441 \u0441\u0441\u044b\u043b\u043a\u0430\u043c\u0438",
                None,
            )
        )
        self.btn_chat_action.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041d\u0430\u0447\u0430\u0442\u044c", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0432\u0445\u043e\u0434\u0430",
                None,
            )
        )
        self.sb_join_delay.setSuffix(
            QCoreApplication.translate("MainWindow", " \u043c\u0441", None)
        )
        self.sb_join_delay.setPrefix("")
        # if QT_CONFIG(tooltip)
        self.rd_join_chat.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0424\u043e\u0440\u043c\u0430\u0442 \u0441\u0441\u044b\u043b\u043a\u0438:</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.rd_join_chat.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u043e\u0439\u0442\u0438 \u0432 \u0447\u0430\u0442\u044b",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lne_chat_links.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412 \u0444\u0430\u0439\u043b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u043e\u0431\u044b\u0447\u043d\u044b\u0435 \u0441\u0441\u044b\u043b\u043a\u0438 \u043d\u0430 \u0447\u0430\u0442\u044b</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u0440\u043e\u0433\u0440\u0435\u0441", None
            )
        )
        self.rd_exit_from_chats.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u044b\u0439\u0442\u0438 \u0441\u043e \u0432\u0441\u0435\u0445 \u0447\u0430\u0442\u043e\u0432",
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_4),
            QCoreApplication.translate(
                "MainWindow",
                "\u0427\u0430\u0442\u044b \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430",
                None,
            ),
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0432\u0442\u043e\u0440\u043e\u0432",
                None,
            )
        )
        self.btn_chat_spam.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041d\u0430\u0447\u0430\u0442\u044c", None
            )
        )
        self.sb_chat_spam_repeats.setSuffix(
            QCoreApplication.translate(
                "MainWindow", " \u043f\u043e\u0432\u0442\u043e\u0440(\u0430)", None
            )
        )
        self.sb_chat_spam_repeats.setPrefix("")
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u0440\u043e\u0433\u0440\u0435\u0441", None
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_9),
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043f\u0430\u043c \u043f\u043e \u0447\u0430\u0442\u0430\u043c",
                None,
            ),
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                None,
            )
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0424\u0430\u0439\u043b \u0441 \u043d\u043e\u043c\u0435\u0440\u0430\u043c\u0438",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.sb_spam_user_count.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d \u043d\u043e\u043b\u044c, \u0442\u043e \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0430 \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442\u044c \u043f\u043e \u0432\u0441\u0435\u043c \u0438\u043c\u0435\u044e\u0449\u0438\u043c\u0441\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.sb_spam_user_count.setSuffix(
            QCoreApplication.translate(
                "MainWindow", " \u0447\u0435\u043b\u043e\u0432\u0435\u043a(a)", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.btn_open_phones.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0424\u043e\u0440\u043c\u0430\u0442 \u043d\u043e\u043c\u0435\u0440\u0430:</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_open_phones.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None
            )
        )
        self.btn_private_spam.setText(
            QCoreApplication.translate(
                "MainWindow", " \u041d\u0430\u0447\u0430\u0442\u044c", None
            )
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u0440\u043e\u0433\u0440\u0435\u0441", None
            )
        )
        self.rd_list_spam.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0430 \u043f\u043e \u0441\u043f\u0438\u0441\u043a\u0443",
                None,
            )
        )
        self.rd_db_spam.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0430 \u043f\u043e \u0431\u0430\u0437\u0435",
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_5),
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043f\u0430\u043c \u043f\u043e \u043b\u0438\u0447\u043a\u0430\u043c",
                None,
            ),
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435",
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430", None
            )
        )
        self.btn_open_photo.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None
            )
        )
        self.t_edit_message.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:7.8pt;">test</span></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;"><br /></p></body></html>',
                None,
            )
        )
        self.sb_message_delay.setSuffix(
            QCoreApplication.translate("MainWindow", " \u043c\u0441", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_6),
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f",
                None,
            ),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate(
                "MainWindow", "\u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0430", None
            ),
        )
        self.rd_db_invite.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c \u043f\u043e \u0431\u0434",
                None,
            )
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0424\u0430\u0439\u043b \u0441 \u043d\u043e\u043c\u0435\u0440\u0430\u043c\u0438",
                None,
            )
        )
        self.rd_list_invite.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c \u043f\u043e \u0441\u043f\u0438\u0441\u043a\u0443",
                None,
            )
        )
        self.btn_start_invite.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0440\u0438\u0433\u043b\u0430\u0441\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432",
                None,
            )
        )
        self.btn_open_phones_2.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.sb_invite_user_count.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d \u043d\u043e\u043b\u044c, \u0442\u043e \u0431\u0443\u0434\u0443\u0442 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u044b \u0432 \u0447\u0430\u0442 \u0432\u0441\u0435 \u0438\u043c\u0435\u044e\u0449\u0438\u0435\u0441\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438 \u0432 \u0431\u0430\u0437\u0435 \u0438\u043b\u0438 \u0441\u043f\u0438\u0441\u043a\u0435</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.sb_invite_user_count.setSuffix(
            QCoreApplication.translate(
                "MainWindow", " \u0447\u0435\u043b\u043e\u0432\u0435\u043a(a)", None
            )
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                None,
            )
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u0440\u043e\u0433\u0440\u0435\u0441", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u044f",
                None,
            ),
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.spinBox_6.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d \u043d\u043e\u043b\u044c, \u0442\u043e \u0431\u0443\u0434\u0443\u0442 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u044b \u0432 \u0431\u0430\u0437\u0443 \u0432\u0441\u0435 \u0438\u043c\u0435\u044e\u0449\u0438\u0435\u0441\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.spinBox_6.setSuffix(
            QCoreApplication.translate(
                "MainWindow",
                " \u0447\u0435\u043b\u043e\u0432\u0435\u043a(\u0430)",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.btn_start_dump.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u0430\u043c\u043f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0438\u0437 \u0438\u043c\u0435\u044e\u0449\u0438\u0445\u0441\u044f \u0447\u0430\u0442\u043e\u0432 \u043d\u0430 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0435</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_start_dump.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0447\u0430\u0442\u044c \u0434\u0430\u043c\u043f",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "\u0414\u0430\u043c\u043f", None),
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041b\u043e\u0433 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_8),
            QCoreApplication.translate("MainWindow", "\u041b\u043e\u0433", None),
        )

    # retranslateUi
