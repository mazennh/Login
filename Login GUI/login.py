from customtkinter import *
from PIL import Image
from register import Register  # Import Register from register.py
import customtkinter

class Login(CTkFrame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.geometry("1028x720")
        self.root.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        customtkinter.set_appearance_mode("system")
        # Load images (adjust paths as per your project structure)
        side_img_data = Image.open("images\side-img.png")
        email_icon_data = Image.open("images\email.png")
        password_icon_data = Image.open("images\password.png")

        side_img = CTkImage(light_image=side_img_data, size=(514, 720))
        email_icon = CTkImage(light_image=email_icon_data, size=(20, 20))
        password_icon = CTkImage(light_image=password_icon_data, size=(20, 20))

        # Left side image
        CTkLabel(master=self, text="", image=side_img).pack(expand=True, side="left")

        # Frame for right side content
        frame = CTkFrame(master=self, width=514, height=720)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # Add widgets to the frame
        CTkLabel(master=frame, text="Welcome Back!", text_color="#E44982", anchor="w", justify="left", font=("Arial Bold", 50)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#E44982", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Email:", text_color="#E44982", anchor="w", justify="left", font=("Arial Bold", 28), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.email_entry = CTkEntry(master=frame, placeholder_text='helloworld@gmail.com', placeholder_text_color='grey', width=250, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.email_entry.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Password:", text_color="#E44982", anchor="w", justify="left", font=("Arial Bold", 28), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        self.password_entry = CTkEntry(master=frame, width=250, placeholder_text='h5D_2*F569', placeholder_text_color='grey', fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.password_entry.pack(anchor="w", padx=(25, 0))

        CTkButton(master=frame, text="No Account?,Sign up", fg_color="#E44982", hover_color="#601E88", font=("Arial Bold", 13), text_color="#ffffff", width=50, command=self.show_register).pack(anchor="w", pady=(15, 0), padx=(25, 0))
        CTkButton(master=frame, text="Sign in", fg_color="#E44982", hover_color="#601E88", font=("Arial Bold", 24), text_color="#ffffff", width=250).pack(anchor="w", pady=(30, 0), padx=(25, 0))

        # Initialize Register widget (hidden initially)
        self.register_widget = None

    def show_register(self):
        # Hide Login widgets
        self.pack_forget()

        # Instantiate and pack Register widget
        self.register_widget = Register(self.root)
        self.register_widget.pack(fill="both", expand=True)


