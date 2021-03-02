import re

def get_item_or_none(item):
    if item:
        return item.strip()
    return None

def find_phone_number(string):
	data = re.findall('[0-9]{10,11}', string)
	if data:
		return data
	return None