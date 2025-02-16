import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
from tkinter import filedialog
from pathlib import Path


current_file = None


def show_about():
    msgbox.showinfo("This is a Menu Demo!")


def on_new():
    global current_file

    confirm = msgbox.askyesno(
        "Open a new File", "Do you want to save currently open file?")

    if confirm:
        save_file()

    text_area.delete("1.0", "end")
    root.title("Untitled - Notepad")


def save_file():
    global current_file
    if current_file:
        Path(current_file).write_text(
            text_area.get("1.0", "end-1c"), encoding='utf-8')

    else:
        saveAs_file()


def saveAs_file():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return

    current_file = file_path
    Path(current_file).write_text(
        text_area.get("1.0", "end-1c"), encoding='utf-8')
    root.title(Path(current_file).name)


def open_file():
    global current_file
    current_file = filedialog.askopenfilename()
    if not current_file:
        return
    file_name = Path(current_file)
    # print()
    content = file_name.read_text(encoding="utf-8")
    text_area.delete("1.0", "end")
    text_area.insert("end", content)
    root.title(file_name.name)


root = tk.Tk()
root.title("Untitled - Notepad")
# root.state("zoomed")
root.geometry("400x300")
# root.attributes("-fullscreen", True)
# root.option_add("*Font", ("Arial", 16))  # Change font family & size


# Menu Frame inside the root
menu_frame = tk.Frame(root, bg='lightgray')
menu_frame.pack(fill="x")

# Menu Bar inside the menu frame
menu_bar = tk.Menu(menu_frame)
root.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=on_new)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=saveAs_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)


menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Help', menu=help_menu)

# Text Frame inside the root
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True)

# Text Widget inside the Text frame
text_area = tk.Text(text_frame, wrap="word", font=("Arial", 16))
text_area.pack(side='left', fill="both", expand=True, padx=5, pady=5)


# Scrollbar inside the Text Frame
scroll_y = tk.Scrollbar(text_frame, orient="vertical", command=text_area.yview)
scroll_y.pack(side="right", fill="y")
text_area.configure(yscrollcommand=scroll_y.set)

root.mainloop()
