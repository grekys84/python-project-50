import json
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


def test_generate_diff_json_flat() -> None:
    """
    Проверяет корректность генерации диффа для JSON-файлов.

    Тест:
    - загружает два JSON-файла с различиями
    - сравнивает результат работы generate_diff
        с ожидаемым выводом в формате 'stylish'

    """
    file1 = get_fixture_path('flat_file1.json')
    file2 = get_fixture_path('flat_file2.json')
    expected = read_fixture('expected_output_flat.txt')

    result = generate_diff(file1, file2, format_name='stylish')

    assert result == expected


def test_generate_diff_yaml_flat() -> None:
    """Тестирует сравнение плоских YAML-файлов."""
    file1 = get_fixture_path('flat_file1.yaml')
    file2 = get_fixture_path('flat_file2.yaml')
    expected = read_fixture('expected_output_flat.txt')

    result = generate_diff(file1, file2, format_name='stylish')

    assert result == expected


def test_generate_diff_json_nested() -> None:
    """Тестирует сравнение вложенных json-файлов."""
    file1 = get_fixture_path('nested_file1.json')
    file2 = get_fixture_path('nested_file2.json')
    expected = read_fixture('expected_output_nested.txt')

    result = generate_diff(file1, file2, format_name='stylish')

    assert result == expected


def test_generate_diff_yaml_nested() -> None:
    """Тестирует сравнение вложенных YAML-файлов."""
    file1 = get_fixture_path('nested_file1.yaml')
    file2 = get_fixture_path('nested_file2.yaml')
    expected = read_fixture('expected_output_nested.txt')

    result = generate_diff(file1, file2, format_name='stylish')

    assert result == expected


def test_generate_diff_json_plain() -> None:
    """Тестирует сравнение вложенных JSON-файлов в формате plain."""
    file1 = get_fixture_path('nested_file1.json')
    file2 = get_fixture_path('nested_file2.json')
    expected = read_fixture('expected_output_plain.txt')

    result = generate_diff(file1, file2, format_name='plain')

    assert result == expected


def test_generate_diff_yaml_plain() -> None:
    """Тестирует сравнение вложенных YAML-файлов в формате plain."""
    file1 = get_fixture_path('nested_file1.yaml')
    file2 = get_fixture_path('nested_file2.yaml')
    expected = read_fixture('expected_output_plain.txt')

    result = generate_diff(file1, file2, format_name='plain')

    assert result == expected


def test_generate_diff_json_files_json() -> None:
    """Тестирует сравнение вложенных JSON-файлов в формате json."""
    file1 = get_fixture_path('nested_file1.json')
    file2 = get_fixture_path('nested_file2.json')

    result = generate_diff(file1, file2, format_name='json')

    # Проверяем, что это валидный JSON
    parsed = json.loads(result)

    assert isinstance(parsed, list)
    assert parsed[0]['key'] == 'common'

