from PySide6.QtWidgets import QMainWindow
from core.loader import load_images
from ui.grid_view import ImageGridView
from PySide6.QtCore import QTimer
from ui.viewer import ImageViewer

class MainWindow(QMainWindow):
    def __init__(self, image_folder: str):
        super().__init__()
        self.image_folder = image_folder
        self.setWindowTitle("Image Sorter")

        self.image_paths = load_images(image_folder)
        self.grid = ImageGridView(self.image_paths)
        self.setCentralWidget(self.grid)

        # Let Qt finish layout, then scroll
        QTimer.singleShot(50, self.grid.scroll_to_bottom_right)

    def start_sorting(self):
        self.current_index = 0
        self.show_next_image()

    def show_next_image(self):
        if self.current_index >= len(self.image_paths):
            self.show_grid_results()
            return

        image_path = self.image_paths[self.current_index]

        self.viewer = ImageViewer(
            image_path=image_path,
            keep_callback=self.keep_image,
            delete_callback=self.delete_image
        )
        self.setCentralWidget(self.viewer)

    def keep_image(self):
        self.current_index += 1
        self.show_next_image()

    def delete_image(self):
        # mark image for deletion
        self.image_paths[self.current_index] = None
        self.current_index += 1
        self.show_next_image()