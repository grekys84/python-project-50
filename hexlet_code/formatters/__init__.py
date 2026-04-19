from hexlet_code.formatters.json import format_diff_json
from hexlet_code.formatters.plain import format_diff_plain
from hexlet_code.formatters.stylish import format_diff_stylish


def format_diff(diff_tree: list[dict], format_name: str) -> str:
    """Форматирует дерево различий в указанном формате."""
    if format_name == 'stylish':
        return format_diff_stylish(diff_tree)
    if format_name == 'plain':
        return format_diff_plain(diff_tree)
    if format_name == 'json':
        return format_diff_json(diff_tree)

    raise ValueError(f'Неизвестный формат: {format_name}')
