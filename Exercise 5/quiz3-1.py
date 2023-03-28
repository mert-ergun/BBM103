import sys

m = int(sys.argv[1]) ** int(sys.argv[2])
print("{} ^ {} = {} = ".format(sys.argv[1], sys.argv[2], m), end='')

summ = 0
temp_sum = 0

for i in range(len(str(m))):
    summ = summ + int(str(m)[i])
    if str(m)[i] != str(m)[-1]:
        print(' {} +'.format(str(m)[i]), end='')
    else:
        print(' {} ='.format(str(m)[i]), end='')
print(' {} ='.format(summ), end='')

while len(str(summ)) > 1:
    for i in str(summ):
        temp_sum += int(i)
        print(' {} +'.format(int(i)), end='')
    summ = temp_sum

print(' = ', summ)

# Mert ERGÜN
# b2220356062
