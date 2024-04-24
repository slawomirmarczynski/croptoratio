import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master  # główne okno aplikacji
        self.filename = tk.StringVar()  # nazwa pliku do wczytania

        # Pole tekstowe do wprowadzania nazwy pliku
        self.entry = tk.Entry(master, textvariable=self.filename)
        self.entry.pack()

        # Przycisk do wyboru pliku
        self.choose_button = tk.Button(master, text="Wybierz plik", command=self.choose_file)
        self.choose_button.pack()

        # Przycisk do wczytania obrazu
        self.load_button = tk.Button(master, text="Załaduj", command=self.load_image)
        self.load_button.pack()

        # Dwa płótna do wyświetlania obrazów
        self.canvas1 = tk.Canvas(master, width=500, height=500)
        self.canvas1.pack(side="left")
        self.canvas2 = tk.Canvas(master, width=500, height=500)
        self.canvas2.pack(side="right")

        # Przycisk do przycinania i zapisywania obrazu
        self.crop_button = tk.Button(master, text="Przytnij i zapisz", command=self.crop_and_save)
        self.crop_button.pack()

    def choose_file(self):
        # Wybór pliku do wczytania
        self.filename.set(filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpeg")]))

    def load_image(self):
        # Wczytanie obrazu i wyświetlenie go na pierwszym płótnie
        self.image = Image.open(self.filename.get())
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas1.create_image(0, 0, anchor="nw", image=self.photo)

    def crop_and_save(self):
        # Przycinanie obrazu do założonych proporcji i zapisanie go
        width, height = self.image.size
        aspect_ratio = 3/2
        new_width = min(width, int(height * aspect_ratio))
        new_height = int(new_width / aspect_ratio)

        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2

        self.cropped_image = self.image.crop((left, top, right, bottom))
        self.cropped_photo = ImageTk.PhotoImage(self.cropped_image)
        self.canvas2.create_image(0, 0, anchor="nw", image=self.cropped_photo)

        # Poprawka tutaj
        if "." in self.filename.get():
            base, ext = self.filename.get().rsplit(".", maxsplit=1)
        else:
            base = self.filename.get()
            ext = "jpeg"
        self.cropped_image.save(f"{base}_cropped.{ext}")

root = tk.Tk()
app = App(root)
root.mainloop()
