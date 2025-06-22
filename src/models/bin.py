from tkinter import ttk

import tkinter as tk
from models.item import Item


class Bin:
    def __init__(self):
        self.items = [Item()]
        header = tk.Frame(self.frame)
        add_button = ttk.Button(header, text="+", command=self.add_item_qty)
        add_button.pack(side="right",padx=5)
        remove_button = ttk.Button(header, text="-", command=self.remove_item_qty)
        remove_button.pack(side="left",padx=5)
        
    def add_item(self, item):
        self.items.append(item)
    
    def add_item_qty(self,item):
        self.items[item].current_qty += 1

    def remove_item(self, item):
        self.items.remove(item)
    
    def remove_item_qty(self,item):
        self.items[item].current_qty -= 1
    
    @property
    def current_qty(self):
        return sum(item.current_qty for item in self.items)
    
    @property
    def max_qty(self):
        return sum(item.maxy_qty for item in self.items)
    
    @property
    def low_qty(self):
        return any(item.current_qty <= item.low_qty for item in self.items)
    
    
        