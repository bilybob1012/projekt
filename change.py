
import tkinter as tk
from tkinter import messagebox


class ParkingSpot:
    """Represents a basic car parking spot."""

    def __init__(self, spot_number, location, base_price):
        self.spot_number = spot_number
        self.location = location
        self.__base_price = base_price

    def get_base_price(self):
        return self.__base_price

    def set_base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
            return True
        else:
            return False

    def calculate_price(self, hours):
        return self.get_base_price() * hours


class PremiumParkingSpot(ParkingSpot):
    """Represents a premium parking spot."""

    def __init__(self, spot_number, location, base_price, extra_fee):
        super().__init__(spot_number, location, base_price)
        self.extra_fee = extra_fee

    def calculate_price(self, hours):
        return (self.get_base_price() + self.extra_fee) * hours


# Izveido objektus
normal_spot = ParkingSpot(1, "Ground floor", 2.0)

premium_spot = PremiumParkingSpot(
    2, "First floor", 2.0, 1.5
)


# Funkcija cenas aprēķināšanai
def calculate():
    try:
        hours = float(hours_entry.get())

        if hours <= 0:
            messagebox.showerror("Error", "Hours must be greater than zero!")
            return

        normal_price = normal_spot.calculate_price(hours)
        premium_price = premium_spot.calculate_price(hours)

        result_label.config(
            text=f"Normal parking: {normal_price:.2f} EUR\n"
                 f"Premium parking: {premium_price:.2f} EUR"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")


# Funkcija cenas maiņai
def change_price():
    try:
        new_price = float(price_entry.get())

        if normal_spot.set_base_price(new_price):
            messagebox.showinfo("Success", "Price successfully changed!")
            price_label.config(
                text=f"New price: {normal_spot.get_base_price():.2f} EUR/hour"
            )
        else:
            messagebox.showerror(
                "Error", "Price must be greater than zero!"
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid price!")


# Galvenais logs
root = tk.Tk()
root.title("Car Parking System")
root.geometry("450x500")
root.config(bg="#eeeeee")

# Virsraksts
title = tk.Label(
    root,
    text="CAR PARKING SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#eeeeee"
)
title.pack(pady=15)

# Autostāvvietu informācija
info_label = tk.Label(
    root,
    text="Normal parking spot: 1\n"
         "Location: Ground floor\n"
         "Price: 2.00 EUR/hour\n\n"
         "Premium parking spot: 2\n"
         "Location: First floor\n"
         "Price: 3.50 EUR/hour",
    font=("Arial", 12),
    bg="#eeeeee"
)
info_label.pack(pady=10)

# Stundu ievade
hours_label = tk.Label(
    root, text="Enter parking hours:", bg="#eeeeee"
)
hours_label.pack()

hours_entry = tk.Entry(root)
hours_entry.pack(pady=5)

# Aprēķina poga
calculate_button = tk.Button(
    root,
    text="Calculate price",
    command=calculate,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11)
)
calculate_button.pack(pady=10)

# Rezultāts
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#eeeeee"
)
result_label.pack(pady=10)

# Cenas maiņa
price_label = tk.Label(
    root,
    text="Change normal parking price:",
    bg="#eeeeee"
)
price_label.pack(pady=5)

price_entry = tk.Entry(root)
price_entry.pack(pady=5)

change_button = tk.Button(
    root,
    text="Change price",
    command=change_price,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11)
)
change_button.pack(pady=10)

# Beigu poga
exit_button = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    bg="#f44336",
    fg="white"
)
exit_button.pack(pady=15)

# Programmas palaišana
root.mainloop()
