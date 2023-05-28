import random
from pickle import dump, load
from os import listdir
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from webbrowser import open_new


class Friend:
    def __init__(self, full_name, phone, job='', city='', address='', email=''):
        self.full_name = full_name
        self.phone = phone
        self.job = job
        self.city = city
        self.address = address
        self.email = email

    def update_info(self, full_name, phone, job='', city='', address='', email=''):
        self.full_name = full_name
        self.phone = phone
        self.job = job
        self.city = city
        self.address = address
        self.email = email


class Friends:
    if 'data.drs' not in listdir():
        with open('data.drs', 'wb') as data:
            dump([], data)
    with open('data.drs', 'rb') as data:
        try:
            list_friends = load(data)
        except Exception:
            with open('data.drs', 'wb') as data:
                dump([], data)
            with open('data.drs', 'rb') as data:
                list_friends = load(data)

    @classmethod
    def add_friend(cls, friend):
        index = cls.search_friend(friend.full_name)
        if index == -1:
            cls.list_friends.append(friend)
            cls.update_list_friends()
        else:
            print('this name exist')

    @classmethod
    def delete_friend(cls, name):
        index = cls.search_friend(name)
        if index != -1:
            cls.list_friends.pop(index)
            cls.update_list_friends()
        else:
            print('this name not exsist')

    @classmethod
    def update_friend(cls, last_full_name, new_full_name, phone, job='', city='', address='', email=''):
        index = cls.search_friend(last_full_name)
        if index != -1:
            cls.list_friends[index].update_info(
                new_full_name, phone, job, city, address, email)
            cls.update_list_friends()
        else:
            print('this name not exsist')

    @classmethod
    def search_friend(cls, name):
        for i in range(len(cls.list_friends)):
            if cls.list_friends[i].full_name == name:
                return i
        else:
            return -1

    @classmethod
    def update_list_friends(cls):
        with open('data.drs', 'wb') as data:
            dump(cls.list_friends, data)

    @classmethod
    def get_data(cls):
        data = []
        for friend in cls.list_friends:
            data.append(friend)
        return data


def update_tree(mode=False, val=''):
    global nb_friends
    nb_friends = 0
    data = Friends.get_data()
    empty_tree()
    if mode == False or val == '':
        for friend in data:
            values = (friend.full_name,
                      friend.phone,
                      friend.job,
                      friend.city,
                      friend.address,
                      friend.email
                      )
            tree_frends.insert('', END, values=values)
            nb_friends += 1
    else:
        val = val.lower().rstrip().lstrip()
        if mode == 'full_name':
            for friend in data:
                if val in friend.full_name.lower():
                    values = (friend.full_name,
                              friend.phone,
                              friend.job,
                              friend.city,
                              friend.address,
                              friend.email
                              )
                    tree_frends.insert('', END, values=values)
                    nb_friends += 1
        elif mode == 'phone':
            for friend in data:
                if val in friend.phone.lower():
                    values = (friend.full_name,
                              friend.phone,
                              friend.job,
                              friend.city,
                              friend.address,
                              friend.email
                              )
                    tree_frends.insert('', END, values=values)
                    nb_friends += 1
        elif mode == 'job':
            for friend in data:
                if val in friend.job.lower():
                    values = (friend.full_name,
                              friend.phone,
                              friend.job,
                              friend.city,
                              friend.address,
                              friend.email
                              )
                    tree_frends.insert('', END, values=values)
                    nb_friends += 1
        elif mode == 'city':
            for friend in data:
                if val in friend.city.lower():
                    values = (friend.full_name,
                              friend.phone,
                              friend.job,
                              friend.city,
                              friend.address,
                              friend.email
                              )
                    tree_frends.insert('', END, values=values)
                    nb_friends += 1
        elif mode == 'address':
            for friend in data:
                if val in friend.address.lower():
                    values = (friend.full_name,
                              friend.phone,
                              friend.job,
                              friend.city,
                              friend.address,
                              friend.email
                              )
                    tree_frends.insert('', END, values=values)
                    nb_friends += 1
        elif mode == 'email':
            for friend in data:
                if val in friend.email.lower():
                    values = (friend.full_name,
                              friend.phone,
                              friend.job,
                              friend.city,
                              friend.address,
                              friend.email
                              )
                    tree_frends.insert('', END, values=values)
                    nb_friends += 1


