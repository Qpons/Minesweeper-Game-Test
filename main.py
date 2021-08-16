from tkinter import *

root = Tk()

x_axis_size = 0
y_axis_size = 0
mine_count = 0
minefield_btn_list = []

top_frame = Frame(root)
top_frame.grid(row=0, column=0)

mine_frame = Frame(root)
mine_frame.grid(row=1, column=0)

Label(top_frame, text='Minefield size').grid(row=0,column=1, pady= 5)
x_axis_entry = Entry(top_frame, width=6)
x_axis_entry.grid(row=1, column=0, pady= 5)
Label(top_frame, text=' x ').grid(row=1, column=1, pady= 5)
y_axis_entry = Entry(top_frame, width=6)
y_axis_entry.grid(row=1, column=2, pady= 5)

Label(top_frame, text= 'Mine Count').grid(row=2,column=1, pady=5)
mine_count_entry = Entry(top_frame, width=6)
mine_count_entry.grid(row=3, column=1, pady= 5)

Button(top_frame, text='Start', command=lambda:build_minefield()).grid(row=4,column=1, pady=5)

def build_minefield():
    global minefield_btn_list
    global mine_count
    print(mine_count)
    print(x_axis_entry.get() + 'x' + y_axis_entry.get())
    row_size = int(x_axis_entry.get())
    column_size = int(y_axis_entry.get())
    mine_count = mine_count_entry.get()
    minefield_btn_list = []
    for i in range(column_size):
        temp_row_list = []
        for j in range(row_size):
            mine_btn = Button(mine_frame, width=2)
            mine_btn.grid(row=i, column=j)
            temp_row_list.append(mine_btn)
        minefield_btn_list.append(temp_row_list)

mainloop()