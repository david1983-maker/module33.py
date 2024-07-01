# Функция с параметрами по умолчанию
def print_params( a=1, b="строка", c=True):
    print(a, b, c)

print_params(b=25)
print_params(3,'num',False,)
print_params(c = [1,2,3])
print_params()

# Распаковка параметров
values_list=[5,'element',6.7]
values_dict={'a':50,'b':"element",'c':False}
print_params(*values_list)
print_params(**values_dict)

 # Распаковка + отдельные параметры
value_list_2 = [54.32, "Строка"]
print_params(*value_list_2,42)


