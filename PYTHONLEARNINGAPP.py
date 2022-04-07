from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import pyttsx3

engine = pyttsx3.init()

def compilerInstructions1():
    root = Tk()
    root.geometry('1000x1000')
    root.title('Compiler - instrukcja obslugi')
    intro = Label(root, text='Compiler')
    intro.config(font=('Courier', 27))
    intro.pack()

    image = ImageTk.PhotoImage(Image.open('code1.png'))
    i1 = Label(image=image)
    i1.pack()

    dtText = Label(root, text='Compiler to swojego rodzaju notatnik do wykonywania kodu')
    dtText.config(font=('Courier', 15))
    dtText.pack()

    dtText1 = Label(root, text='Na ilustracji mozna zobaczyc compiler z prostym kodem wyswietlajacym zmienna a')
    dtText1.config(font=('Courier', 15))
    dtText1.pack()

    Button(root,width=50, height=40,  text='Dalej', command=root.destroy).pack()
    root.mainloop()

def compilerInstructions2():
    root = Tk()
    root.geometry('1000x1000')
    root.title('Compiler - Zapis Pliku 1')
    intro = Label(root, text='Zapis pliku 1')
    intro.config(font=('Courier', 27))
    intro.pack()

    image = ImageTk.PhotoImage(Image.open('filemenu.png'))
    i1 = Label(image=image)
    i1.pack()

    dtText = Label(root, text='By skompilowac kod trzeba go najpierw zapisac')
    dtText.config(font=('Courier', 15))
    dtText.pack()

    dtText1 = Label(root, text='')
    dtText1.config(font=('Courier', 15))
    dtText1.pack()

    Button(root,width=50, height=40,  text='Dalej', command=root.destroy).pack()
    root.mainloop()

def compilerInstructions3():
    root = Tk()
    root.geometry('1000x1000')
    root.title('Compiler - instrukcja obslugi')
    intro = Label(root, text='Compiler')
    intro.config(font=('Courier', 27))
    intro.pack()

    image = ImageTk.PhotoImage(Image.open('codesaving.png'))
    i1 = Label(image=image)
    i1.pack()

    dtText = Label(root, text='Koniecznie zapisz plik z rozszerzeniem .py ! Bez tego kod nie zadziala')
    dtText.config(font=('Courier', 15))
    dtText.pack()

    dtText1 = Label(root, text='Aby to zrobic na koncu nazwy pod jaka chcesz zapisac plik dodaj .py jak na obrazku')
    dtText1.config(font=('Courier', 15))
    dtText1.pack()

    Button(root,width=50, height=40,  text='Dalej', command=root.destroy).pack()
    root.mainloop()

def compilerInstructions4():
    root = Tk()
    root.geometry('1000x1000')
    root.title('Compiler - instrukcja obslugi')
    intro = Label(root, text='Compiler')
    intro.config(font=('Courier', 27))
    intro.pack()

    image = ImageTk.PhotoImage(Image.open('precompile.png'))
    i1 = Label(image=image)
    i1.pack()

    dtText = Label(root, text='Aby uruchomic program wcisnij przycisk RUN z menu')
    dtText.config(font=('Courier', 15))
    dtText.pack()

    Button(root,width=50, height=40,  text='Dalej', command=root.destroy).pack()
    root.mainloop()

def compilerInstructions6():
    root = Tk()
    root.geometry('1000x1000')
    root.title('Compiler - instrukcja obslugi')
    intro = Label(root, text='Compiler')
    intro.config(font=('Courier', 27))
    intro.pack()
    dtText = Label(root, text='Wyprobuj samemu!')
    dtText.config(font=('Courier', 15))
    dtText.pack()
    b2 = Button(root,width=50, height=40,  text='Dalej', command=root.destroy)
    b2.pack()
    root.mainloop()

def firstWindow():

    root = Tk()
    root.geometry('800x800')
    root.title('Python learning program')
    intro = Label(root, text='Witaj w programie do nauki Pythona!')
    intro.config(font=('Courier', 27))
    intro.pack()
    image = ImageTk.PhotoImage(Image.open('pythonlogo.png'))
    i1 = Label(image=image)
    i1.pack()
    Button(root,width=50, height=40,  text='Dalej', command=root.destroy).pack()
    root.mainloop()

def secondWindow():
    root = Tk()
    root.geometry('1000x700')
    root.title('Lekcja 1 - Co to zmienna?')
    intro = Label(root, text='Zmienna')
    intro.config(font=('Courier', 27))
    intro.pack()

    image = ImageTk.PhotoImage(Image.open('exampleVariable.png'))
    i1 = Label(image=image)
    i1.pack()

    dtText = Label(root, text='Jest to pojemnik na dane. Mozemy wrzucic do niego liczbe, tekst lub jakas operacje')
    dtText.config(font=('Courier', 15))
    dtText.pack()

    dtText1 = Label(root, text='Na ilustracji mozna zobaczyc przyklady zmiennych z roznymi zawartosciami')
    dtText1.config(font=('Courier', 15))
    dtText1.pack()

    Button(root,width=50, height=40,  text='Dalej', command=root.destroy).pack()

    root.mainloop()


def thirdWindow():
    root = Tk()
    root.geometry('1000x700')
    root.title('Lekcja 2 - Typy danych')
    intro = Label(root, text='Typy danych')
    intro.config(font=('Courier', 27))
    intro.pack()
    image = ImageTk.PhotoImage(Image.open('examplecode1.png'))
    i1 = Label(image=image)
    i1.pack()

    dtText = Label(root, text='Pierwszym typem danych jest liczba calkowita - z j.ang Integer')
    dtText.config(font=('Courier', 15))
    dtText.pack()

    dtText1 = Label(root, text='Ten typ danych jest na ilustracji pod literka a')
    dtText1.config(font=('Courier', 15))
    dtText1.pack()

    Button(root,width=50, height=40,  text='Dalej', command=root.destroy).pack()

    root.mainloop()


firstWindow()
secondWindow()
thirdWindow()
compilerInstructions1()
compilerInstructions2()
compilerInstructions3()
compilerInstructions4()
compilerInstructions6()

compiler = Tk()
compiler.title('My Fantastic IDE')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=compiler.destroy)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()

