from guiparse import *
from ttkbootstrap import Style
from tkinter import ttk
#style= Style('darkly')
parser = argStation("gsgen")

# String
parser.add_argument(
    '--Project Name',
    type=str,
    default="https://mixer.com/browse/games/70323/fortnite",
    help='The url of the starting page.')

parser.add_argument(
    '--root_path',
    type=str,
    is_path=True,
    default="./Data/Mixer_Videos/",
    help='The root path of recorded videos.')


# Integer
parser.add_argument(
    '--Submission Files',
    type=str,
    default='5',
    help='The maximum value of records.')

parser.add_argument(
    '--Enabled',
    action='store_true',
    help='The quality of recorded videos.')

root = tk.Tk()
#creation of an instance
app = Window(root, parser)
root.geometry(app.geometry)
#mainloop 
root.mainloop() 