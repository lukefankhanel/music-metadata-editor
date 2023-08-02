
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
        
        self.fieldChangedDictionary = {}

        self.actionOpenFolder.triggered.connect(self.openFileDialog)
        self.actionSave.triggered.connect(self.saveMetadata)
        #self.treeView.clicked.connect(self.songSelected2)

        self.songTitle.textEdited.connect(self.trackEdit)
        self.songArtist.textEdited.connect(self.trackEdit)
        self.songAlbum.textEdited.connect(self.trackEdit)
        self.songDate.textEdited.connect(self.trackEdit)
        self.songGenre.textEdited.connect(self.trackEdit)
        self.songComposer.textEdited.connect(self.trackEdit)
        self.songURL.textEdited.connect(self.trackEdit)
        self.songComment.textChanged.connect(self.trackEdit)
        self.songDescription.textChanged.connect(self.trackEdit)

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
        
        model.setNameFilters(["*.flac", "*.opus", "*.m4a", "*.mp4", "*.mp3"])
        #model.setNameFilterDisables(False)


       
        self.treeView.setModel(model)
        for i in range(1, self.treeView.model().columnCount()):
            self.treeView.header().hideSection(i)
        self.treeView.setRootIndex(model.index(fileName))


        self.treeView.selectionModel().selectionChanged.connect(self.itemSelected)
      

    def itemSelected(self, selected, deselected):
        self.fieldChangedDictionary.clear()
        fullSelection = self.treeView.selectionModel().selectedIndexes()
        print(fullSelection)
        if len(fullSelection) > 0:
            model = fullSelection[0].model()
            print(model.isDir(fullSelection[0]))
            for selection in reversed(fullSelection):
                if not model.isDir(selection):

                    # We have to block the textChanged signal from firing for the QTextEdit 
                    # fields because the textChanged signal listens for ALL edits, 
                    # not just user edits. Therefore, tracking the change that the program 
                    # makes just putting the data in does not make sense. We turn the blocking 
                    # off once the data has been put into the fields.
                    self.songComment.blockSignals(True)
                    self.songDescription.blockSignals(True)
                   
                    file = audiotypes.createFileObject(model.filePath(selection))
                    #print(file.getAllFileMetadata())
                    self.songTitle.setText(file.getTitle())
                    self.songArtist.setText(file.getArtist())
                    self.songAlbum.setText(file.getAlbum())
                    self.songDate.setText(file.getDate())
                    self.songGenre.setText(file.getGenre())
                    self.songComposer.setText(file.getComposer())
                    self.songURL.setText(file.getURL())

                    self.songComment.setPlainText(file.getComment())
                    self.songDescription.setPlainText(file.getDescription())
                    # Not listening for changes with trackEdited because this field should be immutable.
                    self.songRawMetadata.setPlainText(file.getAllFileMetadata())

                    self.songComment.blockSignals(False)
                    self.songDescription.blockSignals(False)
                    break
                    #print(filePath)
            #selected[0].setFlags()


    def trackEdit(self):
        self.fieldChangedDictionary[self.sender().objectName()] = True
        print(self.fieldChangedDictionary)

    def saveMetadata(self):
        fullSelection = self.treeView.selectionModel().selectedIndexes()
        songSelectionsOnly = []
        if len(fullSelection) > 0:
            model = fullSelection[0].model()
            for selection in fullSelection:
                if not model.isDir(selection):
                    songSelectionsOnly.append(selection)
            if len(songSelectionsOnly) > 0:
                for selection in songSelectionsOnly:
                    file = audiotypes.createFileObject(model.filePath(selection))
                    for field, value in self.fieldChangedDictionary.items():
                        if value:
                            if field == "songTitle":
                                file.setTitle(self.songTitle.text())
                            if field == "songArtist":
                                file.setArtist(self.songArtist.text())
                            if field == "songAlbum":
                                file.setAlbum(self.songAlbum.text())
                            if field == "songDate":
                                file.setDate(self.songDate.text())
                            if field == "songGenre":
                                file.setGenre(self.songGenre.text())
                            if field == "songComposer":
                                file.setComposer(self.songComposer.text())
                            if field == "songURL":
                                file.setURL(self.songURL.text())
                            if field == "songComment":
                                file.setComment(self.songComment.toPlainText())
                            if field == "songDescription":
                                file.setDescription(self.songDescription.toPlainText())
                    file.saveMetadata()
        self.fieldChangedDictionary.clear()
