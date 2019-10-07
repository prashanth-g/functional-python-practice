def add_border():
    print('--------------------------------')

""" ================= unfunctional ================= """
# CHARACTERISTIC 1 - No side-effects

a = 0;
def unfuntionalIncrement():
    global a
    a += 1

print(unfuntionalIncrement())
print(a)

""" ================= functional ================= """
# CHARACTERISTIC 1

def functionIncrement(a):
    return a + 1

print(functionIncrement(0))

add_border()

""" ================= functional ================= """
# CHARACTERISTIC 2 - Use maps, reduce instead of iterating over collection manually to update data

name_length = map(len, ['Pepsi', 'CocaCola', 'Bovonto'])
print(*name_length)

cubes = map(lambda x: x * x * x, [2,3,4])
print(*cubes)

""" ================= unfunctional ================= """
# CHARACTERISTIC 2

import random

beverages = ['Pepsi', 'CocaCola', 'Bovonto']
code_names = ['Summer', 'Spring', 'Winter']

for i in range(len(beverages)):
    beverages[i] = random.choice(code_names)

print(*beverages)

""" ================= functional ================= """
# CHARACTERISTIC 2

func_beverages_01 = ['Pepsi', 'CocaCola', 'Bovonto']
func_code_names_01 = map(lambda x: random.choice(['Summer', 'Spring', 'Winter']), func_beverages_01)

print(*func_code_names_01)

""" ================= unfunctional ================= """
# CHARACTERISTIC 2

unfunc_beverages = ['Pepsi', 'CocaCola', 'Bovonto']

for i in range(len(unfunc_beverages)):
    unfunc_beverages[i] = hash(unfunc_beverages[i])

print(*unfunc_beverages)

""" ================= functional ================= """
# CHARACTERISTIC 2

func_beverages_02 = ['Pepsi', 'CocaCola', 'Bovonto']
func_code_names_02 = map(hash, func_beverages_02)

print(*func_code_names_02)

""" ================= functional ================= """
# CHARACTERISTIC 2
import functools

sum = functools.reduce(lambda a, x: a + x, [1,2,3,4,5])

print(sum)

""" ================= unfunctional ================= """
# CHARACTERISTIC 2

people = [{'name':'rik', 'height':160}, {'name':'sid', 'height':170}, {'name':'bin'}]

height_total = 0
height_count = 0

for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count
    print(average_height)

""" ================= functional ================= """
# CHARACTERISTIC 2

heights = map(lambda x: x['height'], filter(lambda x: 'height' in x, people))

height_list = list(heights)

if len(height_list) > 0:
    from operator import add
    func_average_height = functools.reduce(add, height_list, 0) / len(height_list)
    print(func_average_height)

