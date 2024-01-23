def attack_monster(playerX,playerY,direction,p):
    total = 0
    # 우.하.좌.상
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for point in range(1,p+1):
        nx, ny = playerX+point*dx[direction], playerY+point*dy[direction]
        total += grid[nx][ny]
        grid[nx][ny] = 0
    return total

def turn_around():
    tmp = []
    # 좌.하.우.상
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    x,y = n//2,n//2
    direction = 0
    distance = 1
    distance_num = 0
    while True:
        distance_num += 1
        for _ in range(distance):
            nx,ny = x+dx[direction],y+dy[direction]
            if nx==0 and ny==-1:
                return tmp
            if grid[nx][ny] != 0:
                tmp.append(grid[nx][ny])
            x,y = nx,ny
        if distance_num == 2:
            distance += 1
            distance_num = 0
        direction = (direction+1) % 4

def move():
    tmp = turn_around()
    # 좌.하.우.상
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # grid 초기화
    grid = [[0 for tmpx in range(n)] for tmpy in range(n)]
    # 나선형 돌기
    direction = 0
    distance = 1
    distance_num = 0
    idx = 0
    x,y = n//2,n//2
    while True:
        distance_num += 1
        for _ in range(distance):
            nx,ny = x+dx[direction],y+dy[direction]
            if nx==0 and ny==-1:
                return grid
            if idx < len(tmp):
                grid[nx][ny] = tmp[idx]
                idx += 1
            x,y=nx,ny
        if distance_num == 2:
            distance += 1
            distance_num = 0
        direction = (direction+1) % 4

def make_count():
    # [[몬스터수,몬스터#],..] 저장
    cnt = []
    # 나선형 돌기
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    direction = 0
    distance = 1
    distance_num = 0
    x,y = n//2,n//2
    while True:
        distance_num += 1
        for _ in range(distance):
            nx,ny = x+dx[direction],y+dy[direction]
            if nx==0 and ny==-1:
                return cnt
            # 값 저장
            if grid[nx][ny] != 0 :
                if len(cnt)!=0 and grid[nx][ny]==cnt[-1][1]:
                    cnt[-1][0] += 1
                else:
                    cnt.append([1,grid[nx][ny]])
            x,y=nx,ny
        if distance_num == 2:
            distance += 1
            distance_num = 0
        direction = (direction+1) % 4

def erase_more_than_four():
    global answer
    cnt = make_count()
    isDifferent = True
    while isDifferent:
        isDifferent = False
        # 4개 이상인 몬스터 (0,0)으로 값 치환
        for c in range(len(cnt)):
            if cnt[c][0]>=4:
                isDifferent = True
                answer += (cnt[c][0]*cnt[c][1])
                cnt[c][0],cnt[c][1] = 0,0
        # (0,0)으로 지운거 없애 버리기
        tmp_cnt = []
        for c in range(len(cnt)):
            if cnt[c] != [0,0]:
                tmp_cnt.append(cnt[c])
        cnt = tmp_cnt
        # 개수 합칠 수 있는거 합치기
        tmp_cnt = []
        for c in range(len(cnt)):
            if c<len(cnt)-1 and cnt[c][1] == cnt[c+1][1]:
                cnt[c+1][0] += cnt[c][0]
            else:
                tmp_cnt.append(cnt[c])
        cnt = tmp_cnt
    return cnt

def store(cnt):
    # grid 초기화
    grid = [[0 for tmpx in range(n)] for tmpy in range(n)]
    # 나선형 돌기
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    direction = 0
    distance = 1
    distance_num = 0
    x, y = n // 2, n // 2
    idx = 0
    while True:
        distance_num += 1
        for _ in range(distance):
            nx,ny = x+dx[direction],y+dy[direction]
            if nx==0 and ny==-1:
                return grid
            # 값 저장
            if idx < len(cnt)*2:
                grid[nx][ny] = cnt[idx//2][idx%2]
                idx += 1
            x,y = nx,ny
        if distance_num==2:
            distance += 1
            distance_num = 0
        direction = (direction+1)%4

###################################################################
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
attack = [list(map(int,input().split())) for _ in range(m)]
answer = 0

for i in range(m):
    playerX, playerY = n // 2, n // 2  # 플레이어의 x,y 좌표
    d,p = attack[i]

    answer += attack_monster(playerX,playerY,d,p)
    grid = move()
    cnt = erase_more_than_four()
    grid = store(cnt)
print(answer)