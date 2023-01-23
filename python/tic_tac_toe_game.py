from tkinter import *
import tkinter.messagebox as tmsg

signbtn1 = ''
signbtn2 = ''
signbtn3 = ''
signbtn4 = ''
signbtn5 = ''
signbtn6 = ''
signbtn7 = ''
signbtn8 = ''
signbtn9 = ''
oddevenval = 0
count = 0

def btn1clicked():
    global oddevenval, signbtn1, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn1var.set('X')
        signbtn1 = 'X'
    else:
        btn1var.set('O')
        signbtn1 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn1.config(state=DISABLED)
    result()

def btn2clicked():
    global oddevenval, signbtn2, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn2var.set('X')
        signbtn2 = 'X'
    else:
        btn2var.set('O')
        signbtn2 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn2.config(state=DISABLED)
    result()

def btn3clicked():
    global oddevenval, signbtn3, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn3var.set('X')
        signbtn3 = 'X'
    else:
        btn3var.set('O')
        signbtn3 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn3.config(state=DISABLED)
    result()

def btn4clicked():
    global oddevenval, signbtn4, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn4var.set('X')
        signbtn4 = 'X'
    else:
        btn4var.set('O')
        signbtn4 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn4.config(state=DISABLED)
    result()

def btn5clicked():
    global oddevenval, signbtn5, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn5var.set('X')
        signbtn5 = 'X'
    else:
        btn5var.set('O')
        signbtn5 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn5.config(state=DISABLED)
    result()

def btn6clicked():
    global oddevenval, signbtn6, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn6var.set('X')
        signbtn6 = 'X'
    else:
        btn6var.set('O')
        signbtn6 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn6.config(state=DISABLED)
    result()

def btn7clicked():
    global oddevenval, signbtn7, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn7var.set('X')
        signbtn7 = 'X'
    else:
        btn7var.set('O')
        signbtn7 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn7.config(state=DISABLED)
    result()

def btn8clicked():
    global oddevenval, signbtn8, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn8var.set('X')
        signbtn8 = 'X'
    else:
        btn8var.set('O')
        signbtn8 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn8.config(state=DISABLED)
    result()

def btn9clicked():
    global oddevenval, signbtn9, count
    zerocrossdecider = int(oddevenval % 2)
    if zerocrossdecider == 0:
        btn9var.set('X')
        signbtn9 = 'X'
    else:
        btn9var.set('O')
        signbtn9 = 'O'
    oddevenval = oddevenval + 1
    count = count + 1
    btn9.config(state=DISABLED)
    result()


def result():
    if count <= 9:
        if signbtn1 == signbtn2 == signbtn3 == 'X':
            btn1.config(bg = "green")
            btn2.config(bg = "green")
            btn3.config(bg = "green")
            print("X won")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
        elif signbtn4 == signbtn5 == signbtn6 == 'X':
            btn4.config(bg = "green")
            btn5.config(bg = "green")
            btn6.config(bg = "green")
            print("X won")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
        elif signbtn7 == signbtn8 == signbtn9 == 'X':
            btn7.config(bg = "green")
            btn8.config(bg = "green")
            btn9.config(bg = "green")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
            print("X won")
        elif signbtn1 == signbtn4 == signbtn7 == 'X':
            btn1.config(bg = "green")
            btn4.config(bg = "green")
            btn7.config(bg = "green")
            print("X won")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
        elif signbtn2 == signbtn5 == signbtn8 == 'X':
            btn2.config(bg = "green")
            btn5.config(bg = "green")
            btn8.config(bg = "green")
            print("X won")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
        elif signbtn3 == signbtn6 == signbtn9 == 'X':
            btn3.config(bg = "green")
            btn6.config(bg = "green")
            btn9.config(bg = "green")
            print("X won")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
        elif signbtn1 == signbtn5 == signbtn9 == 'X':
            btn1.config(bg = "green")
            btn5.config(bg = "green")
            btn9.config(bg = "green")
            print("X won")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
        elif signbtn3 == signbtn5 == signbtn7 == 'X':
            btn3.config(bg = "green")
            btn5.config(bg = "green")
            btn7.config(bg = "green")
            print("X won")
            a = tmsg.showinfo("tic tac toe", "Player X has won")
            if a == "ok":
                exit()
        elif signbtn1 == signbtn2 == signbtn3 == 'O':
            btn1.config(bg = "green")
            btn2.config(bg = "green")
            btn3.config(bg = "green")
            print("O won")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
        elif signbtn4 == signbtn5 == signbtn6 == 'O':
            btn4.config(bg = "green")
            btn5.config(bg = "green")
            btn6.config(bg = "green")
            print("O won")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
        elif signbtn7 == signbtn8 == signbtn9 == 'O':
            btn7.config(bg = "green")
            btn8.config(bg = "green")
            btn9.config(bg = "green")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
            print("O won")
        elif signbtn1 == signbtn4 == signbtn7 == 'O':
            btn1.config(bg = "green")
            btn4.config(bg = "green")
            btn7.config(bg = "green")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
            print("O won")
        elif signbtn2 == signbtn5 == signbtn8 == 'O':
            btn2.config(bg = "green")
            btn5.config(bg = "green")
            btn8.config(bg = "green")
            print("O won")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
        elif signbtn3 == signbtn6 == signbtn9 == 'O':
            btn3.config(bg = "green")
            btn6.config(bg = "green")
            btn9.config(bg = "green")
            print("O won")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
        elif signbtn1 == signbtn5 == signbtn9 == 'O':
            btn1.config(bg = "green")
            btn5.config(bg = "green")
            btn9.config(bg = "green")
            print("O won")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
        elif signbtn3 == signbtn5 == signbtn7 == 'O':
            btn3.config(bg = "green")
            btn5.config(bg = "green")
            btn7.config(bg = "green")
            print("O won")
            a = tmsg.showinfo("tic tac toe", "Player O has won")
            if a == "ok":
                exit()
    if count == 9:
        a = tmsg.showinfo("tic tac toe", "Its a Draw")
        if a == "ok":
            exit()

