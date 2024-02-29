def switch_d(d):
    if d % 2 == 1:
        d -= 1
    else:
        d += 1
    return d

def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def isFinish(x,y):
    if len(horse_grid[x][y])>=4:
        return END
    return NOT_END

def move_n_horse(horse_num):
    global horse_grid,horse_xyd

    isMove = True
    x,y,d = horse_xyd[horse_num]
    nx,ny = x+dx[d],y+dy[d]
    # 같이 다녀야 하는 말들 찾기
    idx_in_horsegrid = horse_grid[x][y].index(horse_num)
    horse_herd = horse_grid[x][y][:idx_in_horsegrid+1]
    # 격자판 범위 내
    if in_range(nx,ny):
        # 빨간색으로 이동
        if grid[nx][ny]==red:
            horse_herd.reverse()
        # 파란색으로 이동
        elif grid[nx][ny]==blue:
            d = switch_d(d)
            nx,ny = x+dx[d],y+dy[d]
            if in_range(nx,ny)==False or grid[nx][ny]==blue:
                nx,ny = x,y
                isMove = False
    else:
        d = switch_d(d)
        nx,ny = x+dx[d],y+dy[d]
    # 저장정보 변경
    if isMove:
        new_horse_herd = horse_herd + horse_grid[nx][ny]
        horse_grid[nx][ny] = new_horse_herd
        horse_grid[x][y] = horse_grid[x][y][idx_in_horsegrid+1:] ##
    for h_idx in horse_herd:
        _,_,tmpd = horse_xyd[h_idx]
        horse_xyd[h_idx] = (nx,ny,tmpd)
    horse_xyd[horse_num] = (nx, ny, d)
    return (nx,ny)



def move_horse():
    for i in range(K):
        x,y = move_n_horse(i)
        if isFinish(x,y) == END:
            return END
    return NOT_END

######## MAIN #######
N,K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
horse_grid = [[[] for x in range(N)] for y in range(N)]
horse_xyd = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(K):
    x,y,d = map(int,input().split())
    horse_grid[x-1][y-1].append(i)
    horse_xyd.append((x-1,y-1,d-1))

# 시뮬레이션
answer = 0
END,NOT_END = 0,1
white,red,blue = 0,1,2
while True:
    answer += 1
    if move_horse() == END:
        break
    if answer > 1000:
        answer = -1
        break
print(answer)