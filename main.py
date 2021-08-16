from tkinter import *
from random import randrange
from tkinter import messagebox

root = Tk()

x_axis_size = 0
y_axis_size = 0
mine_count = 0
minefield_btn_list = []
minefield_mine_list = []

setup_frame = Frame(root)
setup_frame.grid(row=0, column=0)

mine_frame = Frame(root)
mine_frame.grid(row=1, column=0)

Label(setup_frame, text='Minefield size').grid(row=0,column=1, pady= 5)
x_axis_entry = Entry(setup_frame, width=6)
x_axis_entry.grid(row=1, column=0, pady= 5)
Label(setup_frame, text='(1-20)').grid(row=2,column=0)
Label(setup_frame, text=' x ').grid(row=1, column=1, pady= 5)
y_axis_entry = Entry(setup_frame, width=6)
y_axis_entry.grid(row=1, column=2, pady= 5)
Label(setup_frame, text='(1-20)').grid(row=2,column=2)

Label(setup_frame, text= 'Mine Count').grid(row=3,column=1, pady=5)
mine_count_entry = Entry(setup_frame, width=6)
mine_count_entry.grid(row=4, column=1, pady= 5)
Label(setup_frame, text='(1-20)').grid(row=5,column=1)

start_btn = Button(setup_frame, text='Start', command=lambda:build_minefield())
start_btn.grid(row=6,column=1, pady=5)

#Build minefield buttons based on user entry in the status section
def build_minefield():
    global minefield_btn_list
    global minefield_mine_list
    global mine_count
    global mine_frame
    mine_frame.destroy()
    mine_frame = Frame(root)
    mine_frame.grid(row=1, column=0)
    start_btn['text'] = 'Restart'
    print(mine_count_entry.get())
    print(x_axis_entry.get() + 'x' + y_axis_entry.get())
    row_size = int(x_axis_entry.get())
    column_size = int(y_axis_entry.get())
    mine_count = int(mine_count_entry.get())
    if (0 >= row_size > 20) or (0 >= column_size > 20) or (0 >= mine_count > 20):
        print('Error')
        messagebox.showerror('Error!', 'Mine Count and Minefield Size Out of Range!')
    else:
        minefield_btn_list = []
        for i in range(column_size):
            temp_row_list = []
            temp_mine_list = []
            for j in range(row_size):
                mine_btn = Button(mine_frame, command=lambda m=i, n=j:mine_check(m,n), width=2)
                mine_btn.grid(row=i, column=j)
                temp_row_list.append(mine_btn)
                is_mine = 0
                temp_mine_list.append(is_mine)
            minefield_btn_list.append(temp_row_list)
            minefield_mine_list.append(temp_mine_list)
        while mine_count > 0:
            rand_row = randrange(row_size)
            rand_column = randrange(column_size)
            if minefield_mine_list[rand_row][rand_column] == 1:
                print('Already a Mine')
            else:
                minefield_mine_list[rand_row][rand_column] = 1
                mine_count -= 1


def mine_check(mine_row, mine_column):
    print(mine_row)
    print(mine_column)
    minefield_btn_list[mine_row][mine_column].config(relief=SUNKEN)  
    if minefield_mine_list[mine_row][mine_column] == 1:
        minefield_btn_list[mine_row][mine_column]['text'] = ':('
        minefield_btn_list[mine_row][mine_column]['bg'] = 'red'
        minefield_btn_list[mine_row][mine_column]['fg'] = 'white'
        messagebox.showerror('Game Over!', 'Stepped on a Mine :(')
    else:
        minefield_btn_list[mine_row][mine_column]['text'] = ':D'
        minefield_btn_list[mine_row][mine_column]['bg'] = 'green'
        minefield_btn_list[mine_row][mine_column]['fg'] = 'white'
    
mainloop()