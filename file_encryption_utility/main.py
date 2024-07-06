import tkinter as tk
from file_encryption_utility.gui.main_window import MainWindow
from file_encryption_utility.utils.file_handler import create_sandbox_directories

def main():
    create_sandbox_directories()
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
    root.destroy()

if __name__ == "__main__":
    main()