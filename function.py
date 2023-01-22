def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def print_bus():
   for i in read_data_from_file('bus.txt'):
       print(f'Номер автобуса: {i[1]}, Марка автобуса: {i[2]}')
    
def add_bus():
    new_data = input("Введите, пожалуйста, новые данные через запятую и пробел (', '): ID автобуса (Bus_№№), номер автобуса, марку автобуса\n")
    with open('bus.txt', 'a', encoding='utf8') as data:
        data.writelines(new_data + '\n')

def print_driver():
   for i in read_data_from_file('driver.txt'):
       print(f"Фамилия водителя: {i[1]}")

def add_driver():
    new_data = input("Введите, пожалуйста, новые данные через запятую и пробел (', '): ID водителя (Driver_№№), Фамилию водителя\n")
    with open('driver.txt', 'a', encoding='utf8') as data:
        data.writelines(new_data + '\n')

def print_route():
   for i in read_data_from_file('route.txt'):
       print(f"Маршрут №: {i[1]}")

def add_route():
    new_data = input("Введите, пожалуйста, новые данные через запятую и пробел (', '): ID маршрута (M_№№), номер маршрута с начальной и конечной остановкой, ID автобуса на маршруте (Bus_№№), \nID водителя на маршруте (Driver_№№)\n")
    with open('route.txt', 'a', encoding='utf8') as data:
        data.writelines(new_data + '\n')

def show_route_details():
    user_requst = input("Введите, пожалуйста, ID интересующего маршрута (M_№№): ")
    r = read_data_from_file('route.txt')
    d = read_data_from_file('driver.txt')
    b = read_data_from_file('bus.txt')
    count=0
    for i in r:
        if i[0] != user_requst: count +=1
        if count == len(r): print("\033[31mВведен некорректный ID маршрута!")
        if i[0] == user_requst:
            print(f'\033[32mНомер маршрута: {i[1]}')
            for k in b:
                if k[0] == i[2].strip(): print(f'Номер автобуса: {k[1]}, Марка автобуса: {k[2]}')
            for j in d: 
                if j[0] == i[3].strip(): print(F'Фамилия водителя: {j[1]}')
       

def default():
    # Вывод, если ошибка
    print("\033[31mДанный справочник не предусматривает ввод букв или цифр, отличных от указанных. Пожалуйста, проверьте ввод!")

    