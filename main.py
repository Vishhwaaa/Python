from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="yellow")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="Text is Decrypted",font="impack 10 bold").place(x=5,y=6)
        text2=Text(screen2,font="impack 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)


        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("Error","Input password")

    elif password!="1234":
        messagebox.showerror("Error","Invalid password")


def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="pink")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="Text is Encrypted",font="impack 10 bold").place(x=5,y=6)
        text2=Text(screen1,font="impack 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)


        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("Error","Input password")

    elif password!="1234":
        messagebox.showerror("Error","Invalid password")

        
    

def main_screen():

  global screen
  global code
  global text1

  screen= Tk()
  screen.geometry("420x420")

  
  screen.title("Encryption and Decryption")
  screen.configure(bg="grey")

  def reset():
      code.set("")
      text1.delete(1.0,END)
  
 
  Label(screen,text="Enter the text for encryption and decryption",font="impack 14 bold ").place(x=5,y=6)
  text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
  text1.place(x=10,y=50,width=400,height=100)

  Label(text ="Enter secret key for encryption and decryption",fg="black",font="impack 12").place(x=45,y=170)

  code=StringVar()
  Entry(textvariable=code,width=19,bd=0,font="impack 25",show="*").place(x=35,y=200)

  Button(screen,text="ENCRYPT",font="arial 15 bold",bg="red",fg="white",bd=0,command=encrypt).place(x=15,y=250,width=150)
  Button(screen,text="DECRYPT",font="arial 15 bold",bg="green",fg="white",bd=0,command=decrypt).place(x=250,y=250,width=150)
  Button(screen,text="RESET",font="arial 15 bold",bg="blue",fg="white",bd=0,command=reset).place(x=85,y=300,width=280)









  


  screen.mainloop()
   


main_screen()
