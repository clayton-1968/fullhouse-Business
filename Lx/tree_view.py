import datetime
import ttkthemes
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1020x600')
# root.wm_iconbitmap(r'/User/Shadrack/3D Objects')
root.wm_title('Awsome Treeview')
root.update()
style = ttkthemes.ThemedStyle(root)
# print(style.get_themes())
style.theme_use('clam')
style.configure('Treeview', font=('Verdana', 10), foreground='#2b2b2b', cellpadding=19)
style.configure('Treeview.Heading', font=('Verdana', 10, 'bold'), foreground='#444', background='silver')
style.map('Treeview', background=[('selected', 'darkgreen')], foreground=[('selected', 'orange')])

scrollbar = ttk.Scrollbar(root, orient='vertical')
scrollbar.pack(side='right', fill='y')

treeview = ttk.Treeview(root, columns=('ID', 'FNAME', 'SNAME', 'DEPARTAMENT', 'SALARY'), show='headings', selectmode='browse')
treeview.pack(side='left', fill='both', expand=1)


treeview.heading('#1', text='ID', anchor='center')
treeview.heading('#2', text='FNAME', anchor='center')
treeview.heading('#3', text='SNAME', anchor='center')
treeview.heading('#4', text='DEPARTAMENT', anchor='center')
treeview.heading('#5', text='SALARY', anchor='center')

treeview.column('#1', anchor='center')
treeview.column('#2', anchor='center')
treeview.column('#3', anchor='center')
treeview.column('#4', anchor='center')
treeview.column('#5', anchor='center')

treeview.tag_configure('odd', background='#eee')
treeview.tag_configure('even', background='#ddd')
treeview.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=treeview.yview)


def postPopUpMenu(event):
    row_id = treeview.identify_row(event.y)
    if row_id:  # Verifica se a linha existe
        treeview.selection_set(row_id)
        row_values = treeview.item(row_id)['values']
        # print(row_values)
        
        postPopUpMenu = tk.Menu(treeview, tearoff=0, font=('Verdana', 11))
        postPopUpMenu.add_command(label='Edit/Update', accelerator='Ctrl+E')
        postPopUpMenu.add_command(label='Delete', accelerator='Delete', command=lambda: treeview.delete(row_id))
        postPopUpMenu.add_command(label='View', accelerator='Ctrl+P')
        postPopUpMenu.add_separator()
        postPopUpMenu.add_command(label='Send Email', accelerator='Alt+L')
        postPopUpMenu.add_command(label='Remove from payroll', accelerator='Alt+Q')
        postPopUpMenu.post(event.x_root, event.y_root)


treeview.tag_bind('row', '<Button-3>', lambda event: postPopUpMenu(event))


# img = PhotoImage(file=r'C:\Users\Shadrack\Pictures\pics\emoji\135216.png')
for x in range(1, 101):
    if x % 2 == 0:
        treeview.insert('', 'end',
                        values=(x, 'Shiks' + str(x), 'Kapyenga' + str(x), 'Marketing & Sales', datetime.datetime.now()), tags=('event', 'row')
                        )
    else:
        treeview.insert('', 'end',
                        values=(x, 'Shiks' + str(x), 'Kapyenga' + str(x), 'Marketing & Sales', datetime.datetime.now()), tags=('odd', 'row')
                        )
root.mainloop()


