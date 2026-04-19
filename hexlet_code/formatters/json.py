import json


def format_diff_json(diff_tree: list[dict]) -> str:
    """
    Преобразует дерево различий в строковое представление в формате 'json'.

    Args:
        diff_tree: Дерево, возвращаемое функцией build_diff.

    Returns:
        Строка JSON, представляющая дерево различий.

    """
    return json.dumps(diff_tree, indent=2, ensure_ascii=False)
