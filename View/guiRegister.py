import tkinter as tk
from tkinter import messagebox
from Controller import userController

def show_registration_form():
    def register_user():
        if not entry_password.get() or not entry_confirm_password.get() or not entry_username.get():
            messagebox.showerror("Error", "Debe compretar todos los campos solicitados.")
            root.destroy()
        else:
            if entry_password.get() == entry_confirm_password.get():
                userController.createUser(entry_username.get(),entry_password.get())
                messagebox.showinfo("Aviso","Usuario ha sido registrado")
                root.destroy()
            
            else:
                messagebox.showerror("Error", "Contraseñas no coinciden.")
                root.destroy()

    
    
    root = tk.Tk()
    root.title("Registro de nuevo usuario")

    # Dimensiones del formulario de registro
    window_width = 480
    window_height = 480

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

    # Crea y posiciona los elementos en el formulario de registro
    label_title = tk.Label(root, text="Ingresar los datos:", font=("Century Gothic", 16, "bold"))
    label_title.pack(pady=10)

    label_username = tk.Label(root, text="Usuario:", font=("Century Gothic", 12))
    label_username.pack(pady=5)
    entry_username = tk.Entry(root, font=("Century Gothic", 12))
    entry_username.pack(pady=10)

    label_password = tk.Label(root, text="Contraseña:", font=("Century Gothic", 12))
    label_password.pack(pady=5)
    entry_password = tk.Entry(root, show="*", font=("Century Gothic", 12))
    entry_password.pack(pady=10)

    label_confirm_password = tk.Label(root, text="Confirmar contraseña:", font=("Century Gothic", 12))
    label_confirm_password.pack(pady=5)
    entry_confirm_password = tk.Entry(root, show="*", font=("Century Gothic", 12))
    entry_confirm_password.pack(pady=10)

    button_register = tk.Button(root, text="Registrar nuevo usuario", command=register_user, font=("Century Gothic", 12))
    button_register.pack(pady=20)
    

    root.mainloop()

if __name__ == "__main__":
    show_registration_form()
