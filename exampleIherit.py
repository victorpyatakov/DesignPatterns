class Father:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def print_name(self):
        print(self.name, self.lastname)


class Son(Father):
    def __init__(self, name, lastname):
        Father.__init__(self, name, lastname)


class Daughter(Father):
    def __init__(self, name, lastname):
        # super() - позволяет обращаться к методам родителя без указания его имени
        super().__init__(name, lastname)

'''
if __name__ == "__main__git":
    father = Father("Jon", "Week")
    son = Son("Jack", "Week")
    daughter = Daughter("Linda", "Week")
    father.print_name()
'''