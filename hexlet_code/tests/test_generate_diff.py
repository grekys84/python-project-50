import os

from hexlet_code.gendiff import generate_diff


def get_fixture_path(filename: str) -> str:
    """
    Возвращает абсолютный путь до файла фикстуры.

    Args:
        filename (str): Имя файла внутри директории fixtures.

    Returns:
        str: Полный путь до файла.

    """
    return os.path.join('tests', 'test_data', filename)


def read_fixture(filename: str) -> str:
    """
    Читает содержимое файла фикстуры.

    Args:
        filename (str): Имя файла фикстуры.

    Returns:
        str: Содержимое файла без завершающих пробелов и переносов строки.
    """
    with open(get_fixture_path(filename), encoding='utf-8') as f:
        return f.read().strip()


def test_generate_diff_json() -> None:
    """
    Проверяет корректность генерации диффа для JSON-файлов.

    Тест:
    - загружает два JSON-файла с различиями
    - сравнивает результат работы generate_diff
        с ожидаемым выводом в формате 'stylish'

    """
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_fixture('expected_output.txt')

    result = generate_diff(file1, file2)

    assert result == expected