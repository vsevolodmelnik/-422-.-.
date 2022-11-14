a= []
b= int(input("Введите длину массива: "))
for i in range(b):
    a.append(int(input()))
    a.sort()
print(a)
value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1
k = 0

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
    k+=1

if low > high:
    print("Число не найдено")
    print("кол-во шагов =", k)

else:
    print("Число найдено")
    print("кол-во шагов =", k)