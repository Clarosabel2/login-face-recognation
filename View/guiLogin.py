import tkinter as tk
from tkinter import messagebox
import View.guiRegister as guiRegister
import Controller.userController as userCrtl

def iniciar_aplicacion():
    def open_registration_form():
        guiRegister.show_registration_form()
        pass

    def login():
        username = entry_username.get()
        password = entry_password.get()
        user=userCrtl.searchUser(username,password)
        if user:
            messagebox.showinfo("Aviso","Usuario registrado")
            if userCrtl.authenticationUser(user):
                messagebox.showinfo("Aviso",f"Bienvenido: {user.get_username()}")
            else:
                messagebox.showerror("Error de Identificación Facial","Rostro no identificado")
        else:
            messagebox.showerror("Error","Username or Password is incorrect")

    # Crea la ventana principal

    root = tk.Tk()
    root.title("Inicio de sesión")

    # Establece dimensiones de la ventana
    window_width = 1060
    window_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

    # Crea un marco para contener los elementos y centrarlos en la ventana
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Establece la fuente Century Gothic
    font_style = ("Century Gothic", 12)

    # Crea y posiciona los elementos en el marco con la fuente especificada
    label_username = tk.Label(frame, text="Usuario:", font=font_style)
    label_username.pack(pady=10)
    entry_username = tk.Entry(frame, font=font_style)
    entry_username.pack(pady=5)

    label_password = tk.Label(frame, text="Contraseña:", font=font_style)
    entry_password = tk.Entry(frame, show="*", font=font_style)
    
    # Posiciona los elementos
    entry_username.pack(pady=5)
    label_password.pack(pady=10)
    entry_password.pack(pady=10)

    # Crea un nuevo marco para los botones de acción (Iniciar sesión y Registrar nuevo usuario)
    button_frame = tk.Frame(frame)
    button_frame.pack(pady=20)

    button_login = tk.Button(button_frame, text="Iniciar sesión", command=login, font=font_style)
    button_login.pack(side=tk.LEFT, padx=10)

    button_register = tk.Button(button_frame, text="Registrar nuevo usuario", command=open_registration_form, font=font_style)
    button_register.pack(side=tk.RIGHT, padx=10)

    # Inicia el bucle principal
    root.mainloop()
    
if __name__ == "__main__":
    iniciar_aplicacion()
