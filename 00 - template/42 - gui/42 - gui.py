import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="     aku tertekan jhon! ^[]^     \n")
    label2.pack()

label = tkinter.Label(main_window, text="\nsaya adalah gui \n kamu siapa? \n ngajak brantem!\n")
tombol = tkinter.Button(main_window, text="joba tekan!", command = event_tekan)
spasi = tkinter.Label(main_window, text="")

label.pack()
tombol.pack()
spasi.pack()
main_window.mainloop()