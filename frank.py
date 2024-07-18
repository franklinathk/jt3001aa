"""
# 2024-01-12T11:04:56.715750
import vitis
client = vitis.create_client()
client.set_workspace(path="/workspaces/signe/test")
 
platform = client.get_platform_component(name="signe")
status = platform.build()
 
vitis.dispose()
"""
from frank_subdir import *
from tkinter import *
import subprocess
#import pyautogui 
import matplotlib.pyplot as plt
import os
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import StringVar, Radiobutton, Entry, Label
from pprint import pprint
import time
from tkinter import Menu, DISABLED
from tkinter.simpledialog import askfloat
from PIL import Image, ImageTk
from tkinter.colorchooser import askcolor
# UART Tx/Rx demo
import serial
import threading
# from frank_subdir.lib_1 import debug_print
from frank_subdir.items import ITEMS_INA228,  ITEMS_OTP, ITEMS_DB, ITEMS_DC, ITEMS_SETTINGS
from frank_subdir.items import ITEMS_VOL_CUR
from frank_subdir.items import jt3001_entries,labels_entries, tmp421_reges 
from frank_subdir.lib import new_line
"""
import colorsys
# RGB values
red = 133
green = 188
blue = 165

# Normalize RGB values to the range [0, 1]
r = red / 255.0
g = green / 255.0
b = blue / 255.0

# Convert RGB to HSL
h, l, s = colorsys.rgb_to_hls(r, g, b)

# Print the HSL values
print(f'Hue: {int(h * 360)}, Saturation: {int(s * 100)}, Lightness: {int(l * 100)}')
"""
############################################
#  color : magenta,  cyan,   
NAVY_BLUE = '#868d91'
CADET_BLUE = '#5f9ea0'
SAXE_BLUE ='#4798b3'
BROWN = '#d08f34'
MALACHITE_GREEN = '#00a15c'
ORANGE = '#ea7343'
# Convert RGB to hexadecimal color code
GREEN_1 = "#{:02X}{:02X}{:02X}".format(133, 188, 165)
BLUE_1 = "#{:02X}{:02X}{:02X}".format(112, 114, 209)
############################################

# Define the hamburger menu symbol
# hamburger_menu = "☰"
hamburger_menu = '\U00002630'
unicode_char = '\U0001F680'
unicode_char_1 = '\U0001F7E5'
unicode_char_2 = '\U0001F780'
unicode_char_3 = '\U0001F7F1'
unicode_char_4 = '\U0001FA61'
unicode_char_5 = '\U0001F020'
unicode_char_6 = '\U0001F000'
# Print the hamburger menu symbol
print(hamburger_menu)
print(unicode_char)
print(unicode_char_1)
print(unicode_char_2)
print(unicode_char_3)
print(unicode_char_4)
print(unicode_char_5)
print(unicode_char_6)
############################################
#  Define global value 
#DIM_ID = 0x01
#AUTO_SEND_CMD = False
AUTO_SEARCH_FREQ = False 
VPP_TO_10V = False
VDD_TO_5V = False
CHOP_FREQ = False 
ON_LINE_CALIBR = False
LOCK = True
VREF_TRIM = False
CURRENT_TRIM = False
FREQ_COARSE_TRIM = False
FREQ_FINETUNE_TRIM = False
PRINT_MESSAGE = False
EXTCLK_ENABLE = False
DIV256_ENABLE = False
DC_RESET = False
DB_REPEAT = False
GET_LED_CURRENT = False
label_2nd_var = None
# At the beginning of your script or in the global scope
switch_dict = {}
focus_out_flag = False

############################################
def on_eng_mode_change(*args):
    eng_mode_value = ENG_MODE_VAR.get()
    win_name = "win_otp"
    # Assuming write_button is a ttk.Button, you need to replace it with your actual button widget
    for row_index, info_dict in label_widgets_dict.items():
        if info_dict["window_title"] == win_name:
            button_widget = info_dict["button_widget"]
            if eng_mode_value:
                button_widget["state"] = NORMAL
            else:
                button_widget["state"] = DISABLED
        
