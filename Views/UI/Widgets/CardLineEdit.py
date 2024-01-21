import string
from PySide6.QtWidgets import QLineEdit


class CardLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(CardLineEdit, self).__init__(parent)
        self.textChanged.connect(self.MatchText)
        self.readyToEdit = True

    def MatchText(self, text):
        if text is None:
            return
        self.setText(''.join(filter(str.isdigit, text)))

    def focusOutEvent(self, e):
        super(CardLineEdit, self).focusOutEvent(e)
