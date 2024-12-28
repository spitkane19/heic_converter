stylesheet = """
    * {
        font-family: "Arial", sans-serif;
        font-size: 14px;
        color: #E0E0E0;
    }

    QMainWindow {
        background-color: #121212;
    }

    QFrame {
        background-color: #121212;
        border: 2px solid #292929;
        border-radius: 10px;
    }

    QPushButton {
        background-color: #333333;
        color: #E0E0E0;
        border: 2px solid #444444;
        border-radius: 10px;
        padding: 8px;
    }

    QPushButton:hover {
        background-color: #555555;
    }

    QPushButton:pressed {
        background-color: #222222;
    }

    QListWidget {
        background-color: #2A2A2A;
        color: #E0E0E0;
        border: 2px solid #292929;
        border-radius: 10px; 
        padding: 5px; 
    }

    QListWidget::item:selected {
        background-color: #444444;
        color: #FFFFFF; 
    }

    QLineEdit {
        background-color: #2A2A2A;
        color: #E0E0E0; 
        border: 2px solid #292929; 
        border-radius: 10px; 
        padding: 5px;
    }
    QComboBox {
        background-color: #333333;
        color: #E0E0E0;
        border: 2px solid #292929;
        border-radius: 10px;
        padding: 5px;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 20px;
        border-left: 1px solid #292929;
        background-color: #4D4D4D;
        border-radius: 10px;
        padding: 5px;
    }

    QComboBox QAbstractItemView {
        background-color: #333333;
        color: #E0E0E0;
        border: 1px solid #292929;
        selection-background-color: #444444;
        selection-color: #FFFFFF;
    }

    QProgressBar {
        background-color: #292929; 
        border: 2px solid #444444;
        border-radius: 10px; 
        text-align: center; 
        color: #E0E0E0; 
    }

    QProgressBar::chunk {
        background-color: #4CAF50; 
        border-radius: 10px; 
    }
    
"""