############################################
# Function to toggle the visibility of the scroll bar
def open_win(win_name, x_position):
#    def open_win(win_name, x_position):
    global ITEMS # Declare ITEMS as a global variable
    global switch_dict
    global ENG_MODE
    global ENG_MODE_VAR

    default_color = '#eeeeee'
    saved_color = extract_color_from_file_content(win_name.title())
    if not saved_color == None:
        default_color = saved_color

    if win_name.title() == "win_db_wr": 
        ITEMS = ITEMS_DB
    elif win_name.title() == "win_dc_wr_one": 
        ITEMS = ITEMS_DC
    elif win_name.title() == "win_otp": 
        ITEMS = ITEMS_OTP
    elif win_name.title() == "win_ina228": 
        ITEMS = ITEMS_INA228
    elif win_name.title() == "win_settings": 
        ITEMS = ITEMS_SETTINGS
    elif win_name.title() == "win_trim": 
        ITEMS = ITEMS_VOL_CUR
    else:
        ITEMS = []        

    #win_name.configure(bg='grey')
    # Create a top-bar menu
    menu_bar = Menu(win_name)
    win_name.config(menu=menu_bar, bg=default_color)
    # Create a 'View' menu
    view_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=view_menu)

    # Create a sub-menu for font options
    font_menu = Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label="Font", menu=font_menu)
    # Function to change the font size
    # Add font size options to the 'Font' menu
    font_menu.add_command(label="8", command=lambda: change_font_size(8,win_name))
    font_menu.add_command(label="9", command=lambda: change_font_size(9,win_name))
    font_menu.add_command(label="10", command=lambda: change_font_size(10, win_name))
    font_menu.add_command(label="11", command=lambda: change_font_size(11, win_name))
    font_menu.add_command(label="12", command=lambda: change_font_size(12, win_name))
    # Create a sub-menu for font options
    color_menu = Menu(view_menu, tearoff=0)
    #submenu.entryconfig(i, background=bg_color, foreground='white')
    view_menu.add_cascade(label="Color", menu=color_menu)
    color_menu.add_command(label="Choose Color", command=lambda: change_bg_color(win_name, switch_dict))
    """
def change_bg_color(win_name, switch_app_instance, row_index, column_index, class_instance, on_image, off_image):
    color = colorchooser.askcolor()[1]  # Get the selected color
    if color:
        # Change the window's background color
        win_name.configure(bg=color)

        # Change the background color of label widgets
        update_label_widgets_bg_color(win_name, color)

        # Change the background color of the switch
        switch_app_instance.add_switch(row_index, column_index, "SwitchButtonName", class_instance, on_image, off_image, color)

    """
    # Add row height options to the 'View' menu
    view_menu.add_command(label="Thin Rows", command=lambda: change_row_height(1, win_name))
    view_menu.add_command(label="Normal Rows", command=lambda: change_row_height(2, win_name))
    view_menu.add_command(label="Thick Rows", command=lambda: change_row_height(3, win_name))
    if win_name.title() == "win_db_wr": 
        view_menu.add_command(label="Show db register Map" \
                            , command=lambda: show_dc_write_register_map(win_name, \
                            "images/db_reg.png","db_register_map",x_position ,30))
    elif win_name.title() == "win_dc_wr_one": 
        view_menu.add_command(label="Show dc register Map" \
                            ,command=lambda: show_dc_write_register_map(win_name, \
                            "images/dc_write_register_map.png","dc_write_register_map",x_position ,30))
    elif win_name.title() == "win_otp": 
        view_menu.add_command(label="Show otp register Map" \
                            ,command=lambda: show_dc_write_register_map(win_name, \
                            "images/otp_register_map.png","otp_register_map",x_position ,30))
    elif win_name.title() == "win_ina228": 
        view_menu.add_command(label="Show ina228 register Map" \
                            ,command=lambda: show_dc_write_register_map(win_name, \
                            "images/ina228_register_map.png","ina228_register_map",x_position ,30))
    else:
        pass                            

    # Create a 'CMD' menu
    dc_cmd_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="CMD", menu=dc_cmd_menu)

    #############################################################
    #  Create scrollable bar 
    #############################################################
    # Create a canvas and a scrollbar
    '''
    canvas = Canvas(win_name)
    scrollbar = Scrollbar(win_name, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Place canvas and scrollbar in the parent window
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure the parent window to expand with resizing
    win_name.grid_rowconfigure(0, weight=1)
    win_name.grid_columnconfigure(0, weight=1)
    '''
    ######### END OF SCROLLABLE BAR CREATION #######################################

    # Add a command to toggle the visibility of the scroll bar
    #print(f"win_name.title is {win_name.title()}, win_name is {win_name}")
    temp_row_index = 0
    for i, item_text in enumerate(ITEMS):
        switch_dict,check_button, label_2nd, check_var , entry, row_index, \
            frame_row = create_win_row(switch_dict, ser_frame_instance,win_name, item_text, default_color, row_index=(temp_row_index + 1))
        temp_row_index = row_index
        # print(f"row_index is {temp_row_index}, i is {i}")
        # entry, check_var = create_win_row(win_name, item_text, row_index=i)
        #entry, check_var = create_win_row(win_name, item_text, row_index=i)
        # You can store the entry and check_var variables if needed for further processing
    #create_read_program_buttons(win_1)        

#    view_menu.add_command(label="Toggle Scrollbar", command=lambda: toggle_scrollbar(vbar,canvas))

ITEMS = [] # Declare ITEMS as global variable 

def wait_ser():
    #print(win_db_wr.title())
    text_color = "red"
    update_label_2nd_var("win_db_wr", 12, "99", text_color)
    """
    row_number = get_row_number("ITEMS_DB", "0x26")
    label_2nd_var = label_widgets_dict['win_db_wr'][row_number]["label_2nd_var"]    
    label_2nd_var.set("")
    label_2nd_var.set('ff')
    label_2nd_var = label_widgets_dict['win_db_wr'][2]["label_2nd_var"]    
    label_2nd_var.set("")
    label_2nd_var.set('fe')

    label_2nd_var = label_widgets_dict['win_db_wr'][11]["label_2nd_var"]    
    label_2nd_var.set("")
    label_2nd_var.set('11')
    label_2nd_widget = label_widgets_dict['win_db_wr'][11]["label_2nd_widget"]    
    label_2nd_widget.config(text='11')
    label_2nd_var = label_widgets_dict['win_db_wr'][12]["label_2nd_var"]    
    label_2nd_var.set("")
    label_2nd_var.set('12')
    label_2nd_widget = label_widgets_dict['win_db_wr'][12]["label_2nd_widget"]    
    label_2nd_widget.config(text='99')
    update_label_2nd_var("win_db_wr", 12, "99")
    #update_entry_text("win_db_wr", 13, "1f")
    """
    pass

 ######################################################################################
 # Emulate toggling the switch button for a specific row in win_otp (e.g., row 2)
 # NOT WORK
