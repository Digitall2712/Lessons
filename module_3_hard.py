data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_ = 0
def calculate_structure_sum(data):
    global sum_
    if isinstance(data, list):
        for item in data:
            calculate_structure_sum(item)
            if isinstance(item, int):
                sum_ += item
            elif isinstance(item, str):
                sum_ += len(item)

    elif isinstance(data, tuple):
        for item in data:
            calculate_structure_sum(item)
            if isinstance(item, int):
                sum_ += item
            elif isinstance(item, str):
                sum_ += len(item)

    elif isinstance(data, set):
        for item in data:
            calculate_structure_sum(item)
            if isinstance(item, int):
                sum_ += item
            elif isinstance(item, str):
                sum_ += len(item)

    elif isinstance(data, dict):
        for key, value in data.items():
            calculate_structure_sum(value)
            if isinstance(value, int):
                sum_ += value
                if isinstance(key, str):
                    sum_ += len(key)
    return sum_


result = calculate_structure_sum(data_structure)

print(result)




