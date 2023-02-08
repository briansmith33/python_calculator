from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt, QPoint, QSize
from PyQt5.QtGui import QCursor
import qtawesome as qta
import sys
import math


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.menuBar = self.menuBar()
        self.windowControl = QFrame(self)
        self.windowControlLayout = QHBoxLayout(self)
        self.windowControl.setLayout(self.windowControlLayout)

        self.close_btn = QPushButton(self.menuBar)
        self.max_btn = QPushButton(self.menuBar)
        self.min_btn = QPushButton(self.menuBar)

        self.oldPos = self.pos()
        self.screen = app.desktop()
        self.width = 400
        self.height = 600
        self.winX = int((self.screen.width() / 2) - (self.width / 2))
        self.winY = int((self.screen.height() / 2) - (self.height / 2))
        self.pressed = False
        self.isNeg = False

        self.mainLayout = QVBoxLayout(self)
        self.mainFrame = QFrame(self)
        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.mainFrame)
        self.setCentralWidget(self.mainFrame)
        self.calcLayout = QFormLayout(self)
        self.mainFrame.setLayout(self.calcLayout)

        self.formula = QLabel("")
        self.formula.setAlignment(Qt.AlignRight)
        self.formula.setStyleSheet("color: #cccccc; font-size: 16px;")
        self.calcLayout.addWidget(self.formula)

        self.calcScreen = QLabel("0")
        self.calcScreen.setAlignment(Qt.AlignRight)
        self.calcScreen.setStyleSheet("color: #ffffff; font-size: 50px")
        self.calcScreen.setFixedHeight(60)
        self.calcLayout.addWidget(self.calcScreen)

        self.font_color = "#55D6BE"

        self.row1 = QHBoxLayout(self)
        button_height = 65
        self.percentBtn = QPushButton("%")
        self.percentBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.percentBtn.clicked.connect(lambda: self.btnPush(self.percentBtn))
        self.percentBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.percentBtn.setFixedHeight(button_height)

        self.clearEquBtn = QPushButton("CE")
        self.clearEquBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clearEquBtn.clicked.connect(lambda: self.btnPush(self.clearEquBtn))
        self.clearEquBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.clearEquBtn.setFixedHeight(button_height)

        self.clearBtn = QPushButton("C")
        self.clearBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clearBtn.clicked.connect(lambda: self.btnPush(self.clearBtn))
        self.clearBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.clearBtn.setFixedHeight(button_height)

        self.delBtn = QPushButton("⌫")
        self.delBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delBtn.clicked.connect(lambda: self.btnPush(self.delBtn))
        self.delBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.delBtn.setFixedHeight(button_height)

        self.row1.addWidget(self.percentBtn)
        self.row1.addWidget(self.clearEquBtn)
        self.row1.addWidget(self.clearBtn)
        self.row1.addWidget(self.delBtn)

        self.calcLayout.addRow(self.row1)

        self.row2 = QHBoxLayout(self)

        self.invertBtn = QPushButton("1/x")
        self.invertBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.invertBtn.clicked.connect(lambda: self.btnPush(self.invertBtn))
        self.invertBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.invertBtn.setFixedHeight(button_height)

        self.squareBtn = QPushButton("x²")
        self.squareBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.squareBtn.clicked.connect(lambda: self.btnPush(self.squareBtn))
        self.squareBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.squareBtn.setFixedHeight(button_height)

        self.rootBtn = QPushButton("²√x")
        self.rootBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rootBtn.clicked.connect(lambda: self.btnPush(self.rootBtn))
        self.rootBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.rootBtn.setFixedHeight(button_height)

        self.divBtn = QPushButton("÷")
        self.divBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.divBtn.clicked.connect(lambda: self.btnPush(self.divBtn))
        self.divBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.divBtn.setFixedHeight(button_height)

        self.row2.addWidget(self.invertBtn)
        self.row2.addWidget(self.squareBtn)
        self.row2.addWidget(self.rootBtn)
        self.row2.addWidget(self.divBtn)

        self.calcLayout.addRow(self.row2)

        self.row3 = QHBoxLayout(self)

        self.sevenBtn = QPushButton("7")
        self.sevenBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sevenBtn.clicked.connect(lambda: self.btnPush(self.sevenBtn))
        self.sevenBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.sevenBtn.setFixedHeight(button_height)

        self.eightBtn = QPushButton("8")
        self.eightBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.eightBtn.clicked.connect(lambda: self.btnPush(self.eightBtn))
        self.eightBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.eightBtn.setFixedHeight(button_height)

        self.nineBtn = QPushButton("9")
        self.nineBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nineBtn.clicked.connect(lambda: self.btnPush(self.nineBtn))
        self.nineBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.nineBtn.setFixedHeight(button_height)

        self.multBtn = QPushButton("×")
        self.multBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.multBtn.clicked.connect(lambda: self.btnPush(self.multBtn))
        self.multBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.multBtn.setFixedHeight(button_height)

        self.row3.addWidget(self.sevenBtn)
        self.row3.addWidget(self.eightBtn)
        self.row3.addWidget(self.nineBtn)
        self.row3.addWidget(self.multBtn)

        self.calcLayout.addRow(self.row3)

        self.row4 = QHBoxLayout(self)

        self.fourBtn = QPushButton("4")
        self.fourBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fourBtn.clicked.connect(lambda: self.btnPush(self.fourBtn))
        self.fourBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.fourBtn.setFixedHeight(button_height)

        self.fiveBtn = QPushButton("5")
        self.fiveBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fiveBtn.clicked.connect(lambda: self.btnPush(self.fiveBtn))
        self.fiveBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.fiveBtn.setFixedHeight(button_height)

        self.sixBtn = QPushButton("6")
        self.sixBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sixBtn.clicked.connect(lambda: self.btnPush(self.sixBtn))
        self.sixBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.sixBtn.setFixedHeight(button_height)

        self.subBtn = QPushButton("-")
        self.subBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.subBtn.clicked.connect(lambda: self.btnPush(self.subBtn))
        self.subBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.subBtn.setFixedHeight(button_height)

        self.row4.addWidget(self.fourBtn)
        self.row4.addWidget(self.fiveBtn)
        self.row4.addWidget(self.sixBtn)
        self.row4.addWidget(self.subBtn)

        self.calcLayout.addRow(self.row4)

        self.row5 = QHBoxLayout(self)

        self.oneBtn = QPushButton("1")
        self.oneBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.oneBtn.clicked.connect(lambda: self.btnPush(self.oneBtn))
        self.oneBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.oneBtn.setFixedHeight(button_height)

        self.twoBtn = QPushButton("2")
        self.twoBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.twoBtn.clicked.connect(lambda: self.btnPush(self.twoBtn))
        self.twoBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.twoBtn.setFixedHeight(button_height)

        self.threeBtn = QPushButton("3")
        self.threeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.threeBtn.clicked.connect(lambda: self.btnPush(self.threeBtn))
        self.threeBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.threeBtn.setFixedHeight(button_height)

        self.plusBtn = QPushButton("+")
        self.plusBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.plusBtn.clicked.connect(lambda: self.btnPush(self.plusBtn))
        self.plusBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.plusBtn.setFixedHeight(button_height)

        self.row5.addWidget(self.oneBtn)
        self.row5.addWidget(self.twoBtn)
        self.row5.addWidget(self.threeBtn)
        self.row5.addWidget(self.plusBtn)

        self.calcLayout.addRow(self.row5)

        self.row6 = QHBoxLayout(self)

        self.negBtn = QPushButton("+/-")
        self.negBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.negBtn.clicked.connect(lambda: self.btnPush(self.negBtn))
        self.negBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.negBtn.setFixedHeight(button_height)

        self.zeroBtn = QPushButton("0")
        self.zeroBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.zeroBtn.clicked.connect(lambda: self.btnPush(self.zeroBtn))
        self.zeroBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.zeroBtn.setFixedHeight(button_height)

        self.decBtn = QPushButton(".")
        self.decBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.decBtn.clicked.connect(lambda: self.btnPush(self.decBtn))
        self.decBtn.setStyleSheet(f"background-color: #222222; font-size: 20px; color: {self.font_color};")
        self.decBtn.setFixedHeight(button_height)

        self.equalBtn = QPushButton("=")
        self.equalBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.equalBtn.clicked.connect(lambda: self.btnPush(self.equalBtn))
        self.equalBtn.setStyleSheet(f"background-color: #444444; font-size: 20px; color: {self.font_color};")
        self.equalBtn.setFixedHeight(button_height)

        self.row6.addWidget(self.negBtn)
        self.row6.addWidget(self.zeroBtn)
        self.row6.addWidget(self.decBtn)
        self.row6.addWidget(self.equalBtn)

        self.calcLayout.addRow(self.row6)

        self.fullScreen = False
        self.result = False

        self.initUI()

    def initUI(self):
        self.setObjectName('MainWindow')
        self.resize(self.width, self.height)
        self.setMouseTracking(True)

        self.setStyleSheet('background-color: #333333; border: 2px solid #333333;')

        self.menuBar.setCornerWidget(self.windowControl, Qt.TopRightCorner)
        self.windowControlLayout.addWidget(self.min_btn)
        self.windowControlLayout.addWidget(self.max_btn)
        self.windowControlLayout.addWidget(self.close_btn)

        self.min_btn.setStyleSheet("width: 30px; height:20px; border: none;")
        self.min_btn.setIcon(qta.icon('fa5s.window-minimize', color=self.font_color))
        self.min_btn.setIconSize(QSize(20, 20))
        self.min_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.min_btn.clicked.connect(self.minButton)

        self.max_btn.setStyleSheet("width: 30px; height:20px; border: none;")
        self.max_btn.setIcon(qta.icon('fa5s.window-maximize', color=self.font_color))
        self.max_btn.setIconSize(QSize(20, 20))
        self.max_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.max_btn.clicked.connect(self.maxButton)

        self.close_btn.setStyleSheet("width: 30px; height:20px; border: none;")
        self.close_btn.setIcon(qta.icon('fa5s.times', color=self.font_color))
        self.close_btn.setIconSize(QSize(20, 20))
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_btn.clicked.connect(self.closeButton)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(self.winX, self.winY)

        self.show()

    def btnPush(self, btn):
        if btn.text() == "%":
            if "." not in self.calcScreen.text():
                new_text = "0." + self.calcScreen.text()
                self.calcScreen.setText(new_text[:12])
            else:
                new_text = str(float(self.calcScreen.text())/(int(self.calcScreen.text().index(".")) * 10))
                self.calcScreen.setText(new_text[:12])

        if btn.text() == "CE":
            self.calcScreen.setText("0")
            self.isNeg = False

        if btn.text() == "C":
            self.formula.setText("")
            self.calcScreen.setText("0")
            self.isNeg = False

        if btn.text() == "⌫" and self.calcScreen.text() != "0":
            if len(self.calcScreen.text()) == 1:
                self.calcScreen.setText("0")
            else:
                self.calcScreen.setText(self.calcScreen.text()[:-1])

        if btn.text() == "1/x":
            self.formula.setText(f"1/({self.calcScreen.text()})")
            new_text = str(eval(f"1/{self.calcScreen.text()}"))
            self.calcScreen.setText(new_text[:12])

        if btn.text() == "x²":
            self.formula.setText(f"sqr({self.calcScreen.text()})")
            new_text = str(eval(f"{self.calcScreen.text()}*{self.calcScreen.text()}"))
            self.calcScreen.setText(new_text[:12])

        if btn.text() == "²√x":
            self.formula.setText(f"√({self.calcScreen.text()})")
            result = str(math.sqrt(float(self.calcScreen.text())))
            if result[-2:] == ".0":
                result = result[:-2]
            self.calcScreen.setText(result[:12])

        if btn.text() == "÷":
            self.formula.setText(self.formula.text() + self.calcScreen.text() + " ÷ ")
            self.calcScreen.setText("0")
            self.result = True

        if btn.text() == "×":
            self.formula.setText(self.formula.text() + self.calcScreen.text() + " × ")
            self.calcScreen.setText("0")
            self.result = True

        if btn.text() == "-":
            self.formula.setText(self.formula.text() + self.calcScreen.text() + " - ")
            self.calcScreen.setText("0")
            self.result = True

        if btn.text() == "+":
            self.formula.setText(self.formula.text() + self.calcScreen.text() + " + ")
            self.result = True

        if btn.text() == "=":
            self.formula.setText(self.formula.text() + self.calcScreen.text() + " =")
            self.calculate()
            self.result = True

        if btn.text() == "+/-":
            if self.isNeg:
                self.calcScreen.setText(self.calcScreen.text().replace('-', ''))
                self.isNeg = False
            else:
                self.calcScreen.setText("-" + self.calcScreen.text())
                self.isNeg = True

        if btn.text() == ".":
            if "." not in self.calcScreen.text():
                self.calcScreen.setText(self.calcScreen.text()+".")

        if btn.text().isnumeric():
            if self.calcScreen.text() == "0" or self.calcScreen.text() == "-0" or self.result:
                if self.isNeg:
                    self.calcScreen.setText("-"+btn.text())
                else:
                    self.calcScreen.setText(btn.text())
                self.result = False
            else:
                if len(self.calcScreen.text()) < 12:
                    self.calcScreen.setText(self.calcScreen.text() + btn.text())

    def calculate(self):
        formula = self.formula.text().replace(" ", "").replace("÷", "/").replace("×", "*")[:-1]
        result = str(eval(formula))
        if result[-2:] == ".0":
            result = result[:-2]
        self.calcScreen.setText(result)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        self.pressed = True

    def mouseReleaseEvent(self, event):
        self.oldPos = event.globalPos()
        self.pressed = False

    def mouseMoveEvent(self, event):
        if self.pressed:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    @pyqtSlot()
    def minButton(self):
        self.showMinimized()

    @pyqtSlot()
    def maxButton(self):
        if self.fullScreen:
            self.winX = int((self.screen.size().width() / 2) - (self.width / 2))
            self.winY = int((self.screen.size().height() / 2) - (self.height / 2))
            self.setGeometry(self.winX, self.winY, self.width, self.height)
            self.fullScreen = False

        else:
            self.setGeometry(0, 0, self.screen.size().width(), self.screen.size().height())
            self.fullScreen = True

    @pyqtSlot()
    def closeButton(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec_())
