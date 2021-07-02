import pandas as pd
import numpy as np

from tkinter import *
from mywindow import LRwindow


window = Tk() # to create a window
LRwindow(window) # pass empty window to mywindow
window.title("House price prediction") # set title to window
window.mainloop() # this will keep the window alive
