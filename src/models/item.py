class Item:
    DEFAUL_NAME = "Empty"
    DEFAULT_MAX_QTY = 100
    DEFAULT_LOW_QTY = 10
    DEFAULT_CURRENT_QTY = 0
    def __init__(self,name=DEFAUL_NAME, max_qty=DEFAULT_MAX_QTY, low_qty=DEFAULT_LOW_QTY, current_qty=DEFAULT_CURRENT_QTY):
        self.name = name
        self.max_qty = max_qty
        self.low_qty = low_qty
        self.current_qty = current_qty
        
    def __str__(self):
        return f"{self.name}: {self.current_qty}/{self.max_qty}"
    