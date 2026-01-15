from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ImageViewer(QWidget):
    def __init__(self, image_path: str, keep_callback, delete_callback):
        super().__init__()
        self.keep_callback = keep_callback
        self.delete_callback = delete_callback

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Image
        pixmap = QPixmap(image_path)
        self.image_label = QLabel()
        self.image_label.setPixmap(pixmap.scaled(
            self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        # Buttons
        button_layout = QHBoxLayout()
        keep_btn = QPushButton("Keep (→)")
        delete_btn = QPushButton("Delete (←)")
        keep_btn.clicked.connect(self.keep_callback)
        delete_btn.clicked.connect(self.delete_callback)
        button_layout.addWidget(delete_btn)
        button_layout.addWidget(keep_btn)
        layout.addLayout(button_layout)

        # Make fullscreen
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.keep_callback()
        elif event.key() == Qt.Key_Left:
            self.delete_callback()
