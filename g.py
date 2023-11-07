import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os, sys

# Function for startup message
class MyGUI:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Hello, For feedback, upgrade or source code:", font=('Swis721 Cn BT', 8))
        self.label.pack()
        self.label.after(3000, self.label.destroy)
        self.flash_label = tk.Label(self.master, text="Mail: shifat.esolve@gmail.com", font=('Swis721 Cn BT', 10))
        self.flash_label.pack()
        self.flash_label.after(3000, self.flash_label.destroy)

def resource_path0(relative_path):
    """ Get the absolute path to a resource, accounting for PyInstaller and standalone script execution. """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base_path, relative_path)


# Function to calculate the slope based on selected unit
def slope_type_calculation(slope_type, raw_slope):
    if slope_type == '1:Slope':
        return raw_slope
    elif slope_type == '% Slope':
        return 1 / raw_slope
    elif slope_type == '‰ Slope':
        return (1 / raw_slope) * 1000
    else:
        return "err"

# Function to calculate downstream IL in tab 1
def calculate_tab1_output(*args):
    try:
        upstream_IL = float(tab1_input1.get())
        length = float(eval(tab1_input2.get()))
        raw_slope = float(tab1_input3.get())
        slope_type = selected_slope_unit_tab1.get()
        slope = slope_type_calculation(slope_type=slope_type, raw_slope=raw_slope)
        downstream_IL = round(upstream_IL - (length * (1 / slope)), 3)
        tab1_output.config(text=f'Downstream IL: {downstream_IL}')
        return downstream_IL
        
    except (ValueError, TypeError):
        tab1_output.config(text='Invalid input')

#Function to calculate depth of depth of Upstream/downstream

def calculate_tab1_gl2(*args):
    try:
        downstream_IL = calculate_tab1_output(*args)
        gl2 = float(tab1_input1gl2.get())
        if gl2 == "":
            pass
        else:
            tab1_output2.config(text=f"Depth:  {gl2-downstream_IL}")
    except (ValueError, TypeError):
        tab1_output2.config(text='Invalid input')

def calculate_tab1_gl1(*args):
    try:
        upstream_IL = float(tab1_input1.get())
        gl1 = float(tab1_inputgl.get())
        if gl1 == "":
            pass
        else:
            tab1_output1.config(text=f"Depth:  {gl1-upstream_IL}")
    except (ValueError, TypeError):
        tab1_output1.config(text='Invalid input')

# Function to calculate upstream IL in tab 2
def calculate_tab2_output(*args):
    try:
        downstream_IL = float(tab2_input1.get())
        length = float(eval(tab2_input2.get()))
        raw_slope = float(tab2_input3.get())
        slope_type = selected_slope_unit_tab2.get()
        slope = slope_type_calculation(slope_type=slope_type, raw_slope=raw_slope)
        upstream_IL = round(downstream_IL + (length * (1 / slope)), 3)
        tab2_output.config(text=f'Upstream IL: {upstream_IL}')
    except ValueError:
        tab2_output.config(text='Invalid input')

# Function to calculate slope in tab 3
def calculate_tab3_output(*args):
    try:
        upstream_IL = float(tab3_input1.get())
        downstream_IL = float(tab3_input2.get())
        length = float(eval(tab3_input3.get()))
        slope_type = selected_slope_unit_tab3.get()
        raw_slope = round(1 / ((upstream_IL - downstream_IL) / length), 2)
        slope = round(slope_type_calculation(slope_type=slope_type, raw_slope=raw_slope), 5)
        tab3_output.config(text=f'Slope: {slope}')
    except ValueError:
        tab3_output.config(text='Invalid input')

# Create the main application window
root = tk.Tk()
root.title('SlopeWizard beta v0.0.1')
root.attributes('-topmost', True)

# Create an instance of the startup message
gui = MyGUI(root)

# Create a notebook for tabbed interface
notebook = ttk.Notebook(root)

# Create and configure the content for tab 1
tab1_content = tk.Frame(notebook)
tab1_content.pack(fill='both', expand=True)
tab1_label = tk.Label(tab1_content, text='Calculator for Downstream IL', font=('Swis721 Cn BT', 24))
tab1_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create input fields, labels, and dropdown for tab 1
tab1_inputs = tk.Frame(tab1_content)
tab1_inputs.grid(row=1, column=0, padx=20, pady=20)

