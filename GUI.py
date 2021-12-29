import tkinter as tk
from tkinter import Canvas, Entry, Event, ttk , Button
from tkinter.constants import LEFT, NSEW
from pandas.core.window.rolling import Window
import tkintertable as tktable
from tkintertable import TableCanvas , TableModel


#dummy data
import numpy as np
db = np.zeros((10,5))

#tkinter screen
root = tk.Tk()
root.title("Accounting Books")
root.geometry("800x450")

#spreadsheet tree
tree  = ttk.Treeview(root , columns= ("S#" , "Name" , "Rate" , "Qty" , "Total") , show="headings")

tree.heading("S#" , text="S#")
tree.heading("Name" , text="Name")
tree.heading("Rate" , text="Rate")
tree.heading("Qty" , text="Qty")
tree.heading("Total" , text="Total")

#dummy data
for i in range(1,10):
    tree.insert('',tk.END,values=db[i])

tree.grid(row= 10 , column= 5 ,sticky=NSEW)

#will explain
#list to store column value
shape1 = list()
#tracks both col , row on mouse click
def tree_click_handler(event):
    try:
        shape1.pop(0)
        
    except: pass
    cur_item = tree.item(tree.focus())
    col = tree.identify_column(event.x)[1:]
    rowid = tree.identify_row(event.y)[1:]
    #updates list
    shape1.append(col)
    x,y,w,h = tree.bbox('I'+rowid,'#'+col)
    
    tree.tag_configure("highlight", background="yellow")
    
    return(col)
    
#code linked to event    
tree.bind('<ButtonRelease-1>', tree_click_handler)




def delete_row():
    try:
        selected_item = tree.selection()[0]
        tree.delete(selected_item)
    except: pass



def delete_value():
    try:
        selected_item = tree.selection()[0]
        temp = list(tree.item(selected_item , 'values'))
        tree_click_handler
        col_selected = int(shape1[0])-1
        temp[col_selected]= ''
        shape1.pop(0)
        tree.item(selected_item, values= temp)
    except: pass

#edit a value in a clicked cell
def edit(event):
    try:
        selected_item = tree.selection()[0]
        temp = list(tree.item(selected_item , 'values'))
        tree_click_handler
        col_selected = int(shape1[0])-1
        temp[col_selected]= input('Enter value:' )
        shape1.pop(0)
        tree.item(selected_item, values= temp)
    except: pass
#binding allows to edit on screen double click
tree.bind('<Double-Button-1>' , edit)

style = ttk.Style()
# this is set background and foreground of the treeview
style.configure("Treeview",
                background="none",
                foreground="black",
                fieldbackground="green")

# set backgound and foreground color when selected
style.map('Treeview', background=[('selected', 'green')], foreground = [('focus','blue')])
tree.pack(pady=100)

#to call an event that rewuires handler via button also enter handler like tree_click_handler("<Escape>")
button_del = Button(root, text="Delete Row", command=delete_row)
button_del.pack()

button_del_cell = Button(root, text="Delete Cell", command=delete_value)
button_del_cell.pack()


root.mainloop()