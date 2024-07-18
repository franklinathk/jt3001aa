# frank_subdir/__init__.py
import globals
from .lib_1 import debug_print, is_valid_hex, show_warning_message, crc8, get_row_number
from .lib import cmd_to_ser, cmd_to_ser_continous, write_content_to_file, load_file, load_command, \
                 get_label_2nd_var_values, get_file_content, process_loaded_content, \
                 extract_color_from_file_content, extract_value_from_file_content, \
                 update_label_widgets_bg_color, change_bg_color, update_label_2nd_var, \
                 update_label_trim_var, create_win_row, \
                 button_hover, button_leave, button_pressed, button_released, on_menu_enter, \
                 on_menu_item_hover, on_menu_item_leave, on_menu_leave, button_save, write_button_clicked, read_button_clicked, \
                 mainGUIFrame, InformWindow, SwitchApp
from .layout import change_font_size, hide_red_circle, draw_red_circle, RedCircleLabel, change_row_height, update_dc_write_color, toggle_scrollbar, \
                 show                 

def set_global_var_DIM_ID(new_value):
    globals.DIM_ID = new_value

def set_global_var_READ_NUM(new_value):
    globals.READ_NUM = new_value

def set_global_var_READ_NUM_INT(new_value):
    globals.READ_NUM_INT = new_value

def set_global_var_START_REG_ADDR(new_value):
    globals.START_REG_ADDR = new_value

def set_global_var_READ_ROW_NUM(new_value):
    globals.READ_ROW_NUM = new_value

__all__ = [      'debug_print', 'is_valid_hex', 'on_menu_item_hover', 'show_warning_message', 'crc8','get_row_number', 
                 'cmd_to_ser' , 'cmd_to_ser_continous', 'write_content_to_file', 'load_file', 'load_command', 
                 'get_label_2nd_var_values', 'get_file_content', 'process_loaded_content', 
                 'extract_color_from_file_content', 'extract_value_from_file_content', 
                 'update_label_widgets_bg_color', 'change_bg_color', 'update_label_2nd_var', 
                 'update_label_trim_var', 'create_win_row', 
                 'button_hover', 'button_leave', 'button_pressed','button_released', 'on_menu_enter', 
                 'on_menu_item_hover', 'on_menu_item_leave', 'on_menu_leave', 'button_save', 'write_button_clicked', 'read_button_clicked',
                 'mainGUIFrame', 'InformWindow', 'SwitchApp',
                 'change_font_size', 'hide_red_circle', 'draw_red_circle', 'RedCircleLabel', 'change_row_height', 'update_dc_write_color', 'toggle_scrollbar', 'show' 
          ]

"""
The __all__ variable in a Python module is a list of public objects of that module, 
as interpreted by import *. When you define __all__, 
you're specifying which attributes or functions are accessible when a client does a wildcard import from the module.
"""