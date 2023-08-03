
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
        self.isFileReading = False

        self.actionOpenFolder.triggered.connect(self.openFileDialog)
        self.actionSave.triggered.connect(self.saveMetadata)

        self.trackNumberCurrent.valueChanged.connect(self.trackEdited)
        self.trackNumberMaximum.valueChanged.connect(self.trackEdited)
        self.diskNumberCurrent.valueChanged.connect(self.trackEdited)
        self.diskNumberMaximum.valueChanged.connect(self.trackEdited)
        self.songTitle.textEdited.connect(self.trackEdited)
        self.songArtist.textEdited.connect(self.trackEdited)
        self.songAlbum.textEdited.connect(self.trackEdited)
        self.songDate.textEdited.connect(self.trackEdited)
        self.songGenre.textEdited.connect(self.trackEdited)
        self.songComposer.textEdited.connect(self.trackEdited)
        self.songURL.textEdited.connect(self.trackEdited)
        self.replayGain.valueChanged.connect(self.trackEdited)
        self.songComment.textChanged.connect(self.trackEdited)
        self.songDescription.textChanged.connect(self.trackEdited)

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
        fullSelection = self.treeView.selectionModel().selectedIndexes()
        #print(fullSelection)
        if len(fullSelection) > 0:
            model = fullSelection[0].model()
            #print(model.isDir(fullSelection[0]))
            for selection in reversed(fullSelection):
                if not model.isDir(selection):
                    self.isFileReading = True
                    file = audiotypes.createFileObject(model.filePath(selection))

                    self.trackNumberCurrent.setValue(file.getTrackNumberCurrent())
                    self.trackNumberMaximum.setValue(file.getTrackNumberMaximum())
                    self.diskNumberCurrent.setValue(file.getDiskNumberCurrent())
                    self.diskNumberMaximum.setValue(file.getDiskNumberMaximum())

                    self.songTitle.setText(file.getTitle())
                    self.songArtist.setText(file.getArtist())
                    self.songAlbum.setText(file.getAlbum())
                    self.songDate.setText(file.getDate())
                    self.songGenre.setText(file.getGenre())
                    self.songComposer.setText(file.getComposer())
                    self.songURL.setText(file.getURL())
                    self.replayGain.setValue(file.getReplayGain())

                    self.songComment.setPlainText(file.getComment())
                    self.songDescription.setPlainText(file.getDescription())
                    # Not listening for changes with trackEdited because this field should be immutable.
                    self.songRawMetadata.setPlainText(file.getAllFileMetadata())
                    break
                    #print(filePath)
            #selected[0].setFlags()

        # To stop the unblockable signals from firing and affecting the list of changes the user makes
        self.isFileReading = False
        self.fieldChangedDictionary.clear()


    def trackEdited(self):
        if not self.isFileReading:
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
                        if field == "trackNumberCurrent":
                            file.setTrackNumberCurrent(self.trackNumberCurrent.value())
                        if field == "trackNumberMaximum":
                            file.setTrackNumberMaximum(self.trackNumberMaximum.value())
                        if field == "diskNumberCurrent":
                            file.setDiskNumberCurrent(self.diskNumberCurrent.value())
                        if field == "diskNumberMaximum":
                            file.setDiskNumberMaximum(self.diskNumberMaximum.value())
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
                        if field == "replayGain":
                            file.setReplayGain(self.replayGain.value())
                        if field == "songComment":
                            file.setComment(self.songComment.toPlainText())
                        if field == "songDescription":
                            file.setDescription(self.songDescription.toPlainText())
                    file.saveMetadata()
        self.fieldChangedDictionary.clear()
