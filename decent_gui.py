import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLabel, QAbstractItemView
from PySide6.QtGui import QFont, QPixmap, QImage
from scrape import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100, 100, 800, 800) # set window size and position
        self.setWindowTitle("F1 Driver Standing") # set window title

        self.appName()
        self.pointTable()
        self.currentLeader()
        self.nextRace()
        
    
    def appName(self):
        name = QLabel('Formula 1 Driver Standing', self)
        name.move(200, 20)
        name.setFont(QFont('Arial',20))
        

    def pointTable(self):
        data = getF1()
        render = []
        for i in range(len(data[0])):
            render.append((data[0][i], data[1][i]))

        table = QTableWidget(self)
        table.move(50, 100)
        table.setMinimumHeight(630)
        table.setMinimumWidth(330)
        table.setColumnCount(len(render[0]))
        table.setRowCount(len(render))
        table.setColumnWidth(0, 200)
        table.setHorizontalHeaderLabels(['Names', 'Points'])

        for i, (name, point) in enumerate(render):
            item_name = QTableWidgetItem(name)
            item_point = QTableWidgetItem(point)
            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_point)
        
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
    def currentLeader(self):
        leadingRacer = QLabel('Currently Leading Racer', self)
        leadingRacer.move(500, 100)
        leadingRacer.setFont(QFont('Helvetica', 14))

        imageLabel = QLabel(self)
        imageLabel.setScaledContents(True)
        image = QImage('pics/racer/max.jpg')
        imageLabel.setPixmap(QPixmap.fromImage(image))
        imageLabel.move(500, 130)

    def nextRace(self):
        racePlace = QLabel('Next Track', self)
        racePlace.move(500, 350)
        racePlace.setFont(QFont('Helvetica', 14))

        imageLabel = QLabel(self)
        imageLabel.setScaledContents(True)
        image = QImage('pics/tracks/baku.jpg')
        imageLabel.setPixmap(QPixmap.fromImage(image))
        imageLabel.move(500, 380)



    def buttonClicked(self):
        print("Button clicked!")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