tab1_input1_label = tk.Label(tab1_inputs, text='Upstream IL', font=('Swis721 Cn BT', 14))
tab1_input1_label.grid(row=0, column=0, sticky='w')
tab1_input1 = tk.Entry(tab1_inputs)
tab1_input1.grid(row=1, column=0)

tab1_input1_label = tk.Label(tab1_inputs, text='Upstream GL', font=('Swis721 Cn BT', 14))
tab1_input1_label.grid(row=0, column=3, sticky='w')
tab1_inputgl = tk.Entry(tab1_inputs)
tab1_inputgl.grid(row=1, column=3)

tab1_input2_label = tk.Label(tab1_inputs, text='Length', font=('Swis721 Cn BT', 14))
tab1_input2_label.grid(row=2, column=0, sticky='w')
tab1_input2 = tk.Entry(tab1_inputs)
tab1_input2.grid(row=3, column=0)

tab1_input3_label = tk.Label(tab1_inputs, text='Slope', font=('Swis721 Cn BT', 14))
tab1_input3_label.grid(row=4, column=0, sticky='w')
tab1_input3 = tk.Entry(tab1_inputs)
tab1_input3.grid(row=5, column=0)

slope_units = ['Select One', '1:Slope', '% Slope', '‰ Slope']
selected_slope_unit_tab1 = tk.StringVar()
selected_slope_unit_tab1.set(slope_units[0])

slope_dropdown_tab1 = ttk.OptionMenu(tab1_inputs, selected_slope_unit_tab1, *slope_units)
slope_dropdown_tab1.grid(row=5, column=2)

tab1_input1_label = tk.Label(tab1_inputs, text='Downstream GL', font=('Swis721 Cn BT', 14))
tab1_input1_label.grid(row=0, column=3, sticky='w')
tab1_input1gl2 = tk.Entry(tab1_inputs)
tab1_input1gl2.grid(row=6, column=3)


tab1_output = tk.Label(tab1_inputs, text='', font=('Swis721 Cn BT', 14))
tab1_output.grid(row=6, column=0, pady=10)

tab1_output1 = tk.Label(tab1_inputs, text='', font=('Swis721 Cn BT', 14))
tab1_output1.grid(row=1, column=4, pady=10)

tab1_output2 = tk.Label(tab1_inputs, text='', font=('Swis721 Cn BT', 14))
tab1_output2.grid(row=6, column=4, pady=10)

# Bind events for tab 1
tab1_input1.bind("<KeyRelease>", calculate_tab1_output)
tab1_input2.bind("<KeyRelease>", calculate_tab1_output)
tab1_input3.bind("<KeyRelease>", calculate_tab1_output)
tab1_inputgl.bind("<KeyRelease>", calculate_tab1_gl1)
tab1_input1gl2.bind("<KeyRelease>", calculate_tab1_output,calculate_tab1_gl2)
slope_dropdown_tab1.bind("<Configure>", calculate_tab1_output)

# Create an image area for tab 1
tab1_image_area = tk.Frame(tab1_content, bg='white')
tab1_image_area.grid(row=1, column=1, padx=20, pady=20)

image = Image.open(resource_path0('dn.png')).resize((300, 300))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(tab1_image_area, image=photo)
image_label.image = photo
image_label.pack()

# Create and configure the content for tab 2 (similar to tab 1)
tab2_content = tk.Frame(notebook)
tab2_content.pack(fill='both', expand=True)
tab2_label = tk.Label(tab2_content, text='Calculator for Upstream IL', font=('Swis721 Cn BT', 24))
tab2_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tab2_inputs = tk.Frame(tab2_content)
tab2_inputs.grid(row=1, column=0, padx=20, pady=20)

tab2_input1_label = tk.Label(tab2_inputs, text='Downstream IL', font=('Swis721 Cn BT', 14))
tab2_input1_label.grid(row=0, column=0, sticky='w')
tab2_input1 = tk.Entry(tab2_inputs)
tab2_input1.grid(row=1, column=0)

