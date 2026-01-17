import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox

from app.window import MainWindow #Error!


def select_image_folder() -> str | None:
    dialog = QFileDialog()
    dialog.setWindowTitle("Select Image Folder")
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    dialog.setDirectory("/home/user/Pictures")

    if dialog.exec():
        selected = dialog.selectedFiles()
        return selected[0] if selected else None

    return None


def main():
    app = QApplication(sys.argv)

    folder = select_image_folder()
    if folder is None:
        QMessageBox.information(
            None, "No Folder Selected", "No folder was selected. Exiting."
        )
        sys.exit(0)

    window = MainWindow(image_folder=folder)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
