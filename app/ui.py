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

        # Create the main vertical box
        self.vertical_box = QVBoxLayout()

        # QLabel to display the image
        self.image_label = QLabel("No image loaded")
        self.image_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )  # Center-align the image
        self.vertical_box.layout().addWidget(self.image_label)

        # Set the path of your PNG image here
        self.image_path = "resources/heic_logo.png"
        self.load_image(self.image_path)

        # Add recessed frame for file chooser
        self.file_chooser_frame = self.create_recessed_frame()
        self.file_chooser_layout = QHBoxLayout(self.file_chooser_frame)

        self.select_button = QPushButton("Choose files to be converted", parent=self)
        self.select_button.released.connect(self.controller.select_files)
        self.file_chooser_layout.addWidget(self.select_button)

        self.files_chosen = QListWidget()
        self.files_chosen.setFixedSize(400, 200)
        self.file_chooser_layout.addWidget(self.files_chosen)

        self.vertical_box.addWidget(self.file_chooser_frame)

        # Add recessed frame for output layout
        self.output_frame = self.create_recessed_frame()
        self.output_layout = QHBoxLayout(self.output_frame)

        self.output_button = QPushButton("Choose output folder", parent=self)
        self.output_button.released.connect(self.controller.select_output_folder)
        self.output_layout.addWidget(self.output_button)

        self.output_list = QLineEdit()
        self.output_list.setDisabled(True)
        self.output_layout.addWidget(self.output_list)

        self.vertical_box.addWidget(self.output_frame)

        # Add recessed frame for format layout
        self.format_frame = self.create_recessed_frame()
        self.format_layout = QHBoxLayout(self.format_frame)

        self.format_label = QLabel("Choose file format: ")
        self.format_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.format_layout.addWidget(self.format_label)

        self.format_combobox = QComboBox()
        self.format_combobox.addItems(["JPG", "PNG"])
        self.format_combobox.setCurrentText("JPG")
        self.format_layout.addWidget(self.format_combobox)

        self.vertical_box.addWidget(self.format_frame)

        # Add the convert button
        self.convert_button = QPushButton("Convert chosen files")
        self.convert_button.released.connect(self.controller.convert_files)
        self.vertical_box.addWidget(self.convert_button)
        self.progress_bar = QProgressBar(value=0)
        self.vertical_box.addWidget(self.progress_bar)

        # Add the main vertical layout to the central widget
        self.central_widget.layout().addLayout(self.vertical_box)

    def create_recessed_frame(self):
        """Helper function to create a recessed frame."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Sunken)
        return frame

    def load_image(self, image_path):
        """Load the PNG image and display it."""
        pixmap = QPixmap(image_path)  # Load the PNG file into a QPixmap
        if not pixmap.isNull():  # Check if the image loaded successfully
            self.image_label.setPixmap(pixmap)  # Display the QPixmap on the QLabel
            self.image_label.setScaledContents(
                True
            )  # Allow scaling to fit the QLabel size
        else:
            self.image_label.setText("Failed to load image")

    def set_output_list(self, output):
        self.output_list.setText(output)
