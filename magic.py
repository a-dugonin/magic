class Water:
    """Класс для создания объекта 'Вода' """
    def __add__(self, other):
        """Магический метод для объединения элементов"""
        if type(other) is Air:
            return Storm()
        elif type(other) is Fire:
            return Steam()
        elif type(other) is Earth:
            return Dirt()

    def __str__(self):
        return 'Вода'


class Air:
    """Класс для создания объекта 'Воздух' """
    def __add__(self, other):
        """Магический метод для объединения элементов"""
        if type(other) is Water:
            return Storm()
        elif type(other) is Fire:
            return Lightning()
        elif type(other) is Earth:
            return Dust()

    def __str__(self):
        return 'Воздух'


class Fire:
    """Класс для создания объекта 'Огонь' """
    def __add__(self, other):
        """Магический метод для объединения элементов"""
        if type(other) is Water:
            return Steam()
        elif type(other) is Air:
            return Lightning()
        elif type(other) is Earth:
            return Lava()

    def __str__(self):
        return 'Огонь'


class Earth:
    """Класс для создания объекта 'Земля' """
    def __add__(self, other):
        """Магический метод для объединения элементов"""
        if type(other) is Water:
            return Dirt()
        elif type(other) is Air:
            return Dust()
        elif type(other) is Fire:
            return Lava()

    def __str__(self):
        return 'Земля'


class Storm:
    """Класс для создания объекта 'Шторм' """
    def __str__(self):
        return "Шторм"


class Steam:
    """Класс для создания объекта 'Пар' """
    def __str__(self):
        return "Пар"


class Dirt:
    """Класс для создания объекта 'Грязь' """
    def __str__(self):
        return "Грязь"


class Lightning:
    """Класс для создания объекта 'Молния' """
    def __str__(self):
        return "Молния"


class Dust:
    """Класс для создания объекта 'Пыль' """
    def __str__(self):
        return "Пыль"


class Lava:
    """Класс для создания объекта 'Лава' """

    def __str__(self):
        return "Лава"


def init_element(element: str):
    """Функция для инициализации элементов"""
    if element.lower() == 'вода':
        return Water()
    elif element.lower() == 'воздух':
        return Air()
    elif element.lower() == 'огонь':
        return Fire()
    else:
        return Earth()


def union_elements():
    """Функция для объединения элементов"""
    list_elements = ['огонь', 'Земля']
    element_1, element_2 = [init_element(element) for element in list_elements]
    return element_1 + element_2


def main():
    print(union_elements())


if __name__ == '__main__':
    main()
