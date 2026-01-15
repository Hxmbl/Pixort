from PySide6.QtWidgets import QMainWindow

from core.loader import load_images
from ui.grid_view import ImageGridView


class MainWindow(QMainWindow):
    def __init__(self, image_folder: str):
        super().__init__()

        self.image_folder = image_folder
        self.setWindowTitle("Image Sorter")

        image_paths = load_images(image_folder)

        grid = ImageGridView(image_paths)
        self.setCentralWidget(grid)
