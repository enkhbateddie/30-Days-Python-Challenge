items = ["Mic", "Phone", 32121.12112, 2312313.315, "Justin", "Bag", "Cliff Bars", 134]

def parse_list(some_list):
	str_list_items = []
	num_list_items = []
	for i in some_list:
		if isinstance(i, float) or isinstance(i, int):
			num_list_items.append(i)
		elif isinstance(i, str):
			str_list_items.append(i)
		else:
			pass
	return str_list_items, num_list_items

print(parse_list(items))

items2 = ["URSA", "Dino", [123, 3214, "fdsafads"]]

print(parse_list(items2))

items3 = ["Mic", "Phone", 32121.12112, 2312313.315, "Justin", "Bag", "Cliff Bars", 134]

