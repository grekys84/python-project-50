from pathlib import Path

from hexlet_code.scripts.diff_builder import generate_diff


def get_fixture_path(filename: str) -> str:
    """
    Возвращает абсолютный путь до файла фикстуры.

    Args:
        filename (str): Имя файла внутри директории fixtures.

    Returns:
        str: Полный путь до файла.

    """
    current_dir = Path(__file__).parent
    return str(current_dir / 'test_data' / filename)


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

    result = generate_diff(file1, file2, format='stylish')

    assert result == expected


def test_generate_diff_yaml() -> None:
    """Тестирует сравнение плоских YAML-файлов."""
    file1 = get_fixture_path('file1.yaml')
    file2 = get_fixture_path('file2.yaml')
    expected = read_fixture('expected_output.txt')

    result = generate_diff(file1, file2, format='stylish')

    assert result == expected
