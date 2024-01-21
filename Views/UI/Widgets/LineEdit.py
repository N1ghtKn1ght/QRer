import string
from PySide6.QtWidgets import QLineEdit, QMessageBox


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)
        self.textChanged.connect(self.MatchText)
        self.readyToEdit = True

    def MatchText(self, text):
        if text is None:
            return
        self.setText(''.join(filter(str.isalpha, text)))

    def focusOutEvent(self, e):
        super(LineEdit, self).focusOutEvent(e)
