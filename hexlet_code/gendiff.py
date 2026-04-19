import argparse

from hexlet_code.scripts.diff_builder import generate_diff

__all__ = ['generate_diff']


def main():
    """Главная функция точки входа."""
    parser = argparse.ArgumentParser(
        prog='gendiff',  # Имя программы
        description='Сравнивает два конфигурационных'
        ' файла и показывает разницу.',
        add_help=False,
    )
    # Добавляем позиционные аргументы
    parser.add_argument('first_file', help='Первый конфигурационный файл')
    parser.add_argument('second_file', help='Второй конфигурационный файл')

    # Опциональный аргументы
    parser.add_argument(
        '-h', '--help', action='help', help='Показать справку и выйти'
    )
    parser.add_argument(
        '-f',
        '--format_name',
        default='stylish',
        metavar='{FORMAT}',
        help='Выберите формат вывода (По умолчанию: %(default)s)',
    )

    args = parser.parse_args()

    # Вызываем функцию сравнения и печатаем результат
    diff_result = generate_diff(
        args.first_file, args.second_file, format_name=args.format_name
    )
    print(diff_result)


if __name__ == '__main__':
    main()
