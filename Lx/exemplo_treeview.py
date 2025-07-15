from imports import *


root = tk.Tk()

# PNG image path
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, 'icon', 'azul.png')
icon_image = None
# Carregar a imagem
if os.path.exists(icon_path):
    img_canada_flag = PhotoImage(file=icon_path)

# Define columns
column_names = ("country_column", "capital_city_column")

# Pass the column names when we make the treeview.
treeview_country = ttk.Treeview(columns=column_names)

# Create the column texts that the user will see.
treeview_country.heading("country_column", text="Country")
treeview_country.heading("capital_city_column", text="Capital")

treeview_country.insert(parent="",
                     index="end",
                     image=img_canada_flag,
                     values=("Canada", "Ottawa"))

treeview_country.pack(expand=True, fill=tk.BOTH)

root.mainloop()