import tkinter as tk

calculator = tk.Tk()

firstlabel = tk.Label(calculator, text="Enter the first number: ")
firstlabel.pack()
firstnumber = tk.Entry(calculator)
firstnumber.pack()


secondlabel = tk.Label(calculator, text="Enter the second number: ")
secondlabel.pack()
secondnumber = tk.Entry(calculator)
secondnumber.pack()


def a(num1, num2):
    answer = num1 + num2
    tk.MessageBox.showinfo(answer)


def s(num1, num2):
    answer = num1 - num2
    tk.MessageBox.showinfo(answer)


def d(num1, num2):
    answer = num1 / num2
    tk.MessageBox.showinfo(answer)


def m(num1, num2):
    answer = num1 * num2
    tk.MessageBox.showinfo(answer)


add = tk.Button(calculator, text="+",
                command=a(firstnumber.get(), secondnumber.get()))
subtract = tk.Button(calculator, text="-",
                     command=a(firstnumber.get(), secondnumber.get()))
divide = tk.Button(calculator, text="/",
                   command=a(firstnumber.get(), secondnumber.get()))
multiply = tk.Button(calculator, text="x", command=a(
    firstnumber.get(), secondnumber.get()))

add.pack()
subtract.pack()
divide.pack()
multiply.pack()


calculator.mainloop()
