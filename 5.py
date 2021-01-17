# запись рандомных чисел в файл
import random
with open('file5.txt', 'w') as f:
    for i in range(3):
        f.write(str(random.randint(-100, 100))+' ')
# ручная запись
# line = input('Введите цифры через пробел \n')
#              f.writelines(line)
#              myNumbers = line.split()

# подсчет суммы
with open('file5.txt', 'r') as f:
    for line in f:
        numbers = line.split()
    # print(numbers)
    print('the sum of the numbers is: ', sum(map(int, numbers)))

