from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Codemy.com - TreeBase')
#root.iconbitmap('somefile')
root.geometry("1000x500")

# add some style
style = ttk.Style()

# pick a theme
style.theme_use('default')

# configure the treeview colors
style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

# change selected color
style.map('Treeview',
    background=[('selected',"#347083")])

# create a treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# create the treeview scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# create the treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# define our columns
my_tree['columns']=("First Name", "Last Name", "ID", "Address", "City", "State", "Zipcode")

# format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)

# create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)


# add fake data
data = [
    ["Joker", "Black", 1, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Jabi", "Bida", 2, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Silence", "Please", 3, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Titu Bui", "Abunda", 4, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Lolo", "Magaling", 5, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Malakas", "Jalibi", 6, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Nguso", "Jalibi", 7, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Princesa", "Matalino", 8, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Sipuning", "Negro", 9, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Jokey", "Goodslang", 10, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Fat", "Bastard", 11, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Malebolgia", "Clown", 12, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Princess", "Leah", 13, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Han", "Solo", 14, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Chew", "Backa", 15, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Mandalorian", "Yoda", 16, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Omega", "Legend", 17, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Bruce", "Wilkins", 18, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Leonardo", "Michaelangelo", 19, "123 Elm St.", "Las Vegas", "California", "12345" ],
    ["Damon", "Hunter", 20, "123 Elm St.", "Las Vegas", "California", "12345" ],
]


# create striped row tags
my_tree.tag_configure('oddrow', background = 'white')
my_tree.tag_configure('evenrow', background = 'lightblue')

# add record entry box
global count
count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6] ), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6] ), tags=('oddrow',))

    count += 1

# add record entry box
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

ID_label = Label(data_frame, text="ID")
ID_label.grid(row=0, column=4, padx=10, pady=10)
ID_entry = Entry(data_frame)
ID_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1, column=0, padx=5, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=5, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=5, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=5, pady=10)

state_label = Label(data_frame, text="State")
state_label.grid(row=1, column=4, padx=5, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=5, pady=10)

zipcode_label = Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1, column=6, padx=5, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=5, pady=10)

# add buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record")
update_button.grid(row=0, column=0, padx=0, pady=0 )

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=0, pady=0 )

remove_all_button = Button(button_frame, text="Remove All Record")
remove_all_button.grid(row=0, column=2, padx=0, pady=0 )

remove_one_button = Button(button_frame, text="Remove One Record")
remove_one_button.grid(row=0, column=3, padx=0, pady=0 )

remove_many_button = Button(button_frame, text="Remove Many Record")
remove_many_button.grid(row=0, column=4, padx=0, pady=0 )

move_up_button = Button(button_frame, text="Move UP")
move_up_button.grid(row=0, column=5, padx=0, pady=0 )

move_down_button = Button(button_frame, text="Move Down")
move_down_button.grid(row=0, column=6, padx=0, pady=0 )

select_button = Button(button_frame, text="Select Record")
select_button.grid(row=0, column=7, padx=0, pady=0 )



root.mainloop()