

import json
import os
import tkinter as tk
from tkinter import Button, Entry, ttk
from tkinter import messagebox
from gui.bin_detail_window import BinDetailWindow
from models.bin import Bin
from models.location import Location


name_entry = None
class OrganizerWindow:
    def __init__(self, master, location: Location):
        self.location = location
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill = tk.BOTH, expand = True)
        # self.load()
        self.name_display = self.bin_display_buttons = [[None for _ in range(self.location.columns)] for _ in range(self.location.rows)]
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
        grid_container_frame = tk.Frame(self.frame)
        grid_container_frame.pack(padx=10, pady=10)

        for row_idx in range(self.location.rows):
            for col_idx in range(self.location.columns):
                current_bin = self.location.bins[row_idx][col_idx]

                bin_display_frame = tk.Frame(grid_container_frame, relief=tk.RAISED, borderwidth=1)
                bin_display_frame.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                name_entry = tk.Entry(
                    bin_display_frame,
                    textvariable=current_bin.name_var, # Link to the bin's name_var
                    font=("Arial", 10),
                    width=12,
                    justify=tk.CENTER # Center the text
                )
                name_entry.grid(row=0, column=0, columnspan=3, padx=2, pady=2)
                # Bind events to update the Bin's actual item name when the user finishes editing
                name_entry.bind("<FocusOut>", lambda event, b=current_bin: b.update_name_from_entry())
                name_entry.bind("<Return>", lambda event, b=current_bin: b.update_name_from_entry())
                self.name_display[row_idx][col_idx] = name_entry
                # 1. Add Button (+) - Now in column 0
                add_button = ttk.Button(
                    bin_display_frame,
                    text="+",
                    width=3,
                    command=current_bin.add_item_qty
                )
                add_button.grid(row=1, column=2, padx=2, pady=2) # Changed column to 0

                # 2. Quantity Entry - Remains in column 1
                qty_entry = tk.Label(bin_display_frame, textvariable=current_bin.current_qty_var)
                qty_entry.grid(row=1, column=1, padx=2, pady=2)


                # 3. Subtract Button (-) - Now in column 2
                remove_button = ttk.Button(
                    bin_display_frame,
                    text="-",
                    width=3,
                    command=current_bin.remove_item_qty
                )
                remove_button.grid(row=1, column=0, padx=2, pady=2) # Changed column to 2

                self.update_bin_button(name_entry, current_bin)
                
                

    def create_footer(self):
        footer = tk.Frame(self.frame)
        footer.pack(fill=tk.X)
        
        total_bins = self.location.rows * self.location.columns
        low_stock_bins = sum(1 for row in self.location.bins for bin in row if bin.low_qty)
        
        status_label = ttk.Label(footer, text=f"Total Bins: {total_bins} | Low Stock Bins: { low_stock_bins}")
        status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # refresh_button = ttk.Button(footer, text="Refresh", command=self.refresh_display)
        # refresh_button.pack(side=tk.RIGHT, padx=10, pady=5)
        
        create_save_button = ttk.Button(self.frame, text= "Save", command=self.save)
        create_save_button.pack(side=tk.RIGHT, padx=10,pady=5)
        
    def open_bin_details(self, row, col):
        bin = self.location.bins[row][col]
        BinDetailWindow(self.master, bin, f"Bin {row*self.location.columns + col + 1}")    
        
    def update_bin_button(self, button: Entry, bin: Bin):
        print("button",button)
        print("bin",bin)
        if bin.low_qty:
            button.config(bg="red")
        elif bin.current_qty / bin.max_qty < 0.5:
            button.config(bg="yellow")
        else:
            button.config(bg="green")
    
    def search_items(self):
        messagebox.showwarning("Not implemented","Search has not yet been implemented, but will at a later date!")
        print("Function not implemented yet.")
        pass
    
    def refresh_display(self):
        self.create_bin_grid()
        
    
    def save(self):
        print("Saving...")
        bins_dict = {}
        k = 1
        for i in range(self.location.rows):
            for j in range(self.location.columns):
                
                bins_dict[k] = {"name": self.location.bins[i][j].items.name,
                "current_qty":self.location.bins[i][j].items.current_qty,
                "max_qty":self.location.bins[i][j].items.max_qty,
                "low_qty": self.location.bins[i][j].items.low_qty,
                "row": i,
                "column": j,
                "name": self.location.bins[i][j].items.name
                }
                k += 1
                self.update_bin_button(self.name_display[i][j], self.location.bins[i][j])
        bins_dict["location_info"]= {
            "columns":self.location.columns,
            "rows": self.location.rows,
            "name": self.location.name
            }
        with open("./data/data.json","w") as json_file:
            json.dump(bins_dict,json_file,indent=4)
        print("Saved.")
        
