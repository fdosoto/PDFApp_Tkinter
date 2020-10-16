import tkinter as tk
import pdfkit



def pdf(event):
    "EXPORTAR TEXT O HTML A PDF"
    content= text.get('0,0', tk.END)
    pdfkit.from_string(content)

win = tk.Tk()
win.title('EXPORTAR TEXTO')
win.geometry('700x600')
win.resizable(0,0)
text = tk.Text(win)
text['bg'] = 'gold'
text.pack(fill=tk.BOTH, expand=1)
text.bind('<Control-b>', pdf)




win.mainloop()
