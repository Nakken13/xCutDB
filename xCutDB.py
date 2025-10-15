import os
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Entry, Label, Frame, Progressbar


class FileSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("xCutDB - by nakken_ ")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.selected_file = None
        self.style = Style(theme="darkly")  

        self.draw_gradient_background()
        self.create_widgets()

    def draw_gradient_background(self):
        self.canvas = tk.Canvas(self.root, width=800, height=500, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        for i in range(0, 500):
            ratio = i / 499
            r = int(128 * (1 - ratio))    
            g = int(0 * (1 - ratio))      
            b = int(255 * (1 - ratio))    
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, 800, i, fill=color)

        self.main_frame = Frame(self.canvas, bootstyle="dark", padding=30)
        self.canvas.create_window(400, 250, window=self.main_frame)

    def create_widgets(self):
        Label(self.main_frame, text="xCut - by nakken_",
            font=("Segoe UI", 14, "bold")).pack(pady=(0, 20))

        Button(self.main_frame, text="📁 Choisir un fichier",
            command=self.select_file,
            bootstyle="purple-outline", width=25).pack(pady=5)

        self.file_path_label = Label(self.main_frame, text="Aucun fichier sélectionné", wraplength=500)
        self.file_path_label.pack(pady=5)

        Label(self.main_frame, text="Nombre de lignes par fichier :").pack(pady=(20, 5))

        self.line_entry = Entry(self.main_frame, width=15, font=("Segoe UI", 11))
        self.line_entry.insert(0, "100000")
        self.line_entry.pack()

        Button(self.main_frame, text="[+] Découper le fichier",
            command=self.split_file_gui,
            bootstyle="purple", width=25).pack(pady=20)

        self.progress = Progressbar(self.main_frame, bootstyle="purple", length=250, mode="determinate")
        self.progress.pack(pady=10)


    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        if file_path:
            self.selected_file = file_path
            self.file_path_label.config(text=file_path)

    def split_file_gui(self):
        if not self.selected_file:
            messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
            return

        try:
            lines_per_file = int(self.line_entry.get())
            if lines_per_file <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif.")
            return

        self.root.after(100, lambda: self.split_file(self.selected_file, lines_per_file))

    def split_file(self, input_file_path, lines_per_file):
        try:
            total_lines = self.count_lines(input_file_path)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lire le fichier :\n{e}")
            return

        self.progress["maximum"] = total_lines
        self.progress["value"] = 0

        base_dir = os.path.dirname(input_file_path) or '.'
        base_name = os.path.basename(input_file_path)
        file_name, file_ext = os.path.splitext(base_name)

        output_dir = os.path.join(base_dir, f"{file_name}_parts")
        os.makedirs(output_dir, exist_ok=True)

        file_count = 0
        written_lines = 0

        try:
            with open(input_file_path, 'r', encoding='utf-8') as infile:
                while True:
                    lines = []
                    try:
                        for _ in range(lines_per_file):
                            line = next(infile)
                            lines.append(line)
                    except StopIteration:
                        pass

                    if not lines:
                        break

                    output_filename = os.path.join(output_dir, f"{file_name}_part{file_count:03}{file_ext}")
                    with open(output_filename, 'w', encoding='utf-8') as outfile:
                        outfile.writelines(lines)

                    written_lines += len(lines)
                    self.progress["value"] = written_lines
                    self.root.update_idletasks()

                    file_count += 1

        except Exception as e:
            messagebox.showerror("Erreur", str(e))
            return

        messagebox.showinfo("Succès", f"Découpage terminé. {file_count} fichiers créés dans :\n{output_dir}")
        self.progress["value"] = 0

    def count_lines(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSplitterApp(root)
    root.mainloop()
