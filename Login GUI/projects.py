from customtkinter import *  # Example import, adjust as per your library
import customtkinter
from PIL import Image

class ButtonFrame(CTkFrame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.geometry("1028x720")
        self.root.resizable(0, 0)
        self.create_widgets()



    def create_widgets(self):
        customtkinter.set_appearance_mode("system")
        # Load images (adjust paths as per your project structure)
        side_img_data = Image.open("images\pro.jpg")

        side_img = CTkImage(light_image=side_img_data, size=(1028, 720))

        # Left side image
        bg_label = CTkLabel(master=self, text="", image=side_img)
        bg_label.place(relx=0.5, rely=0.5, anchor='center')

        frame = CTkFrame(master=self, width=510, height=520)
        frame.pack_propagate(0)
        frame.pack(expand=True)

        CTkLabel(master=frame, text="Choose Project", text_color="#E44982", anchor="w", justify="center", font=("Arial Bold", 50),).pack(anchor="n",pady=(50, 5), padx=(25, 0))


        

if __name__ == "__main__":

    root = CTk()
    frame = ButtonFrame(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()