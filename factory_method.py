from enum import Enum


class PizzaType(Enum):
    """
    Перечисление текущих рецептов пицц в пицерии,
    которые можно приготовить
    """
    MARGARITA = 0,
    PEPERONY = 1,
    VEGAN = 2


class Pizza:
    """
    Базовый класс для пицц, которые можно
    приготовить в пиццерии
    """
    def __init__(self, price: float):
        self.__price = price # цена пиццы

    def get_price(self) -> float:
        return self.__price


class PizzaMargarita(Pizza):
    """
    Класс, представляющий конрекретный вид пиццы - Маргарита
    """
    def __init__(self):
        super().__init__(3.5)


class PizzaPeperoni(Pizza):
    """
    Класс, представляющий конрекретный вид пиццы - Пеперони
    """
    def __init__(self):
        super().__init__(5.5)


class PizzaVegan(Pizza):
    """
    Класс, представляющий конрекретный вид пиццы - Веганская
    """
    def __init__(self):
        super().__init__(17.5)


def create_pizza(pizza_type : PizzaType) -> Pizza:
    """
    Фабричный метод
    :param pizza_type: Тип пиццы из перечисления
    :return: пицца
    """
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.PEPERONY: PizzaPeperoni,
        PizzaType.VEGAN: PizzaVegan
    }
    return factory_dict[pizza_type]()


if __name__ == "__main__":
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f'Pizza: {pizza.name}, Price: {my_pizza.get_price()}')

