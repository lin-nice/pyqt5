import sys
from MainWindow import test
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.exit(app.exec_())
