
game_field =[["-"]*3 for _ in range(3)]
def show_field(f):
    print(" ", 0,1,2)
    for i in range(len(game_field)):
        print(str(i), *game_field[i])
print("""Добро пожаловать в игру крестики и нолики"
Правила игры простые, первыми ходят X, вторыми 0.
Игрокам достаточно ввести две координаты хода, основываясь на таблице""")
print("Надеюсь Вам все понятно!! Удачи!!!!")



def survey_user(f):
     while True:
        place= input("Введите две координаты, через пробел: ").split()
        if len(place)<2:
            print("Вы ввели меньше двух координат ")
            continue
        if len(place)>2:
            print("Вы ввели больше двух координат")
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Координатами должны являться числа, а не буквы.")
            continue
        x, y = map(int, place)
        if not (x>=0 and x<3 and y>=0 and y<3):
            print("Вышли из диапозона значений,посмотрите на поле внимательнее")
            continue
        if f[x][y]!="-":
            print("Клетка занята,посмотрите на поле внимательнее")
            continue
        break
     return x,y

def win_users(f,user):
    def chek_line(a1,a2,a3,users):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if chek_line(f[n][0],f[n][1],f[n][2], user) or \
            chek_line(f[0][n],f[1][n],f[2][n], user) or\
            chek_line(f[0][0],f[1][1],f[2][2], user) or \
            chek_line(f[2][0],f[1][1],f[0][2], user):
            return True
    return False




def start_game(f):
    count=0
    while True:
        if count==9:
            print("Ничья")
            break
        if count%2==0:
            user="x"
        else:
            user="o"
        show_field(game_field)

        x,y=survey_user(game_field)

        game_field[x][y] = user

        if win_users(game_field, user):
            print("ПООООООБЕЕЕДААА!!!!!! САЛЮТ, ФАН ФАРЫ!!!!! Победил игрок, ходивший за:", user.upper(), "\n", "Игрок ходивший за  ", user.upper()," THE BEST")
            print("P.S Менторам - Строго не судите =)")

            break
        count+= 1
start_game(game_field)




