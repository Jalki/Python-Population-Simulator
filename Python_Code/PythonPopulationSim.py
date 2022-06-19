from unicodedata import name
import dearpygui.dearpygui as dpg
import numpy as np
import scipy as sp


dpg.create_context()
#dpg.set_theme("Gold")

Civ_Info = {}

Civ_Count = 0


#Upon clicking add civilization, this function saves a civilization.
def save_callback(sender, data):
    global Civ_Count
    global Civ_Info
    Civ_Count = Civ_Count + 1
    print(Civ_Count)
    print(dpg.get_value("Civ_Name"))
    print(dpg.get_value("Timescale"))
    print(dpg.get_value("Pop_Grow"))
    print(dpg.get_value("Pop_Dead"))
    print(dpg.get_value("Pop_Dense"))
    print(dpg.get_value("Nat_Dis"))
    print(dpg.get_value("Max_NatDis"))
    print(dpg.get_value("Sick"))
    print(dpg.get_value("Max_Sick"))
    print(dpg.get_value("Sick_Dur"))
    print(dpg.get_value("Ini_Pop"))

    Civ_Info[Civ_Count] = [dpg.get_value("Civ_Name"), dpg.get_value("Timescale"),  
    dpg.get_value("Pop_Grow"),
    dpg.get_value("Pop_Dead"),
    dpg.get_value("Pop_Dense"),
    dpg.get_value("Nat_Dis"),
    dpg.get_value("Max_NatDis"),
    dpg.get_value("Sick"),
    dpg.get_value("Max_Sick"),
    dpg.get_value("Sick_Dur"),
    dpg.get_value("Ini_Pop")]
    print(Civ_Info)

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
            dpg.add_input_text(label="Civ Name", tag = "Civ_Name")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_int(label="Timescale", tag="Timescale")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_float(label="Population Growthrate", tag="Pop_Grow")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_float(label="Population Deathrate", tag="Pop_Dead")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_float(label="Population Area Density", tag="Pop_Dense")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_slider_float(label="Natural Disaster Chance", tag="Nat_Dis")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_int(label="Max amount of Natural Disasters", tag="Max_NatDis")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_float(label="Chance of plague", tag="Sick")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_int(label="Max amounts of plagues", tag="Max_Sick")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_int(label="Duration of plagues in years", tag="Sick_Dur")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            dpg.add_input_int(label="Initial Population", tag="Ini_Pop")
            dpg.add_separator()
            dpg.add_spacing(count=8)
            #dpg.add_bool_value(label="Is this population model exponential or logistical?", use_internal_label=True, default_value=False)
            dpg.add_button(label="Add Civ", callback=save_callback)
            dpg.add_same_line()
            dpg.add_button(label="Delete Civ", callback=delete_callback)
            dpg.add_same_line()
            dpg.add_button(label="Random Civ", callback=random_callback)
            dpg.add_same_line()
            dpg.add_button(label="Clear All", callback= wipe_callback)
            dpg.add_separator()
            dpg.add_spacing(count=8)
            #dpg.add_text("Nice done!", color = [232, 163, 33])

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

                        for i in range(0, Civ_Count):
                            with dpg.table_row():
                                for j in range(0, 3):
                                    dpg.add_text(f"Row{i} Column{j}")

    #Ending for table
        with dpg.tab(label= "Chart Generation"):
            dpg.add_text('Charts')
        with dpg.tab(label= "Exporting"):
            dpg.add_text('Exporting Options')
        with dpg.tab(label= "Importing"):
            dpg.add_text('Coming Soon')
        with dpg.tab(label="Settings"):
            dpg.add_text("Settings")

dpg.create_viewport(title='Civilization Population Simulator', width=720, height=1080)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()