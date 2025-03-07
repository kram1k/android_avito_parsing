def is_not_empty_ads(ad: dict[str, list]) -> bool:
    """Проверка на пустоту словаря с обьявлениями"""
    if len(ad["id"]) == 0 or None:
        return True
    return False


def is_new_ad(ad: dict[str, list], ad_id: list) -> bool:
    if ad_id in ad["id"]:
        return True
    return False