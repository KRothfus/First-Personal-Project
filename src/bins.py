from enum import Enum, auto
class Size(Enum):
    SMALL = auto()
    LARGE = auto()
class Bin:
    def __init__(self, x, y, size,loc):
        self.x = x
        self.y = y
        self.size = size
        self.loc = loc
        self.quantity = 0
        self.max_quantity = Size(size)

    def add_quantity(self):
        se
    
    def remove_quantity(self):
        pass
    
    def change_size(self,new_size):
        self.size = new_size
        
    
class Bins:
    def __init__(self, rows, cols, name):
        self.rows = rows
        self.cols = cols
        self.name = name
        self.bins = []
        
    def add_bins(self):
        pass
    
    def remove_bins(self);
        pass
    
    
