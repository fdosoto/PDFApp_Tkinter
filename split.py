import tkinter as tk
from PyPDF2 import PdfFileWriter, PdfFileReader
import glob
import os
from tkinter import messagebox


def split(file):
    inputpdf = PdfFileReader(file, "rb")
    print(inputpdf)
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("output/document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
    lb.delete(0, tk.END)
    print(glob.glob("*.pdf"))
    refreshlist(lb2)


def refreshlist(lst):
    if lst == lb:
        folder = "input"
    elif lst == lb2:
        folder = "output"
        lst.delete(0, tk.END)
    for file in glob.glob(folder + "/*.pdf"):
        lst.insert(tk.END, file)

root = tk.Tk()
root.geometry("400x400")
root["bg"] = "green"
lb = tk.Listbox(root)
lb.pack(side="left", fill=tk.BOTH, expand=1)
refreshlist(lb)
lb.bind("<Double-Button>", lambda x: split(lb.get(lb.curselection()[0])))

lb2 = tk.Listbox(root)
lb2.pack(side="left", fill=tk.BOTH, expand=1)
refreshlist(lb2)
lb2.bind("<Double-Button>", lambda x: os.startfile(lb2.get(lb2.curselection())))

def remove():
    for f in glob.glob("output/*.pdf"):
        os.remove(f)
    refreshlist(lb2)

b2 = tk.Button(root, text="QUITAR", command=remove)
b2.pack()

def split2():
    print(lb.curselection())
    if lb.curselection() != ():
        split(lb.get(lb.curselection()))
    else:
        messagebox.showwarning("DEBE ELEGIR UN ARCHIVO")


b3 = tk.Button(root, text="DIVIDIR ARCHIVO", command=split2)
b3.pack(fill="both")

root.mainloop()
