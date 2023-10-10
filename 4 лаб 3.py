class Stationery():

    def __init__ (self, title):
        self.title = title

    
    def draw(self):
        print("Запуск отрисовки!!!")


class Pen(Stationery):

    def draw(self):
        super().draw()
        print("Отрисовка ручкой")



class Pencil(Stationery):

    def draw(self):
        super().draw()
        print("Отрисовка карандашом")
    



class Handle(Stationery):
    
    def draw(self):
        super().draw()
        print("Отрисовка маркером")


while True:
    print("1 - Писать ручкой\n2 - Писать карандошом\n3 - Писать маркером\n0 - Выход из программы")
    choice = input("Выберите действие: ")
    if choice == "1":
        a = Pen("Ручка")
        a.draw()
    elif choice == "2":
        a = Pencil("Карандаш")
        a.draw()
    elif choice == "3":
        a = Handle("Маркер")
        a.draw()
    elif choice == "0":
        print("До свидания")
        break
    else:
        print("Неверный выбор, повторите попытку")