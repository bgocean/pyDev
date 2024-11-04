class Car:
    _color = ''
    weight = 0

    def set(self, color, weight):
        self._color = color
        self.weight = weight


class BMW(Car):
    isM_model = False

    def set(self, color, weight, isM_model):
        self._color = color
        self.weight = weight
        self.isM_model = isM_model


class Mercedes(Car):
    speed = 0


x3 = BMW()
x3.set('White', 1500, False)
print(x3._color)

m3 = BMW()
m3.set('Blue', 1200, True)
print(m3.isM_model)

# Одно подчёркивание _color обозначает protected — переменная считается защищённой,
# но по сути доступ к ней всё равно возможен извне. Это больше намёк для программистов,
# что это "внутреннее" свойство класса.

# Два подчёркивания __color активируют name mangling — переменная становится сложнее доступной
# извне, так как Python меняет её имя на _ClassName__color. Это имитирует приватность, но доступ
# по-прежнему возможен.