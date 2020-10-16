import PyPDF2
import tkinter as tk
import os
import sys

# Get all the files in current folder from where we are running the script
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files = list(filter(lambda f: f.lower().endswith(('.pdf')), files))

def rotate_pdf(*args):
    degrees = master.degrees.get()
    pdf_rotator(files, degrees)

# The pdf rotator
def pdf_rotator(files, degrees):

    for filename in files:
        if degrees != 0 and degrees != "":
            with open(filename, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                pdf_writer = PyPDF2.PdfFileWriter()

                print("Rotando", degrees)

                for page_num in range(pdf_reader.numPages):
                    pdf_page = pdf_reader.getPage(page_num)
                    pdf_page.rotateClockwise(degrees)

                    pdf_writer.addPage(pdf_page)

                with open(filename[:-4]+"rotated_"+str(degrees)+".pdf", "wb") as pdf_file_rotated:
                    pdf_writer.write(pdf_file_rotated)
    sys.exit()

# Create our root widget, set title and size
master = tk.Tk()
master.title("Rotar PDF")
master.geometry("400x100")

# Create a IntVar for getting our rotate values
master.degrees = tk.IntVar()

# Create a description label and a couple radiobuttons, add them to the widget
tk.Label(master, text="Rota todos los PDF en la carpeta actual.").grid(row=0,columnspan=4)
tk.Radiobutton(master, text="DERECHA 90 Grados", variable=master.degrees, value=90).grid(row=1,column=1)
tk.Radiobutton(master, text="IZQUIERDA 90 Grados", variable=master.degrees, value=-90).grid(row=1,column=2)
tk.Radiobutton(master, text="180 Grados", variable=master.degrees, value=180).grid(row=1,column=3)

# Create a button for calling our function
master.ok_button = tk.Button(master, command=rotate_pdf, text="ROTAR PDF's")
master.ok_button.grid(row=2,column=1)

# Run
tk.mainloop()
