'''
Пример использования оператора switch в Python
Создается функции для обработки условий,
для инициализации всех условий используется словарь
'''


def first_function():
    print("first function")


def second_function():
    print("second function")


def default():
    print("default")


if __name__ == "__main__":
    func_dict = {'a': first_function,
                 'b': second_function,
                 'c': lambda: print('lambda')
                 }
    func_dict.get('h', default)()