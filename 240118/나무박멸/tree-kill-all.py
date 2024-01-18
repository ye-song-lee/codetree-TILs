def grow():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(n):
        for y in range(n):
            grow_degree = 0
            if grid[x][y]>0:
                for direction in range(4):
                    nx,ny = x+dx[direction],y+dy[direction]
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]>0:
                        grow_degree += 1
            grid[x][y] += grow_degree
    #print(grid)

def breed():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 각 칸에 몇 그루가 번식 되는 지 저장
    breeding = [[0 for x in range(n)] for y in range(n)]
    for x in range(n):
        for y in range(n):
            breed_dir = []
            if grid[x][y]>0: # 나무인 칸
                # 번식할 수 있는 방향 어딘지 체크
                for direction in range(4):
                    nx,ny = x+dx[direction],y+dy[direction]
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and jecho[nx][ny]==0:
                        breed_dir.append([nx,ny])
                for xdir,ydir in breed_dir:
                    breeding[xdir][ydir] += (grid[x][y]//len(breed_dir))
    for x in range(n):
        for y in range(n):
            grid[x][y] += breeding[x][y]
    #print(grid)

def scatter():
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    # 해당 칸을 지웠을 때 박멸 되는 나무 수 저장
    erase = [[0 for x in range(n)] for y in range(n)]
    # 나무가 가장 많이 박멸 되는 곳 저장
    most = -1
    most_list = []
    # 행 -> 열 순으로 돌기 => 자동으로 행 작은->열 작은으로 정렬돼서 저장
    for x in range(n):
        for y in range(n):
            if grid[x][y] > 0:  # 나무인 칸
                erase[x][y] += grid[x][y] # 자기 자신도 더하기
                for direction in range(4):
                    for length in range(1, k+1):  # 1부터 k까지
                        nx, ny = x + length*dx[direction], y + length*dy[direction]
                        if 0 <= nx < n and 0 <= ny < n:
                            if grid[nx][ny] <= 0:
                                break
                            erase[x][y] += grid[nx][ny]
            if erase[x][y] >= most:
                if erase[x][y] > most:
                    most_list = []
                most = erase[x][y]
                most_list.append([x,y])
    #print(most_list)
    # 제초제 뿌리기
    x,y = most_list[0][0],most_list[0][1]
    jecho[x][y] = -(c+1)
    grid[x][y] = 0
    for direction in range(4):
        for length in range(1, k+1):  # 1부터 k까지
            nx, ny = x + length * dx[direction], y + length * dy[direction]
            if 0 <= nx < n and 0 <= ny < n:
                jecho[nx][ny] = -(c+1)
                if grid[nx][ny] <= 0:
                    break
                grid[nx][ny] = 0
    return erase[x][y]

def year_pass():
    for x in range(n):
        for y in range(n):
            if jecho[x][y] < 0:
                jecho[x][y] += 1

############################################################
n,m,k,c = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
jecho = [[0 for x in range(n)] for y in range(n)]
answer = 0
for i in range(m):
    grow()
    #print(grid)
    breed()
    #print(grid)
    answer += scatter()
    #print(grid)
    #print("j",jecho)
    year_pass()
    #print("j",jecho)
print(answer)