def print_all_switch_info(switch_dict):
    pprint(switch_dict)
    for win_name, switch_info in switch_dict.items():
        for row_index, info in switch_info.items():
            switch_name = getattr(info["app_switch_instance"], "switch_name_attribute", None)
            if switch_name:
                print(f"Window: {win_name}, Row Index: {row_index}, Switch Name: {switch_name}")

def print_all_switch_names(switch_dict):
    for win_name, switch_info in switch_dict.items():
        for row_index, info in switch_info.items():
            switch_name_attribute = getattr(info["app_switch_instance"], "switch_name_attribute", None)
            if switch_name_attribute is not None:
                print(f"Window: {win_name}, Row Index: {row_index}, Switch Name Attribute: {switch_name_attribute}")
            else:
                print(f"Window: {win_name}, Row Index: {row_index}, Switch Name Attribute: None")
            print("Switch Info:", info)


def emulate_switch(switch_dict,win_name, switch_name, ser_frame_instance):
    #win_name_text = win_name.title()
    win_name_text = win_name
    # Assuming switch_dict is a global variable
    #pprint(switch_dict)
    debug_print("Emulating switch toggle for window: {} and switch: {}".format(win_name_text, switch_name))
    # Check if the switch_name is in any of the switch dictionaries
    # Check if the switch_name is in any of the switch dictionaries
    matching_rows = [row_index for win_name, switch_info in switch_dict.items() for row_index, info in switch_info.items() if hasattr(info["app_switch_instance"], "switch_name_attribute") and getattr(info["app_switch_instance"], "switch_name_attribute") == switch_name]

    if matching_rows:
        row_index = matching_rows[0]
        win_name_text = win_name
        debug_print("win_name_text resides and row_index is {}".format(row_index))
        switch_app_instance = switch_dict[win_name_text][row_index]["app_switch_instance"]

    # Call the toggle_mode method
        switch_app_instance.toggle_mode(switch_name, ser_frame_instance)
    else:
        debug_print("Switch name not found for window: {} and switch: {}".format(win_name_text, switch_name))

    ######################################################################################

def update_entry_text(window_title, row, new_text):
    window_title_lower = window_title.lower()
    #print(f"314 parent is {parent} for window {parent} not found")
    #if parent.title() in label_widgets_dict and row in label_widgets_dict[parent.title()]:
    if window_title_lower in label_widgets_dict:
        # print(f"keys in label_widgets_dict: {label_widgets_dict[window_title_lower].keys()}, row is {row}]")
        if row in label_widgets_dict[window_title_lower]:
            entry_var = label_widgets_dict[window_title_lower][row]["entry_var"]
            entry_var.set(new_text)
        else:
            pass
            # print(f"Row {row} not found for window {window_title}")            
    else:
        pass
        # print(label_widgets_dict.keys())
        # print(f"318 Entry in row {row} for window {window_title_lower} not found")

