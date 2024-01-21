import qrcode
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QColorDialog
from Views.PY.ui_mainwindow import Ui_MainWindow
from PIL import ImageQt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Ready.clicked.connect(self.ClickReady)
        self.ui.save.clicked.connect(self.Save)

        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.IsGenerate = False

    def Save(self):
        if not self.IsGenerate:
            QMessageBox.information(self, "Ошибка", "Qr-код не сгенерирован")
            return
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "Images (*.png)", options=options)

        if filePath:
            self.ui.qrCode.pixmap().save(filePath, "PNG")

    def ClickReady(self):
        self.IsGenerate = True
        qr = qrcode.QRCode()
        param = [self.ui.Name.text(), self.ui.Surname.text(), self.ui.Email.text(),
                 self.ui.Card.text(),
                 self.ui.Date.date().toString('MMMM yyyy'),
                 self.ui.CVV.text()]
        for e in param:
            if e is None or not e:
                QMessageBox.information(self, "Ошибка", "Неверно введены данные")
                return
        fillColour = QColorDialog.getColor()
        colour = "#000000"
        if fillColour.isValid():
            colour = fillColour.name()
        data = "Name {0} Surname {1} Email {2}\n Card {3} Date {4} CVV {5}" \
            .format(self.ui.Name.text(), self.ui.Surname.text(), self.ui.Email.text(), self.ui.Card.text(),
                    self.ui.Date.date().toString('MMMM yyyy'), self.ui.CVV.text())
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color=colour)

        qr_img_pixmap = QPixmap.fromImage(ImageQt.ImageQt(qr_img))
        self.ui.qrCode.setPixmap(qr_img_pixmap)
