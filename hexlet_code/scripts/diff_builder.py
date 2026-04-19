from hexlet_code.scripts.parser import parse_file
from hexlet_code.formatters import format_diff


def build_diff(data1: dict, data2: dict) -> list[dict]:
    """
    Строит внутреннее представление различий между двумя словарями.

    Args:
        data1: Первый словарь.
        data2: Второй словарь.

    Returns:
        Список словарей, где каждый словарь представляет собой узел различия.

    """
    # Получаем объединенное множество ключей из обоих
    # словарей и сортируем их
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        # Ключ есть только во втором файле - добавлен
        if key not in data1:
            diff.append({'key': key, 'status': 'added', 'value': value2})

        # Ключ есть только в первом файле - удален
        elif key not in data2:
            diff.append({'key': key, 'status': 'removed', 'value': value1})

        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                'key': key,
                'status': 'nested',
                'children': build_diff(value1, value2),
            })

        # Ключ есть в обоих, но значения отличаются - обновлен
        elif value1 != value2:
            diff.append({
                'key': key,
                'status': 'updated',
                'value': value2,  # Новое значение из второго файла
                'old_value': value1,  # Старое значение из первого файла
            })
        # Ключ есть в обоих и значения равны - без изменений
        else:
            diff.append({'key': key, 'status': 'unchanged', 'value': value1})

    return diff


def generate_diff(
    first_file_path: str,
    second_file_path: str,
    format_name: str = 'stylish',
) -> str:
    """
    Генерирует дифф между двумя файлами конфигурации.

    Args:
        first_file_path: Путь к первому файлу.
        second_file_path: Путь ко второму файлу.
        format_name: Формат представления диффа

    Returns:
        Строковое представление диффа в формате 'stylish' или
        'plain'.

    """
    # Читаем и парсим оба файла
    data1 = parse_file(first_file_path)
    data2 = parse_file(second_file_path)

    # Строим дерево различий
    diff_tree = build_diff(data1, data2)
    return format_diff(diff_tree, format_name)
