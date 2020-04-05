def show_types(vars):
    for var in vars:
        print(type(var))


my_number = 5
my_string = "hello"

my_dict = {"some_key": "some value"}
print(my_dict["some_key"])

my_array = [1, 2, 3, 4]
my_other_array = range(4)

my_float = 3.14

show_types([my_number, my_string, my_dict, my_array, my_other_array, my_float])
