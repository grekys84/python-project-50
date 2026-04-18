from hexlet_code.scripts.parser import parse_file


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
        # Ключ есть в обоих, но значения отличаются - обновлен
        elif value1 != value2:
            diff.append({
                'key': key,
                'status': 'updated',
                'value': value2,      # Новое значение из второго файла
                'old_value': value1   # Старое значение из первого файла
            })
        # Ключ есть в обоих и значения равны - без изменений
        else:
            diff.append({'key': key, 'status': 'unchanged', 'value': value1})

    return diff


def format_diff_stylish(diff_tree: list[dict], depth: int = 1) -> str:
    """
    Форматирует дерево различий в строковое представление 'stylish'.

    Args:
        diff_tree: Дерево различий, полученное из build_diff.
        depth: Текущий уровень отступа (внутренний для рекурсии).

    Returns:
        Отформатированная строка, представляющая собой дифф.

    """
    # Размер одного уровня отступа
    indent_size = 4
    # Вычисляем отступ для текущего уровня
    current_indent = " " * (depth * indent_size - 2)
    bracket_indent = " " * ((depth - 1) * indent_size)
    # Начинаем блок фигурной скобкой
    lines = ["{"]

    for node in diff_tree:
        key = node['key']
        status = node['status']
        value = node['value']

        # Форматируем строку в зависимости от статуса узла
        if status == 'added':
            # Значение добавлено во второй файл (+)
            line = f"{current_indent}+ {key}: {format_value(value)}"
        elif status == 'removed':
            # Значение удалено из первого файла (-)
            line = f"{current_indent}- {key}: {format_value(value)}"
        elif status == 'updated':
            # Значение обновилось: сначала старое (-), потом новое (+)
            old_value = node['old_value']
            line_old = f"{current_indent}- {key}: {format_value(old_value)}"
            line_new = f"{current_indent}+ {key}: {format_value(value)}"
            lines.append(line_old)
            lines.append(line_new)
            # Пропускаем добавление одной строки, так как добавили две
            continue
        elif status == 'unchanged':
            # Значение не изменилось
            line = f"{current_indent}  {key}: {format_value(value)}"
        else:
            # Неожиданный статус
            line = f"{current_indent}  {key}: <неизвестный_статус_{status}>"

        lines.append(line)

    lines.append(f"{bracket_indent}}}")  # Заканчиваем блок фигурной скобкой
    return "\n".join(lines)


def format_value(value, depth: int) -> str:
    """
    Форматирует значение для отображения в диффе.

    Args:
        value: Значение, которое необходимо подготовить для отображения
                в диффе. Может быть как простым типом (str, int, bool, None),
                так и словарем с вложенными значениями.
        depth: Текущий уровень вложенности. Используется для расчета
            отступов при форматировании словарей.

    Returns:
        Строка, содержащая отформатированное представление.

    """
    if isinstance(value, dict):
        indent_size = 4
        current_indent = " " * (depth * indent_size)
        bracket_indent = " " * ((depth - 1) * indent_size)

        lines = ["{"]

        for key, val in value.items():
            lines.append(
                f"{current_indent}{key}: {format_value(val, depth + 1)}"
            )

        lines.append(f"{bracket_indent}}}")
        return "\n".join(lines)

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    return str(value)


def generate_diff(first_file_path: str, second_file_path: str) -> str:
    """
    Генерирует дифф между двумя файлами конфигурации.

    Args:
        first_file_path: Путь к первому файлу.
        second_file_path: Путь ко второму файлу.

    Returns:
        Строковое представление диффа в формате 'stylish'.
    """
    # Читаем и парсим оба файла
    data1 = parse_file(first_file_path)
    data2 = parse_file(second_file_path)

    # Строим дерево различий
    diff_tree = build_diff(data1, data2)

    # Форматируем дерево в строку 'stylish'
    return format_diff_stylish(diff_tree)