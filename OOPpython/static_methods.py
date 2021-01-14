class TestClass:
    all_created_classes = []

    def __init__(self, magic = 10):
        self.magic = magic
        TestClass.all_created_classes.append(self)

    def square_magic(self):
        return self.magic ** 2

    @staticmethod
    def sum_all_square_magic():
        return sum([i.square_magic() for i in TestClass.all_created_classes])


if __name__ == "__main__":
    print(TestClass.sum_all_square_magic())
    test1 = TestClass()
    test2 = TestClass(5)
    test3 = TestClass(15)
    print(TestClass.sum_all_square_magic())
    test4 = TestClass(1)
    print(TestClass.sum_all_square_magic())