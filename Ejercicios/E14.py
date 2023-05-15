
def dictdiff(d1, d2):
    diff = {}

    all_keys = d1.keys() | d2.keys()

    for key in all_keys:
        value1 = d1.get(key)
        value2 = d2.get(key)

        if value1 != value2:
            diff[key] = [value1, value2]

    return diff



d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
print(dictdiff(d1, d1))  # prints “{}”, because we’re comparing d1 with itself
print(dictdiff(d1, d2)) # prints “{'c': [3, 4]}”, because d1 contains c:3 and d2 contains c:4
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
print(dictdiff(d3, d4)) # prints “{'c': [None, 4], 'd': [3, None]}”, because d4 has c:4 and d3 has d:3
d5 = {'a': 1, 'b': 2, 'd': 4}
print(dictdiff(d1, d5)) # prints “{'c': [3, None], 'd': [None, 4]}”, because d1 has c:3 and d5 has d:4