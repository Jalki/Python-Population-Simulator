import dearpygui.dearpygui as dpg
import numpy as np
import scipy as sp
import dearpygui.logger as dpg_logger
from dearpygui.core import *

def testfunction(sender,data):
    print("Sender : ", sender)
    print("Data : ", data)

with dpg.window(label="Example", width=500, height=500 ):
    #Sender -> Button
    dpg.add_button(label="Click Here...", callback = testfunction)

dpg.setup_viewport()
dpg.start_dearpygui()