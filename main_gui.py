#=============================================
# IMPORTS
#=============================================
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import math
from tkinter import ttk
from tkinter import Menu
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Create Instance of tkinter
win = tk.Tk()
win.title("MMI Demo Stand")
# win.resizable(width=False, height=False)
win.geometry('{}x{}'.format(1800,1200))

#=============================================
# Menu Callbacks
#=============================================
def _quit():
    """Closes out of the program."""
    win.quit()
    win.destroy()
    exit()
#=============================================
# Create Tabs
#=============================================
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Connect to Meters")
tabControl.add(tab2, text="Test Tone Demo")
tabControl.add(tab3, text="Meter Verify Demo")
tabControl.add(tab4, text="Plot Process Variables")
tabControl.pack(expand=1, fill="both")

#=============================================
# Create Menu
#=============================================
menuBar = Menu(win)
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="Status", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Demo.exe Overview")
helpMenu.add_command(label="USB to 232 Converter Tip")
helpMenu.add_command(label="Setting Up Demo Stands")
helpMenu.add_command(label="SMV Overview")
helpMenu.add_command(label="Useful SMV Tip")
helpMenu.add_command(label="SMV & Prolink General Information")
helpMenu.add_command(label="Resetting Factory Baselines")
helpMenu.add_separator()
helpMenu.add_command(label="About Demo.exe")
menuBar.add_cascade(label="Help", menu=helpMenu)

#=============================================
# CREATE OBJECTS IN TAB1: CONNECT TO METERS
#=============================================
# Create Connect LabelFrame
connFrame = ttk.LabelFrame(tab1, text="  Connect a Meter  ")
connFrame.grid(column=0, row=0)

# Add Connect button
connectButton = ttk.Button(connFrame, text="Connect")
connectButton.grid(column=0, row=0, padx=40, pady=20)

# Add Serial Port label
serialPortLabel = ttk.Label(connFrame, text="Serial Port:")
serialPortLabel.grid(column=1, row=0, pady=20)

# Add combobox for COMs
number = tk.StringVar()
comBox = ttk.Combobox(connFrame, width=12, textvariable=number, state='readonly')
comBox['values'] = ["COM" + str(num) for num in list(range(1,21))]
comBox.grid(column=2, row=0, padx=10)

# Add label for Connected Transmitters
connTransLabel = ttk.Label(connFrame, text="Connected Transmitters:")
connTransLabel.grid(column=3, row=0, padx=10)
connTrans = ttk.Label(connFrame, text="N/A", relief=tk.GROOVE, background="white", width=10)
connTrans.grid(column=4, row=0, padx=10)

# Create Device Types LabelFrame
devTypeFrame = ttk.LabelFrame(tab1, text="  Device Types  ")
devTypeFrame.grid(column=0, row=1)
# Create label for Uses:
useLabel = ttk.Label(devTypeFrame, text="Use As:")
useLabel.grid(column=2, row=0)
# Create Device Type at Address number label
for i in range(1,4):
    label = ttk.Label(devTypeFrame, text="Device Type at Address %d" % i)
    label.grid(column=0, row=i, padx=20, pady=5)

# Create actual Device Type label
devType1 = ttk.Label(devTypeFrame, text="N/A", relief=tk.GROOVE, background="white", width=40)
devType1.grid(column=1, row=1, padx=5, sticky="W")
devType2 = ttk.Label(devTypeFrame, text="N/A", relief=tk.GROOVE, background="white", width=40)
devType2.grid(column=1, row=2, padx=5, sticky="W")
devType3 = ttk.Label(devTypeFrame, text="N/A", relief=tk.GROOVE, background="white", width=40)
devType3.grid(column=1, row=3, padx=5, sticky="W")

# Create meter type comboboxes
useType1Var = tk.StringVar()
useType2Var = tk.StringVar()
useType3Var = tk.StringVar()

useTypes = ['UUT','Water Ref', 'Air Ref']
useType1 = ttk.Combobox(devTypeFrame, textvariable=useType1Var, state='readonly', width=15, values=useTypes)
useType1.grid(column=2, row=1, padx=5, sticky="W")
useType2 = ttk.Combobox(devTypeFrame, textvariable=useType2Var, state='readonly', width=15, values=useTypes)
useType2.grid(column=2, row=2, padx=5, sticky="W")
useType3 = ttk.Combobox(devTypeFrame, textvariable=useType3Var, state='readonly', width=15, values=useTypes)
useType3.grid(column=2, row=3, padx=5, sticky="W")
# Align objects in tab 1
for child in tab1.winfo_children():
    child.grid_configure(padx=20, pady=10, sticky="WE")

#=============================================
# CREATE OBJECTS IN TAB2: TEST TONE DEMO
#=============================================
# Create data for tone plots
pitch1 = 350
pitch2 = 440
sec1 = 2 #seconds
x_range1 = np.arange(0, 1, .001)
x_range2 = np.arange(0, .1, .0001)
wav1 = np.sin(2*x_range1*pitch1*math.pi) # original 350 hz
wav2 = np.sin(2*x_range1*pitch2*math.pi) # original 440 hz
wav3 = np.sin(2*x_range2*pitch1*math.pi) # zoomed in 350 hz
wav4 = np.sin(2*x_range2*pitch2*math.pi) # zoomed in 440 hz

t350 = Figure(figsize=(22,15))
t350.subplots_adjust(right=0.7, left=0.1, top=0.9, bottom=0.1, hspace=0.5)
a1 = t350.add_subplot(611)
a2 = t350.add_subplot(612)
a3 = t350.add_subplot(613)
a4 = t350.add_subplot(614)
a5 = t350.add_subplot(615)
a6 = t350.add_subplot(616)

a1.plot(x_range1, wav1)
a1.set_ylabel("First Tone 350 Hz")
a2.plot(x_range2, wav3)
a2.set_ylabel("Zoomed...")
a3.plot(x_range1, wav2)
a3.set_ylabel("Second Tone 440 Hz")
a4.plot(x_range2, wav4)
a4.set_ylabel("Zoomed...")
a5.plot(x_range1, (wav1 + wav2))
a5.set_ylabel("Combined 350 & \n440 Hz Tones")
a6.plot(x_range2, (wav3 + wav4))
a6.set_ylabel("Zoomed")

canvasT350 = FigureCanvasTkAgg(t350, tab2)

canvasT350.show()

canvasT350.get_tk_widget().grid(column=0, row=0, pady=15)


#=============================================
# START GUI
#=============================================
win.mainloop()