from tkinter import *
from random import randrange
from tkinter import messagebox

root = Tk()

x_axis_size = 0
y_axis_size = 0
mine_count = 0
minefield_btn_list = []
minefield_mine_list = []
safe_count = 0

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
    global safe_count
    mine_frame.destroy()
    mine_frame = Frame(root)
    mine_frame.grid(row=1, column=0)
    start_btn['text'] = 'Restart'
    print(mine_count_entry.get())
    print(x_axis_entry.get() + 'x' + y_axis_entry.get())
    row_size = int(x_axis_entry.get())
    column_size = int(y_axis_entry.get())
    mine_count = int(mine_count_entry.get())
    safe_count = (row_size*column_size) - mine_count
    if (0 >= row_size > 20) or (0 >= column_size > 20) or (safe_count <= 0):
        print('Error')
        messagebox.showerror('Error!', 'Mine Count and Minefield Size Out of Range!')
    else:
        minefield_btn_list = []
        minefield_mine_list = []
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
        #Keep placing mines randomly until mine count reaches 0
        while mine_count > 0:
            rand_row = randrange(row_size)
            rand_column = randrange(column_size)
            if minefield_mine_list[rand_row][rand_column] == 1:
                print('Already a Mine')
            else:
                minefield_mine_list[rand_row][rand_column] = 1
                mine_count -= 1


def mine_check(mine_row, mine_column):
    global safe_count
    print(mine_row)
    print(mine_column)
    minefield_btn_list[mine_row][mine_column].config(relief=SUNKEN)
    #If current button is a mine then end game
    if minefield_mine_list[mine_row][mine_column] == 1:
        minefield_btn_list[mine_row][mine_column]['text'] = ':('
        minefield_btn_list[mine_row][mine_column]['bg'] = 'red'
        minefield_btn_list[mine_row][mine_column]['fg'] = 'white'
        messagebox.showerror('Game Over!', 'Stepped on a Mine :(')
    #Otherwise, check to see how many mines are nearby and change button text
    elif minefield_mine_list[mine_row][mine_column] == 0:
        minefield_mine_list[mine_row][mine_column] = 2
        safe_count -= 1
        if safe_count == 0:
            messagebox.showinfo('Winner!', 'All mines avoided!')
        nearby_mines = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if mine_row+i >= int(x_axis_entry.get()) or mine_row+i < 0 or mine_column+j >= int(y_axis_entry.get()) or mine_column+j < 0:
                    print('Ignore')
                elif minefield_mine_list[mine_row+i][mine_column+j] == 1:
                    nearby_mines += 1
        minefield_btn_list[mine_row][mine_column]['text'] = str(nearby_mines)
        minefield_btn_list[mine_row][mine_column]['bg'] = 'green'
        minefield_btn_list[mine_row][mine_column]['fg'] = 'white'

mainloop()