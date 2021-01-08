from enum import Enum


class Pizza(Enum):
    margarita = 1
    peperoni = 2
    barbeky = 3

    def info(self):
        print("Name is - %s, Value is - %s"%(self.name, self.value))

'''
if __name__ == "__main__":
    print(Pizza.barbeky)
    print(Pizza.margarita.name)
    print(Pizza.peperoni.value)
    Pizza.margarita.info()
'''