def show_dc_write_register_map(parent_window, image_path, window_title, x_position, y_position):
    image_window = Toplevel(parent_window)
    image_window.title(window_title)
    
    img = Image.open(image_path)
    img = img.resize((950, 450), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
 
    label = Label(image_window, image=img_tk)
    label.image = img_tk  # Keep a reference to avoid garbage collection

    # Set the position of the image window to the left of the root window
    image_window.geometry(f"+{x_position}+{y_position}")
    label.pack()

def read_otp_values():
    # Add your logic for reading OTP values here
    print("Reading OTP values")

def write_otp_values():
    # Add your logic for reading OTP values here
    print("Writing OTP values")

def program_otp_values():
    # Add your logic for programming OTP values here
    print("Programming OTP values")

def main():
    root = Tk()
    root.title("Main Window")

    button = Button(root, text="btn_1", command=lambda: open_win(200,200))
    button.pack(side=LEFT, padx=10)

    root.mainloop()

def on_tab_selected(event):
    #selected_tab_id = notebook.index(notebook.seclect())
    #for tab_id in range(notebook.index("end")):
    #    notebook.tab(tab_id, option="text", text=notebook.tab(tab_id, "text" ))
    #notebook.tab(selected_tab_id, option="text", text="Tab 1", tag="selected")
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    
    if tab_text == " COM port   ":
#        update_com_port_content()
        frame4.focus_set()  # Set focus to the frame to trigger the update
    elif tab_text ==" jt3001     ":
#        update_jt3001_content()
        frame1.focus_set()  # Set focus to the frame to trigger the update
    elif tab_text ==" INA288     ":
#        update_INA228_content()
        frame2.focus_set()  # Set focus to the frame to trigger the update
    elif tab_text ==" tmp421     ":
#        update_tmp421_content()
        frame3.focus_set()  # Set focus to the frame to trigger the update

def update_com_port_content():
    # Update content for 
    # entry1.delete(0, tk.END)
    # entry1.insert(0, "Updated content for Tab 1")
    pass    

def update_jt3001_content():
    pass    

def update_INA228_content():
    pass    

def update_tmp421_content():
    pass    


####################################################################
#  Create the top-bar menu with windows , tools , Q&A 
####################################################################

sub_window_1_1 = None 
red_circle_label = None 
ina228_frame = None
win_dc_wr_one = None 
win_db_wr = None
win_otp = None
win_ina228 = None 
win_settings = None 
win_trim = None 


def on_menu_click(option):
    #debug_print("Selected option: {}", option)
    global red_circle_label
    if option == "i2c Ti current":
        show_ina228_frame()
        #disable_windows_option("i2c Ti current")
        #disable_cmd_option("Get Current")
    elif option == "Launch Vitis":
        try : 
            # subprocess.run(vitis_cmd, check=True, shell=True)
          pass
        except subprocess.CalledProcessError as e:
            # print(f"Error: {e}")
          pass

    elif option == "Run Application":
        try : 
          # Execute vitis.bat with the provided Tcl script
          #  subprocess.run([vitis_cmd, '-mode', 'batch', '-source', r'.\frank_subdir\launch_workspace.tcl', '-workspace', workspace_dir], shell=True)  
          pass
        except subprocess.CalledProcessError as e:
          #  print(f"Error: {e}")
          pass

    elif option == "Trim Vol_Cur":
        global win_trim
        if win_trim is None or not win_trim.winfo_exists():
            win_trim = create_subwindow("win_trim",330,680)
            open_win(win_trim, root.winfo_width() + 250)  
        # Bind the protocol to handle windows close event
        win_trim.protocol("WM_DELETE_WINDOW", on_trim_close)
        disable_cmd_option("Trim Vol_Cur")
    elif option == "Get Current":
        show_ina228_frame()
        #disable_windows_option("i2c Ti current")
        #disable_cmd_option("Get Current")
    elif option == "VPP_to_10V":
        show_red_circle()
        disable_cmd_option("VPP_to_10V")
        enable_cmd_option("VPP_to_5V")
    elif option == "VPP_to_5V":
        hide_red_circle()
        enable_cmd_option("VPP_to_10V")
        disable_cmd_option("VPP_to_5V")
    elif option == "Settings":
        global win_settings
        if win_settings is None or not win_settings.winfo_exists():
            win_settings = create_subwindow("win_settings",310,700)
            open_win(win_settings, root.winfo_width() + 250)  
        # Bind the protocol to handle windows close event
        win_settings.protocol("WM_DELETE_WINDOW", on_settings_close)
        disable_cmd_option("Settings")
    elif option == "dc write one":
        global win_dc_wr_one
        if win_dc_wr_one is None or not win_dc_wr_one.winfo_exists():
            win_dc_wr_one = create_subwindow("win_dc_wr_one",310,920)
            open_win(win_dc_wr_one, root.winfo_width() + 250)  
        # Bind the protocol to handle windows close event
        win_dc_wr_one.protocol("WM_DELETE_WINDOW", on_dc_wr_one_close)
        disable_cmd_option("dc write one")
    elif option == "OTP":
        global win_otp
        if win_otp is None or not win_otp.winfo_exists():
            win_otp = create_subwindow("win_otp",340,670)
            open_win(win_otp, root.winfo_width() + 250)  
        win_otp.protocol("WM_DELETE_WINDOW", on_otp_close)
        disable_cmd_option("OTP")

    elif option == "Reset DCON":
        cmd_to_ser(new_line, ser_frame_instance, f"RESET_DCON")

    elif option == "Ti_INA228":
        global win_ina228
        if win_ina228 is None or not win_ina228.winfo_exists():
            win_ina228 = create_subwindow("win_ina228",310,870)
            open_win(win_ina228, root.winfo_width() + 250)  
        win_ina228.protocol("WM_DELETE_WINDOW", on_ina228_close)
        disable_cmd_option("Ti_INA228")

    elif option == "db write":
        global win_db_wr
        if win_db_wr is None or not win_db_wr.winfo_exists():
            win_db_wr = create_subwindow("win_db_wr",300,720)
            open_win(win_db_wr, root.winfo_width() + 250)  
        win_db_wr.protocol("WM_DELETE_WINDOW", on_db_wr_close)
        disable_cmd_option("db write")

    elif option == "Suboption 1.1":
        global sub_window_1_1 
        if sub_window_1_1 is None or not sub_window_1_1.winfo_exists():
            sub_window_1_1 = create_subwindow("Suboption 1.1",250,300)

    elif option == "Suboption 1.2":
        create_subwindow("Suboption 1.2",250,300)
    #else:
    #    hide_ina228_frame()
###############################################################
#   to enable disable cmd option of "Ti ina228"        
def on_ina228_close():
    enable_cmd_option("Ti_INA228")
    #Destroy the dc_write_one window
    win_ina228.destroy()

###############################################################
#   to enable disable CMD option of "Trim Vol_Cur"        
def on_trim_close():
    enable_cmd_option("Trim Vol_Cur")
    #Destroy the settings window
    win_trim.destroy()

###############################################################
#   to enable disable cmd option of "Settings"        
def on_settings_close():
    enable_cmd_option("Settings")
    #Destroy the settings window
    win_settings.destroy()

###############################################################
#   to enable disable cmd option of "otp"        
def on_otp_close():
    enable_cmd_option("OTP")
    #Destroy the dc_write_one window
    win_otp.destroy()

###############################################################
#   to enable disable cmd option of "dc write on"        
def on_dc_wr_one_close():
    # This function will be called when the user closes the dc_write_one window
    # Enable the command button when the dc_write_one window is closed
    enable_cmd_option("dc write one")
    #Destroy the dc_write_one window
    #win_dc_wr_one.withdraw()
    #win_dc_wr_one.deiconify()
    debug_print("win_dc_wr_one destroy")
    win_dc_wr_one.destroy()

###############################################################
#   to enable disable cmd option of "db write"        
def on_db_wr_close():
    # This function will be called when the user closes the db_write window
    # Enable the command button when the db_write window is closed
    enable_cmd_option("db write")
    #Destroy the db_write window
    win_db_wr.destroy()

#############################################################
#  hide and show red_circle 
def on_frame2_close():
    enable_windows_option("i2c Ti current")
    enable_cmd_option("Get Current")
def show_ina228_frame():
    notebook.select(frame2)
    #global ina228_frame
    #if ina228_frame is None:
    #    notebook.select(frame2)
    #    frame2.protocol("WM_DELETE_WINDOW", on_ina228_frame_close)
def hide_ina228_frame():        
    global ina228_frame
    if ina228_frame is None:
        notebook.hide(frame2)
        enable_windows_option("i2c Ti current")
        enable_cmd_option("Get Current")
def on_ina228_frame_close():
    debug_print("Selected option x: {}", option)
    enable_cmd_option("Get Current")
    enable_windows_option("i2c Ti current")
def disable_windows_option(option):
    windows_menu.entryconfig(option, state=DISABLED)
def enable_windows_option(option):
    windows_menu.entryconfig(option, state=NORMAL)
def disable_cmd_option(option):
    CMD_menu.entryconfig(option, state=DISABLED)
def enable_cmd_option(option):
    CMD_menu.entryconfig(option, state=NORMAL)
def show_red_circle():
    global red_circle_label
    if red_circle_label is not None:
        #red_circle_label.grid(row=0, column=len(CMD_options), sticky="ne")  # Place it in the right corner (northeast)
        red_circle_label.place(relx=1.0, rely=0.0, anchor="ne")  # Place it in the right corner (northeast)

#############################################################

def create_subwindow(sub_option,width, height):
    sub_window = Toplevel(root)
    sub_window.title(f"{sub_option}")
    sub_window.resizable(True, True)

    # Calculate the cumulative width of all sub-windows
    cumulative_width = sum(win.winfo_width() for win in root.winfo_children() if isinstance(win, Toplevel))

    # Set the geometry to place the sub-window on the right side of the root window
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    sub_window_width = 500  # Set the width of the sub-window
    sub_window.geometry(f"{width}x{height}+{root_x + root.winfo_width() + cumulative_width}+{root_y}")
    # Add widgets to the sub-window if needed
    return sub_window


######  end of Create top_bar function ####################################


root = Tk()
ENG_MODE_VAR = StringVar()
#root.geometry('500x700+40+20')
root.resizable(False, False)
root.configure(bg='#eeeeee')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 450
h = 700
x = 10
y = 0
#x = (screenWidth - w) / 2
#y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

ENG_MODE_VAR.set("0")
ENG_MODE_VAR.trace_add("write", on_eng_mode_change)

# Keep track of the button state on/off
img = Image.open('images/logo_int_tech.png')
img = img.resize((100, 50), Image.LANCZOS)
img_tk = ImageTk.PhotoImage(img)
root.iconphoto(False, img_tk)
root.title("INT-TECH 創王 v1.0.0")

style = ttk.Style()
style.configure("TNotebook.Tab", padding=[0,0])
notebook = ttk.Notebook(root)

frame4 = Frame(notebook, bg='white', width=200, height=200, background="white")
frame1 = Frame(notebook, bg='white', width=200, height=200, background="white")
frame2 = Frame(notebook, bg='white', width=200, height=200, background="white")
frame3 = Frame(notebook, bg='white', width=200, height=200, background="white")

###############################################################
#   create menu top-bar 
###############################################################
#reate a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a drop-down menu
windows_menu = Menu(menu_bar, tearoff=0)
# Add options to the drop-down menu
windows_options = ["db_register", "dbo_freq", "i2c Ti current"]
for i, option in enumerate(windows_options):
        if option == "db_register":
            submenu = Menu(windows_menu, tearoff=0)
            # Adding an image to "channel_1"
            image_settings = PhotoImage(file="images/settings.png")
            submenu.add_command(label="channel_1", command=lambda: on_menu_click("Suboption 1.1"), image=image_settings, compound=LEFT)
            submenu.add_command(label="changel_2", command=lambda: on_menu_click("Suboption 1.2"))
            submenu.add_command(label="channel_3", command=lambda: on_menu_click("Suboption 1.2"))
            windows_menu.add_cascade(label=option, menu=submenu)
        else:
            windows_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt))
     # Add a separator between labels in "windows" menu
        if i < len(windows_options) - 1:
            windows_menu.add_separator()
