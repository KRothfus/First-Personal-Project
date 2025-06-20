from models.item import Item


class Bin:
    def __init__(self):
        self.items = [Item()]
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
    
    @property
    def current_qty(self):
        return sum(item.current_qty for item in self.items)
    
    @property
    def max_qty(self):
        return sum(item.maxy_qty for item in self.items)
    
    @property
    def low_qty(self):
        return any(item.current_qty <= item.low_qty for item in self.items)
    
    
        