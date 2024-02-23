
1.# T##he `__init__` method is misspelled as `_init__`.
2. The `super` call is incorrect. It should be `super().__init__(root)` instead of `super(Main, self).init(root)`.
3. The `build` method is not indented properly. It should be inside the `Main` class.
4. There is a missing `self` in the `__init__` method. It should be `self.app = Frame(root)` instead of `app = Frame(root)`.
5. There is a typo in the `logicals` method. `self,formula` should be `self.formula`.
6. The `update` method is not indented properly. It should be inside the `Main` class.
7. There is a typo in the `if` statement of the `update` method. `if self.formula == "":` should be `if self.formula == "":`.
8. The `if` statement in the `logicals` method should have `==` instead of `=`.
9. The `if` statement in the `logicals` method should check if `self.formula == "0"` before appending to it.
Here is the corrected code:
```
from tkinter import *

class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.app = Frame(root)
        self.app.pack()
        self.build()
    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#fff")
        self.lbl.place(x=11, y=50)
        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "(", "0", ")", "X^2"
        ]
        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicals(x)
            Button(text=bt, bg="#fff", font=("Times New Roman", 15), command=com).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81
    def logicals(self, operation):
        if operation == "C":
            self.formula = "0"
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()
    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    root.mainloop()
