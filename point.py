x_position = 0
y_position = 0
class Point:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def show_info(self):
        print("Координата вошої точки по вісі 'X': ", self.x_position,
              "\nКоордината вашої точки по вісі 'Y': ", self.y_position)


while True:
    print("""
        ------МЕНЮ------
        1: Ввести координату "Х"
        2: Ввести координату "Y"
        3: Показати координати вашої точки
        0: Вийти
    """)
    try:
        menu_cheker = int(input("Ввести: "))
        if menu_cheker == 1:
            print("Введіть координату 'Х'")
            x_position = int(input(": "))
        elif menu_cheker == 2:
            print("Введіть координату 'Y'")
            y_position = int(input(": "))
        elif menu_cheker == 3:
            new_point = Point(x_position, y_position)
            new_point.show_info()
        elif menu_cheker == 0:
            print("Bye ;)")
            break
    except Exception as err:
        print("Помилка -> ", err)
