

import json
import os
import tkinter as tk
from tkinter import Button, ttk
from gui.bin_detail_window import BinDetailWindow
from models.bin import Bin
from models.location import Location


class OrganizerWindow:
    def __init__(self, master, location: Location):
        self.location = location
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill = tk.BOTH, expand = True)
        # self.load()
        self.create_header()
        self.create_bin_grid()
        self.create_footer()
        
    def create_header(self):
        header = tk.Frame(self.frame)
        header.pack(fill=tk.X)
        
        title = ttk.Label(header, text=f"Organizer: {self.location.name}", font=("Arial",16))
        title.pack(side=tk.LEFT, padx=10,pady=10)
        
        search_label = ttk.Label(header, text="Search:")
        search_label.pack(side= tk.LEFT, padx=(20,5),)
        self.search_entry = ttk.Entry(header)
        self.search_entry.pack(side=tk.LEFT)
        search_button = ttk.Button(header, text="Search", command=self.search_items)
        search_button.pack(side="left",padx=5)
        
        
    def create_bin_grid(self):
        grid_frame = tk.Canvas(self.frame)
        grid_frame.pack(padx=10,pady=10)
        k = 1
        for row in range(self.location.rows):
            k+=1
            for col in range(self.location.columns):
                bin = self.location.bins[row][col]
                # btn_frame = tk.Frame(grid_frame)
                # btn_frame.pack()
                btn = tk.Button(grid_frame, 
                                 text = f"Bin {row*self.location.columns + col + 1}", 
                                 width=10,height=2, 
                                 command=lambda r = row, c = col: self.open_bin_details(r,c))
                btn.grid(row=row, column=col,padx=2,pady=2)
                
                add_button = ttk.Button(grid_frame, text="+",width = 2,  command=self.location.bins[row][col].add_item_qty)
                add_button.grid(row=row+k, column=col,padx=2,pady=2)
                remove_button = ttk.Button(grid_frame, text="-", width = 2,  command=self.location.bins[row][col].remove_item_qty)
                remove_button.grid(row=row+k, column=col,padx=2,pady=2)
                self.update_bin_button(btn,bin)
        
    def create_footer(self):
        footer = tk.Frame(self.frame)
        footer.pack(fill=tk.X)
        
        total_bins = self.location.rows * self.location.columns
        low_stock_bins = sum(1 for row in self.location.bins for bin in row if bin.low_qty)
        
        status_label = ttk.Label(footer, text=f"Total Bins: {total_bins} | Low Stock Bins: { low_stock_bins}")
        status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        refresh_button = ttk.Button(footer, text="Refresh", command=self.refresh_display())
        refresh_button.pack(side=tk.RIGHT, padx=10, pady=5)
        
        create_save_button = ttk.Button(self.frame, text= "Save", command=self.save())
        create_save_button.pack(side=tk.RIGHT, padx=10,pady=5)
        
    def open_bin_details(self, row, col):
        bin = self.location.bins[row][col]
        BinDetailWindow(self.master, bin, f"Bin {row*self.location.columns + col + 1}")    
        
    def update_bin_button(self, button: Button, bin: Bin):
        print("button",button)
        print("bin",bin)
        if bin.low_qty:
            button.config(bg="red")
        elif bin.current_qty / bin.max_qty < 0.5:
            button.config(bg="yellow")
        else:
            button.config(bg="green")
    
    def search_items(self):
        pass
    
    def refresh_display(self):
        self.create_bin_grid()
    
    def save(self):
        
        bins_dict = {}
        k = 0
        for i in range(self.location.rows):
            for j in range(self.location.columns):
                bins_dict[k] = {"name": self.location.bins[i][j].items.name,
                "current_qty":self.location.bins[i][j].items.current_qty,
                "max_qty":self.location.bins[i][j].items.max_qty,
                "low_qty": self.location.bins[i][j].items.low_qty}
                k += 1
        with open("./data/data.json","w") as json_file:
            json.dump(bins_dict,json_file,indent=4)
    
    def load(self):
        file_path = "./data/data.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
            
        for bin in data:
            pass