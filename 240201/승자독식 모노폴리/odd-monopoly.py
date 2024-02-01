def inrange(x,y):
   if 0<=x<N and 0<=y<N:
       return True
   return False

def getNextSpot():
    global next
    for player_num in range(len(current)):
        if isDead[player_num] == Dead:
            continue
        x,y,d = current[player_num]
        # 비어 있는 칸 찾기
        for direction in priority[player_num][d]:
            nx,ny = x+dx[direction],y+dy[direction]
            if inrange(nx,ny) and grid[nx][ny]==0:
                next[player_num] = [nx,ny,direction]
                break
        # 비어 있는 칸 못 찾았다면
        if next[player_num]==[]:
            for direction in priority[player_num][d]:
                nx, ny = x + dx[direction], y + dy[direction]
                if inrange(nx,ny) and grid[nx][ny]==(player_num+1):
                    next[player_num] = [nx, ny, direction]
                    break

def move():
    global grid,time,isDead,current,next
    for player_num in range(len(next)):
        if isDead[player_num] == Dead:
            continue
        x,y,d = next[player_num]
        if grid[x][y] != 0 and grid[x][y] != (player_num+1):
            isDead[player_num] = Dead
            continue
        grid[x][y] = (player_num+1)
        time[x][y] = (K+1)
        current[player_num] = next[player_num]
    next = [[] for _ in range(M)]

def timeSpend():
    global grid,time
    for i in range(N):
        for j in range(N):
            if time[i][j]>0:
                time[i][j] -= 1
            if time[i][j]==0:
                grid[i][j] = 0
def isFinish():
    global answer
    answer += 1
    if answer > 1000:
        answer = -1
        return True
    if sum(isDead)==1:
        return True
    return False

#############################################################
N,M,K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
first_d = list(map(int,input().split()))
priority = []
for player in range(M):
    tmp_priority = []
    for direction in range(4):
        one,two,three,four = map(int,input().split())
        tmp_priority.append([one-1,two-1,three-1,four-1])
    priority.append(tmp_priority)

# 상.하.좌.우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 현재 player의 위치
current = [[] for _ in range(M)]
# player의 다음 움직일 위치
next = [[] for _ in range(M)]
# 독점 남은 시간
time = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            time[i][j] = (K+1)
            player_num = grid[i][j]
            current[player_num-1] = [i,j,first_d[player_num-1]-1]
Dead,Alive = 0,1
isDead = [Alive for _ in range(M)]
answer = 0

while True:
    getNextSpot()
    move()
    timeSpend()
    if isFinish():
        break
print(answer)