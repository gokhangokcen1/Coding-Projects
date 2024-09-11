import tkinter as tk
from tkinter import filedialog, messagebox

# Ana uygulama
class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

        # Menü oluşturma
        self.create_menu()

        # Metin alanı
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Kaydedilecek dosya yolu
        self.file_path = None

    def create_menu(self):
        # Menü çubuğu
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Menü bar
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Yardım 
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("Notepad - New File")

    def open_file(self):
        self.file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_path:
            with open(self.file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.root.title(f"Notepad - {self.file_path}")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"Notepad - {self.file_path}")

    def show_about(self):
        messagebox.showinfo("About", "github.com/gokhangokcen1")

# Ana pencere
if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
