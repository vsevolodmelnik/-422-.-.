a = input().split()
c = []
l = []
f = False
for i in range(len(a)):
    if a[i] == '(':
        c.append(a[i])
        l.append(i)
    if a[i] == ')':
        if len(c) == 0:
            print('Обнаружена лишняя закрывающая скобка на ', i + 1, ' позиции')
            f = True
            break
        if len(c) > 0:
            if c[-1] == '(':
                c.pop()
                l.pop()
if len(c) == 0 and f == False:
    print('Последовательность задана корректно')
if len(c) > 0 and f == False:
    print('Обнаружена лишняя закрывающая скобка на позиции', l[-1])
