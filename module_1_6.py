# Работа со словарями:

my_dict = {'Andrey': 1981, 'Vasya': 1985, 'Vlad': 1999, 'Tonya': 1988}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Anton'))
my_dict.update({'Anton': 1978, 'Tom': 2001})
print(my_dict)
name_1 = my_dict.pop('Anton')
print(name_1)
print(my_dict)


# Работа с множествами:

my_set = {1, 1, 2, 1, 3, 5, 5, 4, True, 'String', (1, 2, 3)}
print(my_set)
my_set.add(6)
my_set.add(7)
print(my_set)
my_set.discard(1)
#my_set.discard(8)
print(my_set)