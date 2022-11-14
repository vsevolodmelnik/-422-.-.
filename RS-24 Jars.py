import Kinzhal
import timeit

print('Доступные методы сортировки:')
print('  Быстрая(1)     Расчёска(2)')
print()
q = input('Введите номер нужного метода сортировки: ')
while q not in('1','2'):
    q = input('Неверно выбран метод: ')
print()

x=int(input('Введите длину массива: '))
a=[0]*x
print()
for i in range(x):
    a[i]=int(input())
print(); print('Задан массив:', a); print()
set_up='''sort.fs(a)'''
set_up1='''sort.rs(a)'''
if q in ('1'):
    print('Результат быстрой сортировки:'); print(sort.fs(a)); print()
    print('Время выполнения программы:', timeit.timeit(setup=set_up, number=100000, globals=globals()))

if q in ('2'):
    print('Результат сортировки методом "Расчёска":'); print(sort.rs(a)); print()
    print('Время выполнения программы:', timeit.timeit(setup=set_up1, number=100000, globals=globals()))