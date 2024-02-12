# 팩맨이 움직일 수 있는 방향 조합
def make_move_combinations():
    global move_combination
    option = [0,2,4,6]
    for one in range(4):
        for two in range(4):
            for three in range(4):
                move_combination.append([option[one],option[two],option[three]])

def in_range(x,y):
    if 0<=x<4 and 0<=y<4:
        return True
    return False

def make_eggs():
    global eggs
    eggs = [[[] for i in range(4)] for j in range(4)]
    for x in range(4):
        for y in range(4):
            if len(monsters[x][y]) > 0:
                eggs[x][y] = monsters[x][y]

def move_monster():
    global monsters
    new_monsters = [[[] for i in range(4)] for j in range(4)]
    for x in range(4):
        for y in range(4):
            if len(monsters[x][y]) > 0:
                for monster_dir in (monsters[x][y]):
                    isMove = False
                    for d in range(8):
                        now_d = monster_dir - 1
                        nd = (now_d+d) % 8
                        nx,ny = x+dx[nd], y+dy[nd]
                        if in_range(nx,ny) and carcases[nx][ny]==0 and [nx,ny]!=packman:
                            new_monsters[nx][ny].append(nd+1)
                            isMove = True
                            break
                    # 못 움직이면 제자리에
                    if isMove == False:
                        new_monsters[x][y].append(monster_dir)
    for x in range(4):
        for y in range(4):
            monsters[x][y] = new_monsters[x][y]
def move_packman():
    global packman,monsters
    maxEat, maxDir = 0, [0,0,0]
    for directions in move_combination:
        x,y = packman
        howmany = 0
        isVisit = [[False for ni in range(4)] for nj in range(4)]
        for direction in directions:
            nx,ny = x+dx[direction],y+dy[direction]
            if in_range(nx,ny)==False:
                howmany = 0
                break
            if isVisit[nx][ny]==False:
                howmany += len(monsters[nx][ny])
                isVisit[nx][ny]=True
            x,y = nx,ny
        if howmany > maxEat:
            maxEat,maxDir = howmany,directions
    #print(maxDir)
    # 최대위치로 팩맨 옮기기 + 잡아먹은 몬스터 시체로 바꾸기
    x,y = packman
    for direction in maxDir:
        nx,ny = x+dx[direction], y+dy[direction]
        #print(x,y,direction,dx[direction],dy[direction])
        if len(monsters[nx][ny])>0:
            carcases[nx][ny] = -3
        monsters[nx][ny] = []
        x,y = nx,ny
    packman = [x,y]

def eggs_hatching():
    global monsters,eggs
    for x in range(4):
        for y in range(4):
            if len(eggs[x][y]) > 0:
                monsters[x][y].extend(eggs[x][y])

def minus_carcase():
    global carcases
    for x in range(4):
        for y in range(4):
            if carcases[x][y]<0:
                carcases[x][y] += 1

def get_answer():
    answer = 0
    for x in range(4):
        for y in range(4):
            answer += len(monsters[x][y])
    print(answer)

#######################################################
monsters = [[[] for i in range(4)] for j in range(4)]
eggs = [[[] for i in range(4)] for j in range(4)]
carcases = [[0 for i in range(4)] for j in range(4)]
packman = []
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
M,T = map(int,input().split())
r,c = map(int,input().split())
packman = [r-1,c-1]
for i in range(M):
    r,c,d = map(int,input().split())
    monsters[r-1][c-1].append(d)

move_combination = []
make_move_combinations()

for i in range(T):
    make_eggs()
    move_monster()
    move_packman()
    eggs_hatching()
    minus_carcase()
get_answer()