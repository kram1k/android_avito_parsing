def check_to_empty_advertisements(ad: dict[str, list]) -> bool:
    """Проверка на пустоту словаря с обьявлениями"""
    if len(ad["id"]) == 0:
        return True
    return False
