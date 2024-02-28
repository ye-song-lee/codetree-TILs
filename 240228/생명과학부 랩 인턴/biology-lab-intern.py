def SY_search(col):
    global grid,answer
    for row in range(N):
        if grid[row][col] != [-1,-1,-1]:
            answer += grid[row][col][2]
            grid[row][col] = [-1,-1,-1]
            break

def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

""""
if d % 2 == 0:
    nd = d + 1
else:
    nd = d - 1
# 상-하-우-좌 순
nx, ny = x, y
if d == 0:
    nx = x + s - 2 * x
elif d == 1:
    nx = x + 2 * ((N - 1) - x) - s
elif d == 2:
    ny = y + 2 * ((M - 1) - y) - s
else:
    ny = y + s - 2 * y
"""
def get_place(x,y,s,d):
    # 상-하-우-좌 순
    if d==0:
        how_many = min(x,s)
        nx,ny = x-how_many,y
        if nx==0:
            d=1
    elif d==1:
        how_many = min((N-1)-x,s)
        nx,ny = x+how_many,y
        if nx==(N-1):
            d=0
    elif d==2:
        how_many = min((M-1)-y,s)
        nx,ny = x,y+how_many
        if ny==(M-1):
            d = 3
    else:
        how_many = min(y,s)
        nx,ny = x,y-how_many
        if ny==0:
            d = 2
    if (s-how_many)>0:
        return [AGAIN,nx,ny,s-how_many,d]
    else:
        return [NOT_AGAIN,nx,ny,s,d]


def move_mold():
    global grid
    new_grid = [[[-1,-1,-1] for x in range(M)] for y in range(N)]
    # 갈 수 있는지 체크
    for x in range(N):
        for y in range(M):
            if grid[x][y] != [-1,-1,-1]:
                d,s,b = grid[x][y]
                if d==0 or d==1:
                    ns = s % (2*(N-1))
                else:
                    ns = s % (2*(M-1))
                nx,ny = x+dx[d]*ns, y+dy[d]*ns
                # 갈 수 있음
                if in_range(nx,ny) and b>new_grid[nx][ny][2]:
                    new_grid[nx][ny] = [d,s,b]
                # 갈 수 없음
                else:
                    return_value = get_place(x,y,s,d)
                    while return_value[0] == AGAIN:
                        flag,nx,ny,ns,nd = return_value
                        return_value = get_place(nx, ny, ns, nd)
                    flag, nx, ny, ns, nd = return_value
                    if b>new_grid[nx][ny][2]:
                        new_grid[nx][ny] = [nd,s,b]
    # 값 대치
    for x in range(N):
        for y in range(M):
            grid[x][y] = new_grid[x][y]




####### MAIN #######
AGAIN,NOT_AGAIN = 0,1
answer = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
N,M,K = map(int,input().split())
# 곰팡이의 (d.s.b) 저장
grid = [[[-1,-1,-1] for i in range(M)] for j in range(N)]
for _ in range(K):
    x,y,s,d,b = map(int,input().split())
    grid[x-1][y-1] = [d-1,s,b]

# 시뮬레이션
for i in range(M):
    SY_search(i)
    move_mold()
print(answer)