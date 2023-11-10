def start():
    print ("   Добро пожаловать ")
    print ("В игру 'Крестики нолики'")
    print ("________________________")
    print ("      формат ввода:     ")
    print(" первая координата - номер строки  ")
    print(" вторая координата - номер столбца ")
def pole():
    print ()
    print ("   | 0 | 1 | 2 | ")
    print (" ______________")
    for i, row in enumerate(field):
        row_str = f" {i} | { ' | '.join(row)} | "
        print (row_str)
        print (" ______________")
    print()
def ask():
    while True:
        cords = input("Ваш ход (введите координаты) :").split()

        if len(cords) != 2:
            print ( "Пожайлуста введите 2 координаты")
            continue
        x, y  = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print ("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x >2 or 0 > y or y > 2:
            print ("Неверные координаты ")
            continue

        if field[x][y] != "-":
            print("Клетка уже занята ")
            continue

        return x,y
def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

start()
name_1 = input("Введите имя первого игрока :")
name_2 = input("Введите имя второго игрока :")
field = [["-"] * 3 for i in range(3)]
hod = 0
while True:
    hod += 1

    pole()

    if hod % 2 == 1:
        print ("Ходит крестик", name_1)
    else:
        print ("Ходит нолик", name_2)

    x, y = ask()

    if hod % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if hod == 9:
        print("Ничья")
        break
