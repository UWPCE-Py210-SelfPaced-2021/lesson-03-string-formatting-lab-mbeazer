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

