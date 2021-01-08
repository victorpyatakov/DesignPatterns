class Demo:
    a = 0
    b = 0
    c = 0

    def __init__(self, A, B, C):
        self.a = A
        self.b = B
        self.c = C

    def display(self):
        print(self.a, self.b, self.c)


class NewDemo(Demo):
    d = 0

    def __init__(self, A, B, C, D):
        self.a = A
        self.b = B
        self.c = C
        self.d = D

    def display(self):
        print(self.a, self.b, self.c, self.d, sep=", ")


class NewDemoWithSuper(Demo):
    d = 0

    def __init__(self, A, B, C, D):
        self.d = D
        super().__init__(A, B, C) # super to call super Class #The __init__() Method

    def display(self):
        print(self.a, self.b, self.c, self.d, sep=", ")


if __name__ == "__main__":
    demo = Demo(1,  2, 3)
    new_demo = NewDemo(1, 2, 3, 4)
    new_demo_with_super = NewDemoWithSuper(5, 6, 7, 8)
    print("Base class content : {0}, {1} , {2}".format(str(demo.a), str(demo.b), str(demo.c)))
    print("Derived content : ", end="")
    new_demo.display()
    print("Derived content with super method: ", end="")
    new_demo_with_super.display()