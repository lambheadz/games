from configparser import ConfigParser


def config(filename=r'C:\Users\Lenovo\OneDrive\Рабочий стол\pp2 2nd att\games\lab11\database.ini', section='postgresql'):
    # создайте синтаксический анализаторя
    parser = ConfigParser()
    # прочитать конфигурационный файл
    parser.read(filename)

    # раздел get, по умолчанию используется postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename)) #если есть ошибка

    return db
#читает desktop.ini файл и возвращает параметры подключения.