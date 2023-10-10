class Circle():
    def __init__(self,radius):
        self.radius = radius

    def circleLen(self):
        l = 3.14 * self.radius
        return l
    
    def circleSquare(self):
        s = 3.14 * (self.radius ** 2)
        return s


while True: 
    r = input("Введите радиус: ")
    try:
        r = int(r)
        if r == 0:
            print("Вы ввели 0, такое значение не допустимо.")
        elif r < 0:
            print("Длинна не может быть отрицательной, повторите ввод.")
        else:    
            circle = Circle(r)
            print(f"Длинна окружности - {circle.circleLen()}")
            print(f"Площадь окружности - {circle.circleSquare()}") 
    except:
        print("Введено не число")
