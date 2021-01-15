class TestClass:
    all_created_classes = []

    def __init__(self, magic=10):
        self.magic = magic
        TestClass.all_created_classes.append(self)

    def square_magic(self):
        return self.magic ** 2

    def third_power_magic(self):
        return self.magic ** 3

    @staticmethod
    def sum_all_square_magic():
        return sum([i.square_magic() for i in TestClass.all_created_classes])

    @classmethod
    def test_class_method(cls):
        return sum([i.third_power_magic() for i in TestClass.all_created_classes])


class TestInheritClass(TestClass):

    def __init__(self, magic=20):
        self.magic = magic

    def four_power_magic(self):
        return self.magic ** 4


if __name__ == "__main__":
    print(TestClass.sum_all_square_magic())
    test1 = TestClass()
    test2 = TestClass(5)
    test3 = TestClass(15)
    print(TestClass.sum_all_square_magic())
    test4 = TestClass(1)
    print(TestClass.sum_all_square_magic())
    print(TestClass.test_class_method())
    print(TestInheritClass.sum_all_square_magic())
