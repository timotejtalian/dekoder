from Pil import Image, ImageDraw
chboard = []
counter = 0
def create_chboard():
    global chboard
    for i in range(8):
        row = [0] * 8
        chboard.append(row)

def check_it(x,y):
    for i in range(0,8):
        if chboard[y][x] == 1:
            return False
        if chboard[i][x] == 1:
            return False
    for i in range(0,8):
        for j in range(0,8):
            if j + i == x + y:
                if chboard[i][j] == 1:
                    return False
            if i - j == y - x:
                if chboard[i][j] == 1:
                    return False
    return True


def queens(n):
    global chboard
    global counter
    if n == 8:
        counter += 1
        createImage()
        print(chboard)
        print("---------------------------------------------")
    else:
        for i in range(0,8):
            if check_it(i,n):
                chboard[n][i] = 1
                queens(n+1)
                chboard[n][i] = 0

create_chboard()
queens(0)

