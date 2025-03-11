b = int(input("Введите количество сегментов сети (1, 2 или 3):"))
match b:
    case 1:
        w = int(input("Введите первый сегмент сети:"))
        f = open(f'{w}.txt','w')
        for x in range(0, 256, 1):
            for y in range(0, 256, 1):
                for z in range(0, 256, 1):
                    a = str(w)+'.'+str(x)+'.'+str(y)+'.'+str(z)+'\n'
                    f.write(a)
        f.close()
    case 2:
        w = int(input("Введите первый сегмент сети:"))
        v = int(input("Введите второй сегмент сети:"))
        f = open(f'{w}.{v}.txt','w')
        for y in range(0, 256, 1):
            for z in range(0, 256, 1):
                a = str(w)+'.'+str(v)+'.'+str(y)+'.'+str(z)+'\n'
                f.write(a)
        f.close()
    case 3:
        w = int(input("Введите первый сегмент сети:"))
        v = int(input("Введите второй сегмент сети:"))
        u = int(input("Введите трерий сегмент сети:"))
        f = open(f'{w}.{v}.{u}.txt','w')
        for z in range(0, 256, 1):
            a = str(w)+'.'+str(v)+'.'+str(u)+'.'+str(z)+'\n'
            f.write(a)
        f.close()
    case _:
        print("некорректное количество сегментов")