def exitbtn():
    exitbuttonreturnvalfortic = tmsg.askquestion("Tic Tac Toe","Are you sure you want to exit ?")

    if exitbuttonreturnvalfortic == "yes":
        exit()
    else:
        pass

if __name__ == '__main__':

    root = Tk()

    root.geometry("500x500")
    root.title("Tic Tac Toe")

    btn1var = StringVar()
    btn1var.set('  ')
    btn2var = StringVar()
    btn2var.set('  ')
    btn3var = StringVar()
    btn3var.set('  ')
    btn4var = StringVar()
    btn4var.set('  ')
    btn5var = StringVar()
    btn5var.set('  ')
    btn6var = StringVar()
    btn6var.set('  ')
    btn7var = StringVar()
    btn7var.set('  ')
    btn8var = StringVar()
    btn8var.set('  ')
    btn9var = StringVar()
    btn9var.set('  ')

    Label(root, font = "Lucida 35 bold", bg = "yellow").pack()

    frame1 = Frame(root)
    btn1 = Button(frame1, textvariable = btn1var, font = "Lucida 30 bold", bg = "light blue", command = btn1clicked)
    btn1.pack(side = LEFT, ipadx = 40, ipady = 25)
    btn2 = Button(frame1, font = "Lucida 30 bold", textvariable = btn2var, bg = "light blue", command = btn2clicked)
    btn2.pack(side = LEFT, ipadx = 40, ipady = 25)
    btn3 = Button(frame1, font = "Lucida 30 bold", textvariable = btn3var, bg = "light blue", command = btn3clicked)
    btn3.pack(side = LEFT, ipadx = 40, ipady = 25)
    frame1.pack()

    frame2 = Frame(root)
    btn4 = Button(frame2, font = "Lucida 30 bold", textvariable = btn4var, bg = "light blue", command = btn4clicked)
    btn4.pack(side = LEFT, ipadx = 40, ipady = 25)
    btn5 = Button(frame2, font = "Lucida 30 bold", textvariable = btn5var, bg = "light blue", command = btn5clicked)
    btn5.pack(side = LEFT, ipadx = 40, ipady = 25)
    btn6 = Button(frame2, font = "Lucida 30 bold", textvariable = btn6var, bg = "light blue", command = btn6clicked)
    btn6.pack(side = LEFT, ipadx = 40, ipady = 25)
    frame2.pack()

    frame3 = Frame(root)
    btn7 = Button(frame3, font = "Lucida 30 bold", textvariable = btn7var, bg = "light blue", command = btn7clicked)
    btn7.pack(side = LEFT, ipadx = 40, ipady = 25)
    btn8 = Button(frame3, font = "Lucida 30 bold", textvariable = btn8var, bg = "light blue", command = btn8clicked)
    btn8.pack(side = LEFT, ipadx = 40, ipady = 25)
    btn9 = Button(frame3, font = "Lucida 30 bold", textvariable = btn9var, bg = "light blue", command = btn9clicked)
    btn9.pack(side = LEFT, ipadx = 40, ipady = 25)
    frame3.pack()

    root.config(bg = "yellow")

    root.mainloop()
