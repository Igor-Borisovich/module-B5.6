'''Приветствие и краткое описание правил игры'''
def greeting():
    print('''            ПРИВЕТ!!!
    ------------------------
    это игра крестики-нолики
    ------------------------
    введите координаты х и у,
    где х - номер строки
        у - номер столбца
    ''')


greeting()


'''Создаём поле в виде двумерной матрицы 3 на 3'''
field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


'''Выводим игровое поле'''
def draw_a_field():
    print(f'  | 0 | 1 | 2 |')
    print('---------------')
    print(f'0 | {field[0][0]} | {field[0][1]} | {field[0][2]} |')
    print('---------------')
    print(f'1 | {field[1][0]} | {field[1][1]} | {field[1][2]} |')
    print('---------------')
    print(f'2 | {field[2][0]} | {field[2][1]} | {field[2][2]} |')
    print('---------------')


'''Получаем координаты и проверяем на соответствие условиям'''
def entering_coordinates():
    while True:
        coordinates = input('        Ваш ход: ').split()

        if len(coordinates) != 2:
            print('Введите две координаты! ')
            continue

        x, y = coordinates

        if not (x.isdigit()) or not (y.isdigit()):
            print('Нужно вводить цифры! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона! ')
            continue

        if field[x][y] != ' ':
            print('Клетка занята!')
            continue

        return x, y


'''Составляем выигрышные комбинации и выявляем победителя'''
def check_winner():
    win_coords = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                  ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                  ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for coord in win_coords:
        a = coord[0]
        b = coord[1]
        c = coord[2]

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != ' ':
            if field[a[0]][a[1]] == 'X':
                print('Выиграли КРЕСТИКИ!')
            else:
                print('Выиграли НОЛИКИ!')

            return True

    return False


'''Заполняем игровое поле крестиками/ноликами введёнными игроками'''
number_of_moves = 0
while True:
    number_of_moves += 1

    draw_a_field()

    if check_winner():
        break

    if number_of_moves % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = entering_coordinates()

    if number_of_moves % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if number_of_moves == 9:
        print('НИЧЬЯ!')
        break