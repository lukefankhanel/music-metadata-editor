
from json import JSONDecodeError
import PyQt5
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
import PyQt5.QtWidgets as pqw
from gui import mainWindow
import audiotypes

class Application(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.actionSave.triggered.connect(self.saveMetadata)
        #self.treeView.clicked.connect(self.songSelected2)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName = QFileDialog.getExistingDirectory(self,"QFileDialog.getOpenFileName()", "", options=options)
        if fileName:
            print(fileName)

        model = pqw.QFileSystemModel()
        model.setRootPath(fileName)
        

        #model.setFilter()
        #iter = PyQt5.QDirIterator(self.path, QDirIterator.Subdirectories)
        #print(model.data())
        
        model.setNameFilters(["*.flac","*.opus","*.m4a"])
        #model.setNameFilterDisables(False)


       
        self.treeView.setModel(model)
        for i in range(1, self.treeView.model().columnCount()):
            self.treeView.header().hideSection(i)
        self.treeView.setRootIndex(model.index(fileName))


        self.treeView.selectionModel().selectionChanged.connect(self.songSelected2)
      



    def songSelected(self, value):
        pass
        # # print(str(value.column()) + "    " + str(value.row()))
        # print(value.data(0))
        # print(value.data(2))
        # selected = self.treeView.selectionModel().selectedIndexes()
        # print(selected)
        # if len(selected) > 0:
        #     model = selected[0].model()
        #     print(model.isDir(selected[0]))
        #     if not model.isDir(selected[0])
        #     #selected[0].setFlags()


    def songSelected2(self, selected, deselected):
        fullSelection = self.treeView.selectionModel().selectedIndexes()
        print(fullSelection)
        if len(fullSelection) > 0:
            model = fullSelection[0].model()
            print(model.isDir(fullSelection[0]))
            for selection in reversed(fullSelection):
                if not model.isDir(selection):
                    
                    filePath = model.filePath(selection)
                    JSONData = {
                        "metadataFieldMatches": "",
                        "artistNameTranslations": ""
                    }
                    file = audiotypes.createFileObject(filePath, JSONData)
                    print(file.getAllFileMetadata())
                    self.songTitle.setText(file.getOriginalTitle())
                    break
                    #print(filePath)
            #selected[0].setFlags()

    # def getItems(self):
    #     selected = self.treeView.selectionModel().selectedIndexes()
    #     # print(selected)
    #     for index in selected:
    #         if index.column() == 0:
    #             print (index.data(0))

    def saveMetadata(self):
        selected = self.treeView.selectionModel().selectedIndexes()
        # print(selected)
        for index in selected:
            if index.column() == 0:
                print (index.data(0))