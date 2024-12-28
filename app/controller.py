from PySide6.QtWidgets import QFileDialog


class controller:
    def __init__(self, parent_window):
        self.parent_window = parent_window

    def select_files(self):
        # TODO change starting dir
        selected_files = QFileDialog.getOpenFileNames(
            parent=self.parent_window,
            caption="Select HEIC Files",
            dir="",
            filter="Heic Files (*.heic);;All Files (*)",
        )

        return selected_files

    def select_output_folder(self):
        selected_folder = QFileDialog.getExistingDirectory(
            parent=self.parent_window, caption="Select Output Folder", dir=""
        )

    def convert_files(self):
        # TODO Multithread conversion logic
        print("Converting")