def show_window_add_friend():
    main_window.place_forget()

    window_add_friend = Frame(app)
    window_add_friend.place(width=650, height=500)

    Label(window_add_friend, text='Add Friend', font=(
        'arial rounded mt bold', 30, 'bold'), borderwidth=5, relief="solid", ).place(x=0, y=0, width=650, height=100)
    font_label = ('cascadia code semiBold', 20, 'bold')
    Label(window_add_friend, text='Full name : ', anchor='w',
          font=font_label).place(x=20, y=115, width=180, height=45)
    Label(window_add_friend, text='Phone     : ', anchor='w',
          font=font_label).place(x=20, y=165, width=180, height=45)
    Label(window_add_friend, text='Job       : ', anchor='w',
          font=font_label).place(x=20, y=215, width=180, height=45)
    Label(window_add_friend, text='City      : ', anchor='w',
          font=font_label).place(x=20, y=265, width=180, height=45)
    Label(window_add_friend, text='Address   : ', anchor='w',
          font=font_label).place(x=20, y=315, width=180, height=45)
    Label(window_add_friend, text='Email     : ', anchor='w',
          font=font_label).place(x=20, y=365, width=180, height=45)

    var_name = StringVar()
    var_phone = StringVar()
    var_job = StringVar()
    var_city = StringVar()
    var_address = StringVar()
    var_email = StringVar()
    font_entry = ('Cascadia code', 18)
    entry_name = Entry(window_add_friend,
                       textvariable=var_name, font=font_entry)
    entry_phone = Entry(
        window_add_friend, textvariable=var_phone, font=font_entry)
    entry_job = Entry(window_add_friend, textvariable=var_job, font=font_entry)
    entry_city = Entry(window_add_friend,
                       textvariable=var_city, font=font_entry)
    entry_address = Entry(
        window_add_friend, textvariable=var_address, font=font_entry)
    entry_email = Entry(window_add_friend,
                        textvariable=var_email, font=font_entry)
    entry_name.place(x=210, y=115, width=420, height=45)
    entry_phone.place(x=210, y=165, width=420, height=45)
    entry_job.place(x=210, y=215, width=420, height=45)
    entry_city.place(x=210, y=265, width=420, height=45)
    entry_address.place(x=210, y=315, width=420, height=45)
    entry_email.place(x=210, y=365, width=420, height=45)
    Button(window_add_friend, text='Save Friend', relief=GROOVE, font=(
        'segoe ui black', 25, 'bold'), bg='#1b611b', fg='#fff', activebackground='#fff', activeforeground='#1b611b',  command=lambda: add_friend(window_add_friend, var_name, var_phone, var_job, var_city, var_address, var_email)).place(x=0, y=430, height=70, width=450)
    Button(window_add_friend, text='R', font=('segoe ui black', 25, 'bold'), relief=GROOVE, bg='#be7b00', fg='#fff', activebackground='#fff', activeforeground='#be7b00', command=lambda: empty_entry_add_friend(var_name, var_phone, var_job, var_city, var_address, var_email)).place(
        x=450, y=430, height=70, width=100)
    Button(window_add_friend, text='X', font=('segoe ui black', 25, 'bold'), relief=GROOVE, bg='#9d0000', fg='#fff', activebackground='#fff', activeforeground='#9d0000', command=lambda: (window_add_friend.place_forget(), main_window.place(width=650, height=500))).place(
        x=550, y=430, height=70, width=100)


def add_friend(window, var_name, var_phone, var_job, var_city, var_address, var_email):
    if var_name.get().strip() == '':
        messagebox.showwarning('Warning', 'Please enter a valid Name')
    elif not var_phone.get().isnumeric():
        messagebox.showwarning('Warning', 'Please enter a valid Phone')
    else:
        index = Friends.search_friend(var_name.get().strip())
        if index == -1:
            full_name = check_entry(var_name.get().strip())
            phone = check_entry(var_phone.get().strip())
            job = check_entry(var_job.get().strip())
            city = check_entry(var_city.get().strip())
            address = check_entry(var_address.get().strip())
            email = check_entry(var_email.get().strip())
            Friends.add_friend(
                Friend(full_name, phone, job, city, address, email))
            window.place_forget()
            main_window.place(width=650, height=500)
            update_tree()
        else:
            messagebox.showwarning('Warning', 'This name already exists')


def check_entry(val):
    if val != '':
        return val
    else:
        return "Null"


