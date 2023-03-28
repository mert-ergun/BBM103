import sys

my_list = sys.argv[1].split(',')

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

for i in my_list:
    if i < 1:
        my_list.remove(i)

m = 1

while int(my_list[m]) < len(my_list):
    temp_list = []
    for i in range(len(my_list)):
        if (i+1)%int(my_list[m]) != 0:
            temp_list.append(my_list[i])
    if my_list[m] == temp_list[1]:
        m = m+1
    my_list = temp_list
    for element in my_list:
        print(element, end=' ')
    print('\n')
for element in my_list:
    print(element, end=' ')

# Mert ERGÜN
# b2220356062
