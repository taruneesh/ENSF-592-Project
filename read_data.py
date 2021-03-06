'''
@author(s) Neha Singh, Sanyam, Taruneesh Sachdeva

This .py file has a class read_data and uses the db_manager_new class.
'''
from tkinter import *
import tkinter as tk
from db_manager_new import DbManagerNew


class read_data():
    '''class read_data displays the data fetched from database based on year and type selected by the user in the GUI.
    '''
    def read(self, win,text, year, type,obj):
        text.delete('1.0', tk.END) #clears status

        #If the user selection is not valid
        if((year == 0) or (type == "")):
            text.insert(tk.END, "Please select valid type and year.")
        else:
            print("I am reading, year, type")
            # calling ret_data method from db_manager class to fetch data from db.
            list1 = obj.ret_data(type, year)

            total_rows = len(list1)
            header = list(list1[0].keys())
            total_columns = len(list1[0])

            canvas = tk.Canvas(win)
            canvas.grid(row=0, column=1, sticky="nsew")

            # printing header
            for i in range(1,len(header)):
                self.e = Entry(canvas, fg='black', font=('Arial', 8,'bold'))
                self.e.grid(row=0, column=i-1)
                self.e.insert(END, header[i])
                self.e.config(state = 'readonly')

            # code for creating table
            for i in range(total_rows):
                for j in range(1, total_columns):
                    self.e = Entry(canvas, fg='black',font=('Arial', 8))
                    self.e.grid(row=i+1, column=j-1)
                    self.e.insert(END, list(list1[i].values())[j])
                    self.e.config(state = 'readonly')
                    
            # displays in the checkbox if data is loaded successfully
            text.insert(tk.END, "Data is loaded successfully.")

