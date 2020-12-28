import sys

from ChainReaction import Game, GameState, CellState, CellColor, CellShape, Cell
from Rules import Rules
from MainWindowsUi import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QIcon, QPainter, QStandardItemModel, QColor, QPen, QBrush, QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QItemDelegate, QStyleOptionViewItem, \
    QTextBrowser, QWidget, QLabel


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._game = Game(3)
        self.game_set_model(self._game)

        self._rules = Rules()

        class MyDelegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                painter.save()
                self.parent().on_item_paint(idx, painter, option)
                painter.restore()

        def my_mouse_press_event(e: QMouseEvent):
            idx = self.ui.tableView.indexAt(e.pos())
            self.on_item_clicked(idx, e)
            self.update_view()

        self.ui.tableView.setItemDelegate(MyDelegate(self))
        self.ui.tableView.mousePressEvent = my_mouse_press_event

        self.ui.new_game.triggered.connect(lambda: self.on_new_game())
        self.ui.change_lvl.triggered.connect(lambda: self.game_resize(self._game))
        self.ui.exit.triggered.connect(lambda: self.close())
        self.ui.rules.triggered.connect(lambda: self._rules.show())

    def game_set_model(self, game: Game):
        model = QStandardItemModel(game.size, game.size)
        self.ui.tableView.setModel(model)
        horCircleSize = int(self.ui.gameWidget.width() / game.size-1)
        verCircleSize = int(self.ui.gameWidget.height() / game.size-1)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(horCircleSize)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(verCircleSize)
        self.update_view()

    def game_resize(self, game: Game):
        if game.size == 3:
            game._size = 4
        else:
            game._size = 3
        game.new_game()
        self.game_set_model(game)

    def update_view(self):
        self.ui.tableView.viewport().update()

    def on_new_game(self):
        self._game.new_game()
        self.update_view()

    def on_item_paint(self, e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem):
        item = self._game.field.get((e.row(), e.column()))
        color = QColor()
        if item.color == CellColor.RED:
            color.setRgb(255, 0, 0)
        elif item.color == CellColor.BLUE:
            color.setRgb(0, 0, 255)
        else:
            color.setRgb(0, 255, 0)

        brush = QBrush(color)

        if item.state == CellState.ACTIVE:
            brush.setStyle(Qt.Dense2Pattern)
        elif item.state == CellState.MARKED:
            brush.setStyle(Qt.BDiagPattern)

        painter.setBrush(brush)

        if item.shape == CellShape.SQUARE:
            painter.drawRect(option.rect)
        else:
            painter.drawEllipse(option.rect)

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None):
        if me.button() == Qt.LeftButton:
            self._game.left_mouse_click(e.row(), e.column())


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
