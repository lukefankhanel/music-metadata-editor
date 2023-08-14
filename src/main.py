
import sys
import PyQt5
from gui.application import Application


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    # app.setStyle("fusion")
    win = Application()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

# import sys

# from PyQt5 import QtCore, QtGui, QtWidgets


# class TabBarStyle(QtWidgets.QProxyStyle):
#     def drawControl(self, element, option, painter, widget=None):
#         index = -1
#         if element == QtWidgets.QStyle.CE_TabBarTab:
#             if isinstance(widget, TabBar):
#                 for i in widget.fonts.keys():
#                     if widget.tabRect(i) == option.rect:
#                         index = i
#                         break
#             if index > -1:
#                 painter.save()
#                 painter.setFont(widget.fonts[index])
#         super(TabBarStyle, self).drawControl(element, option, painter, widget)
#         if index > -1:
#             painter.restore()


# class TabBar(QtWidgets.QTabBar):
#     def __init__(self, parent=None):
#         super(TabBar, self).__init__(parent)
#         self._fonts = dict()

#     @property
#     def fonts(self):
#         return self._fonts


# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)

#         self.tab_widget = QtWidgets.QTabWidget()
#         self.setCentralWidget(self.tab_widget)

#         self.tab_bar = TabBar()
#         self.tabbar_style = TabBarStyle(self.tab_bar.style())
#         self.tab_bar.setStyle(self.tabbar_style)
#         self.tab_widget.setTabBar(self.tab_bar)

#         self.tab_widget.addTab(QtWidgets.QWidget(), "Foo")
#         self.tab_widget.addTab(QtWidgets.QWidget(), "Bar")
#         self.tab_widget.addTab(QtWidgets.QWidget(), "Baz")

#         font = self.tab_widget.font()
#         font.setBold(True)
#         self.tab_bar.fonts[1] = font
#         self.tab_bar.fonts[10] = font
#         print(self.tab_bar.fonts)
#         self.tab_bar.update()


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     app.setStyle("fusion")
#     w = MainWindow()
#     w.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()