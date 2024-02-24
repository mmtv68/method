import random
import time
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array

sp = []
count = 0
while count != 1000:
    rnd_number = random.randint(0, 1000000)
    if rnd_number is sp:
        continue
    count += 1
    sp.append(rnd_number)
p = input('Введите символ для продолжения выполнения программы: ')

# начальное время
start_time = time.time()
print(sp)
# конечное время
end_time = time.time()

# разница между конечным и начальным временем
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)
