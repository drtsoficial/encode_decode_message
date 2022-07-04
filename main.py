# Import Tkinter
from tkinter import *

# Others necessary modules
import time

# Create root object
root = Tk()

# Set window size
root.geometry("1200x6000")

# Set window title
root.title("Encriptador") 

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f = Frame(root, width=800,  height=700, relief=SUNKEN)

f.pack(side=LEFT)


# Time
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial', 50, 'bold'),
                text="Encriptador", 
                fg="Steel Blue", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
                text=localtime, fg="Steel Blue",
                bd=10, anchor='w')

lblInfo.grid(row=1, column=0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# Exit function     
def qExit():
    root.destroy()

# Reset the window function
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# Reference
lblReference = Label(f, font=('arial', 16, 'bold'),
                        text = "Nome:", bd=16, anchor='w')

lblReference.grid(row=0, column=0)

txtReference = Entry(f, font=('arial', 16, 'bold'),
                        textvariable=rand, bd=10, insertwidth=4,
                        bg="powder blue", justify='right')

txtReference.grid(row=0, column=1)

# Labels

lblMsg = Label(f, font=('arial', 16, 'bold'),
                text = "Mensagem", bd=16, anchor='w')

lblMsg.grid(row=1, column=0)

txtMsg = Entry(f, font=('arial', 16, 'bold'),
                textvariable = Msg, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtMsg.grid(row=1, column=1)

lblKey = Label(f, font=('arial', 16, 'bold'),
        text="Chave", bd=16, anchor='w')

lblKey.grid(row=2, column=0)

txtKey = Entry(f, font=('arial', 16, 'bold'),
        textvariable=key, bd=10, insertwidth=4,
        bg="powder blue", justify='right')

txtKey.grid(row=2, column=1)

lblmode = Label(f, font=('arial', 16, 'bold'),
        text = "Modo('e' para encrypt, d para decrypt)", 
        bd=16, anchor='w')

lblmode.grid(row=3, column=0)

txtmode = Entry(f, font=('arial', 16, 'bold'),
        textvariable=mode, bd=10, insertwidth=4,
        bg="powder blue", justify='right')

txtmode.grid(row=3, column=1)

lblService = Label(f, font=('arial', 16, 'bold'),
        text=" Resultado -", bd=16, anchor='w')

lblService.grid(row=2, column=2)

txtService = Entry(f, font=('arial', 16, 'bold'),
        textvariable=Result, bd=10, insertwidth=4,
        bg="powder blue", justify='right')

txtService.grid(row=2, column=3)

# Vigenere Cipher
import base64

# Encode function
def encode(key, clear):
    enc = []
    
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
    
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Decode function
def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
    
        dec.append(dec_c)
    return "".join(dec)

def Ref():
    print("Mensagem=", (Msg.get()))

    clear = Msg.get()
    k  = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))

# Show message button
btnTotal = Button(f, padx=16, pady=8, bd=16, fg="black",
                    font='arial', width=10, text='Ver Mensagem',
                    bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset =  Button(f, padx=16, pady=8, bd=16, fg="black",
                    font='arial', width=10, text='Resetar',
                    bg="powder blue", command=Ref).grid(row=7, column=2)

btnExit =  Button(f, padx=16, pady=8, bd=16, fg="black",
                    font='arial', width=10, text='Sair',
                    bg="powder blue", command=Ref).grid(row=7, column=1)

# Window alive
root.mainloop()