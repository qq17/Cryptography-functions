import sys

import numpy as np
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.mainLayout.addWidget(self.canvas)

        x1 = []
        y1 = []

        x2 = []
        y2 = []

        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor('#DCDCDC')

        self.line1, = self.ax.plot(x1, y1, color='#000000')
        self.line2, = self.ax.plot(x2, y2, color='#007000')
        self.ax.legend(["x1", "x2"])

    def plot(self, xb, xe, y1, y2):
        x1 = np.linspace(xb, xe, len(y1))
        x2 = np.linspace(xb, xe, len(y2))

        self.line1.set_xdata(x1)
        self.line1.set_ydata(y1)
        print(self.line1.get_xdata())
        print(self.line1.get_ydata())

        self.line2.set_xdata(x2)
        self.line2.set_ydata(y2)

        self.ax.set_xlim([xb, xe])
        self.ax.set_ylim([-70, max(max(y1), max(y2))])

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()


class BarPlotWidget(QWidget):

    def __init__(self, parent=None):
        super(BarPlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.mainLayout.addWidget(self.canvas)

    def plot(self, xb, xe, y1, y2):
        x1 = np.linspace(xb, xe, len(y1))
        x2 = np.linspace(xb, xe, len(y2))

        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor('#DCDCDC')

        self.ax.set_xticks(range(xb, xe+1))

        self.ax.bar(x1, y1, color='#000000', width=0.25, align='edge')
        self.ax.bar(x2, y2, color='#007000', width=-0.25, align='edge')
        self.ax.legend(["x1", "x2"])

        self.canvas.draw()

    def pan(self):
        self.ax.xaxis.pan(2)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUi()
        self.connectUi()

    def initUi(self):
        self.centralWidget = QWidget(self)

        self.l = QVBoxLayout(self.centralWidget)
        # self.bl = QHBoxLayout(self.centralWidget)

        self.plotWidget = BarPlotWidget()

        self.plotButton = QPushButton('Plot')
        self.clearButton = QPushButton('Clear')
        self.panButton = QPushButton('Pan')

        self.plotButton.setStyleSheet('font-size: 12pt; font-weight: 530;')
        self.clearButton.setStyleSheet('font-size: 12pt; font-weight: 530;')
        self.panButton.setStyleSheet('font-size: 12pt; font-weight: 530;')

        self.l.addWidget(self.plotButton)
        self.l.addWidget(self.clearButton)
        self.l.addWidget(self.panButton)

        # self.l.addLayout(self.bl)
        self.l.addWidget(self.plotWidget)

        self.setCentralWidget(self.centralWidget)

    def connectUi(self):
        self.plotButton.clicked.connect(self.plot)
        self.clearButton.clicked.connect(self.clear)
        self.panButton.clicked.connect(self.pan)

    def clear(self):
        # self.plotWidget.figure.clear()
        self.plotWidget.plot(0, 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
                             [0.5, 1.5, 2.5, 3.5, 5.5, 5.5, 6.5, 7.5, 8.5, 9.5])
        # self.plotWidget.canvas.draw()

    def plot(self):
        self.plotWidget.plot(0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                             [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9])

        self.msg = QMessageBox(QMessageBox.Warning, 'I2C error', 'error_msg', parent=self)
        # self.msg.finished.connect(self._on_msgbox_close)
        self.msg.setModal(False)
        self.msg.show()

    def pan(self):
        self.plotWidget.pan()

if __name__ == '__main__':
    # app = QApplication([])
    # p = MainWindow()
    # p.show()
    #
    # sys.exit(app.exec_())

    a = [1,2,3]
    # # if a[-1] if a else False:
    # if a:
    #     print('yes')
    # if not a:
    #     print('no')
    print('pr', (a[-1] if a else 'no'))