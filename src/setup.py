import json
import sys
import os

def read_json_to_dict(file_path):
    try:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write('{"example":"data"}\n')
                data = json.load(file)
                return data
        else:
            with open(file_path,'r') as file:
                data = json.load(file)
                return data
    except Exception as e:
        print(f'error: {e}')
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'")
        return None
    
def copy_from_public_to_private():
    pass


def location_creation():
    try:
        input_count: int = input("How many locations do you want to keep track of?: ")
        
    except Exception as e:
        print(e,"Must input a number")
        location_creation()