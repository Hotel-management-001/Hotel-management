from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x650+120+80")

        # ================= TITLE =================
        Label(
            self.root,
            text="ROOM BOOKING DETAILS",
            font=("times new roman", 18, "bold"),
            bg="black", fg="gold", bd=4, relief=RIDGE
        ).place(x=0, y=0, width=1295, height=50)

        # ================= HEADER IMAGE =================
        base_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(base_dir, "images", "hotel2.png")
        try:
            img = Image.open(logo_path)
            img = img.resize((1295, 50), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            Label(self.root, image=self.photoimg, bd=2, relief=RIDGE
                  ).place(x=0, y=50, width=1295, height=50)
        except Exception:
            Label(
                self.root, text="HOTEL MANAGEMENT SYSTEM",
                font=("arial", 17, "bold"), bg="white"
            ).place(x=0, y=50, width=1295, height=50)

        # ================= LEFT FRAME =================
        # FIX: ab ye try/except ke BAHAR hai, isliye hamesha dikhega
        left = LabelFrame(
            self.root, bd=2, relief=RIDGE,
            text="ROOMBOOKING DETAILS",
            font=("times new roman", 12, "bold"),
            padx=5, pady=3
        )
        left.place(x=5, y=105, width=425, height=535)

        # Yahan se aage room ke fields (customer ref, check-in, check-out,
        # room type, etc.) aur buttons add karte jao.


if __name__ == "__main__":
    root = Tk()
    app = Roombooking(root)
    root.mainloop()