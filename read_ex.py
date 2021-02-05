import tkinter as tk
from tkinter import filedialog
import pandas as pd


def getExcel():
    global df

    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel(import_file_path)
    print(df)

root = tk.Tk()
root.title('Excel reader')

frame1 = tk.Frame()
#canvas1 = tk.Canvas(frame1, width=300, height=300, bg='lightsteelblue')
#canvas1.pack()
label1 = tk.Label(master=frame1, text='Annual average wind speed')
label2 = tk.Label(master=frame1, text='Weibull shape factor')
entry1 = tk.Entry(master=frame1, width=50)
entry2 = tk.Entry(master=frame1, width=50)
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
V_ave = entry1.get()
k = entry2.get()
Button_Excel = tk.Button(master=frame1, text='Import Excel File', command=getExcel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
Button_Excel.pack()
frame1.pack()


root.mainloop()
