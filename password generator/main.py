import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 20, "bold"), fg="purple")
        self.title_label.pack(pady=20)

        self.name_label = tk.Label(root, text="Name:", font=("Helvetica", 12))
        self.name_label.pack()
        self.name_entry = tk.Entry(root, font=("Helvetica", 12))
        self.name_entry.pack(pady=5)

        self.length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
        self.length_label.pack()
        self.length_entry = tk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Generated Password:", font=("Helvetica", 12))
        self.password_label.pack()
        self.password_display = tk.Entry(root, state="readonly", font=("Helvetica", 12))
        self.password_display.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12), bg="blue", fg="white")
        self.generate_button.pack(pady=10)

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password, font=("Helvetica", 12), bg="blue", fg="white")
        self.accept_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields, font=("Helvetica", 12), bg="blue", fg="white")
        self.reset_button.pack(pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.configure(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, generated_password)
        self.password_display.configure(state="readonly")

    def accept_password(self):
        name = self.name_entry.get()
        password = self.password_display.get()
        if name and password:
            with open("passwords.txt", "a") as file:
                file.write(f"Name: {name}\nPassword: {password}\n\n")
            self.reset_fields()

    def reset_fields(self):
        self.name_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.password_display.configure(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.configure(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.geometry("400x400")  # Set window size
    root.configure(bg="lightgray")  # Set background color
    root.mainloop()
