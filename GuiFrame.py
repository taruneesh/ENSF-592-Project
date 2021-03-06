'''
@author(s) Neha Singh, Sanyam, Taruneesh Sachdeva
'''
import tkinter as tk
from tkinter import ttk
from draw_graph import draw_graph
from db_manager_new import DbManagerNew
import pymongo
import csv
import matplotlib

from draw_map import draw_map
from read_data import read_data
from sort_data import sort_data

# Specifying the backend "TkAgg" to be used with Matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GuiFrame():
    '''GuiFrame implements the main frame of the Gui to display data based on selections made by the user.
    '''
    global db_manager
    global yr
    global tp
    db_manager = DbManagerNew()
    yr = 0
    tp = ""

    # comboFunc is called when the user selects type
    def comboFunc(self,event):
        global tp
        if comboType.get() == "Accident":
            tp = "traffic_incidents"
        elif comboType.get() == "Traffic Volume":
            tp = "traffic_volume"

    # comboFuncYr is called when the user selects year
    def comboFuncYr(self, event):
        global yr 
        if (comboYear.get()) == "2016":
            yr = "2016"
        elif (comboYear.get()) == "2017":
            yr = "2017"
        else:
            yr = "2018"

    def drawFrame(self, window):

        # setting row and column configurations
        window.rowconfigure(0, minsize=700, weight=1)
        window.columnconfigure(1, minsize=1000, weight=1)

        # creating a frame to add all the buttons
        fr_buttons = tk.Frame(window)

        # creating widget Combobox for the type of data
        global comboType
        comboType = ttk.Combobox(fr_buttons, values=["Accident", "Traffic Volume"],state='readonly')
        comboType.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        # creates Tkinter combobox widget instance
        comboType.current(0)

        # creating widget Combobox for the year
        global comboYear
        comboYear = ttk.Combobox(fr_buttons, values=["2016", "2017", "2018"],state = 'readonly')
        comboYear.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
        # creates Tkinter combobox widget instance
        comboYear.current(0)

        # adding button for reading the data
        readButton = tk.Button(fr_buttons, text='Read', bg='white', activebackground='red')
        readButton.grid(row=3, column=0, sticky='ew', padx=5, pady=5)

        # adding button for sorting the data
        sortButton = tk.Button(fr_buttons, text='Sort', bg='white')
        sortButton.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

        # adding button for displaying the analysis of the data
        analyseButton = tk.Button(fr_buttons, text='Analyse', bg='white')
        analyseButton.grid(row=5, column=0, sticky='ew', padx=5, pady=5)

        # adding button for displaying the map
        mapButton = tk.Button(fr_buttons, text='Map', bg='white')
        mapButton.grid(row=6, column=0, sticky='ew', padx=5, pady=5)

        # Label added to the frame
        # anchor adjusts the label to the left
        statusLabel = tk.Label(fr_buttons, text='Status : ', anchor='w')
        statusLabel.grid(row=7, column=0, sticky='ew', padx=5, pady=5)

        # Text box for displaying the status of the execution
        statusText = tk.Text(fr_buttons, height=5, width=15)
        statusText.grid(row=8, column=0)

        # adding frame to the main window
        fr_buttons.grid(row=0, column=0, sticky="ns")

        # Right Frame
        canvas = tk.Canvas(window)
        canvas.grid(row=0, column=1, sticky="nsew")

        # calls the read method of read_data class when Read button is pressed
        readButton.bind("<Button-1>", lambda event: read_data.read(event, win = window, text = statusText,
                                                                       year = yr, type = tp, obj = db_manager))
        # calls the sort method of sort_data class when Sort button is pressed
        sortButton.bind("<Button-1>", lambda event: sort_data.sort(event, win = window, text = statusText,
                                                                       year = yr, type = tp, obj = db_manager))
        # calls the draw method of draw_map class when Map button is pressed
        mapButton.bind("<Button-1>", lambda event: draw_map.draw(event, year = yr, type = tp,
                                                                 text = statusText, win = window, obj = db_manager))
        # calls the draw method of draw_graph class when Analyse button is pressed
        analyseButton.bind("<Button-1>", lambda event: draw_graph.draw(event,  win = window,
                                                                       text = statusText,  type = tp, obj = db_manager))

        # comboFunc and comboFuncYr function are called when user selects the type and year
        comboType.bind("<<ComboboxSelected>>", self.comboFunc)
        comboYear.bind("<<ComboboxSelected>>", self.comboFuncYr)

        # Event driven Programming. Continuously run the code and
        # waits for the user input.
        window.mainloop()

if __name__ == '__main__':

    # creates an object of class GuiFrame
    fr = GuiFrame()

    # creating an instance of Tkinter's Tk class
    window = tk.Tk()

    window.title('Data Analysis')

    #global db_manager
    fr.drawFrame(window)



    


