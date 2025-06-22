import tkinter as tk
from tkinter import ttk

class BinDetailWindow:
    def __init__(self, master, bin, title):
        self.bin = bin
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.title = title
        