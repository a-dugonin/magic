class Water:
    """Класс Water использяется для объединения с другими элементами и получения Storm, Steam, Dirt"""

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()

    def __str__(self):
        return 'Вода'


class Air:
    """Класс Air использяется для объединения с другими элементами и получения Storm, Lightning, Dust"""

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()

    def __str__(self):
        return 'Воздух'


class Fire:
    """Класс Fire использяется для объединения с другими элементами и получения Steam, Lightning, Lava"""

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()

    def __str__(self):
        return 'Огонь'


class Earth:
    """Класс Earth использяется для объединения с другими элементами и получения Dirt, Dust, Lava"""

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()

    def __str__(self):
        return 'Земля'


class Storm:
    def __str__(self):
        return f'Объединили элемент {Water()} c элементом {Air()} и получили элемент Шторм'


class Steam:
    def __str__(self):
        return f'Объединили элемент {Water()} c элементом {Fire()} и получили элемент Пар'


class Dirt:
    def __str__(self):
        return f'Объединили элемент {Water()} c элементом {Earth()} и получили элемент Грязь'


class Lightning:
    def __str__(self):
        return f'Объединили элемент {Air()} c элементом {Fire()} и получили элемент Молния'


class Dust:
    def __str__(self):
        return f'Объединили элемент {Earth()} c элементом {Air()} и получили элемент Пыль'


class Lava:

    def __str__(self):
        return f'Объединили элемент {Earth()} c элементом {Fire()} и получили элемент Лава'


def main():
    elements = [Air(), Water(), Fire(), Earth()]
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            result = elements[i] + elements[j]
            print(result)


if __name__ == '__main__':
    main()
