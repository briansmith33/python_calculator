from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt, QPoint, QRect
from PyQt5.QtGui import QIcon, QBitmap, QFont
import sys
import json
import math


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.menuBar = self.menuBar()
        self.windowControl = QFrame(self)
        self.windowControlLayout = QHBoxLayout(self)
        self.windowControl.setLayout(self.windowControlLayout)

        self.close_btn = QPushButton(self.menuBar)
        self.max_btn = QPushButton("", self.menuBar)
        self.min_btn = QPushButton("_", self.menuBar)

        self.oldPos = self.pos()
        self.screen = app.desktop()
        self.width = 320
        self.height = 480
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
        self.formula.setStyleSheet("color: #cccccc; font-size: 12px;")
        self.calcLayout.addWidget(self.formula)

        self.calcScreen = QLabel("0")
        self.calcScreen.setAlignment(Qt.AlignRight)
        self.calcScreen.setStyleSheet("color: #ffffff; font-size: 30px;")
        self.calcScreen.setFixedHeight(50)
        self.calcLayout.addWidget(self.calcScreen)

        self.row1 = QHBoxLayout(self)

        self.percentBtn = QPushButton("%")
        self.percentBtn.clicked.connect(lambda: self.btnPush(self.percentBtn))
        self.percentBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.percentBtn.setFixedHeight(40)

        self.clearEquBtn = QPushButton("CE")
        self.clearEquBtn.clicked.connect(lambda: self.btnPush(self.clearEquBtn))
        self.clearEquBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.clearEquBtn.setFixedHeight(40)

        self.clearBtn = QPushButton("C")
        self.clearBtn.clicked.connect(lambda: self.btnPush(self.clearBtn))
        self.clearBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.clearBtn.setFixedHeight(40)

        self.delBtn = QPushButton("⌫")
        self.delBtn.clicked.connect(lambda: self.btnPush(self.delBtn))
        self.delBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.delBtn.setFixedHeight(40)

        self.row1.addWidget(self.percentBtn)
        self.row1.addWidget(self.clearEquBtn)
        self.row1.addWidget(self.clearBtn)
        self.row1.addWidget(self.delBtn)

        self.calcLayout.addRow(self.row1)

        self.row2 = QHBoxLayout(self)

        self.invertBtn = QPushButton("1/x")
        self.invertBtn.clicked.connect(lambda: self.btnPush(self.invertBtn))
        self.invertBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.invertBtn.setFixedHeight(40)

        self.squareBtn = QPushButton("x²")
        self.squareBtn.clicked.connect(lambda: self.btnPush(self.squareBtn))
        self.squareBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.squareBtn.setFixedHeight(40)

        self.rootBtn = QPushButton("²√x")
        self.rootBtn.clicked.connect(lambda: self.btnPush(self.rootBtn))
        self.rootBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.rootBtn.setFixedHeight(40)

        self.divBtn = QPushButton("÷")
        self.divBtn.clicked.connect(lambda: self.btnPush(self.divBtn))
        self.divBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.divBtn.setFixedHeight(40)

        self.row2.addWidget(self.invertBtn)
        self.row2.addWidget(self.squareBtn)
        self.row2.addWidget(self.rootBtn)
        self.row2.addWidget(self.divBtn)

        self.calcLayout.addRow(self.row2)

        self.row3 = QHBoxLayout(self)

        self.sevenBtn = QPushButton("7")
        self.sevenBtn.clicked.connect(lambda: self.btnPush(self.sevenBtn))
        self.sevenBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.sevenBtn.setFixedHeight(40)

        self.eightBtn = QPushButton("8")
        self.eightBtn.clicked.connect(lambda: self.btnPush(self.eightBtn))
        self.eightBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.eightBtn.setFixedHeight(40)

        self.nineBtn = QPushButton("9")
        self.nineBtn.clicked.connect(lambda: self.btnPush(self.nineBtn))
        self.nineBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.nineBtn.setFixedHeight(40)

        self.multBtn = QPushButton("×")
        self.multBtn.clicked.connect(lambda: self.btnPush(self.multBtn))
        self.multBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.multBtn.setFixedHeight(40)

        self.row3.addWidget(self.sevenBtn)
        self.row3.addWidget(self.eightBtn)
        self.row3.addWidget(self.nineBtn)
        self.row3.addWidget(self.multBtn)

        self.calcLayout.addRow(self.row3)

        self.row4 = QHBoxLayout(self)

        self.fourBtn = QPushButton("4")
        self.fourBtn.clicked.connect(lambda: self.btnPush(self.fourBtn))
        self.fourBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.fourBtn.setFixedHeight(40)

        self.fiveBtn = QPushButton("5")
        self.fiveBtn.clicked.connect(lambda: self.btnPush(self.fiveBtn))
        self.fiveBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.fiveBtn.setFixedHeight(40)

        self.sixBtn = QPushButton("6")
        self.sixBtn.clicked.connect(lambda: self.btnPush(self.sixBtn))
        self.sixBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.sixBtn.setFixedHeight(40)

        self.subBtn = QPushButton("-")
        self.subBtn.clicked.connect(lambda: self.btnPush(self.subBtn))
        self.subBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.subBtn.setFixedHeight(40)

        self.row4.addWidget(self.fourBtn)
        self.row4.addWidget(self.fiveBtn)
        self.row4.addWidget(self.sixBtn)
        self.row4.addWidget(self.subBtn)

        self.calcLayout.addRow(self.row4)

        self.row5 = QHBoxLayout(self)

        self.oneBtn = QPushButton("1")
        self.oneBtn.clicked.connect(lambda: self.btnPush(self.oneBtn))
        self.oneBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.oneBtn.setFixedHeight(40)

        self.twoBtn = QPushButton("2")
        self.twoBtn.clicked.connect(lambda: self.btnPush(self.twoBtn))
        self.twoBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.twoBtn.setFixedHeight(40)

        self.threeBtn = QPushButton("3")
        self.threeBtn.clicked.connect(lambda: self.btnPush(self.threeBtn))
        self.threeBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.threeBtn.setFixedHeight(40)

        self.plusBtn = QPushButton("+")
        self.plusBtn.clicked.connect(lambda: self.btnPush(self.plusBtn))
        self.plusBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.plusBtn.setFixedHeight(40)

        self.row5.addWidget(self.oneBtn)
        self.row5.addWidget(self.twoBtn)
        self.row5.addWidget(self.threeBtn)
        self.row5.addWidget(self.plusBtn)

        self.calcLayout.addRow(self.row5)

        self.row6 = QHBoxLayout(self)

        self.negBtn = QPushButton("+/-")
        self.negBtn.clicked.connect(lambda: self.btnPush(self.negBtn))
        self.negBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.negBtn.setFixedHeight(40)

        self.zeroBtn = QPushButton("0")
        self.zeroBtn.clicked.connect(lambda: self.btnPush(self.zeroBtn))
        self.zeroBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.zeroBtn.setFixedHeight(40)

        self.decBtn = QPushButton(".")
        self.decBtn.clicked.connect(lambda: self.btnPush(self.decBtn))
        self.decBtn.setStyleSheet("background-color: #222222; font-size: 20px; color: #2CF6B3;")
        self.decBtn.setFixedHeight(40)

        self.equalBtn = QPushButton("=")
        self.equalBtn.clicked.connect(lambda: self.btnPush(self.equalBtn))
        self.equalBtn.setStyleSheet("background-color: #444444; font-size: 20px; color: #2CF6B3;")
        self.equalBtn.setFixedHeight(40)

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

        self.min_btn.setStyleSheet("width: 20px; height:20px;")
        self.min_btn.clicked.connect(self.minButton)

        self.max_btn.setStyleSheet("width: 20px; height:20px;")
        self.max_btn.clicked.connect(self.maxButton)

        self.close_btn.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_MessageBoxCritical')))
        self.close_btn.setStyleSheet("width: 20px; height:20px;")
        self.close_btn.clicked.connect(self.closeButton)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(self.winX, self.winY)

        self.show()

    def btnPush(self, btn):
        if btn.text() == "%":
            self.formula.setText(f"{self.formula.text()} 0.{self.calcScreen.text()}")
            self.calcScreen.setText("0." + self.calcScreen.text())

        if btn.text() == "CE":
            self.calcScreen.setText("0")

        if btn.text() == "C":
            self.formula.setText("")
            self.calcScreen.setText("0")

        if btn.text() == "⌫" and self.calcScreen.text() != "0":
            if len(self.calcScreen.text()) == 1:
                self.calcScreen.setText("0")
            else:
                self.calcScreen.setText(self.calcScreen.text()[:-1])

        if btn.text() == "1/x":
            self.formula.setText(f"1/({self.calcScreen.text()})")
            self.calcScreen.setText(str(eval(f"1/{self.calcScreen.text()}")))

        if btn.text() == "x²":
            self.formula.setText(f"sqr({self.calcScreen.text()})")
            self.calcScreen.setText(str(eval(f"{self.calcScreen.text()}*{self.calcScreen.text()}")))

        if btn.text() == "²√x":
            self.formula.setText(f"√({self.calcScreen.text()})")
            result = str(math.sqrt(int(self.calcScreen.text())))
            if result[-2:] == ".0":
                result = result[:-2]
            self.calcScreen.setText(result)

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
                self.calcScreen.setText(self.calcScreen.text()[1:])
                self.isNeg = False
            else:
                self.calcScreen.setText("-" + self.calcScreen.text())
                self.isNeg = True

        if btn.text().isnumeric():
            if self.calcScreen.text() == "0" or self.result:
                self.calcScreen.setText(btn.text())
                self.result = False
            else:
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
