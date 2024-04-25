import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from PIL import ImageTk

from backend import load_image, crop_image

APPLICATION_NAME = "croptoatio"

root = tk.Tk()
root.resizable(True, True)
root.call("tk", "scaling", 2.0)
root.title(APPLICATION_NAME)

var_filename = tk.StringVar()
persistient_images = []


def button_callback(*args):
    def display_in_canvas(canvas, image):
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        image_ratio = image.width / image.height
        canvas_ratio = canvas_width / canvas_height
        if image_ratio > canvas_ratio:
            new_width = canvas_width
            new_height = int(canvas_width / image_ratio)
        else:
            new_height = canvas_height
            new_width = int(canvas_height * image_ratio)
        image_as_big_as_canvas = image.resize((new_width, new_height))
        photoimage_as_big_as_canvas = ImageTk.PhotoImage(image_as_big_as_canvas)
        persistient_images.append(photoimage_as_big_as_canvas)
        x = (canvas_width - new_width) // 2
        y = (canvas_height - new_height) // 2
        canvas.create_image(x, y, anchor="nw", image=photoimage_as_big_as_canvas)

    persistient_images.clear()
    file_name = askopenfilename(filetypes=[("pliki JPEG", "*.jpeg;*.jpg")])
    var_filename.set(file_name)
    old = load_image(file_name)
    new = crop_image(old)
    new.save("cropped.jpeg")
    display_in_canvas(canvas_old, old)
    display_in_canvas(canvas_new, new)


frame0 = ttk.Frame(root)
frame1 = ttk.Frame(frame0)
frame2 = ttk.Frame(frame0)

frame0.grid(sticky="news")
frame1.grid(row=0, sticky="news")
frame2.grid(row=1, sticky="news")

label = ttk.Label(frame1, text="obrazek do przyciecia")
entry = ttk.Entry(frame1, width=40, textvariable=var_filename)
button_choose_file = ttk.Button(frame1, text="wybierz plik", command=button_callback)

label_old = ttk.Label(frame2, text="obrazek przed przycięciem")
label_new = ttk.Label(frame2, text="obrazek po przycięciu")
canvas_old = tk.Canvas(frame2, width=400, height=400, highlightbackground="black", highlightthickness=1)
canvas_new = tk.Canvas(frame2, width=400, height=400, highlightbackground="black", highlightthickness=1)

label.grid(column=0, row=0, sticky="we")
entry.grid(column=0, row=1, sticky="we")
button_choose_file.grid(column=1, row=1, sticky="e")

label_old.grid(column=0, row=0, sticky="w")
label_new.grid(column=1, row=0, sticky="w")
canvas_old.grid(column=0, row=1, sticky="we")
canvas_new.grid(column=1, row=1, sticky="we")

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", foreground='white', background='green')
style.map("TButton", background=[('active', 'lightgreen')])

for i in range(2):
    frame1.columnconfigure(i, weight=1)
    frame2.columnconfigure(i, weight=1, minsize=420)

frame1.grid_configure(padx=20, pady=20)
frame2.grid_configure(padx=20, pady=20)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=5, pady=10)

for widget in frame2.winfo_children():
    widget.grid_configure(padx=5, pady=10)

root.mainloop()
