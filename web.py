import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items)
        return total


users = {'aliz2012': User('aliz2012', 'idk8888', 100)}
products = {'Apple': Product('Apple', 0.5), 'Banana': Product('Banana', 0.3), 'Orange': Product('Orange', 0.4)}


def login_window():
    login_window = tk.Tk()
    login_window.title("Bejelentkezés")

    username_label = tk.Label(login_window, text="Felhasználónév:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text="Jelszó:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username in users and users[username].password == password:
            login_window.destroy()
            shopping_window(users[username])
        else:
            messagebox.showerror("Hiba", "Sikertelen bejelentkezés!")

    login_button = tk.Button(login_window, text="Bejelentkezés", command=login)
    login_button.pack()

    login_window.mainloop()


def shopping_window(user):
    shopping_window = tk.Tk()
    shopping_window.title("Vásárlás")

    welcome_label = tk.Label(shopping_window, text=f"Üdvözöllek, {user.username}! Egyenleg: ${user.balance}")
    welcome_label.pack()

    products_label = tk.Label(shopping_window, text="Elérhető termékek:")
    products_label.pack()

    def buy_product(product_name, product_price):
        if user.balance >= product_price:
            user.balance -= product_price
            messagebox.showinfo("Sikeres vásárlás", f"{product_name} sikeresen megvásárolva!")
            welcome_label.config(text=f"Üdvözöllek, {user.username}! Egyenleg: ${user.balance}")
        else:
            messagebox.showerror("Hiba", "Nincs elegendő pénz a vásárláshoz!")

    for product_name, product in products.items():
        product_button = tk.Button(shopping_window, text=f"{product_name}: ${product.price}",
                                   command=lambda name=product_name, price=product.price: buy_product(name, price))
        product_button.pack()

    shopping_window.mainloop()

if __name__ == "__main__":
    login_window() # xd bocsánat meg csináltam tkinterrel :,)
