
import sys
from setup import read_json_to_dict

required_version = (3,12)

if sys.version_info < required_version:
    errror_message = f"this script requires Python version {required_version[0]},{required_version[1]}"
    print(errror_message,file=sys.stderr)
    sys.exit(1)  
def main():
    
    file_path = './private/data.json'
    data_dict = read_json_to_dict(file_path)
    print(data_dict)
if __name__ == '__main__':
    main()
