from tkinter import ttk

import tkinter as tk
from models.item import Item

class Bin:
    def __init__(self,col,row):
        self.items = Item()
        self.col = col
        self.row = row
        # header = tk.Frame(self.frame)
        # add_button = ttk.Button(header, text="+", command=self.add_item_qty)
        # add_button.pack(side="right",padx=5)
        # remove_button = ttk.Button(header, text="-", command=self.remove_item_qty)
        # remove_button.pack(side="left",padx=5)
        
    # def add_item(self, item):
    #     self.items.append(item)
    
    def add_item_qty(self):
        self.items.current_qty += 1
        print(f"Bin (row x col: qty): {self.row+1} x {self.col+1}: {self.items.current_qty}")
        
    # def remove_item(self, item):
    #     self.items.remove(item)
    
    def remove_item_qty(self):
        self.items.current_qty -= 1
        print(f"Bin (row x col: qty): {self.row+1} x {self.col+1}: {self.items.current_qty}")
        
    
    @property
    def current_qty(self):
        return self.items.current_qty
    
    @property
    def max_qty(self):
        return self.items.max_qty 
    
    @property
    def low_qty(self):
        return self.items.current_qty <= self.items.low_qty 
    
    
        