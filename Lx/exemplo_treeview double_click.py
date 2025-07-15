from imports import *

class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.tree = ttk.Treeview(self)
        # # self.tree.pack()
        self.bind('<Double-1>', self.on_double_click) 

    def on_double_click(self, event):
        # Identifica a região que ocorreu o duplo clique
        region_clicked = self.identify_region(event.x, event.y)
        # print(region_clicked)

        # Verifica se o clique foi em uma célula ou na árvore
        if region_clicked not in ('tree', 'cell'):
            return
        
        col_id = self.identify_column(event.x)
        # print(col_id)
        # por exemplo, '#0' retornando -1, '#1' retornando 0, '#2' retornando 1, etc.
        column_index = int(col_id[1:]) - 1

        lin_id = self.identify_row(event.y)
        # print(lin_id)
        
        # por exemplo:001
        selected_iid = self.focus() # O numero da linha tbem é o iid
        # print(selected_iid)

        # Contem os valores adicionados na linha
        selected_values = self.item(selected_iid)
        # print(selected_values)
        
        if col_id == '#0':
            selected_text = selected_values.get('text')
        else:
            selected_text = selected_values.get('values')[column_index]
        # print(selected_text)

        column_box = self.bbox(selected_iid, col_id)

        print(column_box)

        entry_edit = tk.Entry(root, width=column_box[2])

        # Registro da coluna index e item iid
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_iid = selected_iid

        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0, tk.END)

        entry_edit.focus_set()

        entry_edit.bind('<FocusOut>', self.on_focus_out)
        entry_edit.bind('<Return>', self.on_enter_pressed)


        entry_edit.place(x=column_box[0], 
                         y=column_box[1],
                         width=column_box[2],
                         height=column_box[3])
        
    def on_focus_out(self, event):
        event.widget.destroy()

    def on_enter_pressed(self, event):
        # Obtém o valor editado
        new_value = event.widget.get()
        
        selected_iid = event.widget.editing_item_iid


        column_index = event.widget.editing_column_index

        if column_index == -1:
            self.item(selected_iid, text=new_value)
        else:
            current_values = self.item(selected_iid).get('values')
            current_values[column_index] = new_value
            self.item(selected_iid, values=current_values)
            # print(current_values)

        event.widget.destroy()

if __name__ == '__main__':
    # Cria uma instância da classe Tkinter
    root = tk.Tk()
    
    # Cria uma instância da classe TreeView
    column_names = ('veiculo_nome', 'veiculo_ano', 'veiculo_cor')
    treeview_veiculos = TreeviewEdit(root, columns=column_names)
    treeview_veiculos.heading('#0', text='Tipo Veículo')
    treeview_veiculos.heading('veiculo_nome', text='Veículo Nome')
    treeview_veiculos.heading('veiculo_ano', text='Ano')
    treeview_veiculos.heading('veiculo_cor', text='Cor')
    sedan_row = treeview_veiculos.insert(parent='', 
                                        index='end', 
                                        text='Sedan')
    
    treeview_veiculos.insert(parent=sedan_row,
                                        index='end',
                                        text='',
                                        values=('Fusca', '1970', 'azul')) 

    treeview_veiculos.insert(parent=sedan_row,
                                        index='end',
                                        text='',
                                        values=('Civic', '2020', 'preto'))     


    # Exibe a árvore na tela
    treeview_veiculos.pack(fill=tk.BOTH, expand=True)
        
    # Inicia o loop principal do Tkinter
    root.mainloop()