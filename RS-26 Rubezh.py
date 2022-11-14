print("Программа выполнения пирамидальной сортировки"); print()

x=int(input('Введите количество чисел в массиве: '))
a=[0]*x
print()
for i in range(x):
    print('Введите число', i+1 ,'элемента массива:')
    a[i]=int(input())
print(); print('Задан массив:', a); print()

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    с = 0
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        с += 1
        print("Действие №", с, array)
    print ()
    return array

print('Отсортированный массив:', heapSort(a))