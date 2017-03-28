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
from winsound import *

# Create Instance of tkinter
win = tk.Tk()
win.title("MMI Demo Stand")
# win.resizable(width=False, height=False)
w, h = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry("%dx%d+0+0" % (w-100, h-100))


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
# CREATE CALLBACKS FOR BUTTONS IN TEST TONE DEMO
#=============================================
def _play440():
    "Plays 440Hz tone for 5s"
    old_color = 'whitesmoke'
    new_color = 'dodgerblue'
    # f1.set_facecolor(new_color)
    PlaySound('440_sound.wav', SND_FILENAME)
    # f1.set_facecolor(old_color)

def _play350():
    "Plays 350Hz tone for 5s"
    PlaySound('350_sound.wav', SND_FILENAME)

def _playDual():
    "Plays Dual Tone for 5s"
    PlaySound('dual_sound.wav', SND_FILENAME)


#=============================================
# CREATE OBJECTS IN TAB2: TEST TONE DEMO
#=============================================
# Set background color of tab to white

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

f1 = Figure(figsize=(w/110, h/275), facecolor="whitesmoke")
f2 = Figure(figsize=(w/110, h/275), facecolor="whitesmoke")
f3 = Figure(figsize=(w/110, h/275), facecolor="whitesmoke")

a1 = f1.add_subplot(211)
a2 = f1.add_subplot(212)
a3 = f2.add_subplot(211)
a4 = f2.add_subplot(212)
a5 = f3.add_subplot(211)
a6 = f3.add_subplot(212)

a1.plot(x_range1, wav1)
a1.set_title("First Tone 350 Hz")
a2.plot(x_range2, wav3)
a2.set_title("Zoomed...")
a3.plot(x_range1, wav2)
a3.set_title("Second Tone 440 Hz")
a4.plot(x_range2, wav4)
a4.set_title("Zoomed...")
a5.plot(x_range1, (wav1 + wav2))
a5.set_title("Combined 350 & 440 Hz Tones")
a6.plot(x_range2, (wav3 + wav4))
a6.set_title("Zoomed")

# plt.setp([a.get_xticklabels() for a in f1.axes[:-1]], visible=False)
plt.setp([a.get_yticklabels() for a in f1.axes], visible=False)
# plt.setp([a.get_xticklabels() for a in f2.axes[:-1]], visible=False)
plt.setp([a.get_yticklabels() for a in f2.axes], visible=False)
# plt.setp([a.get_xticklabels() for a in f3.axes[:-1]], visible=False)
plt.setp([a.get_yticklabels() for a in f3.axes], visible=False)

canvasf1 = FigureCanvasTkAgg(f1, tab2)
canvasf2 = FigureCanvasTkAgg(f2, tab2)
canvasf3 = FigureCanvasTkAgg(f3, tab2)
canvasf1.show()
canvasf2.show()
canvasf3.show()
canvasf1.get_tk_widget().grid(column=1, row=0, sticky="W")
canvasf2.get_tk_widget().grid(column=1, row=1, sticky="W")
canvasf3.get_tk_widget().grid(column=1, row=2, sticky="W")
f1.tight_layout()
f2.tight_layout()
f3.tight_layout()

playButton1 = ttk.Button(tab2, text="Play 350 Hz", command=_play350)
playButton1.grid(column=0, row=0, padx=10)
playButton2 = ttk.Button(tab2, text="Play 440 Hz", command=_play440)
playButton2.grid(column=0, row=1, padx=10)
playButton3 = ttk.Button(tab2, text="Play Dual Tone", command=_playDual)
playButton3.grid(column=0, row=2, padx=10)


#=============================================
# START GUI
#=============================================
win.mainloop()