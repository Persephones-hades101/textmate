import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
from tkinter import filedialog
from pathlib import Path


class TEXT_MATE:
    def __init__(self):

        self.current_file = None

        self.root = tk.Tk()
        self.root.title("Untitled - Notepad")
        # root.state("zoomed")
        self.root.geometry("400x300")
        # root.attributes("-fullscreen", True)
        # root.option_add("*Font", ("Arial", 16))  # Change font family & size

        # Menu Frame inside the root
        menu_frame = tk.Frame(self.root, bg='lightgray')
        menu_frame.pack(fill="x")

        # Menu Bar inside the menu frame
        menu_bar = tk.Menu(menu_frame)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='New', command=self.on_new)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save As', command=self.saveAs_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menu_bar.add_cascade(label='File', menu=file_menu)
        menu_bar.add_cascade(label='Help', menu=help_menu)

        # Text Frame inside the root
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill="both", expand=True)

        # Text Widget inside the Text frame
        self.text_area = tk.Text(text_frame, wrap="word", font=("Arial", 16))
        self.text_area.pack(side='left', fill="both",
                            expand=True, padx=5, pady=5)

        # Scrollbar inside the Text Frame
        scroll_y = tk.Scrollbar(
            text_frame, orient="vertical", command=self.text_area.yview)
        scroll_y.pack(side="right", fill="y")
        self.text_area.configure(yscrollcommand=scroll_y.set)

        self.root.mainloop()

    def show_about(self):
        msgbox.showinfo(
            "About TextMate", "TextMate is a simple text editor built with Tkinter.\n\nDeveloped by Sudhanshu.")

    def on_new(self):

        confirm = msgbox.askyesno(
            "Open a new File", "Do you want to save currently open file?")

        if confirm:
            self.save_file()

        self.text_area.delete("1.0", "end")
        self.root.title("Untitled - Notepad")

    def save_file(self):
        if self.current_file:
            Path(self.current_file).write_text(
                self.text_area.get("1.0", "end-1c"), encoding='utf-8')

        else:
            self.saveAs_file()

    def saveAs_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        self.current_file = file_path
        Path(file_path).write_text(
            self.text_area.get("1.0", "end-1c"), encoding='utf-8')
        self.root.title(Path(file_path).name)

    def open_file(self):
        self.current_file = filedialog.askopenfilename()
        if not self.current_file:
            return
        file_name = Path(self.current_file)
        # print()
        content = file_name.read_text(encoding="utf-8")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", content)
        self.root.title(file_name.name)


TEXT_MATE()
