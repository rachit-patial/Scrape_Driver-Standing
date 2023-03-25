import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget,QTableWidgetItem)
from scrape import *

data = getF1()
render = []
for i in range(len(data[0])):
    render.append((data[0][i], data[1][i]))

app = QApplication()

table = QTableWidget()
table.setRowCount(len(render))
table.setColumnCount(len(render[0]))
table.setColumnWidth(0, 200)
table.setHorizontalHeaderLabels(['Name', 'Points'])

for i, (name, point) in enumerate(render):
    item_name = QTableWidgetItem(name)
    item_point = QTableWidgetItem(point)
    table.setItem(i, 0, item_name)
    table.setItem(i, 1, item_point)

table.show()
sys.exit(app.exec())

