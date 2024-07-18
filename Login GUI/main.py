import customtkinter
from PIL import Image
from customtkinter import *
from login import Login

def main():
    
    root = CTk()

    login_frame = Login(root)
    login_frame.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()

