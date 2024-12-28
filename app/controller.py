from PySide6.QtWidgets import QFileDialog
from PIL import Image
import pillow_heif


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

        self.parent_window.set_input_list(selected_files[0])

    def select_output_folder(self):
        selected_folder = QFileDialog.getExistingDirectory(
            parent=self.parent_window, caption="Select Output Folder", dir=""
        )
        self.parent_window.set_output_list(selected_folder)

    def convert_files(self, input_path, output_path, format):
        # TODO Multithread conversion logic
        percent = (1 / len(input_path)) * 100
        progress = 0
        for file in input_path:
            self.parent_window.set_progress(progress)
            file_output = f"{output_path}/{self.extract_filename(file)}.{format}"
            heif_file = pillow_heif.open_heif(file)
            img = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
            img.save(file_output, format)
            progress += percent

    def extract_filename(self, file_path):
        file_name_with_extension = file_path.split("/")[-1]
        file_name = file_name_with_extension.split(".")[0]

        return file_name
