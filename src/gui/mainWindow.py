# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 557)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 550))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.treeView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.treeView.setAnimated(True)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.trackNumberCurrent = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackNumberCurrent.sizePolicy().hasHeightForWidth())
        self.trackNumberCurrent.setSizePolicy(sizePolicy)
        self.trackNumberCurrent.setMinimumSize(QtCore.QSize(45, 0))
        self.trackNumberCurrent.setWrapping(False)
        self.trackNumberCurrent.setFrame(True)
        self.trackNumberCurrent.setMaximum(999)
        self.trackNumberCurrent.setObjectName("trackNumberCurrent")
        self.horizontalLayout_2.addWidget(self.trackNumberCurrent)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.trackNumberMaximum = QtWidgets.QSpinBox(self.groupBox)
        self.trackNumberMaximum.setMinimumSize(QtCore.QSize(45, 0))
        self.trackNumberMaximum.setMaximum(999)
        self.trackNumberMaximum.setObjectName("trackNumberMaximum")
        self.horizontalLayout_2.addWidget(self.trackNumberMaximum)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.diskNumberCurrent = QtWidgets.QSpinBox(self.groupBox)
        self.diskNumberCurrent.setMinimumSize(QtCore.QSize(45, 0))
        self.diskNumberCurrent.setMaximum(999)
        self.diskNumberCurrent.setObjectName("diskNumberCurrent")
        self.horizontalLayout_2.addWidget(self.diskNumberCurrent)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.diskNumberMaximum = QtWidgets.QSpinBox(self.groupBox)
        self.diskNumberMaximum.setMinimumSize(QtCore.QSize(45, 0))
        self.diskNumberMaximum.setMaximum(999)
        self.diskNumberMaximum.setObjectName("diskNumberMaximum")
        self.horizontalLayout_2.addWidget(self.diskNumberMaximum)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.songTitle = QtWidgets.QLineEdit(self.groupBox)
        self.songTitle.setObjectName("songTitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.songTitle)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.songArtist = QtWidgets.QLineEdit(self.groupBox)
        self.songArtist.setObjectName("songArtist")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.songArtist)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.songAlbum = QtWidgets.QLineEdit(self.groupBox)
        self.songAlbum.setObjectName("songAlbum")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.songAlbum)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.songDate = QtWidgets.QLineEdit(self.groupBox)
        self.songDate.setStyleSheet("")
        self.songDate.setClearButtonEnabled(False)
        self.songDate.setObjectName("songDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.songDate)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.songGenre = QtWidgets.QLineEdit(self.groupBox)
        self.songGenre.setObjectName("songGenre")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.songGenre)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.songComposer = QtWidgets.QLineEdit(self.groupBox)
        self.songComposer.setObjectName("songComposer")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.songComposer)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.songURL = QtWidgets.QLineEdit(self.groupBox)
        self.songURL.setObjectName("songURL")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.songURL)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.replayGain = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.replayGain.setSuffix("")
        self.replayGain.setMinimum(-99.99)
        self.replayGain.setObjectName("replayGain")
        self.horizontalLayout_3.addWidget(self.replayGain)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.songComment = QtWidgets.QTextEdit(self.tab)
        self.songComment.setObjectName("songComment")
        self.gridLayout.addWidget(self.songComment, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.songDescription = QtWidgets.QTextEdit(self.tab_2)
        self.songDescription.setObjectName("songDescription")
        self.gridLayout_3.addWidget(self.songDescription, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.songRawMetadata = QtWidgets.QTextEdit(self.tab_3)
        self.songRawMetadata.setReadOnly(True)
        self.songRawMetadata.setObjectName("songRawMetadata")
        self.gridLayout_5.addWidget(self.songRawMetadata, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(2, 10)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpenFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenFolder.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionOpenFolder.setObjectName("actionOpenFolder")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpenFolder)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Metadata"))
        self.label_10.setText(_translate("MainWindow", "Track #"))
        self.label_12.setText(_translate("MainWindow", "/"))
        self.label_11.setText(_translate("MainWindow", "Disk #"))
        self.label_13.setText(_translate("MainWindow", "/"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.label_2.setText(_translate("MainWindow", "Artist"))
        self.label_3.setText(_translate("MainWindow", "Album"))
        self.label_4.setText(_translate("MainWindow", "Date"))
        self.label_5.setText(_translate("MainWindow", "Genre"))
        self.label_6.setText(_translate("MainWindow", "Composer"))
        self.label_7.setText(_translate("MainWindow", "URL"))
        self.label_8.setText(_translate("MainWindow", "Replay Gain"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Comment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Raw Metadata"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpenFolder.setText(_translate("MainWindow", "Open Folder..."))
        self.actionOpenFolder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
