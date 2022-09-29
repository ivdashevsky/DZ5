# Создайте программу для игры в ""Крестики-нолики"".

Matrix = [[0 for x in range(3)] for y in range(3)]

for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
        Matrix[i][j] = str((3*i + j) + 1)

def input_value(type_step):
    valid = False
    while not valid:
        pl_step= input("Ход " + type_step + " ")
        pl_step = int(pl_step)

        if pl_step >= 1 and pl_step <= 9:
            for i in range(len(Matrix)):
                for j in range(len(Matrix[i])):
                    if ((Matrix[i][j] == str(pl_step)) & (Matrix[i][j] not in "XO")):
                        Matrix[i][j] = type_step
                        valid = True
        else:
            print("Введено неверное значение. Введите число от 1 до 9")

def main(board):
    counter = 0
    end = False
    while not end:
        for i in range(len(Matrix)):
            print(Matrix[i])
        if counter % 2 == 0:
            input_value("X")
        else:
            input_value("O")
        counter += 1


main(Matrix)