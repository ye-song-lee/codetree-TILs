from collections import deque

# 격자 안에 있는지 체크
def is_out_range(x,y):
    if 0<=x<n and 0<=y<n:
        return False
    return True

# 어느 방향으로 주사위를 굴릴지 정하기
def determine_direction():
    global dir_now
    if dice[0] > grid[x][y]:
        dir_now = (dir_now+1) % 4
    elif dice[0] < grid[x][y]:
        dir_now = dir_now-1
        if dir_now < 0:
            dir_now += 4
    # 격자판 밖으로 벗어 나는지 체크
    if is_out_range(x + direction[dir_now][0], y + direction[dir_now][1]):
        if dir_now < 2:
            dir_now += 2
        else:
            dir_now -= 2

# 해당 방향으로 주사위 굴리기
def roll_dice():
    global dir_now, dice, x, y
    if dir_now == 0: # 우
        new_dice = [dice[2],dice[1],abs(7-dice[0])]
    elif dir_now == 1: # 하
        new_dice = [dice[1],abs(7-dice[0]),dice[2]]
    elif dir_now == 2:  # 좌
        new_dice = [abs(7-dice[2]),dice[1],dice[0]]
    else: # 상
        new_dice = [abs(7-dice[1]),dice[0],dice[2]]

    dice = new_dice
    x,y = x+direction[dir_now][0], y+direction[dir_now][1]

def get_answer():
    global x,y
    q = deque()
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    visited = [[False for tmp1 in range(n)] for tmp2 in range(n)]
    result = 0

    q.append((x,y))
    visited[x][y]=True
    result += grid[x][y]
    while q:
        now_x,now_y = q.popleft()
        for k in range(4):
            nx,ny = now_x+dx[k],now_y+dy[k]
            if is_out_range(nx,ny):
                continue
            if grid[nx][ny]==grid[x][y] and visited[nx][ny]==False:
                q.append((nx,ny))
                visited[nx][ny]=True
                result += grid[nx][ny]
    return result

#############################################################
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

direction = [[0,1],[1,0],[0,-1],[-1,0]] # 우.하.좌.상
dir_now = 0 # 현재의 방향(처음 방향은 우니까 0으로 초기화)
x, y = 0,0 # 현재 grid에 있는 위치
dice = [6,2,3] # 주사위[밑면.앞면.오른면]
answer = 0

for i in range(m):
    if i != 0: # 처음에는 오른쪽이라고 방향 정해져 있으므로
        determine_direction()
    roll_dice()
    answer += get_answer()
    #print(x,y)
print(answer)