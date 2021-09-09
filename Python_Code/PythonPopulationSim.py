import dearpygui.dearpygui as dpg
import numpy as np
import scipy as sp
import dearpygui.logger as dpg_logger
from dearpygui.core import *

set_global_font_scale(1.25)
#dpg.set_theme("Gold")


#This function is for generating a chart GUI based on the civilizations given. Each civilization is assigned a random color for its identification and it can not be the same color!
def generate_chart(sender, data):
    print("Making Chart")
    with dpg.window("Chart Printing"):
        print("Making Chart")

#Upon clicking delete civilization while highlighting a potential civ, this function deletes the information!
def delete_callback():
    print("Kamehameha!")

def random_callback():
    pass

def wipe_callback():
    pass

with dpg.window(label="Civ_Setup", width= 520, height= 720):
    with dpg.tab_bar():
        with dpg.tab(label="Civilization Creation"):
            dpg.add_input_text(label="Civ_Name")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_int(label="Timescale")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_float(label="Population_Growthrate")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_float(label="Population_Deathrate")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_float(label="Population_Area_Density")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_slider_float(label="Natural Disaster Chance")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_int(label="Max amount of Natural Disasters")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_float(label="Chance of plague")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_int(label="Max amounts of plagues")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_int(label="Duration of plagues in years")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_input_int(label="Initial Population")
            dpg.add_separator()
            dpg.add_spacing(count=16)
            #dpg.add_bool_value(label="Is this population model exponential or logistical?", use_internal_label=True, default_value=False)

            #Upon clicking add civilization, this function saves a civilization.
            def save_callback(sender, data, civ =[], time=[], pop_grow=[], pop_death=[], pop_density=[], naturaldis=[], plague=[], max_plague=[], dur_plague=[], ini_pop=[]):
                print("Save Clicked, civilization made!")
                input_value_civ = get_value ("Civ_Name")
                civ.append(input_value_civ)
                input_value_time = get_value ("Timescale")
                time.append(input_value_time)
                input_value_popgrow = get_value("Population_Growthrate")
                pop_grow.append(input_value_popgrow)
                input_value_popdead = get_value("Population_Deathrate")
                pop_death.append(input_value_popdead)
                input_value_density = get_value("Population_Area_Density")
                pop_density.append(input_value_density)

            dpg.add_button(label="Add Civ", callback=save_callback)
            add_same_line()
            dpg.add_button(label="Delete Civ", callback=delete_callback)
            add_same_line()
            dpg.add_button(label="Random Civ", callback=random_callback)
            add_same_line()
            dpg.add_button(label="Clear Civ", callback= wipe_callback)
            dpg.add_separator()
            dpg.add_spacing(count=16)
            dpg.add_text("Nice done!", color = [232, 163, 33])


            with dpg.table(header_row=False, delay_search=True,
                            borders_innerH=True, borders_outerH=True, borders_innerV=True,
                            borders_outerV=True, row_background=True) as table_id1:
                
                        dpg.add_table_column() #Civilization Name
                        dpg.add_table_column() #Timescale
                        dpg.add_table_column() #Population Growth Rate
                        dpg.add_table_column() #Population Death Rate
                        dpg.add_table_column() #Population Area Density
                        dpg.add_table_column() #Natural Disaster Chance
                        dpg.add_table_column() #Max amount of Natural Disasters
                        dpg.add_table_column() #Chance of Plagues
                        dpg.add_table_column() #Max Amounts of Plagues
                        dpg.add_table_column() #Duration of Plagues in Years
                        dpg.add_table_column() #Initial Population

        with dpg.tab(label= "Chart Generation"):
            dpg.add_text('Charts')
        with dpg.tab(label= "Exporting"):
            dpg.add_text('Exporting Options')
        with dpg.tab(label= "Importing"):
            dpg.add_text('Coming Soon')

dpg.setup_viewport()
dpg.start_dearpygui()