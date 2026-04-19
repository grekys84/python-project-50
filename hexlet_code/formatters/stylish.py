def format_value(value, depth: int = 0) -> str:
    """
    Форматирует значение для отображения в диффе.

    Args:
        value: Значение, которое необходимо подготовить для отображения
                в диффе. Может быть как простым типом (str, int, bool, None),
                так и словарем с вложенными значениями.
        depth: Текущий уровень вложенности (для рекурсивного
                форматирования словарей).
               По умолчанию 0.
    Returns:
        Строка, содержащая отформатированное представление.

    """
    if isinstance(value, dict):
        indent_size = 4
        current_indent = ' ' * ((depth + 1) * indent_size)
        bracket_indent = ' ' * (depth * indent_size)

        lines = ['{']

        for key, val in value.items():
            lines.append(
                f'{current_indent}{key}: {format_value(val, depth + 1)}'
            )

        lines.append(f'{bracket_indent}}}')
        return '\n'.join(lines)

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return 'null'

    return str(value)


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
    current_indent = ' ' * (depth * indent_size - 2)
    bracket_indent = ' ' * ((depth - 1) * indent_size)
    # Начинаем блок фигурной скобкой
    lines = ['{']

    for node in diff_tree:
        key = node['key']
        status = node['status']

        # Форматируем строку в зависимости от статуса узла
        if status == 'added':
            # Значение добавлено во второй файл (+)
            value = node['value']
            value_str = format_value(value, depth)
            line = f'{current_indent}+ {key}:' + (
                f' {value_str}' if value_str != '' else ''
            )

        elif status == 'removed':
            # Значение удалено из первого файла (-)
            value = node['value']
            value_str = format_value(value, depth)
            line = f'{current_indent}- {key}:' + (
                f' {value_str}' if value_str != '' else ''
            )

        elif status == 'updated':
            # Значение обновилось: сначала старое (-), потом новое (+)
            old_value = node['old_value']
            new_value = node['value']

            old_str = format_value(old_value, depth)
            new_str = format_value(new_value, depth)

            line_old = f'{current_indent}- {key}:' + (
                f' {old_str}' if old_str != '' else ''
            )
            line_new = f'{current_indent}+ {key}:' + (
                f' {new_str}' if new_str != '' else ''
            )
            lines.append(line_old)
            lines.append(line_new)
            # Пропускаем добавление одной строки, так как добавили две
            continue

        elif status == 'nested':
            children = node['children']
            line = (
                f'{current_indent}  {key}: '
                f'{format_diff_stylish(children, depth + 1)}'
            )

        elif status == 'unchanged':
            # Значение не изменилось
            value = node['value']
            value_str = format_value(value, depth)
            line = f'{current_indent}  {key}:' + (
                f' {value_str}' if value_str != '' else ''
            )

        else:
            # Неожиданный статус
            line = f'{current_indent}  {key}: <неизвестный_статус_{status}>'

        lines.append(line)

    lines.append(f'{bracket_indent}}}')
    return '\n'.join(lines)
