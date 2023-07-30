from PySide6.QtWidgets import QApplication
from swipetool_ui import Ui_Widget
from widget import Widget

import sys   

app = QApplication(sys.argv)

window = Widget()
window.show()

app.exec()