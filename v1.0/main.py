import sys
from PyQt4.QtGui import QApplication, QDialog
from gui import Ui_WaveMixer
 
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_WaveMixer()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
