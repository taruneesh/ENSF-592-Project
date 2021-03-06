'''
@author(s) Neha Singh, Sanyam, Taruneesh Sachdeva

This .py file has a class sort_data and uses the db_manager_new class.
'''

from tkinter import *
import tkinter as tk
from db_manager_new import DbManagerNew


class sort_data():
    '''
    class sort_data displays the sorted in the GUI based on year and type selected by the user.
    '''
    def sort(self, win,text, year, type, obj):
        text.delete('1.0', tk.END)
        if((year == 0) or (type == "")):
            text.insert(tk.END, "Please select valid type and year.")
        else:
            # calling sort_data method from db_manager class
            list1 = obj.sort_data(type, year)

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

            #displays in the checkbox if data is sorted successfully
            text.insert(tk.END, "Data is sorted successfully.")

