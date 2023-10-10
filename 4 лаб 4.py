class Employee:

    __SALARY = 10


    def __init__ (self, days_worked):
        self.__salary = Employee.__SALARY
        self.days_worked = self.__more_than_0(days_worked)
        self.total_salary_salary = Employee.__SALARY * days_worked


    @classmethod
    def set_cls_salary(cls, salary = 10):
        cls.__SALARY = cls.__more_than_0(salary)
        

    @property
    def salary(self):
        return self.__salary
    

    @salary.setter
    def salary(self,salary):
        self.__salary = salary


    @staticmethod
    def __more_than_0(value):
        if value == 0:
            raise ValueError ("Значение должно быть больше 0")
        elif value < 0:
            raise ValueError (f"Вы ввели {value}, значение должно быть больше 0")
        else:
            return value
            

first = None
second = None
days_worked = None
while True:
    choice = input("1 - Внести кол-во дней, которых сотрудники отработал в будние дни\n2 - Просмотр зарплаты сотрудников\n0 - Выход из программы\n")
    if choice == "1":
        days_worked = input("Введите количество дней один сотрудник работал в будние дни, пока второй работал в выходные дни: ")
        try:
            days_worked = int(days_worked)
            if days_worked == 0:
                print("Вы ввели 0, значение должно быть больше 0")
            elif days_worked <= 0:
                print(f"Вы ввели {days_worked}, значение больжно быть больше нуля")
            else:
                Employee.set_cls_salary()
                first = Employee(days_worked)
                Employee.set_cls_salary(15)
                second = Employee(days_worked)
        except:
            print ("\nВведено не число\n")
    
    elif choice == "2":
        if first is None or second is None:
            print("\nДля начала создайте сотрудников\n")
        else:
            print("Инофрмация о зарплате сотрудников: ")
            print(f"\nСотрудники работали - {days_worked} дня(ей)")
            print(f"\nСотрудник который работал по будням заработал - {first.total_salary_salary}$\nЗа день он зарабатывает {first.salary}$\n")
            print(f"\nСотрудник который работал по выходным дням заработал - {second.total_salary_salary}$\nЗа день он зарабатывает {second.salary}$\n")
    elif choice == "0":
        print("До свидания")
        break
    else:
        print("Неверный выбор, повторите попытку")