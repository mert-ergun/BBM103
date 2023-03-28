my_list = [1000, 298, 3579, 100, 200, -45, 900]
my_list.sort(key=lambda x: int(x))
print(my_list)


def nth_biggest(n):
    global my_list
    x = int(n)
    nth_element = my_list[-x]
    return nth_element

print(nth_biggest(4))