tab2_input2_label = tk.Label(tab2_inputs, text='Length', font=('Swis721 Cn BT', 14))
tab2_input2_label.grid(row=2, column=0, sticky='w')
tab2_input2 = tk.Entry(tab2_inputs)
tab2_input2.grid(row=3, column=0)

tab2_input3_label = tk.Label(tab2_inputs, text='Slope', font=('Swis721 Cn BT', 14))
tab2_input3_label.grid(row=4, column=0, sticky='w')
tab2_input3 = tk.Entry(tab2_inputs)
tab2_input3.grid(row=5, column=0)

selected_slope_unit_tab2 = tk.StringVar()
selected_slope_unit_tab2.set(slope_units[0])

slope_dropdown_tab2 = ttk.OptionMenu(tab2_inputs, selected_slope_unit_tab2, *slope_units)
slope_dropdown_tab2.grid(row=5, column=2)

tab2_output = tk.Label(tab2_inputs, text='', font=('Swis721 Cn BT', 14))
tab2_output.grid(row=6, column=0, pady=10)

tab2_input1.bind("<KeyRelease>", calculate_tab2_output)
tab2_input2.bind("<KeyRelease>", calculate_tab2_output)
tab2_input3.bind("<KeyRelease>", calculate_tab2_output)
slope_dropdown_tab2.bind("<Configure>", calculate_tab2_output)

tab2_image_area = tk.Frame(tab2_content, bg='white')
tab2_image_area.grid(row=1, column=1, padx=20, pady=20)

image = Image.open(resource_path0('up.png')).resize((300, 300))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(tab2_image_area, image=photo)
image_label.image = photo
image_label.pack()

# Create and configure the content for tab 3 (similar to tab 1)
tab3_content = tk.Frame(notebook)
tab3_content.pack(fill='both', expand=True)
tab3_label = tk.Label(tab3_content, text='Calculator for Slope', font=('Swis721 Cn BT', 24))
tab3_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tab3_inputs = tk.Frame(tab3_content)
tab3_inputs.grid(row=1, column=0, padx=20, pady=20)

tab3_input1_label = tk.Label(tab3_inputs, text='Upstream IL', font=('Swis721 Cn BT', 14))
tab3_input1_label.grid(row=0, column=0, sticky='w')
tab3_input1 = tk.Entry(tab3_inputs)
tab3_input1.grid(row=1, column=0)

tab3_input2_label = tk.Label(tab3_inputs, text='Downstream IL', font=('Swis721 Cn BT', 14))
tab3_input2_label.grid(row=2, column=0, sticky='w')
tab3_input2 = tk.Entry(tab3_inputs)
tab3_input2.grid(row=3, column=0)

tab3_input3_label = tk.Label(tab3_inputs, text='Length', font=('Swis721 Cn BT', 14))
tab3_input3_label.grid(row=4, column=0, sticky='w')
tab3_input3 = tk.Entry(tab3_inputs)
tab3_input3.grid(row=5, column=0)

selected_slope_unit_tab3 = tk.StringVar()
selected_slope_unit_tab3.set(slope_units[0])

slope_dropdown_tab3 = ttk.OptionMenu(tab3_inputs, selected_slope_unit_tab3, *slope_units)
slope_dropdown_tab3.grid(row=6, column=2)

tab3_output = tk.Label(tab3_inputs, text='', font=('Swis721 Cn BT', 14))
tab3_output.grid(row=6, column=0, pady=10)

tab3_input1.bind("<KeyRelease>", calculate_tab3_output)
tab3_input2.bind("<KeyRelease>", calculate_tab3_output)
tab3_input3.bind("<KeyRelease>", calculate_tab3_output)
slope_dropdown_tab3.bind("<Configure>", calculate_tab3_output)

tab3_image_area = tk.Frame(tab3_content, bg='white')
tab3_image_area.grid(row=1, column=1, padx=20, pady=20)

image = Image.open(resource_path0('sl.png')).resize((300, 300))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(tab3_image_area, image=photo)
image_label.image = photo
image_label.pack()

# Add the tabs to the notebook
notebook.add(tab1_content, text='Downstream IL')
notebook.add(tab2_content, text='Upstream IL')
notebook.add(tab3_content, text='Slope')
notebook.pack(fill='both', expand=True)

# Start the main application loop
root.mainloop()