################################################################
# Bind events to change the background color of selected bar            
windows_menu.bind("<Enter>", on_menu_enter)
windows_menu.bind("<Leave>", on_menu_leave)
################################################################

# Add the drop-down menu to the menu bar
menu_bar.add_cascade(label="Windows", menu=windows_menu)
################################################################

# Add a separator between "Windows" and "Q&A"
menu_bar.add_separator()

####################################################################
#   create qa_menu on the top-bar
qa_menu = Menu(menu_bar, tearoff=0)

# Adding an image to "Ask a Question" in "Q&A"

# Add options to the drop-down menu
qa_options = ["how to send db", "how to send dc", "how to program otp"]
for i, option in enumerate(qa_options):
        if option == "db_register":
            submenu = Menu(windows_menu, tearoff=0)
            submenu.add_command(label="channel_1", command=lambda: on_menu_click("Suboption 1.1"))
            submenu.add_command(label="changel_2", command=lambda: on_menu_click("Suboption 1.2"))
            submenu.add_command(label="channel_3", command=lambda: on_menu_click("Suboption 1.2"))
            qa_menu.add_cascade(label=option, menu=submenu)
        else:
            qa_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt))
     # Add a separator between labels in "qa" menu
        if i < len(qa_options) - 1:
            qa_menu.add_separator()
