from tkinter import * 
from .lib import crc8, cmd_to_ser, cmd_to_ser_continous,debug_print
from tkinter import PhotoImage
from .lib_1 import debug_print
from .common import DIM_ID 
import common
import sys
#sys.path.append('/Users/at891/source/prgtst')
sys.path.append('at891/source/prgtst/SerialMonitor_main')

def update_new_line():
    if common.new_line: 
        common.new_line = False

#from . import frank  
#from SerialMonitor_main import frank  
def on_menu_item_hover(event):
    # Change the foreground color only if the menu item is not disabled
    if event.widget["state"] != DISABLED:
        event.widget.config(fg="blue")

def on_menu_item_leave(event):
    # Reset the foreground color when leaving the menu item
    event.widget.config(fg="black")

def on_menu_enter(event):
    #if not event.widget.instate(['disabled']):
    event.widget.configure(background="#FFBFFF")
        #event.widget.configure(background="#00BFFF")
    #menu_bar.entryconfig(background="deep sky blue")

def on_menu_leave(event):
    #if not event.widget.instate(['disabled']):
    event.widget.configure(background="#FFBFFF")
    #menu_bar.entryconfig(event.widget.name, background="")

####################   snippet for create switch button ########################
#  Tempalate for usage 
"""
#def open_sub_window():
#    sub_window = tk.Toplevel(root)
#    app = SwitchApp(sub_window)

    # Add buttons dynamically to the subwindow
    app.add_button("EngMode", app.img_eng_mode_on, app.img_eng_mode_off)
    app.add_button("VppMode", app.img_vpp_on, app.img_vpp_off)
"""
