import json
import os
import tkinter as tk
from tkinter import ttk
from gui.organizer_window import OrganizerWindow
from models.bin import Bin
from models.location import Location


class SetupWindow:
    def __init__(self, master):
          self.master = master
          self.frame = tk.Frame(self.master)
          self.frame.pack()
          
          self.location_name_label = ttk.Label(self.frame, text= "Location Name:")
          self.location_name_label.grid(row=0, column = 0, padx = 5, pady=5)
          self.location_name_entry = ttk.Entry(self.frame)
          self.location_name_entry.grid(row=0,column=1,padx=5,pady=5)
          
          self.rows_label = ttk.Label(self.frame, text="Number of Rows:")
          self.rows_label.grid(row=1,column=0,padx=5,pady=5)
          self.rows_entry = ttk.Entry(self.frame)
          self.rows_entry.grid(row=1,column=1,padx=5,pady=5)
          
          self.columns_label = ttk.Label(self.frame, text="Number of Columns:")
          self.columns_label.grid(row=2,column=0,padx=5,pady=5)
          self.columns_entry = ttk.Entry(self.frame)
          self.columns_entry.grid(row=2,column=1,padx=5,pady=5)
          
          self.create_button = ttk.Button(self.frame, text="Create Location", command=self.create_location)
          self.create_button.grid(row=3, column=0, columnspan=2,pady=10)
          
          self.load_button = ttk.Button(self.frame, text="Load", command=self.load)
          self.load_button.grid(row=4,column=0, columnspan=2,pady=10)
          

    def load(self):
        print("hello")
        pass
        file_path = "./data/data.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            print("No file exists to load.")
            return
        location = Location(data["location_info"]["name"], data["location_info"]["rows"], data["location_info"]["columns"])
        
        for bin, info in data.items():
            try:
                is_bin = int(bin)
            except:
                break
            print(bin)
            row = int(info["row"])
            col = int(info["column"])
            location.bins[row][col].items.current_qty = info["current_qty"]
            location.bins[row][col].items.max_qty = info["max_qty"]
            location.bins[row][col].items.low_qty = info["low_qty"]
            location.bins[row][col].name_var.set(info["name"])
            location.bins[row][col].update_name_from_entry()
            location.bins[row][col].row = info["row"]
            location.bins[row][col].col = info["column"]
            location.bins[row][col].current_qty_var.set(info["current_qty"])
            
        OrganizerWindow(self.master, location)
            
              
    def create_location(self):
        name = self.location_name_entry.get()
        rows = int(self.rows_entry.get())
        columns = int(self.columns_entry.get())
        location = Location(name, rows, columns)
        organizer_window = OrganizerWindow(self.master, location)
        print(f"Created location: {name}")
        
        