from collections import deque
def findIsland(x,y):
    global isVisited
    # 빨간색 폭탄 이번에 지났는지 체크
    thisTimeVisited = [[False for i in range(n)] for j in range(n)]
    way = []
    redcnt = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    color = grid[x][y]
    q = deque()
    q.append((x,y))
    isVisited[x][y]=True
    way.append((x,y))
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<n:
                if (grid[nx][ny]==color and isVisited[nx][ny]==False) or (grid[nx][ny]==0 and thisTimeVisited[nx][ny]==False):
                    q.append((nx,ny))
                    isVisited[nx][ny]=True
                    if grid[nx][ny]==0:
                        redcnt += 1
                        thisTimeVisited[nx][ny] = True
                    way.append((nx,ny))
    way.sort(key=lambda x:(-x[0],x[1]))
    # 빨간색 아닌 폭탄 중 (행 가장 큰+열 가장 작은) 좌표를 0번으로 옮겨줌
    maxidx = 0
    for idx in range(len(way)):
        if grid[way[idx][0]][way[idx][1]] != 0:
            maxidx = idx
            break
    way[0],way[maxidx] = way[maxidx],way[0]
    return [redcnt,way]

# 가장 큰 폭탄 묶음 찾아서 return
def findMaxBomb():
    bomb_bundle = []
    for i in range(n):
        for j in range(n):
            color = grid[i][j]
            if color >= 1 and isVisited[i][j] == False:
                bomb_bundle.append(findIsland(i,j))
    bomb_bundle.sort(key=lambda x:(-len(x[1]),x[0],-x[1][0][0],x[1][0][1]))
    return bomb_bundle[0] if len(bomb_bundle)>0 else []

# 가장 큰 폭탄 묶음 터짐
def bombExplosion(max_bomb_bundle):
    global grid, answer
    way = max_bomb_bundle[1]
    for x,y in way:
        grid[x][y] = -100
    answer += (len(way))**2

# 중력 작용해서 폭탄 떨어짐
def gravity():
    global grid
    for x in range(n-1,0,-1):
        for y in range(n):
            # 빈칸 이라면
            if grid[x][y]==-100:
                for dx in range(1,x+1):
                    nx = x-dx
                    # 위에 돌 있으면 멈추기
                    if grid[nx][y]==-1:
                        break
                    # 위에 폭탄 있으면 내려주기
                    if grid[nx][y]>=0:
                        grid[x][y]=grid[nx][y]
                        grid[nx][y]=-100
                        break

# 반시계 90도 회전
def rotate():
    global grid
    tmp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[(n-1)-j][i] = grid[i][j]
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp[i][j]

############################################################
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
isVisited = [[False for i in range(n)] for j in range(n)]
answer = 0
while True:
    # 초기화
    isVisited = [[False for i in range(n)] for j in range(n)]
    max_bomb_bundle = findMaxBomb()
    if len(max_bomb_bundle)==0 or len(max_bomb_bundle[1]) <= 1:
        break
    bombExplosion(max_bomb_bundle)
    gravity()
    rotate()
    gravity()
print(answer)