import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from converter import convert_heic

class FileConverterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Converter")
        self.root.geometry("500x450")
        
        # Instance variables to hold the state
        self.selected_files = []
        self.output_folder = ""
        self.convert_button_ready = [False, False]
        
        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        """Create the UI components."""
        # Label and Listbox for file selection
        self.files_label = tk.Label(self.root, text="Selected Files:")
        self.files_label.pack(pady=10)

        # Listbox to show selected files
        self.file_listbox = tk.Listbox(self.root, height=6, width=50, selectmode=tk.SINGLE)
        self.file_listbox.pack(pady=5)

        # Button to select files
        self.select_files_button = tk.Button(self.root, text="Select Files", command=self.choose_files)
        self.select_files_button.pack(pady=5)

        # Label and Entry for output folder selection
        self.output_folder_label = tk.Label(self.root, text="Output Folder:")
        self.output_folder_label.pack(pady=10)

        # Entry widget for output folder path
        self.output_folder_entry = tk.Entry(self.root, width=40)
        self.output_folder_entry.pack(pady=5)

        # Button to select output folder
        self.select_output_button = tk.Button(self.root, text="Select Output Folder", command=self.choose_output_folder)
        self.select_output_button.pack(pady=5)

        # Label and Combobox for output file format
        self.format_label = tk.Label(self.root, text="Choose the output file format:")
        self.format_label.pack(pady=10)

        # Combobox for selecting output file format (jpg or png)
        self.file_format = ttk.Combobox(self.root, values=["jpeg", "png"], state="normal", width=15)
        self.file_format.set("jpeg")  # Set default value to "jpg"
        self.file_format.pack(pady=5)

        # Convert button (initially disabled)
        self.convert_button = tk.Button(self.root, text="Convert", state=tk.DISABLED, command=self.convert_files)
        self.convert_button.pack(pady=20)

    def choose_files(self):
        """Open file explorer to select multiple files."""
        self.selected_files = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=(("HEIC files", "*.heic"), ("All files", "*.*"))
        )
        if self.selected_files:
            # Clear the listbox and update it with selected files
            self.file_listbox.delete(0, tk.END)
            for file in self.selected_files:
                self.file_listbox.insert(tk.END, file)
            self.convert_button_ready[0] = True  # Enable Convert button
        else:
            self.convert_button_ready[0] = False
        
        self.is_convert_ready()

    def choose_output_folder(self):
        """Open file explorer to select an output folder."""
        self.output_folder = filedialog.askdirectory(title="Select Output Folder")
        if self.output_folder:
            self.output_folder_entry.delete(0, tk.END)  # Clear current text
            self.output_folder_entry.insert(tk.END, self.output_folder)  # Insert new folder path
            self.convert_button_ready[-1] = True
        else:
            self.convert_button_ready[-1] = False
        
        self.is_convert_ready()

    def convert_files(self):
        """Convert selected files."""
        if not self.selected_files or not self.output_folder or not self.file_format.get():
            messagebox.showerror("Error", "Please select files, output location, and file format!")
            return
        selected_format = self.file_format.get()
        convert_heic(self.selected_files, self.output_folder, selected_format)
    
    def is_convert_ready(self):
        if self.convert_button_ready[0] and self.convert_button_ready[-1]:
            self.convert_button.config(state=tk.NORMAL)
        else:
            self.convert_button.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()

# Initialize the FileConverterApp with the root window
app = FileConverterUI(root)

# Run the application
root.mainloop()