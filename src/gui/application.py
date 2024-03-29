
from json import JSONDecodeError
import PyQt5
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog, QProxyStyle, QTabBar, QStyle
)
import PyQt5.QtWidgets as pqw
from gui import mainWindow
import audiotypes


class Application(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        # Maps the object names of the fields to the instantiated label 
        # objects so that we can set the label text to bold dynamically.
        # PyQT5's buddy system could also achieve a similar effect, 
        # but since you can only attach one buddy to each field label pair,
        # the Disk and Track number fields will not work correctly 
        # unless we do it in a different way.
        self.labelFieldMappingDictionary = {
            "TrackNumberCurrentField": self.TrackNumberLabel,
            "TrackNumberMaximumField": self.TrackNumberLabel,
            "DiskNumberCurrentField": self.DiskNumberLabel,
            "DiskNumberMaximumField": self.DiskNumberLabel,
            "TitleField": self.TitleLabel,
            "ArtistField": self.ArtistLabel,
            "AlbumField": self.AlbumLabel,
            "DateField": self.DateLabel,
            "GenreField": self.GenreLabel,
            "ComposerField": self.ComposerLabel,
            "URLField": self.URLLabel,
            "ReplayGainField": self.ReplayGainLabel,
            # "CommentField": self.CommentLabel,
            # "DescriptionField": self.DescriptionLabel
            }
        self.fieldChangedDictionary = {}
        self.isFileReading = False

        self.actionOpenFolder.triggered.connect(self.openFileDialog)
        self.actionSave.triggered.connect(self.saveMetadata)

        self.TrackNumberCurrentField.valueChanged.connect(self.trackEdited)
        self.TrackNumberMaximumField.valueChanged.connect(self.trackEdited)
        self.DiskNumberCurrentField.valueChanged.connect(self.trackEdited)
        self.DiskNumberMaximumField.valueChanged.connect(self.trackEdited)
        self.TitleField.textEdited.connect(self.trackEdited)
        self.ArtistField.textEdited.connect(self.trackEdited)
        self.AlbumField.textEdited.connect(self.trackEdited)
        self.DateField.textEdited.connect(self.trackEdited)
        self.GenreField.textEdited.connect(self.trackEdited)
        self.ComposerField.textEdited.connect(self.trackEdited)
        self.URLField.textEdited.connect(self.trackEdited)
        self.ReplayGainField.valueChanged.connect(self.trackEdited)
        self.CommentField.textChanged.connect(self.trackEdited)
        self.DescriptionField.textChanged.connect(self.trackEdited)

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

                    self.TrackNumberCurrentField.setValue(file.getTrackNumberCurrent())
                    self.TrackNumberMaximumField.setValue(file.getTrackNumberMaximum())
                    self.DiskNumberCurrentField.setValue(file.getDiskNumberCurrent())
                    self.DiskNumberMaximumField.setValue(file.getDiskNumberMaximum())

                    self.TitleField.setText(file.getTitle())
                    self.ArtistField.setText(file.getArtist())
                    self.AlbumField.setText(file.getAlbum())
                    self.DateField.setText(file.getDate())
                    self.GenreField.setText(file.getGenre())
                    self.ComposerField.setText(file.getComposer())
                    self.URLField.setText(file.getURL())
                    self.ReplayGainField.setValue(file.getReplayGain())

                    self.CommentField.setPlainText(file.getComment())
                    self.DescriptionField.setPlainText(file.getDescription())
                    # Not listening for changes with trackEdited because this field should be immutable.
                    self.RawMetadataField.setPlainText(file.getAllFileMetadata())
                    break
                    #print(filePath)
            #selected[0].setFlags()

        # To stop the unblockable signals from firing and affecting the list of changes the user makes
        self.isFileReading = False
        self.fieldChangedDictionary.clear()
        self.clearCSS()


    def trackEdited(self):
        if not self.isFileReading:
            fieldName = self.sender().objectName()
            self.labelFieldMappingDictionary[fieldName].setStyleSheet("font-weight: bold")
            self.fieldChangedDictionary[fieldName] = True
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
                        if field == "TrackNumberCurrentField":
                            file.setTrackNumberCurrent(self.TrackNumberCurrentField.value())
                        if field == "TrackNumberMaximumField":
                            file.setTrackNumberMaximum(self.TrackNumberMaximumField.value())
                        if field == "DiskNumberCurrentField":
                            file.setDiskNumberCurrent(self.DiskNumberCurrentField.value())
                        if field == "DiskNumberMaximumField":
                            file.setDiskNumberMaximum(self.DiskNumberMaximumField.value())
                        if field == "TitleField":
                            file.setTitle(self.TitleField.text())
                        if field == "ArtistField":
                            file.setArtist(self.ArtistField.text())
                        if field == "AlbumField":
                            file.setAlbum(self.AlbumField.text())
                        if field == "DateField":
                            file.setDate(self.DateField.text())
                        if field == "GenreField":
                            file.setGenre(self.GenreField.text())
                        if field == "ComposerField":
                            file.setComposer(self.ComposerField.text())
                        if field == "URLField":
                            file.setURL(self.URLField.text())
                        if field == "ReplayGainField":
                            file.setReplayGain(self.ReplayGainField.value())
                        if field == "CommentField":
                            file.setComment(self.CommentField.toPlainText())
                        if field == "DescriptionField":
                            file.setDescription(self.DescriptionField.toPlainText())
                    file.saveMetadata()
        self.fieldChangedDictionary.clear()
        self.clearCSS()

    def clearCSS(self):
        for key, value in self.labelFieldMappingDictionary.items():
            value.setStyleSheet("font-weight: normal")