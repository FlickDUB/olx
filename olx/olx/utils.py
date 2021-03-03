import re


def get_item_or_none(item):
    return item.strip() if item else None


def find_phone_number(string):
    raw = re.sub(r'[^+\s\d()-]', '', string)
    raw = re.sub(r'([\s]|[^+\d()-]){2,}', '  ', raw).split('  ')
    result = [re.sub(r'[^\d]', '', phone) for phone in raw if len(phone) >= 10]
    return result if result else None
