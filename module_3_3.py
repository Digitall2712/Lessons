def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(4, 3, 335.5)
print_params(5)
print_params('hello', False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, 553.25, 'Hi!']
values_dict = {'a': 'Hello', 'b': True, 'c': [3, 1, 5]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = (877, 'my number')
print_params(*values_list_2, 42)