################################################################
# Bind events to change the background color of selected bar            
qa_menu.bind("<Enter>", on_menu_enter)
qa_menu.bind("<Leave>", on_menu_leave)
################################################################

menu_bar.add_cascade(label="Q&A", menu=qa_menu)
####################################################################
# Add a separator between "Q&A" and "CMD"
menu_bar.add_separator()

####################################################################
#   create TOOLS menu on the top-bar
####################################################################
tools_menu = Menu(menu_bar, tearoff=0)
# Add options to the drop-down menu
tools_options = ["vivado", "vitis", "VSCode", "vim" ]
for i, option in enumerate(tools_options):
    command = lambda opt=option: on_menu_click(opt)
    if option == "vivado":
        tools_menu.add_command(label=option, command=command, state=DISABLED)
    elif option == "vitis":
        # Create a submenu for "Vitis"
        vitis_submenu = Menu(tools_menu, tearoff=0)
        vitis_submenu.add_command(label="Launch Vitis", command=command)
        vitis_submenu.add_command(label="Run Application", command=command)
        # Add the submenu to the "Vitis" option in "Tools" menu
        tools_menu.add_cascade(label=option, menu=vitis_submenu)

    elif option == "VSCode":
        tools_menu.add_command(label=option, command=command, state=DISABLED)
    elif option == "vim":
        tools_menu.add_command(label=option, command=command, state=DISABLED)
    else:
        tools_menu.add_command(label=option, command=command)

    tools_menu.bind("<Enter>", on_menu_item_hover) # actually , the 1-level item won't have hover, leave, and image 
    tools_menu.bind("<Leave>", on_menu_item_leave) # actually , the 1-level item won't have hover, leave, and image

     # Add a separator between labels in "Tools" menu
    if i < len(tools_options) - 1:
        tools_menu.add_separator()

menu_bar.add_cascade(label="Tools", menu=tools_menu)

####################################################################
#   create CMD_menu on the top-bar
####################################################################
CMD_menu = Menu(menu_bar, tearoff=0)

# Add options to the drop-down menu
CMD_options = ["Settings", "Tools","Reset DCON", "Reset dimmer db", "Reset dimmer dc", "VPP_to_10V", 
               "VPP_to_5V","VDD_to_5V","VDD_to_3.3V","Ti_INA228",
               "i2c Ti current", "Trim Vol_Cur", "OTP", 
               "dc read multiple", "dc write one", "db write", 
               "Current Operation","emulate engineer mode", "Save settings to file", "Load settings from file"]
for i, option in enumerate(CMD_options):
    if option == "Get Current and compared last current":
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=DISABLED)
    elif option == "Reset dimmer db":
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=DISABLED)
    elif option == "Reset dimmer dc":
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=DISABLED)
    elif option == "Reset DCON": 
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=NORMAL)
    elif option == "Trim Vol_Cur":
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=NORMAL)
    elif option == "VPP_to_5V":
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=DISABLED)
    elif option == "VDD_to_3.3V":
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=DISABLED)
    elif option == "dc read multiple":
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt), state=DISABLED)
    elif option == "emulate engineer mode":
        CMD_menu.add_command(label=option, command=lambda opt=option: emulate_switch(switch_dict, "win_otp","ENGINEER MODE", ser_frame_instance))
    elif option == "Save settings to file":
        CMD_menu.add_command(label=option, command=lambda opt=option: write_content_to_file())
    elif option == "Load settings from file":
        CMD_menu.add_command(label=option, command=lambda opt=option: load_command())
    elif option == "Tools":
        CMD_submenu = Menu(CMD_menu, tearoff=0)
        # Adding an image to "Vivado"
        image_settings_vivado = PhotoImage(file="images/vivado_logo_16x16.png")
        CMD_submenu.add_command(label="Vivado", command=lambda: on_menu_click("vivado"), image=image_settings_vivado, compound=LEFT)

        # Adding a submenu for "Vitis"
        vitis_submenu = Menu(CMD_submenu, tearoff=0)
        image_settings_vitis = PhotoImage(file="images/vitis_logo_16x16.png")
        image_settings_running_vitis = PhotoImage(file="images/running.png")
        vitis_submenu.add_command(label="Launch Vitis", command=lambda: on_menu_click("Launch Vitis"), image=image_settings_vitis, compound=LEFT )
        vitis_submenu.add_command(label="Run Application", command=lambda: on_menu_click("Run Application"),image=image_settings_running_vitis, compound=LEFT )
        CMD_submenu.add_cascade(label="Vitis", menu=vitis_submenu,image=image_settings_vitis, compound=LEFT )

        #image_settings_vitis = PhotoImage(file="images/vitis_logo_16x16.png")
        #CMD_submenu.add_command(label="Vitis", command=lambda: on_menu_click("vitis"), image=image_settings_vitis, compound=LE

        CMD_submenu.add_command(label="VIM", command=lambda: on_menu_click("vim"), state=DISABLED)
        CMD_submenu.bind("<Enter>", lambda event: on_menu_item_hover("Tools"))  # Adjust the event handling accordingly
        CMD_submenu.bind("<Leave>", lambda event: on_menu_item_leave("Tools"))  # Adjust the event handling accordingly

        CMD_menu.add_cascade(label=option, menu=CMD_submenu)
    else:    
        CMD_menu.add_command(label=option, command=lambda opt=option: on_menu_click(opt))
     # Add a separator between labels in "CMD" menu
    if i < len(CMD_options) - 1:
        CMD_menu.add_separator()
