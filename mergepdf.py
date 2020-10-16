
import os, io
import sys
from tkinter import *
from tkinter.filedialog import *
import PyPDF2

class PDF_doc():

    def __init__(self, filename):
        self.filename = filename
        self.display = filename.split('/')[-1]
        self.pdf = load_pdf(filename)
        self.pages = self.pdf.getNumPages()
        self.start = 1
        self.end = self.pages

    def add_to_writer(self, writer):
        for i in range(self.start-1, self.end):
            writer.addPage(self.pdf.getPage(i))

def load_pdf(filename):
    f = open(filename, 'rb')
    return PyPdf2.PdfFileReader(f)

def load():
    f = askopenfilenames(filetypes=(('PDF', '*.pdf'), ('Todos los archivos','*.*')))
    pdf = PDF_doc(f)
    pdf_list.append(pdf)
    listbox.insert(END,pdf.display)
    print(pdf_list)


def remove():
    index= int(listbox.curselection()[0])
    pdf_list.pop(index)
    listbox.delete(ANCHOR)
    print(pdf_list)

def save_pdf():
    writer = PyPDF2.PdfFileWriter()

    output_filename = asksaveasfilename(filetypes=(('PDF', '*.pdf'), ('Todos los archivos','*.*')))
    output_file = open(output_filename, 'wb')

    for doc in pdf_list:
        doc.add_to_writer(writer)

    writer.write(output_file)
    output_file.close()
    root.quit()


def display(*args):
    index= int(listbox.curselection()[0])
    value = listbox.get(index)
    filename.set(value)
    pages.set(pdf_list(index).pages)
    start.set(pdf_list(index).start)
    end.set(pdf_list(index).end)

def set_start(*args):
    index= int(listbox.curselection()[0])
    pdf_list(index).start = int(start.get())

def set_end(*args):
    index= int(listbox.curselection()[0])
    pdf_list(index).end = int(end.get())

pdf_list = []

root = Tk()
root.title('UNIR PDF')

filename = StringVar()
pages = StringVar()
start = StringVar()
end = StringVar()

Label(root, text='ADMINISTRAR PDF').grid(row=0, column=0, columnspan=4)

Button(root,text='AÑADIR PDF', command=load).grid(row=2, column=0)
Button(root,text='QUITAR PDF', command=remove).grid(row=3, column=0)

listbox = Listbox(root)
listbox.bind('<<ListboxSelect>>', display)
listbox.grid(row=1, rowspan=4, column=1)

Label(root,text='ARCHIVO: ').grid(row=1, column=2)
Label(root,textvariable=filename, width=20).grid(row=1, column=3, sticky=(N, S, E, W))

Label(root,text='PÁGINAS: ').grid(row=2, column=2)
Label(root, textvariable=pages).grid(row=2, column=3)

Label(root,text='COMIENZO: ').grid(row=3, column=2)
s = Entry(root,textvariable=start, width=3)
s.grid(row=3, column=3)

Label(root, text='FINAL: ').grid(row=4, column=2)
e = Entry(root, textvariable=end,width=3)
e.grid(row=3, column=3)

Button(root, text='Guardar PDF como: ', command=save_pdf, width=10).grid(row=5, column=0, columnspan=4)

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)


start.trace('w', set_start)
end.trace('w', set_end)


root.mainloop()
