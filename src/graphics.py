from tkinter import Tk, BOTH, Canvas, Button

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Parts Organizer")
        self.__canvas = Canvas(self.__root, bg="orange", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self._on_closing)  # Use a different name for the close method
        self.__buttons_list = []
        self.initialize_buttons()# Renamed button method
        self.__counts = []

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # def wait_for_close(self): # Consider using mainloop if you don't need this specific functionality
    #     self.__running = True
    #     while self.__running:
    #         self.redraw()
    #     print("window closed...")

    def _on_closing(self): # This is the method for handling window closing
        self.save()
        self.__root.destroy()
    
    def add_button(self):
        new_button_index = len(self.__buttons_list)
        new_button = Button(self.__root, text=f'Bin {new_button_index + 1}',
                            command=lambda i=new_button_index: self.increment_count(i)) # Pass index using lambda
        
        # Append to buttons list and counts list
        self.__buttons_list.append(new_button)
        self.__counts.append(0) # Initialize count for the new button

        # Pack the new button
        new_button.pack()
    
    def save(self):
        print('saving')
    
    def initialize_buttons(self):
        add_button = Button(self.__root,text=f'Add Button',command=self.add_button)
        add_button.pack()
        quit_button = Button(self.__root, text=f"QUIT", command=self._on_closing)
        quit_button.pack()

