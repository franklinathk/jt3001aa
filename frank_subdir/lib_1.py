import inspect
import os
from tkinter import messagebox, NORMAL, DISABLED
from .common import DIM_ID, READ_NUM, START_REG_ADDR, READ_ROW_NUM, READ_NUM_INT 
import time
import threading

MALACHITE_GREEN = '#00a15c'

def get_row_number(array_name, item_text):
    row_num = None
    debug_print("here is get_row_number function")
    #for row_num, item_info in enumerate(globals()[array_name], start=1):
    for idx, item_info in enumerate(array_name):
        debug_print("here is get_row_number function")
        #if item_info[0].startswith("COARSE FREQ"):
        if item_info[0] == item_text:
            row_num = idx + 1
            break
    return row_num
    # return None  # Return None if item_text is not found in the array

def is_valid_hex(value):
    try:
        int_value = int(value, 16)
        return 0 <= int_value <= 255
    except ValueError:
        return False

def show_warning_message(title, message):
    messagebox.showerror(title,message)
    # Implement your warning message window display here
    # You can use tkinter's Toplevel to create a new window with the warning message
    pass

def crc8(input_string):
    #nput_string = "00 01 00 00"
    input_data = [int(byte, 16) for byte in input_string.split()]
    crc = 0xFF
    for byte in input_data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x31 # x^8 + x^5 + x^4 + 1
            else:
                crc <<= 1
    return_crc = crc & 0xFF            
    return "{:02X}".format(return_crc)

def debug_print(debug_message, *args):
    frame_info = inspect.stack()[1]
    line_num = frame_info[2]
    file_name = os.path.basename(frame_info[1])
    
    formatted_message = debug_message.format(*args)
    
    # Convert text representations to unsigned 32-bit binary
    args_binary = [
        format(int(arg) & 0xFFFFFFFF, '032b') if str(arg).lstrip('-').isdigit() else arg
        for arg in args
    ]
    
    print(f"Debug: {file_name}, Line {line_num} - {formatted_message.format(*args_binary)}")

