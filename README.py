# musicplayer
import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.text_widget = tk.Text(self.root, wrap="word", undo=True)
        self.text_widget.pack(expand="yes", fill="both")

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_program)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)
        self.root.title("Simple Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
                self.root.title(f"Simple Text Editor - {file_path}")

    def save_file(self):
        if not hasattr(self, 'file_path'):
            self.save_as_file()
        else:
            content = self.text_widget.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
            self.root.title(f"Simple Text Editor - {self.file_path}")

    def
