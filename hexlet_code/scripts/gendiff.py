import argparse

def main():
    """
    Главная функция точки входа.
    """
    parser = argparse.ArgumentParser(
        prog='gendiff', # Имя программы
        description='Сравнивает два файла и показывает разницу.'
    )
    # Добавляем позиционные аргументы
    parser.add_argument('first_file', help='Первый файл')
    parser.add_argument('second_file', help='Второй файл')

    args = parser.parse_args()

if __name__ == '__main__':
    main()