################################################################
# Bind events to change the background color of selected bar            
CMD_menu.bind("<Enter>", on_menu_enter)
CMD_menu.bind("<Leave>", on_menu_leave)
################################################################

menu_bar.add_cascade(label="CMD", menu=CMD_menu)
################################################################

################################################################
# to create a red circle to the right of top
################################################################
red_circle_label = RedCircleLabel(root)
#red_circle_label.place(relx=1.0, rely=0.0, anchor="ne")  # Place it in the right corner (northeast)
#red_circle_label.grid(row=0, column=4, sticky="ne")  # Place it in the right corner (northeast)
################################################################


current_value = '1000'


Label(frame1, text="  ").grid(row=2, column=1, padx=2, sticky='w')
Label(frame1, text="CURRENT").grid(row=3, column=2, padx=2, sticky='w')
Label(frame1, text="VSHUNT").grid(row=4, column=2, padx=2, sticky='w')
Label(frame1, text="TEMPERATURE").grid(row=5, column=2, padx=2, sticky='w')

Label(frame2, text="  ").grid(row=2, column=1, padx=2, sticky='w')
Label(frame2, text="CONFIG").grid(row=3, column=1, padx=2, sticky='w')
ina228_config_value = Text(frame2, height=1, width=20)
ina228_config_value.insert("1.0", "0000 0000")
ina228_config_value.tag_configure("right", justify='right')
ina228_config_value.tag_add("right", "1.0", "end")
ina228_config_value.grid(row=3, column=2, padx=2, sticky='w')

Label(frame2, text="ADC_CONFIG").grid(row=4, column=1, padx=2, sticky='w')
ina228_adc_config_value = Text(frame2, height=1, width=20)
ina228_adc_config_value.insert("1.0", "0000 0000") 
ina228_adc_config_value.tag_configure("right", justify='right')
ina228_adc_config_value.tag_add("right", "1.0", "end")
ina228_adc_config_value.grid(row=4, column=2, padx=2, sticky='w')

Label(frame2, text="SHUNT_CAL").grid(row=5, column=1, padx=2, sticky='w')
ina228_shunt_cal_value = Text(frame2, height=1, width=20)
ina228_shunt_cal_value.insert("1.0", "0000 0000") 
ina228_shunt_cal_value.tag_configure("right", justify='right')
ina228_shunt_cal_value.tag_add("right", "1.0", "end")
ina228_shunt_cal_value.grid(row=5, column=2, padx=2, sticky='w')

Label(frame2, text="SHUNT_TEMPCO").grid(row=6, column=1, padx=2, sticky='w')
Label(frame2, text="VSHUNT").grid(row=7, column=1, padx=2, sticky='w')
ina228_vshunt_value = Text(frame2, height=1, width=20)
ina228_vshunt_value.insert("1.0", "0000 0000") 
ina228_vshunt_value.tag_configure("right", justify='right')
ina228_vshunt_value.tag_add("right", "1.0", "end")
ina228_vshunt_value.grid(row=6, column=2, padx=2, sticky='w')

Label(frame2, text="VBUS 電壓").grid(row=8, column=1, padx=2, sticky='w')
ina228_vbus_value = Text(frame2, height=1, width=20)
ina228_vbus_value.insert("1.0", "0000 0000 V") 
ina228_vbus_value.tag_configure("right", justify='right')
ina228_vbus_value.tag_add("right", "1.0", "end")
ina228_vbus_value.grid(row=8, column=2, padx=2, sticky='w')

Label(frame2, text="DIETEMP").grid(row=9, column=1, padx=2, sticky='w')

Label(frame2, text="CURRENT 電流").grid(row=10, column=1, padx=2, sticky='w')
ina228_current_value = Text(frame2, height=1, width=20)
ina228_current_value.insert("1.0", "0000 0000 A") 
ina228_current_value.tag_configure("right", justify='right')
ina228_current_value.tag_add("right", "1.0", "end")
ina228_current_value.grid(row=10, column=2, padx=2, sticky='w')

