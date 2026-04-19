from hexlet_code.formatters.stylish import format_diff_stylish
from hexlet_code.formatters.plain import format_diff_plain


def format_diff(diff_tree, format_name: str):
    if format_name == 'stylish':
        return format_diff_stylish(diff_tree)
    if format_name == 'plain':
        return format_diff_plain(diff_tree)

    raise ValueError(f'Неизвестный формат: {format_name}')
