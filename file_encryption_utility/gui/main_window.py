import tkinter as tk
from tkinter import ttk, messagebox
import os
from file_encryption_utility.gui.file_dialog import FileDialog
from file_encryption_utility.crypto.encryption import encrypt_file, decrypt_file, get_output_path
from file_encryption_utility.utils.file_handler import secure_delete_file

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("File Encryption Utility")
        self.master.geometry("600x400")

        self.file_dialog = FileDialog(self.master)

        self.create_widgets()

    def create_widgets(self):
        # File selection
        ttk.Button(self.master, text="Select File", command=self.select_file, cursor="hand2").pack(pady=10)
        self.file_label = ttk.Label(self.master, text="No file selected")
        self.file_label.pack()

        # Password input
        ttk.Label(self.master, text="Password:").pack()
        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.pack()

        # Encryption/Decryption buttons
        ttk.Button(self.master, text="Encrypt", command=self.encrypt, cursor="hand2").pack(pady=5)
        ttk.Button(self.master, text="Decrypt", command=self.decrypt, cursor="hand2").pack(pady=5)

        # Secure delete button
        ttk.Button(self.master, text="Secure Delete", command=self.secure_delete, cursor="hand2").pack(pady=5)

    def select_file(self):
        file_path = self.file_dialog.select_file()
        if file_path:
            self.file_label.config(text=file_path)

    def encrypt(self):
        file_path = self.file_label.cget("text")
        password = self.password_entry.get()
        if file_path != "No file selected" and password:
            try:
                encrypt_file(file_path, password)
                output_path = os.path.join(get_output_path(), f"{os.path.basename(file_path)}.encrypted")
                messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {output_path}")
                self.master.quit()
            except Exception as e:
                messagebox.showerror("Error", f"Encryption failed: {str(e)}")
        else:
            messagebox.showerror("Error", "Please select a file and enter a password.")

    def decrypt(self):
        file_path = self.file_label.cget("text")
        password = self.password_entry.get()
        if file_path != "No file selected" and password:
            try:
                decrypt_file(file_path, password)
                output_path = os.path.join(get_output_path(), f"decrypted_{os.path.basename(file_path)[:-10]}")
                messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {output_path}")
                self.master.quit()
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {str(e)}")
        else:
            messagebox.showerror("Error", "Please select a file and enter a password.")

    def secure_delete(self):
        file_path = self.file_label.cget("text")
        if file_path != "No file selected":
            try:
                secure_delete_file(file_path)
                messagebox.showinfo("Success", "File securely deleted!")
                self.master.quit()
            except Exception as e:
                messagebox.showerror("Error", f"Secure deletion failed: {str(e)}")
        else:
            messagebox.showerror("Error", "Please select a file to delete.")