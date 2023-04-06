from tkinter import *
from tkinter import ttk

def show_questionnaire():
    questionnaire_window = Toplevel(root)
    questionnaire_window.title("Küsimustik")
    
    questionnaire_frame = ttk.Frame(questionnaire_window, padding=10)
    questionnaire_frame.pack()
    
    ttk.Label(questionnaire_frame, text="Вопрос 1").pack()
    ttk.Entry(questionnaire_frame).pack()
    
    ttk.Button(questionnaire_frame, text="Saada").pack()

root = Tk()
root.title("Tarkvara vastuvõtt")
root.geometry("550x250")
frm = ttk.Frame(root, padding=20)
menu = Menu(root)
root.config(menu=menu)
m1 = Menu(menu)
menu.add_cascade(label="Tabs",menu = m1)
m1.add_command(label="Card1", accelerator = "Command+A", command = lambda:new_window(0))
m1.add_command(label="Card2", accelerator = "Command+B", command = lambda:new_window(1))
m1.add_command(label="Card3", accelerator = "Command+C", command = lambda:new_window(2))
m1.add_command(label="Card4", accelerator = "Command+D", command = lambda:new_window(3))

ttk.Label(frm, text="Tere taotleja!").pack()
ttk.Button(frm, text="Quit", command=root.destroy).pack()
lbl = Label(root, text = ". . .", font = "Comic_Sans_MS 15")
btn = Button(frm, text = "Alusta eksamit!", font = "Comic_Sans_MS 15", fg = "White", bg = "#148038",
             relief = GROOVE, width = 15, height = 2, command=show_questionnaire)

frm.pack()
btn.pack()
lbl.pack()

root.mainloop()