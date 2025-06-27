from models.bin import Bin


class Location:
    DEFAULT_NAME = "Example"
    DEFAULT_ROWS = 4
    DEFAULT_COLS = 4
    
    def __init__(self, name= DEFAULT_NAME, rows = DEFAULT_ROWS, columns = DEFAULT_COLS):
        self.name = name
        self.rows = rows
        self.columns = columns
        
        self.bins = [[Bin(i,j) for i in range(columns)] for j in range(rows)]
        
        # if load_bins:
        #     # self.items = Item()
        #     # self.col = col
        #     # self.row = row
        #     # self.current_qty_var = tk.StringVar()
        #     for bin in load_bins:
                
        #                 self.bins[i][j].col = load_bins[bin]
    
    def __str__(self):
        return f" Location: {self.name} ({self.rows}x{self.columns})"
        
    def add_bin(self):
        self.bins.append(Bin())