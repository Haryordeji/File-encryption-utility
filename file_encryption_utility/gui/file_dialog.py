from tkinter import filedialog
import os

class FileDialog:
    def __init__(self, master):
        self.master = master

    def select_file(self):
        initial_dir = os.path.join(os.path.dirname(__file__), "..", "..", "sandbox", "input")
        file_path = filedialog.askopenfilename(initialdir=initial_dir)
        return file_path

    def save_file(self):
        initial_dir = os.path.join(os.path.dirname(__file__), "..", "..", "sandbox", "output")
        file_path = filedialog.asksaveasfilename(initialdir=initial_dir)
        return file_path