def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 3, b = 'не строка')
print_params(b = 86, c = False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list =  [False, 65, 'кошка']
values_dict = {'a': 'змея', 'b' : [2, 5], 'c' : 84 }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [27, ['строка', 'ещё строка']]
print_params(*values_list_2, 42)