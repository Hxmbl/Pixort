from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, Qt

from core.loader import load_images
from core.state import ReviewState
from ui.grid_view import ImageGridView
from ui.image_viewer import ImageViewer


class MainWindow(QMainWindow):
    def __init__(self, image_folder: str):
        super().__init__()

        self.setWindowTitle("Image Sorter")

        # Load images + state
        self.image_paths = load_images(image_folder)
        self.state = ReviewState(self.image_paths)

        # Grid view
        self.grid = ImageGridView(self.image_paths)

        # CONNECT SIGNAL
        self.grid.startReviewRequested.connect(self.start_review)

        self.setCentralWidget(self.grid)

        # Scroll after layout
        QTimer.singleShot(0, self.grid.scroll_to_bottom_right)

    # ---------- REVIEW MODE ----------

    def start_review(self):
        self.viewer = ImageViewer()
        self.setCentralWidget(self.viewer)
        self.showFullScreen()
        self.show_current_image()

    def show_current_image(self):
        path = self.state.current()
        if path is None:
            self.end_review()
            return

        self.viewer.show_image(path)

    def keyPressEvent(self, event):
        if not hasattr(self, "viewer"):
            return

        if event.key() == Qt.Key_Right:
            self.state.keep()
            self.show_current_image()

        elif event.key() == Qt.Key_Left:
            self.state.delete()
            self.show_current_image()

    def end_review(self):
        self.showNormal()
        self.setCentralWidget(self.grid)
        self.grid.update_overlays(self.state)
