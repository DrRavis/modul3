data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0

def calculate_structure_sum(data_structure):
    global sum
    for element in data_structure:
        if isinstance(element, str) == True:
            sum += len(element)
        elif isinstance(element, int) == True or isinstance(element, float):
            sum += element
        elif isinstance(element, dict) == True:
            for key, value in element.items():
                list_1 = [key, value]
                calculate_structure_sum(list_1)
        else:
            calculate_structure_sum(element)
    return sum

result = calculate_structure_sum(data_structure)
print(result)

