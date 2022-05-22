# import everything from tkinter module
from tkinter import *
import tkinter as tk

# declare the expression variable
calcul = ""

# printing Function
def print_calcul(symbol):
    global calcul
    # concatenation of string
    calcul += str(symbol)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0,calcul)

# Function to evaluate
def calculer_calcul():
    global calcul

    if calcul != "":
        # use Try and except statement
        # for handling the errors like zero
        # division error etc.
        try:
            calcul=str(eval(calcul))
            text_resultat.delete(1.0, "end")
            text_resultat.insert(1.0, calcul)
        except:
            effacer_ecran()
            text_resultat.insert(1.0, "Erreur")

def effacer_ecran():
    global calcul
    calcul=""
    text_resultat.delete(1.0,"end")

# objet interface
root =Tk()
# titre
root.title("Calculatrice")
# demention of calculator interface
root.geometry("325x295")
# background
root.configure(background="#000")
root.maxsize(370,300)

text_resultat = tk.Text(root,height=2, width=17, font=('Arial',24) , borderwidth=2,bg='#242729' , fg='white')
text_resultat.grid(columnspan=5, pady=5 , ipadx=5)

button_AC = Button(root, text=' AC ', fg='white', bg='#242729', borderwidth=1,relief=RIDGE,
                 command= effacer_ecran, height=1, width=6 ,font=('Arial',15,"bold"))
button_AC.grid(row=1, column=0)

button_point = Button(root, text=' . ', fg='white', bg='#242729', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul("."), height=1, width=6 ,font=('Arial',15,"bold"))
button_point.grid(row=1, column=1)

button_modu = Button(root, text=' % ', fg='white', bg='#242729', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul("%"), height=1, width=6 ,font=('Arial',15,"bold"))
button_modu.grid(row=1, column=2)

button_sostraction = Button(root, text=' / ', fg='white', bg='#242729', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul("/"), height=1, width=6 ,font=('Arial',15,"bold"))
button_sostraction.grid(row=1, column=3)

button9 = Button(root, text=' 9 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(9), height=1, width=6 ,font=('Arial',15,"bold"))
button9.grid(row=2, column=2)

button8 = Button(root, text=' 8 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(8), height=1, width=6 ,font=('Arial',15,"bold"))
button8.grid(row=2, column=1)

button7 = Button(root, text=' 7 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(7), height=1, width=6 ,font=('Arial',15,"bold"))
button7.grid(row=2, column=0)

button6 = Button(root, text=' 6 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(6), height=1, width=6 ,font=('Arial',15,"bold"))
button6.grid(row=3, column=2)

button5 = Button(root, text=' 5 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(5), height=1, width=6 ,font=('Arial',15,"bold"))
button5.grid(row=3, column=1)

button4 = Button(root, text=' 4 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(4), height=1, width=6 ,font=('Arial',15,"bold"))
button4.grid(row=3, column=0)

button3 = Button(root, text=' 3 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(3), height=1, width=6 ,font=('Arial',15,"bold"))
button3.grid(row=4, column=2)

button2 = Button(root, text=' 2 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(2), height=1, width=6 ,font=('Arial',15,"bold"))
button2.grid(row=4, column=1)

button1 = Button(root, text=' 1 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(1), height=1, width=6 ,font=('Arial',15,"bold"))
button1.grid(row=4, column=0)

button0 = Button(root, text=' 0 ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(0), height=1, width=6 ,font=('Arial',15,"bold"))
button0.grid(row=5, column=1)

button_open = Button(root, text=' ( ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul("("), height=1, width=6 ,font=('Arial',15,"bold"))
button_open.grid(row=5, column=0)

button_close = Button(root, text=' ) ', fg='white', bg='#000', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul(")"), height=1, width=6 ,font=('Arial',15,"bold"))
button_close.grid(row=5, column=2)

button_mult = Button(root, text=' x ', fg='white', bg='#242729', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul("*"), height=1, width=6 ,font=('Arial',15,"bold"))
button_mult.grid(row=2, column=3)

button_sostraction = Button(root, text=' - ', fg='white', bg='#242729', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul("-"), height=1, width=6 ,font=('Arial',15,"bold"))
button_sostraction.grid(row=3, column=3)

button_add = Button(root, text=' + ', fg='white', bg='#242729', borderwidth=1,relief=RIDGE,
                 command=lambda: print_calcul("+"), height=1, width=6 ,font=('Arial',15,"bold"))
button_add.grid(row=4, column=3)

button_somme = Button(root, text=' = ', fg='white', bg='green', borderwidth=1,relief=RIDGE,
                 command=calculer_calcul, height=1, width=6 ,font=('Arial',15,"bold"))
button_somme.grid(row=5, column=3)

root.mainloop()