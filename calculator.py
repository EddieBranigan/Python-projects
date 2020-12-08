import tkinter as tk


class calculator:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Calculator")
        self.label = tk.Label(self.root, text="0", width=33, height=3, bg="white")
        self.b_plus = tk.Button(
            text="+",
            width=10,
            height=3,
            command=lambda: self.button_click_operator("+"),
        )
        self.b1 = tk.Button(
            text="1", width=10, height=3, command=lambda: self.button_click_num("1")
        )
        self.b2 = tk.Button(
            text="2", width=10, height=3, command=lambda: self.button_click_num("2")
        )
        self.b3 = tk.Button(
            text="3", width=10, height=3, command=lambda: self.button_click_num("3")
        )
        self.b_minus = tk.Button(
            text="-",
            width=10,
            height=3,
            command=lambda: self.button_click_operator("-"),
        )
        self.b4 = tk.Button(
            text="4", width=10, height=3, command=lambda: self.button_click_num("4")
        )
        self.b5 = tk.Button(
            text="5", width=10, height=3, command=lambda: self.button_click_num("5")
        )
        self.b6 = tk.Button(
            text="6", width=10, height=3, command=lambda: self.button_click_num("6")
        )
        self.b_multi = tk.Button(
            text="*",
            width=10,
            height=3,
            command=lambda: self.button_click_operator("*"),
        )
        self.b7 = tk.Button(
            text="7", width=10, height=3, command=lambda: self.button_click_num("7")
        )
        self.b8 = tk.Button(
            text="8", width=10, height=3, command=lambda: self.button_click_num("8")
        )
        self.b9 = tk.Button(
            text="9", width=10, height=3, command=lambda: self.button_click_num("9")
        )
        self.b_divide = tk.Button(
            text="/",
            width=10,
            height=3,
            command=lambda: self.button_click_operator("/"),
        )
        self.b_C = tk.Button(
            text="C", width=10, height=3, command=lambda: self.change_text("0")
        )
        self.b0 = tk.Button(
            text="0", width=10, height=3, command=lambda: self.button_click_num("0")
        )
        self.b_del = tk.Button(text="Del", width=10, height=3)
        self.b_equal = tk.Button(
            text="=", width=10, height=3, command=self.button_click_equals
        )

        self.label.grid(column=0, row=0, columnspan=3)
        self.b_plus.grid(column=3, row=0)
        self.b1.grid(column=0, row=1)
        self.b2.grid(column=1, row=1)
        self.b3.grid(column=2, row=1)
        self.b_minus.grid(column=3, row=1)
        self.b4.grid(column=0, row=2)
        self.b5.grid(column=1, row=2)
        self.b6.grid(column=2, row=2)
        self.b_multi.grid(column=3, row=2)
        self.b7.grid(column=0, row=3)
        self.b8.grid(column=1, row=3)
        self.b9.grid(column=2, row=3)
        self.b_divide.grid(column=3, row=3)
        self.b_C.grid(column=0, row=4)
        self.b0.grid(column=1, row=4)
        self.b_del.grid(column=2, row=4)
        self.b_equal.grid(column=3, row=4)

        self.root.mainloop()

    def change_text(self, text_arg):
        self.label["text"] = text_arg

    def button_click_num(self, no):
        label_text = self.label["text"]
        if len(label_text) == 1:
            self.change_text(no)
        if len(label_text) == 3:
            self.change_text(label_text + " " + no)

    def button_click_operator(self, op):
        label_text = self.label["text"]
        if len(label_text) == 1:
            self.change_text(label_text + " " + op)
        print(len(self.label["text"]))

    def button_click_equals(self):
        label_text = self.label["text"]
        first_num = label_text[0]
        op = label_text[2]
        sec_num = label_text[4]
        minus_num = int(first_num) - int(sec_num)
        div_num = int(first_num) / int(sec_num)
        multi_num = int(first_num) * int(sec_num)
        add_num = int(first_num) + int(sec_num)
        if len(label_text) == 5:
            if op == "+":
                self.change_text(label_text + " " + "=" + " " + str(add_num))
            elif op == "-":
                self.change_text(label_text + " " + "=" + " " + str(minus_num))
            elif op == "*":
                self.change_text(label_text + " " + "=" + " " + str(multi_num))
            elif op == "/":
                self.change_text(label_text + " " + "=" + " " + str(div_num))


app = calculator()
