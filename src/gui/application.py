
import PyQt5
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
import PyQt5.QtWidgets as pqw
from gui import mainWindow

class Application(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName = QFileDialog.getExistingDirectory(self,"QFileDialog.getOpenFileName()", "", options=options)
        if fileName:
            print(fileName)

        model = pqw.QFileSystemModel()
        model.setRootPath(fileName)

        #model.setFilter()

        
        model.setNameFilters(["*.txt","*.opus","*.m4a"])
        #model.setNameFilterDisables(False)

        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(fileName))

        self.treeView.selectionModel().selectionChanged.connect(self.getItems)


    def songSelected(self, value):
        pass
        # print(str(value.column()) + "    " + str(value.row()))
        # print(value.data(0))


    def getItems(self):
        selected = self.treeView.selectionModel().selectedIndexes()
        # print(selected)
        for index in selected:
            if index.column() == 0:
                print (index.data(0))