Label(frame2, text="POWER").grid(row=11, column=1, padx=2, sticky='w')
Label(frame2, text="ENERGY").grid(row=12, column=1, padx=2, sticky='w')
Label(frame2, text="CHARGE").grid(row=13, column=1, padx=2, sticky='w')
Label(frame2, text="DIAG_ALRT").grid(row=14, column=1, padx=2, sticky='w')
Label(frame2, text="SOVL").grid(row=15, column=1, padx=2, sticky='w')
Label(frame2, text="SUVL").grid(row=16, column=1, padx=2, sticky='w')
Label(frame2, text="BOVL").grid(row=17, column=1, padx=2, sticky='w')
Label(frame2, text="BUVL").grid(row=18, column=1, padx=2, sticky='w')
Label(frame2, text="TEMP_LIMIT").grid(row=19, column=1, padx=2, sticky='w')
Label(frame2, text="PWR_LIMIT").grid(row=20, column=1, padx=2, sticky='w')

Label(frame2, text="MANUFACTURE ID").grid(row=21, column=1, padx=2, sticky='w')
ina228_manufacture_id_value = Text(frame2, height=1, width=20)
ina228_manufacture_id_value.insert("1.0", "0000 0000") 
ina228_manufacture_id_value.tag_configure("right", justify='right')
ina228_manufacture_id_value.tag_add("right", "1.0", "end")
ina228_manufacture_id_value.grid(row=21, column=2, padx=2, sticky='w')

Label(frame2, text="DEVICE_ID").grid(row=22, column=1, padx=2, sticky='w')
ina228_device_id_value = Text(frame2, height=1, width=20)
ina228_device_id_value.insert("1.0", "0000 0000") 
ina228_device_id_value.tag_configure("right", justify='right')
ina228_device_id_value.tag_add("right", "1.0", "end")
ina228_device_id_value.grid(row=22, column=2, padx=2, sticky='w')

Label(frame2, text="").grid(row=23, column=1, padx=2, sticky='w')

# This way, the show function will only be executed when the button is clicked, and not immediately when the program runs.
btn_1_3_input_resistor = Button(frame2, text ="Change Resistor", command = lambda: show(ina228_shunt_cal_value))
btn_1_3_input_resistor.grid(row=24, column=1)
Label(frame2, text="   ").grid(row=24, column=2)
btn_1_1 = Button(frame2, text="Read", command=lambda: button_save(btn_1_1))
btn_1_1.grid(row=24, column=3)
Label(frame2, text="   ").grid(row=24, column=4)
btn_1_2 = Button(frame2, text="Save", command=button_save)
btn_1_2.grid(row=24, column=5)

for i, (label_text, entry_type) in enumerate(tmp421_reges):
    Label(frame3, text=label_text, cursor='plus').grid(row=i, column=0, padx=10, pady=1, sticky='w')
    if entry_type == 'Entry':
        Entry(frame3).grid(row=i, column=1, padx=2, sticky='w')
    else:
        Label(frame3, text=entry_type).grid(row=i, column=2, padx=2, sticky='w')

btn_2_1 = Button(frame3, text="Read", command=button_save)
btn_2_1.grid(row=len(labels_entries), column=1)
btn_2_2 = Button(frame3, text="Save", command=button_save)
btn_2_2.grid(row=len(labels_entries), column=2)

#frame4 = Frame(notebook, bg='white', width=200, height=200, background="white")
BAUD_RATES = (300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 76800, 115200, 23040, 500000, 1000000, 2000000)

#ser_frame_instance = mainGUIFrame(frame4)
ser_frame_instance = mainGUIFrame(frame4, ina228_vshunt_value=ina228_vshunt_value)

notebook.add(frame4, text=' COM port   ')
notebook.add(frame1, text=' jt3001     ')
notebook.add(frame2, text=' INA288     ')
notebook.add(frame3, text=' tmp421     ')
notebook.pack(padx=2, pady=1, fill=BOTH, expand=True)
#notebook.bind("<<NotebookTabChanged>>", on_tab_selected)
notebook.bind("<ButtonRelease-1>", on_tab_selected)

style = ttk.Style()
style.configure("TNotebook.Tab", foreground="black", font=("Tahoma", 10, "bold"))
style.map("TNotebook.Tab", foreground=[("selected", "Blue")])

# Bind focus event to update content when a tab gains focus
frame1.bind("<FocusIn>", lambda event: update_jt3001_content())
frame2.bind("<FocusIn>", lambda event: update_INA228_content())
frame3.bind("<FocusIn>", lambda event: update_tmp421_content())
frame4.bind("<FocusIn>", lambda event: update_com_port_content())

# Update text for Entry in row 0 for window "Window1"
#update_entry_text(win_db_wr", 1, "1f")

on_menu_click('db write')
root.update() # Manually trigger an update
on_menu_click("dc write one")
root.update() # Manually trigger an update
on_menu_click("Settings") # CMD_options
root.update() # Manually trigger an update
# on_menu_click("Trim Vol_Cur")
# root.update() # Manually trigger an update
# on_menu_click("OTP")
# root.update() # Manually trigger an update

root.mainloop()
