
import sys
import PyQt5
from gui.application import Application


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    win = Application()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()