def empty_entry_add_friend(var_name, var_phone, var_job, var_city, var_address, var_email):
    var_name.set('')
    var_phone.set('')
    var_job.set('')
    var_city.set('')
    var_address.set('')
    var_email.set('')


def empty_tree():
    for friend in tree_frends.get_children():
        tree_frends.delete(friend)


def try_update_friend():
    try:
        name = tree_frends.item(tree_frends.focus())['values'][0]
    except:
        return messagebox.showwarning('Warning', 'Please select friend')
    index = Friends.search_friend(name)
    show_window_update_friend(Friends.list_friends[index])


def show_window_update_friend(friend):
    main_window.place_forget()

    window_update_friend = Frame(app)
    window_update_friend.place(width=650, height=500)

    Label(window_update_friend, text='Update Friend', font=(
        'arial rounded mt bold', 30, 'bold'), borderwidth=5, relief="solid", ).place(x=0, y=0, width=650, height=100)
    font_label = ('cascadia code semiBold', 20, 'bold')
    Label(window_update_friend, text='Full name : ', anchor='w',
          font=font_label).place(x=20, y=115, width=180, height=45)
    Label(window_update_friend, text='Phone     : ', anchor='w',
          font=font_label).place(x=20, y=165, width=180, height=45)
    Label(window_update_friend, text='Job       : ', anchor='w',
          font=font_label).place(x=20, y=215, width=180, height=45)
    Label(window_update_friend, text='City      : ', anchor='w',
          font=font_label).place(x=20, y=265, width=180, height=45)
    Label(window_update_friend, text='Address   : ', anchor='w',
          font=font_label).place(x=20, y=315, width=180, height=45)
    Label(window_update_friend, text='Email     : ', anchor='w',
          font=font_label).place(x=20, y=365, width=180, height=45)

    var_name = StringVar()
    var_phone = StringVar()
    var_job = StringVar()
    var_city = StringVar()
    var_address = StringVar()
    var_email = StringVar()
    var_name.set(check_null(friend.full_name))
    var_phone.set(check_null(friend.phone))
    var_job.set(check_null(friend.job))
    var_city.set(check_null(friend.city))
    var_address.set(check_null(friend.address))
    var_email.set(check_null(friend.email))
    font_entry = ('Cascadia code', 18)
    entry_name = Entry(window_update_friend,
                       textvariable=var_name, font=font_entry)
    entry_phone = Entry(
        window_update_friend, textvariable=var_phone, font=font_entry)
    entry_job = Entry(window_update_friend,
                      textvariable=var_job, font=font_entry)
    entry_city = Entry(window_update_friend,
                       textvariable=var_city, font=font_entry)
    entry_address = Entry(
        window_update_friend, textvariable=var_address, font=font_entry)
    entry_email = Entry(window_update_friend,
                        textvariable=var_email, font=font_entry)
    entry_name.place(x=210, y=115, width=420, height=45)
    entry_phone.place(x=210, y=165, width=420, height=45)
    entry_job.place(x=210, y=215, width=420, height=45)
    entry_city.place(x=210, y=265, width=420, height=45)
    entry_address.place(x=210, y=315, width=420, height=45)
    entry_email.place(x=210, y=365, width=420, height=45)
    Button(window_update_friend, text='Save Change', relief=GROOVE, font=(
        'segoe ui black', 25, 'bold'), bg='#1b611b', fg='#fff', activebackground='#fff', activeforeground='#1b611b',  command=lambda: update_friend(window_update_friend, var_name, var_phone, var_job, var_city, var_address, var_email, friend)).place(x=0, y=430, height=70, width=450)
    Button(window_update_friend, text='R', font=('segoe ui black', 25, 'bold'), relief=GROOVE, bg='#be7b00', fg='#fff', activebackground='#fff', activeforeground='#be7b00', command=lambda: reset_entry_update_friend(var_name, var_phone, var_job, var_city, var_address, var_email, friend)).place(
        x=450, y=430, height=70, width=100)
    Button(window_update_friend, text='X', font=('segoe ui black', 25, 'bold'), relief=GROOVE, bg='#9d0000', fg='#fff', activebackground='#fff', activeforeground='#9d0000', command=lambda: (window_update_friend.place_forget(), main_window.place(width=650, height=500))).place(
        x=550, y=430, height=70, width=100)


