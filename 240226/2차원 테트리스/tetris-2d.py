def move_to_yellow(type,i,j):
    global yellow
    # 놓을 행 찾기
    bottom = 6
    if type==1 or type==3:
        for x in range(6):
            if yellow[x][j]==1:
                bottom = x
                break
    else:
        for x in range(6):
            if yellow[x][j]==1 or yellow[x][j+1]==1:
                bottom = x
                break
    # 타일 놓기
    yellow[bottom-1][j]=1
    if type==2:
        yellow[bottom-1][j+1]=1
    elif type==3:
        yellow[bottom-2][j]=1

def move_to_red(type,i,j):
    global red
    # 놓을 열 찾기
    right = 6
    if type==1 or type==2:
        for x in range(6):
            if red[i][x]==1:
                right = x
                break
    else:
        for x in range(6):
            if red[i][x]==1 or red[i+1][x]==1:
                right = x
                break
    # 타일 놓기
    red[i][right-1]=1
    if type==2:
        red[i][right-2]=1
    elif type==3:
        red[i+1][right-1]=1

def get_score():
    global yellow,red,score
    # 노란색
    for x in range(5,-1,-1):
        if sum(yellow[x])==4:
            score += 1
            yellow[x]=[0,0,0,0]
            yellow_gravity(x)
    # 빨간색
    for x in range(5,-1,-1):
        SUM = 0
        for y in range(4):
            SUM += red[y][x]
        if SUM == 4:
            score += 1
            for y in range(4):
                red[y][x] = 0
            red_gravity(x)

# i행 위에 있는 것들 한줄씩 아래로
def yellow_gravity(i):
    global yellow
    for x in range(i,0,-1):
        yellow[x] = yellow[x-1]
    yellow[0] = [0,0,0,0]

# i열 왼쪽에 있는 것들 한줄씩 오른쪽으로
def red_gravity(i):
    global red
    for x in range(i,0,-1):
        for y in range(4):
            red[y][x] = red[y][x-1]
    for x in range(4):
        red[x][0] = 0

def yellow_light():
    global yellow
    how_many = 0
    for x in range(2):
        if sum(yellow[x])>0:
            how_many += 1
    for x in range(5,1,-1):
        yellow[x]=yellow[x-how_many]
    yellow[0] = [0,0,0,0]
    yellow[1] = [0,0,0,0]

def red_light():
    global red
    how_many = 0
    for x in range(2):
        for y in range(4):
            if red[y][x]==1:
                how_many += 1
                break
    for x in range(4):
        for y in range(5,1,-1):
            red[x][y]=red[x][y-how_many]
        for y in range(2):
            red[x][y]=0

def light_color():
    yellow_light()
    red_light()

def get_answer():
    answer2 = 0
    for x in range(6):
        for y in range(4):
            if yellow[x][y] == 1:
                answer2 += 1
    for x in range(4):
        for y in range(6):
            if red[x][y] == 1:
                answer2 += 1
    print(score)
    print(answer2)


################# MAIN ####################
yellow = [[0 for x in range(4)] for y in range(6)]
red = [[0 for x in range(6)] for y in range(4)]
score = 0

K = int(input())
for k in range(K):
    type,i,j = map(int,input().split())
    move_to_yellow(type,i,j)
    move_to_red(type,i,j)
    get_score()
    light_color()
get_answer()