import tkinter as tk
from tkinter import messagebox


class TwoInputDialog:
    def __init__(self, parent, title, label1, label2):
        self.result = None  # Store input values
        self.dialog = tk.Toplevel(parent)  # Store the dialog window
        self.dialog.title(title)

        tk.Label(self.dialog, text=label1).grid(
            row=0, column=0, padx=5, pady=5)
        tk.Label(self.dialog, text=label2).grid(
            row=1, column=0, padx=5, pady=5)

        self.entry1 = tk.Entry(self.dialog)
        self.entry2 = tk.Entry(self.dialog)

        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.dialog, text="OK", command=self.validate_inputs).grid(
            row=2, column=0, columnspan=2, pady=5)

        self.dialog.transient(parent)
        self.dialog.grab_set()
        # Pause execution until dialog is closed
        parent.wait_window(self.dialog)

    def validate_inputs(self):
        input1 = self.entry1.get().strip()
        input2 = self.entry2.get().strip()

        if not input1:  # Check if either field is empty
            messagebox.showerror("Input Error", "first fields is required!")
            return  # Do not close the dialog

        if not input2:
            self.result = (input1, '')
        self.result = (input1, input2)
        self.dialog.destroy()  # Close dialog if inputs are valid


def get_inputs(root):
    dialog = TwoInputDialog(root, title="Find and Replace",
                            label1="Pattern to replace", label2="Replace with")
    return dialog.result
