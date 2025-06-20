
import sys
from setup import location_creation, read_json_to_dict
from graphics import Window
required_version = (3,12)

if sys.version_info < required_version:
    errror_message = f"this script requires Python version {required_version[0]},{required_version[1]}"
    print(errror_message,file=sys.stderr)
    sys.exit(1)  
    
    
import tkinter as tk
from gui.setup_window import SetupWindow
    
    
def main():
    root = tk.Tk()
    root.title("Parts Organizer")
    app = SetupWindow(root)
    root.mainloop()

    # file_path = './private/data.json'
    # data_dict = read_json_to_dict(file_path)
    # win = Window(400,400)
    # win._Window__root.mainloop()
    # location_creation()
    
if __name__ == '__main__':
    main()
