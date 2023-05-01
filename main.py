from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pymysql




class base:
    def __init__(self):
        print('base has started')

    def base(self):
        home=homepage()
        home.home()
class homepage(base):

    def home(self):
        global global_file
        global_file=False
        def new_file_fn():
            txt_area.delete('1.0',END)
            status_l.config(text="New file     ")
            win.title("Text editor - New file")
            global global_file
            global_file = False

        def open_file_fn():
            # txt_area.delete('1.0',END)
            open_file=filedialog.askopenfilename(title="Open File",filetypes=(("Text Files","*.txt"),("All files","*."),("Python files","*.py")))
            if open_file:
                global global_file
                global_file = open_file

            file=open_file # duplicating to make changes
            print(file)
            status_l.config(text=f'path : {file}     ')
            file=file.replace("/"," ")
            file=file.split() # to take the .txt file name
            file=file[-1] # slicing the file name

            # file=file.replace()
            win.title(f"Text editor - {file}")
            txt_area.delete('1.0',END)
            #saving file
            insert_file=open(open_file,'r')  #open file to read and insert in the text area
            r=insert_file.read()
            txt_area.insert(END,r)
            insert_file.close()


        def save():
            global global_file
            if global_file:
                text=txt_area.get('1.0',END)
                # saving file
                write = open(global_file, 'w')
                write.write(text)
                write.close()
            else:
                save_as()


        def save_as():
            def save_file(text):
                print(text)
                myfile=filedialog.asksaveasfilename(defaultextension='.txt',initialdir="C:\\Users\\vasanth rohith\\2023_python\\mini_projects\\text_editor\\sample_files",filetypes=(("Text Files","*.txt"),("All files","*."),("Python files","*.py")))
                print(myfile)

                if myfile:
                    write = open(myfile, 'w')
                    write.write(text)
                    write.close()

                    status_l.config(text=f"path : {myfile}     ")
                    myfile=myfile.replace("/"," ")
                    myfile=myfile.split()
                    myfile_1=myfile[-1]
                    win.title(f"Text editor - {myfile_1}")

            # after clicking save
            text=txt_area.get('1.0',END)
            text_li=[]
            text_li.append(text)
            # print(text)
            # print(text_li)

            empty=text_li[:2]
            if empty==['\n']:
                msg=messagebox.askyesno('Empty file','Your file is empty')
                # print(msg)
                if msg==True:
                    save_file(text)
            else:
                save_file(text)

        # Changing font size
        def font_size_12():
            def_font_size=12
            print(def_font_fam)
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_14():
            def_font_size=14
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_16():
            def_font_size=16
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_18():
            def_font_size=18
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_20():
            def_font_size=20
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_22():
            def_font_size=22
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_24():
            def_font_size=24
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_26():
            def_font_size=26
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_28():
            def_font_size=28
            txt_area.config(font=(f"{def_font_fam}", def_font_size))
        def font_size_30():
            print(def_font_fam)
            def_font_size=30
            txt_area.config(font=(f"{def_font_fam}", def_font_size))


        def Helvetica_fn():
            pass
        #     def_font_fam=
        #     'Helvetica'
        #     print(def_font_size)
        #     txt_area.config(font=(f"{def_font_fam}", def_font_size))
        # def Garamond_fn():
        #     def_font_fam='Garamond'
        #     txt_area.config(font=(f"{def_font_fam}", def_font_size))
        # def Futura_fn():
        #     def_font_fam='Futura'
        #     txt_area.config(font=(f"{def_font_fam}", def_font_size))
        # def Arial_fn():
        #     global def_font_fam
        #     def_font_fam='Arial'
        #     txt_area.config(font=(f"{def_font_fam}", def_font_size))
        # def Futura_fn():
        #     def_font_fam='Futura'
        #     txt_area.config(font=(f"{def_font_fam}", def_font_size))





        print("home")
        win=Tk()
        win.geometry('700x500')
        win.title('Text editor')

        frame0 = Frame(win)
        frame0.pack(ipadx=50, ipady=50, expand=True, fill='both')

        def_font_fam = 'Courier'    #Default ffamily
        def_font_size = 16      #Defaut fsize

        #Creating scroll bar and text area
        vert_bar = Scrollbar(frame0, orient=VERTICAL)
        vert_bar.pack(fill='both', side='right')
        txt_area = Text(frame0, font='14', yscrollcommand=vert_bar.set)
        txt_area.config(font=(f"{def_font_fam}", def_font_size))
        txt_area.pack(ipadx=50, ipady=50, expand=True, fill='both')

        #creating nav bar(Menu bar)
        base_menu=Menu(win)
        win.config(menu=base_menu)
        # Adding submenu options
        file_menu=Menu(base_menu,tearoff=0)
        # File
        base_menu.add_cascade(label='File',menu=file_menu)
        file_menu.add_command(label='New', command=new_file_fn)
        # file_menu.add_command(label='New File', command=new_file_fn)
        file_menu.add_command(label='open', command=open_file_fn)
        file_menu.add_command(label='Save', command=save)
        file_menu.add_command(label='Save as..',command=save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit',command=lambda:win.quit())

        # edit bar
        edit_menu = Menu(base_menu, tearoff=0)
        base_menu.add_cascade(label='Edit',menu=edit_menu)

        # edit - font size(creating cascade inside a cascade)
        font_size=Menu(edit_menu,tearoff=0)
        edit_menu.add_cascade(label='font size',menu=font_size)
        print(def_font_fam)
        font_size.add_command(label='12',command=font_size_12)
        font_size.add_command(label='14', command=font_size_14)
        font_size.add_command(label='16', command=font_size_16)
        font_size.add_command(label='18', command=font_size_18)
        font_size.add_command(label='20', command=font_size_20)
        font_size.add_command(label='22', command=font_size_22)
        font_size.add_command(label='24', command=font_size_24)
        font_size.add_command(label='26', command=font_size_26)
        font_size.add_command(label='28', command=font_size_28)
        font_size.add_command(label='30', command=font_size_30)

        # font family
        font_fam=Menu(edit_menu,tearoff=0)
        edit_menu.add_cascade(label='font family',menu=font_fam)
        font_fam.add_command(label='Helvetica')
        font_fam.add_command(label='Garamond',)
        font_fam.add_command(label='Futura',)
        font_fam.add_command(label='Arial',)

        foramt=Menu(base_menu,tearoff=0,borderwidth=5)
        base_menu.add_cascade(label='Format',menu=foramt)

        view=Menu(base_menu,tearoff=0)
        base_menu.add_cascade(label='View',menu=view)

        help=Menu(base_menu,tearoff=0)
        base_menu.add_cascade(label='Help',menu=help)


        status_l=Label(frame0,text='Ready    ')
        status_l.pack(ipady=5,side=BOTTOM,anchor='ne')



        win.mainloop()



obb=base()
obb.base()


