import sys
# import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('QtAgg')

import random, timeit

from sorts import *

from PySide6.QtWidgets import QFileDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox, QSpinBox, QLabel

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel('Inputs')
        self.axes.set_ylabel('Seconds')
        self.axes.set_title('Sorts')

        super(MplCanvas, self).__init__(fig)


class MainWindow(QWidget):

    def sortChoice(self, arr, sortType):

        if sortType == 0:
            start = timeit.default_timer()
            bubbleSort(arr)
            end = timeit.default_timer()
            return start, end, arr
        elif sortType == 1:
            start = timeit.default_timer()
            quickSort(arr, 0, len(arr) - 1)
            end = timeit.default_timer()
            return start, end, arr

        return arr, start, end


    def sort(self, low, high, minVal, maxVal, sortType):

        timings = []
        inputs = []

        for i in range(low, high + 1):
            arr = [random.randrange(minVal, maxVal, 1) for j in range(i)]

            start, end, arr = self.sortChoice(arr, sortType)

            inputs.append(i)
            timings.append(end-start)

            print ("Time: ", end-start)
            print ("Input Count: ", i)

            # self.curTimeLabel.setText(str(end-start))
            # self.curValueLabel.setText(str(i))

        totalTime = 0

        for entry in timings:
            totalTime = totalTime + entry

        chartLabel = self.sortCombo.currentText().split(' ')[0] + ' - ' + str(high) + ' | ' + str("{:.2f}".format(totalTime))
        return inputs, timings, chartLabel

    def addsort_Clicked(self):
        inputs, timings, chartLabel = self.sort(2, self.numSpin.value(), 1, 1000, self.sortCombo.currentIndex())

        self.sc.axes.plot(inputs, timings, self.colorCombo.currentText(), label=chartLabel)

        self.sc.axes.legend()

        self.sc.figure.canvas.draw()

    def clearSorts_Clicked(self):
        self.sc.axes.cla()
        self.sc.figure.canvas.draw()

    def saveButton_Clicked(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save File', 'plot.png', 'PNG Files (*.png)')
        self.sc.figure.savefig(fileName[0])
        

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Sorting Test")

        mainLayout = QVBoxLayout()

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        mainLayout.addWidget(self.sc)

        sortLayout = QHBoxLayout()

        self.sortCombo = QComboBox()
        self.sortCombo.addItem('Bubble Sort')
        self.sortCombo.addItem('Quick Sort')
        sortLayout.addWidget(self.sortCombo)

        self.colorCombo = QComboBox()
        self.colorCombo.addItem('Red')
        self.colorCombo.addItem('Green')
        self.colorCombo.addItem('Blue')
        self.colorCombo.addItem('Cyan')
        self.colorCombo.addItem('Magenta')
        self.colorCombo.addItem('Yellow')
        self.colorCombo.addItem('Black')
        sortLayout.addWidget(self.colorCombo)

        self.numSpin = QSpinBox()
        self.numSpin.setMinimum(2)
        self.numSpin.setMaximum(10000)
        self.numSpin.setValue(100)
        sortLayout.addWidget(self.numSpin)

        mainLayout.addLayout(sortLayout)

        # entryLayout = QHBoxLayout()

        # timeLayout = QHBoxLayout()

        # self.timeLabel = QLabel('Time - ')
        # timeLayout.addWidget(self.timeLabel)

        # self.curTimeLabel = QLabel()
        # timeLayout.addWidget(self.curTimeLabel)

        # valueLayout = QHBoxLayout()

        # self.valueLabel = QLabel('Value - ')
        # valueLayout.addWidget(self.valueLabel)

        # self.curValueLabel = QLabel()
        # valueLayout.addWidget(self.curValueLabel)

        # entryLayout.addLayout(timeLayout)
        # entryLayout.addLayout(valueLayout)

        # mainLayout.addLayout(entryLayout)

        chartLayout = QHBoxLayout()

        self.addSort = QPushButton("Add New Sort")
        self.addSort.clicked.connect(self.addsort_Clicked)
        chartLayout.addWidget(self.addSort)

        self.clearSorts = QPushButton("Clear All Sorts")
        self.clearSorts.clicked.connect(self.clearSorts_Clicked)
        chartLayout.addWidget(self.clearSorts)

        mainLayout.addLayout(chartLayout)

        self.saveButton = QPushButton("Save Image")
        self.saveButton.clicked.connect(self.saveButton_Clicked)
        mainLayout.addWidget(self.saveButton)

        self.setLayout(mainLayout)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())