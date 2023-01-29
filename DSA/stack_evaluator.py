from tkinter import *
import arithmatic_evaluators

def evaluate_clicked(expression_entry, type_var, ans_label):
    if type_var.get() == 1:
        calculate_prefix(expression_entry.get(), ans_label)
    elif type_var.get() == 2:
        calculate_postfix(expression_entry.get(), ans_label)

def calculate_prefix(expression, ans_label):
    result = "Answer : " + str(arithmatic_evaluators.evaluate_prefix(expression))
    ans_label.configure(text=result)
    ans_label.update()

def calculate_postfix(expression, ans_label):
    result = "Answer : " + str(arithmatic_evaluators.evaluate_postfix(expression))
    ans_label.configure(text=result)
    ans_label.update()

if __name__ == '__main__':
    root = Tk()

    root.geometry("750x450")
    root.title("Arithmetic Expression Evaluator")
    root.configure(background="yellow")

    title_label = Label(root, text="Welcome to the arithmetic expression evaluator", font=("Ariel", 20, "bold"))
    title_label.configure(background="yellow")
    title_label.configure(foreground="blue")
    title_label.place(x=50, y=20)

    info_label = Label(root, text="Please enter your expression", font=("Ariel", 20, "bold"))
    info_label.configure(background="yellow")
    info_label.configure(foreground="red")
    info_label.place(x=170, y=100)

    note_label = Label(root, text="Note : Please enter the values space seperated. For eg. 9 + 12 - 123", font=("Ariel", 12, "bold"))
    note_label.configure(background="yellow")
    note_label.configure(foreground="red")
    note_label.place(x=110, y=130)

    expression_entry = Entry(root, font=("Ariel", 15, "bold"))
    expression_entry.place(x=190, y=170, width=350)

    type_var = IntVar()
    prefix_button = Radiobutton(root, text="Prefix", variable=type_var, value=1, font=("Ariel", 15, "bold"))
    prefix_button.configure(background="yellow")
    prefix_button.place(x=200, y=200)

    postfix_button = Radiobutton(root, text="Postfix", variable=type_var, value=2, font=("Ariel", 15, "bold"))
    postfix_button.configure(background="yellow")
    postfix_button.place(x=400, y=200)

    evaluate_button = Button(root, text="Evaluate!", font=("Ariel", 15, "bold"), command=lambda : evaluate_clicked(expression_entry, type_var, ans_label))
    evaluate_button.configure(background="red")
    evaluate_button.configure(foreground="white")
    evaluate_button.place(x=300, y=250)

    ans_label = Label(root, text="", font=("Ariel", 20, "bold"), anchor="center")
    ans_label.configure(background="yellow")
    ans_label.configure(foreground="red")
    ans_label.place(x=0, y=300, width=750)

    credits_label1 = Label(root, text="Developed by : Prakhar Parikh", font=("Ariel", 14, "bold"))
    credits_label1.configure(background="yellow")
    credits_label1.configure(foreground="blue")
    credits_label1.place(x=200, y=350)
    credits_label2 = Label(root, text="Tarun Nagwadia", font=("Ariel", 14, "bold"))
    credits_label2.configure(background="yellow")
    credits_label2.configure(foreground="blue")
    credits_label2.place(x=340, y=380)
    credits_label3 = Label(root, text="Pratham Chelaramani", font=("Ariel", 14, "bold"))
    credits_label3.configure(background="yellow")
    credits_label3.configure(foreground="blue")
    credits_label3.place(x=345, y=410)

    root.mainloop()