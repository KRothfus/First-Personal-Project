from tkinter import messagebox, ttk

import tkinter as tk
from models.item import Item


class Bin:
    def __init__(self,col,row):
        self.items = Item()
        self.col = col
        self.row = row
        self.current_qty_var = tk.StringVar(value=self.items.current_qty)
        self.name_var = tk.StringVar(value=self.items.name)
    def update_qty_from_entry(self, qty: tk.Entry):
        try:
            new_qty = int(qty.get())
            if new_qty >= 0:
                self.items.current_qty
            else:
                self.items.current_qty = 0
                messagebox.showwarning("Invalid Input", "Quantity cannot be negative. Setting to 0.")
        except ValueError:
            messagebox.showerror("Invalid Input", f"Please enter a valid number for quantity. Reverting to {self.items.current_qty}.")
    
    def add_item_qty(self):
        self.items.current_qty += 1
        print(f"Added to {self.items.name}. New quantity: {self.items.current_qty}")
        self.current_qty_var.set(self.items.current_qty)

    def remove_item_qty(self):
        if self.items.current_qty > 0:
            self.items.current_qty -= 1
            self.current_qty_var.set(self.items.current_qty)
            print(f"Removed from {self.items.name}. New quantity: {self.items.current_qty}")
        else:
            messagebox.showwarning("Quantity Error", "Quantity cannot go below zero!")

    def update_name_from_entry(self):
        new_name = self.name_var.get().strip() # Get text and remove leading/trailing whitespace
        if not new_name: # Simple validation: Name cannot be empty
            messagebox.showerror("Invalid Name", "Bin name cannot be empty. Reverting to previous name.")
            self.name_var.set(self.items.name) # Revert to previous valid name
            return
        try:
            self.items.name = new_name # Use the setter on the Item object
        except ValueError as e:
            messagebox.showerror("Invalid Name", f"Error updating bin name: {e}")
            self.name_var.set(self.items.name)
    
    @property
    def current_qty(self):
        return self.items.current_qty
    
    @property
    def max_qty(self):
        return self.items.max_qty 
    
    @property
    def low_qty(self):
        return self.items.current_qty <= self.items.low_qty 
    
    
        