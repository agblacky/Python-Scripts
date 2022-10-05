import array as arr
import random
from tkinter import Tk
r=Tk()
r.withdraw()

a = arr.array('B', [33,36,37,45,48,49,50,51,52,53,54,55,56,57,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122])
inputs=""


while inputs=="":
    string=""
    for x in range(0, 16):
        string+=chr(a[random.randrange(0,68)])
    print(string) 
    r.clipboard_clear()
    r.clipboard_append(string)
    r.update()
    print("Password has been saved to the clipboard!")
    inputs=input("Press Enter to continue...")
