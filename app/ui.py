from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QFrame,
    QProgressBar,
    QLineEdit,
)
from PySide6.QtGui import QPixmap

from app.controller import controller


class ui_window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Heic Converter")
        self.resize(800, 500)
        self.controller = controller(self)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.central_widget.setLayout(QVBoxLayout())

        self.vertical_box = QVBoxLayout()

        self.image_label = QLabel("No image loaded")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_box.layout().addWidget(self.image_label)

        self.image_path = "resources/WIN.png"
        self.load_image(self.image_path)
        self.image_label.setFixedSize(800, 100)

        self.file_chooser_frame = self.create_recessed_frame()
        self.file_chooser_layout = QHBoxLayout(self.file_chooser_frame)

        self.select_button = QPushButton("Choose files to be converted", parent=self)
        self.select_button.released.connect(self.controller.select_files)
        self.file_chooser_layout.addWidget(self.select_button)

        self.files_chosen = QListWidget()
        self.files_chosen.setFixedSize(400, 200)
        self.file_chooser_layout.addWidget(self.files_chosen)

        self.vertical_box.addWidget(self.file_chooser_frame)

        self.output_frame = self.create_recessed_frame()
        self.output_layout = QHBoxLayout(self.output_frame)

        self.output_button = QPushButton("Choose output folder", parent=self)
        self.output_button.released.connect(self.controller.select_output_folder)
        self.output_layout.addWidget(self.output_button)

        self.output_list = QLineEdit()
        self.output_list.setDisabled(True)
        self.output_layout.addWidget(self.output_list)

        self.vertical_box.addWidget(self.output_frame)

        self.format_frame = self.create_recessed_frame()
        self.format_layout = QHBoxLayout(self.format_frame)

        self.format_label = QLineEdit("Choose file format: ")
        self.format_label.setDisabled(True)
        self.format_layout.addWidget(self.format_label)

        self.format_combobox = QComboBox()
        self.format_combobox.addItems(["JPG", "PNG"])
        self.format_combobox.setCurrentText("JPG")
        self.format_layout.addWidget(self.format_combobox)

        self.vertical_box.addWidget(self.format_frame)

        self.convert_button = QPushButton("Convert chosen files")
        self.convert_button.released.connect(self.start_conversion)
        self.vertical_box.addWidget(self.convert_button)
        self.progress_bar = QProgressBar(value=0)
        self.vertical_box.addWidget(self.progress_bar)

        self.central_widget.layout().addLayout(self.vertical_box)

        self.input_list = []
        self.output_location = None

    def create_recessed_frame(self):
        """Helper function to create a recessed frame."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Sunken)
        return frame

    def load_image(self, image_path):
        """Load the PNG image and display it."""
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
        else:
            self.image_label.setText("Failed to load image")

    def set_output_list(self, output):
        self.output_list.setText(output)
        self.output_location = output

    def set_input_list(self, input):
        for file in input:
            self.files_chosen.addItem(file)

        self.input_list = input

    def set_progress(self, prog):
        self.progress_bar.setValue(prog)

    def start_conversion(self):
        print(self.format_combobox.currentText())
        self.controller.convert_files(
            self.input_list, self.output_location, self.format_combobox.currentText()
        )
