def format_value(value) -> str:
    """Преобразует значение в строку для plain-формата."""
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_diff_plain(diff_tree: list[dict], parent: str = ''):
    """Рекурсивно форматирует дерево различий в плоский текстовый вид."""
    lines = []

    for node in diff_tree:
        key = node['key']
        status = node['status']

        full_key = f'{parent}.{key}' if parent else key

        if status == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{full_key}' was added with value: {value}"
            )

        elif status == 'removed':
            lines.append(f"Property '{full_key}' was removed")

        elif status == 'updated':
            old = format_value(node['old_value'])
            new = format_value(node['value'])

            lines.append(
                f"Property '{full_key}' was updated. From {old} to {new}"
            )

        elif status == 'nested':
            lines.extend(
                format_diff_plain(node['children'], full_key).splitlines()
            )

        # unchanged игнорируем

    return '\n'.join(lines)
