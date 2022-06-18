import tkinter

mainWindow = tkinter.Tk()
# print(mainWindow.__dict__)

# label
label1 = tkinter.Label(mainWindow, text="Laravel")
label2 = tkinter.Label(mainWindow, text="CodeIgniter")
button1 = tkinter.Button(mainWindow, text="Click Me")
button2 = tkinter.Button(mainWindow, text="Click Me")

# positioning merupakan sebuah method yang digunakan untuk mengatur posisi widget dan tidak akan diterapkan pada widget yang belum ditampilkan
label1.pack()
label2.pack()
button1.pack()
button2.pack()

# mainloop() merupakan method yang digunakan untuk menjalankan program dan menampilkan window
mainWindow.mainloop()
