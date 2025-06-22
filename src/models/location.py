from models.bin import Bin


class Location:
    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns
        self.bins = [[Bin(i,j) for i in range(columns)] for j in range(rows)]
    
    def __str__(self):
        return f" Location: {self.name} ({self.rows}x{self.columns})"
        
    def add_bin(self):
        self.bins.append(Bin())