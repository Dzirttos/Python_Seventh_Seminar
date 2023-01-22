from menu import Menu
import function as fn

if __name__ == "__main__":
    # основной блок
    menuitems = [
        ("1", "Вывод автобусов", fn.print_bus),
        ("2", "Добавление автобусов", fn.add_bus),
        ("3", "Вывод водителей", fn.print_driver),
        ("4", "Добавление водителей", fn.add_driver),
        ("5", "Вывод маршрута", fn.print_route),
        ("6", "Добавление маршрута", fn.add_route),
        ("7", "Выход", lambda: exit())]

    menu = Menu(menuitems)
    # fn.clear_screen()

for i in menuitems:
    print(i[0],i[1])

text = input('Введите номер: ')
if text == '1':
    print(fn.print_bus())
elif text == '3':
    print(fn.print_driver())
elif text == '5':
    print(fn.print_route())    