import os
import sys
import base64

from PySide6.QtGui import (
    QIcon,
    QCursor
)
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QApplication,
    QFileDialog,
)

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setStyleSheet("background-color: white")

        main_size = QSize(450,450)

        self.setWindowTitle("Image Recoder/Decoder")
        self.setFixedSize(QSize(500, 500))

        self.file_zone = QPushButton()
        self.file_zone.setFixedSize(main_size)
        self.file_zone.setIcon(QIcon("drag drop.png"))
        self.file_zone.setIconSize(main_size)
        self.file_zone.setStyleSheet("QPushButton {border: 0px; background-color: transparent}")
        self.file_zone.setCursor(QCursor(Qt.PointingHandCursor))
        self.file_zone.clicked.connect(self.main_logic)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.file_zone)
        self.main_layout.setAlignment(Qt.AlignCenter)

        container = QWidget()
        container.setLayout(self.main_layout)

        self.setCentralWidget(container)

    def main_logic(self):
        file_path = QFileDialog.getOpenFileName(self, filter="Images (*.png, *.jpg, *.jpeg);; Text (*.txt)")[0]
        if file_path:
            self.process_file(file_path)
        else:
            pass

    def process_file(self, file_path):
        file_split = os.path.splitext(file_path)

        if file_split[1] == ".txt":
            with open(file_path, 'r') as f:
                image_s = f.read()
                image_s = image_s.replace('data:image/png;base64,', '')

            with open(r"{}.jpeg".format(file_split[0]), "wb") as f:
                f.write(base64.b64decode(image_s))
        else:
            with open(file_path, "rb") as f:
                image = f.read()
                image_s = str(base64.b64encode(image).decode("utf-8"))

            with open(r"{}.txt".format(file_split[0]), "w") as f:
                f.write(image_s)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                self.process_file(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    app.exec()
