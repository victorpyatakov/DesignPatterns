"""
Приватнгыми членами класса являются поля и методы, имя которых начинается с __
Приватные они по соглащшению, не как в с,java,c# и т.д.  без модификатора доступа private
"""


class PrivateTest:
    def __init__(self):
        self.public_x = "I'm a public"
        self._private_y = "I'm a quite private"
        self.__private_z = "I'm a private"

    def print_z(self):
        print(self.__private_z)

    def __get_z(self):
        return self.__private_z


if __name__ == "__main__":
    private_test = PrivateTest()
    print(private_test.public_x)
    print(private_test._private_y)
    private_test.print_z()
   # print(private_test.__private_z) # exeption применяется механизм искажения
    print(private_test._PrivateTest__private_z)# все норм
    print(private_test._PrivateTest__get_z())