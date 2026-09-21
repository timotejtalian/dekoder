
from PIL import Image, ImageDraw
chboard = []
counter = 0
img = Image.new('RGB', (640, 640), color = 'white')
draw = ImageDraw.Draw(img)
img2 = Image.open("dama.png")
img2 = img2.resize((60, 60))



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

def obr():
    for i in range(0,8):
        for j in range(0,8):
            if (i + j) % 2 != 0:
                img.paste((0,0,0), (j*80,i*80,(j+1)*80,(i+1)*80))

def nakresli_damy():
    for y in range(8):
        for x in range(8):
            if chboard[y][x] == 1:
                img.paste(img2, (x * 80 + 10, y * 80 + 10))

def queens(n):
    global chboard
    global counter
    if n == 8:
        counter += 1
        nakresli_damy()
        print(chboard)
        print("---------------------------------------------")
        return True
    else:
        for i in range(0,8):
            if check_it(i,n):
                chboard[n][i] = 1
                if queens(n+1):
                    return True
                chboard[n][i] = 0
    return False


create_chboard()
obr()
queens(0)
img.save('chboard.png')
img.show()