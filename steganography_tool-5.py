from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from stegano import lsb

root = Tk()
root.title("Steganography - Hide Message")
root.geometry("700x500")
root.resizable(False, False)
root.config(bg="#2f4155")

# ---------------- ICON FIX ----------------
try:
    img = Image.open("logo.jpg")   # make sure file exists
    icon = ImageTk.PhotoImage(img)
    root.iconphoto(False, icon)
except:
    print("Icon not found, skipping...")

# ---------------- FUNCTIONS ----------------
def showimage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select Image",
        filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"),)
    )
    if filename:
        img = Image.open(filename)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)
        lbl_image.config(image=img)
        lbl_image.image = img

def hide_data():
    message = text1.get(1.0, END)
    if filename and message.strip() != "":
        secret = lsb.hide(filename, message)
        secret.save("hidden.png")
        messagebox.showinfo("Success", "Message hidden successfully!")
    else:
        messagebox.showerror("Error", "Select image and enter message")

def show_data():
    if filename:
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
        text1.insert(END, clear_message)
    else:
        messagebox.showerror("Error", "Select image first")

# ---------------- UI ----------------
Label(root, text="Steganography Tool", font=("Arial", 20, "bold"), bg="#2f4155", fg="white").pack(pady=10)

# Image area
lbl_image = Label(root, bg="gray")
lbl_image.pack(pady=10)

# Buttons
Button(root, text="Select Image", command=showimage, width=10).pack(pady=3)

# Text box
text1 = Text(root, width=30, height=3)
text1.pack(pady=5)

# Action buttons
Button(root, text="Hide Message", command=hide_data, width=10, bg="green", fg="white").pack(pady=5)
Button(root, text="Show Message", command=show_data, width=10, bg="blue", fg="white").pack(pady=5)

# Run app
root.mainloop()