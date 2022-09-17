import math

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/,**,math.log(x, Base),math.ceil(z),math.floor(f)):")
    if s == '0':
        break
    if s in ('+', '-', '*', '/', '**', 'math.log(x, Base)', 'math.ceil(z)', 'math.floor(f)'):
        if s == 'math.ceil(z)':
            z = float(input("z="))
            print("%.2f" % (math.ceil(z)))
        else:
            f = float(input("f="))
            x = float(input("x="))
            y = float(input("y="))
            if s == '+':
                print("%.2f" % (x + y))
            elif s == 'math.floor(f)':
                print("%.2f" % (math.floor(f)))
            elif s == '-':
                print("%.2f" % (x - y))
            elif s == '*':
                print("%.2f" % (x * y))
            elif s == '/':
                if y != 0:
                    print("%.2f" % (x / y))
                else:
                    print("Деление на ноль!")
            elif s == '**':
                print("%.2f" % (x ** y))
            elif s == 'math.log(x, Base)':
                print("%.2f" % (math.log(x, y)))
    else:
        print("Неверный знак операции!")
