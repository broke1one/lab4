class Worker:

    def __init__ (self, name, surnmae, position):
        self.name = name
        self.surname = surnmae
        self.position = position
        self._income = None


class Position(Worker):

    def __init__ (self, name, surnmae, position,payday):
        super().__init__(name, surnmae, position)
        self.full_name = self.name + " " + self.surname
        self.set_income(payday)


    def set_income(self,payday):
        self._income = payday["wage"] + payday["bonus"]
        


    def get_income(self):
        return self._income
    


payday = {
    
}

while True:
    print("1 - Создать сотрудника\n2 - Просмотр информации о сотруднике\n0 - Выход из программы")
    choice = input("Выберите действие: ")
    if choice == "1":
        name = input("Введите имя сотрудника: ")
        surname = input("Введите фамилию сотрудника: ")
        position = input("Введите должность сотрудника: ")
        wage = input("Введите зарплату сотрудника: ")
        payday["wage"] = int(wage)
        bonus = input("Введите премию сотрудника: ")
        payday["bonus"] = int(bonus)
        w1 = Position(name,surname,position, payday)
    elif choice == "2":
        print("Информаия о сотруднике: ")
        print(f"Полное имя сотрудника - {w1.full_name}")
        print(f"Должность сотрудника - {w1.position}")
        print(f"Зарплата сотрудника - {w1._income}")
    elif choice == "0":
        print("До свидания")
        pass
    else:
        print("Неверный выбор, повторите попытку")