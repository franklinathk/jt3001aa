from tkinter import Frame, StringVar, Button, Canvas 
from tkinter import Label, Text, END, W, E, RIGHT, LEFT, ttk
from tkinter import Scrollbar, WORD , Y, BOTH, Checkbutton
from .items import ITEMS_SETTINGS,ITEMS_VOL_CUR,ITEMS_INA228,  ITEMS_OTP, ITEMS_DB, ITEMS_DC
from tkinter.simpledialog import askfloat
# Note the dot (.) before 'items'. This indicates a relative import from the same directory.
def change_font_size(size,parent):
    new_font = ("Helvetica", size)
    for child in parent.winfo_children():
        if isinstance(child, Button) or isinstance(child, Label) or isinstance(child, Checkbutton):
            child.configure(font=new_font)


#############################################################
def hide_red_circle():
    global red_circle_label
    if red_circle_label is not None:
        red_circle_label.place_forget()  # Hide the red circle

def draw_red_circle(canvas):
    canvas.create_oval(0, 0, 20, 20, fill="red", outline="red")
    #canvas.create_text(10, 10, text="VPP_10V", fill="white")

class RedCircleLabel(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.canvas = Canvas(self, width=20, height=20, background="white", highlightthickness=0)
        self.canvas.create_oval(0,0,20,20, fill="red", outline ="red")
        self.label = Label(self, text="VPP_10V")
        self.canvas.pack(side=LEFT,pady=(5,0))
        self.label.pack(side=LEFT)
        #draw_red_circle(self.canvas)
        #self.grid_forget() # Initially hide the red circle

#############################################################
# Function to change the row height
def change_row_height(height, parent):
    if parent.title() == "win_db_wr": 
        for i in range(len(ITEMS_DB)):
            parent.rowconfigure(i, weight=0, minsize=height)
    elif parent.title() == "win_dc_wr_one": 
        for i in range(len(ITEMS_DC)):
            parent.rowconfigure(i, weight=0, minsize=height)
    elif parent.title() == "win_otp": 
        for i in range(len(ITEMS_OTP)):
            parent.rowconfigure(i, weight=0, minsize=height)
    elif parent.title() == "win_ina228": 
        for i in range(len(ITEMS_INA228)):
            parent.rowconfigure(i, weight=0, minsize=height)
    elif parent.title() == "win_trim": 
        for i in range(len(ITEMS_VOL_CUR)):
            parent.rowconfigure(i, weight=0, minsize=height)
    elif parent.title() == "win_settings": 
        for i in range(len(ITEMS_SETTINGS)):
            parent.rowconfigure(i, weight=0, minsize=height)

def update_dc_write_color(entry, var):
    if var.get() == 1:
        entry.config(fg="red")
    else:
        entry.config(fg="black")

def toggle_scrollbar(vbar, canvas):
    if vbar.get():
        vbar.grid_forget()
    else:
        #vbar.pack(side=tk.RIGHT, fill=tk.Y)
        #vbar.grid(row=0, column=1, sticky='ns', rowspan=len(ITEMS) +1)
        pass
    canvas.config(scrollregion=canvas.bbox("all"))

def show(widget):
   rshunt = askfloat("Input", "Input a floating point number")
   print("rshunt is %f:", rshunt)
   shunt_cal = 350 * 13107.2 * 0.001 * 10**6 / 2**19 * rshunt  # 350mA 
   print("shunt_cal is %f: ", shunt_cal)
   widget.delete(1.0, "end")
   widget.tag_configure("right", justify="right")
   text_to_insert = f"{shunt_cal} Ohm"
   widget.insert("1.0", text_to_insert, "right") 