def show_window_more():
    main_window.place_forget()

    window_more = Frame(app)
    window_more.place(width=650, height=500)
    Label(window_more, text='About Friends', font=('cascadia mono semibold',
          50, 'bold'), bg='#c1c1c1').place(x=0, y=0, width=650, height=100)
    Label(window_more, text=f'Number friends : {nb_friends} friends', font=(
        'cascadia mono', 18, 'bold')).place(x=30, y=120)
    Label(window_more, text="""This application enables you to save, delete or modify the 
information of your friends,and you can also search in the 
list of friends by name, phone number, profession, city,
or email,this is to facilitate the search.
""", font=('cascadia mono', 13, 'italic')).place(x=0, y=180, width=650)
    Label(window_more, text='Connect with us : ',
          font=('locida fax', 20)).place(x=30, y=300)
    Label(window_more, text='Facebook : ', font=(
        'cascadia mono semibold', 16)).place(x=30, y=350)
    Label(window_more, text='linkedin : ', font=(
        'cascadia mono semibold', 16)).place(x=30, y=385)
    Label(window_more, text='Instagram : ', font=(
        'cascadia mono semibold', 16)).place(x=360, y=350)
    Label(window_more, text='Github    : ', font=(
        'cascadia mono semibold', 16)).place(x=360, y=385)

    fb = Label(window_more, text='Driss Raiss',
               font=('cascadia mono semibold', 16), fg='#5596ff', cursor='hand2')
    linkedin = Label(window_more, text='DRISS RAISS',
                     font=('cascadia mono semibold', 16), fg='#5596ff', cursor='hand2')
    insta = Label(window_more, text='drissrays',
                  font=('cascadia mono semibold', 16), fg='#5596ff', cursor='hand2')
    github = Label(window_more, text='Driss25',
                   font=('cascadia mono semibold', 16), fg='#5596ff', cursor='hand2')
    fb.place(x=160, y=350)
    linkedin.place(x=160, y=385)
    insta.place(x=500, y=350)
    github.place(x=500, y=385)

    fb.bind("<Button-1>",
            lambda e: callback("https://www.facebook.com/mohamad.zaze.12"))
    linkedin.bind(
        "<Button-1>", lambda e: callback("https://www.linkedin.com/in/drissraiss/"))
    insta.bind(
        "<Button-1>", lambda e: callback("https://www.instagram.com/drissraiss_/"))
    github.bind(
        "<Button-1>", lambda e: callback("https://github.com/drissraiss"))

    Button(window_more, text='X', font=('segoe ui black', 25, 'bold'), relief=GROOVE, bg='#9d0000', fg='#fff', activebackground='#fff', activeforeground='#9d0000', command=lambda: (window_more.place_forget(), main_window.place(width=650, height=500))).place(
        x=0, y=430, height=70, width=650)


def callback(url):
    open_new(url)


def update_friend(window, var_name, var_phone, var_job, var_city, var_address, var_email, friend):
    if var_name.get().strip() == '':
        messagebox.showwarning('Warning', 'Please enter a valid Name')
    elif not var_phone.get().isnumeric():
        messagebox.showwarning('Warning', 'Please enter a valid Phone')
    elif friend.full_name != var_name.get() and Friends.search_friend(var_name.get()) != -1:
        messagebox.showwarning('Warning', 'This name already exists')
    else:
        full_name = check_entry(var_name.get().strip())
        phone = check_entry(var_phone.get().strip())
        job = check_entry(var_job.get().strip())
        city = check_entry(var_city.get().strip())
        address = check_entry(var_address.get().strip())
        email = check_entry(var_email.get().strip())
        Friends.update_friend(friend.full_name, full_name,
                              phone, job, city, address, email)
        window.place_forget()
        main_window.place(width=650, height=500)
        update_tree()


def reset_entry_update_friend(var_name, var_phone, var_job, var_city, var_address, var_email, friend):
    var_name.set(check_null(friend.full_name))
    var_job.set(check_null(friend.job))
    var_city.set(check_null(friend.city))
    var_phone.set(check_null(friend.phone))
    var_address.set(check_null(friend.address))
    var_email.set(check_null(friend.email))


def check_null(val):
    if val != 'Null':
        return val
    else:
        return ''


def delete_friend():
    try:
        name = tree_frends.item(tree_frends.focus())['values'][0]
    except:
        return messagebox.showwarning('Warning', 'Please select friend')
    Friends.delete_friend(name)
    update_tree()


