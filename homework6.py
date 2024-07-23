my_dict = {'Иванов': 42, 'Петров': 35, 'Сидоров': 88} # Пары фамилия - номер квартиры
print(my_dict)
print(my_dict ['Иванов'])
my_dict ['Комаров'] = 57
print(my_dict ['Комаров'])
my_dict.update({'Королев': 117, 'Васечкин': 12})
my_dict.pop('Петров')
print(my_dict.get ('Петров'))
print(my_dict)

my_set = {7, 4, 5, 'cat', 4, 'sun', 5, 7, 'cat', True}
print(my_set)
my_set.add((1, 2, 3))
my_set.add('dog')
my_set.remove('cat')
print(my_set)