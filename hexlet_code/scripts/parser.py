import json
import yaml

def parse_file(filepath: str) -> dict:
    """
    Считывает файл на основе его расширения.

     Args:
         filepath - Путь к файлу.

     Returns:
         Словарь с содержимым файла.

    """
    with open(filepath, 'r') as f:
        content = f.read()

    if filepath.endswith('.json'):
        return json.loads(content)
    elif filepath.endswith('.yaml'):
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Не поддерживаемый формат файла: {filepath}")