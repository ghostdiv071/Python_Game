# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\1\PycharmProjects\Game\main_windows_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gameWidget = QtWidgets.QWidget(self.centralwidget)
        self.gameWidget.setGeometry(QtCore.QRect(220, 10, 650, 600))
        self.gameWidget.setMouseTracking(True)
        self.gameWidget.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.gameWidget.setToolTipDuration(3)
        self.gameWidget.setObjectName("gameWidget")

        self.gameLayout = QtWidgets.QVBoxLayout(self.gameWidget)
        self.gameLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gameLayout.setContentsMargins(0, 0, 0, 0)
        self.gameLayout.setSpacing(6)
        self.gameLayout.setObjectName("verticalLayout_2")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setStyleSheet("QTableView { gridline-color: white; }")
        self.tableView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setObjectName("gameFieldTableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.gameLayout.addWidget(self.tableView)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_game = QtWidgets.QAction(MainWindow)
        self.new_game.setObjectName("new_game")
        self.change_lvl = QtWidgets.QAction(MainWindow)
        self.change_lvl.setObjectName("change_lvl")
        self.rules = QtWidgets.QAction(MainWindow)
        self.rules.setObjectName("rules")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.menu.addAction(self.new_game)
        self.menu.addAction(self.change_lvl)
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.rules)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Игра"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.new_game.setText(_translate("MainWindow", "Новая игра"))
        self.change_lvl.setText(_translate("MainWindow", "Сменить уровень"))
        self.rules.setText(_translate("MainWindow", "Правила"))
        self.exit.setText(_translate("MainWindow", "Выход"))
