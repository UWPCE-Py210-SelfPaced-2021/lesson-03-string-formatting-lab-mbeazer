# Task 1
print('file_00{:d} :   {:.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67))

# Task 2
elements = (2, 123.4567, 10000, 12345.67)
print(f'file_00{elements[0]} :   {elements[1]:.2f}, {elements[2]:.2e}, {elements[3]:.2e}')


# Task 3
def formatter(in_tuple):
    form_string = f'The {len(in_tuple)} numbers are: '
    for i in range(len(in_tuple)):
        """Returns last number with no comma"""
        if i == len(in_tuple) - 1:
            form_string = form_string + '{:d}'
        else:
            form_string = form_string + '{:d}, '

    return form_string.format(*in_tuple)


print(formatter((2, 3, 5, 7, 9)))

# Task 4
print('{3:0>2d} {4} {2} {0:0>2d} {1}'.format(4, 30, 2017, 2, 27))

# Task 5
test_list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {test_list[0][:-1]} is {test_list[1] * 1.2:.2f} and the weight of a {test_list[2][:-1]} is {test_list[3] * 1.2:.2f}')

# Task 6
name_tuples = [('Mario', 35, 1000), ('Luigi', 33, 100), ('Peach', 35, 3000), ('Toad', 32, 10)]
for character in name_tuples:
    print(f'{character[0]:<8s}{character[1]:<6d}${character[2]:<6d}')
