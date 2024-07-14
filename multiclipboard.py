import sys 
import clipboard
import json

SAVED_DATA="clipboard.json"

def save_data(filepath,data):
    with open(filepath,"w") as file:
        json.dump(data,file)

def load_data(filepath):
    try:
        with open(filepath,"r") as file:
            data=json.load(file)
            return data
    except: 
        return {}


if len(sys.argv)==2:
    data= load_data(SAVED_DATA)
    command=sys.argv[1]

    if command=="save":
        key=input("Enter a key: ")
        data[key]=clipboard.paste()
        save_data(SAVED_DATA,data)
        print("data saved!")
    
    elif command=="load":
        key=input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied")
        else:
            print("Key not found")

    elif command=="list":
        print(data)

    else:
        print("Wrong command")

else:
    print("Please enter only one command")


