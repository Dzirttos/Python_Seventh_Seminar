# def convert():
#     # result = []
    # with open(name, 'r', )
    # return

def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def print_bus():
    return read_data_from_file('bus.txt')
    

def add_bus():
    return

def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    return

def print_route():
    return read_data_from_file('route.txt')

def add_route():
    return