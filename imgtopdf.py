import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image
import os
from tkinter import filedialog
from tkinter import messagebox

#APP

win = tk.Tk()
win.title('Imagen a PDF')

win.geometry('700x600')
win.resizable(0,0)

def disable(btn):
    btn['state']= 'disabled'

def enable(btn):
    btn['state'] = 'active'

files = {}
def upload_imgs():
    global files
    files ['filename']= filedialog.askopenfilenames(filetypes=[('JPG', '*.jpg'), ('PNG', '*.png'), ('JPEG', '*.jpeg')],
    initialdir = os.getcwd(), title='SELECCIONAR ARCHIVOS')
    if len(files['filename'])!=0:
        enable(download_button)

def saveas():
    try:
        img_list=[]
        for file in files['filename']:
            img_list.append(Image.open(file).convert('RGB'))
        save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF', '*.pdf')], initialdir=os.getcwd(), title='Save file')
        img_list[0].save(f'{save_file_name}.pdf', save_all=True, append_images = img_list[1:])
        disable(download_button)
        messagebox.showinfo(message='¡GUARDADO!', title='EXITO')
    except:
        return

#MAIN

canvas = Canvas(win, bg='white', width=250, height= 250)
canvas.grid(row=0, column=0, sticky=tk.N, padx=220, pady=25)

main_img = ImageTk.PhotoImage(Image.open('main_app_img.jpg'))
canvas.create_image(125,120, image=main_img)



#INFO

canvas_info = Canvas(win, bg='white', width=600, height=120)
canvas_info.grid(row=1, column=0, padx=25)

info_img = ImageTk.PhotoImage(Image.open('welcome.png'))
canvas_info.create_image(302,62, image=info_img)

#UPLOAD BUTTON

upload_button = tk.Button(win, text='CARGAR IMAGEN', width=20, height=1, font=('arial', 14, 'bold'), bg='white', fg='green', command=upload_imgs)
upload_button.grid(row=2, column=0, padx=200, pady=20)

#DOWNLOAD BUTTON

download_button = tk.Button(win, text= 'GUARDAR PDF', width=20, height=1, font=('arial', 14, 'bold'), bg='white', fg='red', command=saveas)
download_button.grid(row=3, column=0)
disable(download_button)

win.mainloop()