def filter_tree():
    dict_mode = {1: 'full_name', 2: 'phone',
                 3: 'job', 4: 'city', 5: 'address', 6: 'email'}
    update_tree(mode=dict_mode[v.get()], val=var_search.get())


nb_friends = 0
if __name__ == '__main__':
    app = Tk()
    app.title('Friends')
    app.geometry('650x500+480+200')
    app.resizable(0, 0)
    try:
        photo = PhotoImage(file="a.ico")
        app.iconphoto(False, photo)
    except TclError as error:
        print("Error = ", error)
    main_window = Frame(app)
    main_window.place(width=650, height=500)
    var_search = StringVar()
    entry_search = Entry(main_window, textvariable=var_search,
                         font=('ariel', 25), bg='#fff', fg='#00f')
    entry_search.place(x=0, y=0, height=50, width=300)
    Button(main_window, text='Filter', font=('ariel', 25, 'bold'), fg='#1c7c24', bg='#ebc480', relief=GROOVE,
           cursor='hand2', command=filter_tree).place(x=530, height=50, width=120)
    v = IntVar()
    font_radio_button = ('Gabriola', 16)
    Radiobutton(main_window, text='Name', variable=v, value=1, background='#d8d8d8',
                font=font_radio_button, cursor='dotbox', anchor='w').place(x=300, y=0, height=25, width=75)
    Radiobutton(main_window, text='Phone', variable=v, value=2, background='#d8d8d8',
                font=font_radio_button, cursor='dotbox', anchor='w').place(x=373, y=0, height=25, width=82)
    Radiobutton(main_window, text='Job', variable=v, value=3, background='#d8d8d8',
                font=font_radio_button, cursor='dotbox', anchor='w').place(x=455, y=0, height=25, width=75)
    Radiobutton(main_window, text='City', variable=v, value=4, background='#d8d8d8',
                font=font_radio_button, cursor='dotbox', anchor='w').place(x=300, y=25, height=25, width=75)
    Radiobutton(main_window, text='Address', variable=v, value=5, background='#d8d8d8',
                font=font_radio_button, cursor='dotbox', anchor='w').place(x=373, y=25,  height=25, width=82)
    Radiobutton(main_window, text='Email', variable=v, value=6, background='#d8d8d8',
                font=font_radio_button, cursor='dotbox', anchor='w').place(x=455, y=25, height=25, width=75)

    v.set(1)

    columns = ('full_name', 'phone', 'job', 'city', 'address', 'email')
    tree_frends = ttk.Treeview(main_window, columns=columns, show='headings')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Gadugi', 14, 'bold'))
    tree_frends.heading('full_name', text='Full name', anchor='w')
    tree_frends.heading('phone', text='Phone', anchor='w')
    tree_frends.heading('job', text='Job', anchor='w')
    tree_frends.heading('city', text='City', anchor='w')
    tree_frends.heading('address', text='Address', anchor='w')
    tree_frends.heading('email', text='Email', anchor='w')

    tree_frends.column('full_name', width=50)
    tree_frends.column('phone', width=5)
    tree_frends.column('job', width=5)
    tree_frends.column('city', width=5)
    tree_frends.column('address', width=50)
    tree_frends.column('email', width=90)
    tree_frends.place(x=0, y=50, width=650, height=400)

    update_tree()

    Button(main_window, text='Add', font=(None, 20, 'bold'), command=show_window_add_friend, relief=FLAT, cursor='cross', bg='#5cb85c', fg='#fff',
           activeforeground='#5cb85c', activebackground='#fff').place(x=0, y=450, height=50, width=162.5)
    Button(main_window, text='Update', font=(None, 20, 'bold'), command=try_update_friend, relief=FLAT, cursor='exchange', bg='#f0ad4e', fg='#fff',
           activeforeground='#f0ad4e', activebackground='#fff').place(x=162.5, y=450, height=50, width=162.5)
    Button(main_window, text='Delete', font=(None, 20, 'bold'), command=delete_friend, relief=FLAT, cursor='pirate', bg='#d9534f', fg='#fff',
           activeforeground='#d9534f', activebackground='#fff').place(x=325, y=450, height=50, width=162.5)
    Button(main_window, text='More', font=(None, 20, 'bold'), command=show_window_more, relief=FLAT, cursor='circle', bg='#0275d8', fg='#fff',
           activeforeground='#0275d8', activebackground='#fff').place(x=487.5, y=450, height=50, width=162.5)

    main_window.mainloop()
