from ast import Return
from threading import Event
import tkinter as tr


def yaz1():
    ekran.insert(tr.END, "1")

def yaz2():
    ekran.insert(tr.END, "2")

def yaz3():
    ekran.insert(tr.END, "3")

def yaz4():
    ekran.insert(tr.END, "4")

def yaz5():
    ekran.insert(tr.END, "5")



def yaz6():
    ekran.insert(tr.END, "6")

def yaz7():
    ekran.insert(tr.END, "7")

def yaz8():
    ekran.insert(tr.END, "8")

def yaz9():
    ekran.insert(tr.END, "9")

def yaz0():
    ekran.insert(tr.END, "0")

def yaz_plus():
    ekran.insert(tr.END, "+")

def yaz_minus():
    ekran.insert(tr.END, "-")

def yaz_carpi():
    ekran.insert(tr.END, "*")

def yaz_bolme():
    ekran.insert(tr.END, "/")

def yaz_yuzde():
    ekran.insert(tr.END,"/100")

def temizle():
    ekran.delete(0, tr.END)

def virgul():
    ekran.instert(tr.END,",")

def hesapla():
    islem = ekran.get()
    sonuc = eval(islem)          
    ekran.delete(0, tr.END)
    ekran.insert(0, sonuc)




form = tr.Tk()
form.title("Hesap Makinesi (BJK STORE)")
form.geometry("300x350")
form.bind("<Return>",lambda Event:hesapla())




ekran = tr.Entry(form, font=("Arial", 16),bg="white",fg="blue")
ekran.grid(row=0, column=0, columnspan=4, pady=10, ipadx=10, ipady=10)



btn1 = tr.Button(form, text="1", width=5, height=2, command=yaz1,bg="black",fg="white")
btn1.grid(row=1, column=0, padx=5, pady=5)

btn2 = tr.Button(form, text="2", width=5, height=2, command=yaz2,bg="black",fg="white")
btn2.grid(row=1, column=1, padx=5, pady=5)

btn3 = tr.Button(form, text="3", width=5, height=2, command=yaz3,bg="black",fg="white")
btn3.grid(row=1, column=2, padx=5, pady=5)

btnPlus = tr.Button(form, text="+", width=5, height=2, command=yaz_plus,bg="black",fg="white")
btnPlus.grid(row=1, column=3, padx=5, pady=5)


btn4 = tr.Button(form, text="4", width=5, height=2, command=yaz4,bg="black",fg="white")
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = tr.Button(form, text="5", width=5, height=2, command=yaz5,bg="black",fg="white")
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = tr.Button(form, text="6", width=5, height=2, command=yaz6,bg="black",fg="white")
btn6.grid(row=2, column=2, padx=5, pady=5)

btnMinus = tr.Button(form, text="-", width=5, height=2, command=yaz_minus,bg="black",fg="white")
btnMinus.grid(row=2, column=3, padx=5, pady=5)


btn7 = tr.Button(form, text="7", width=5, height=2, command=yaz7,bg="black",fg="white")
btn7.grid(row=3, column=0, padx=5, pady=5)

btn8 = tr.Button(form, text="8", width=5, height=2, command=yaz8,bg="black",fg="white")
btn8.grid(row=3, column=1, padx=5, pady=5)

btn9 = tr.Button(form, text="9", width=5, height=2, command=yaz9,bg="black",fg="white")
btn9.grid(row=3, column=2, padx=5, pady=5)

btnDiv = tr.Button(form, text="/", width=5, height=2, command=yaz_bolme,bg="black",fg="white")
btnDiv.grid(row=3, column=3, padx=5, pady=5)


btn0 = tr.Button(form, text="0", width=5, height=2, command=yaz0,bg="black",fg="white")
btn0.grid(row=4, column=0, padx=5, pady=5)

btnEqual = tr.Button(form, text="=", width=33, height=2, command=hesapla,bg="black",fg="white")
btnEqual.grid(row=5, column=0,columnspan=4,padx=5, pady=5)

btnCarpi = tr.Button(form, text="*", width=5, height=2, command=yaz_carpi,bg="black",fg="white")
btnCarpi.grid(row=4, column=2, padx=5, pady=5)

btnTemizle = tr.Button(form, text="C", width=5, height=2, command=temizle,bg="black",fg="white")
btnTemizle.grid(row=4, column=3, padx=5, pady=5)

btn_yuzde = tr.Button(form, text="/100", width=5, height=2, command=yaz_yuzde,bg="black",fg="white")
btn_yuzde.grid(row=4, column=3,padx=5, pady=5)

virgul_buton=tr.Button(form,text=",",command=virgul,width=5,height=2,bg="black",fg="white")
virgul_buton.grid(row=4,column=1)



form.mainloop()
