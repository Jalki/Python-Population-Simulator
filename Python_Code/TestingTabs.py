import dearpygui.dearpygui as dpg
import numpy as np
import scipy as sp
import dearpygui.logger as dpg_logger
from dearpygui.core import *

with dpg.window(label="Civ_Setup", width= 520, height= 720):
   with dpg.tab_bar():
       with dpg.tab(label="Line Series Tab"):
           with dpg.tree_node(label="Line Series"):
               dpg.add_text("Anti-aliasing can be enabled from the plot's context menu (see Help).", bullet=True)
       with dpg.tab(label="Testing Table"):
           with dpg.table(header_row=False, delay_search=True,
                                borders_innerH=True, borders_outerH=True, borders_innerV=True,
                                borders_outerV=True, row_background=True) as table_id1:
                
                        dpg.add_table_column()
                        dpg.add_table_column()
                        dpg.add_table_column()

                        for i in range(0, 8):
                            dpg.add_text("Oh dear")
                            dpg.add_table_next_column()
                        dpg.add_text("Oh dear")


dpg.setup_viewport()
dpg.start_dearpygui()