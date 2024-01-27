def store_tagger_route(n):
    global tagger_route
    # 상.우.하.좌 -> 하.우.상.좌
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    x,y = n//2,n//2
    distance = 1
    distance_num = 0
    direction = 0
    while True:
        distance_num += 1
        for _ in range(distance):
            nx,ny = x+dx[direction],y+dy[direction]
            if nx==-1 and ny==0:
                # 반대 경로 저장
                reverse_route = []
                for ridx in range(len(tagger_route)-2,-1,-1):
                    rx,ry,rd,rcorner = tagger_route[ridx]
                    if rcorner == True:
                        rd = (rd+1)%4
                    else:
                        if rd >= 2:
                            rd -= 2
                        else:
                            rd += 2
                    reverse_route.append([rx,ry,rd,rcorner])
                tagger_route = [[n//2,n//2,0,True]] + tagger_route # 시작점 저장
                tagger_route.extend(reverse_route)
                return
            # 저장하는 부분
            nd = direction
            isCorner = False
            if _ == (distance-1):
                nd = (direction+1)%4
                isCorner = True
            if nx==0 and ny==0:
                nd = 2
                isCorner = True
            tagger_route.append([nx,ny,nd,isCorner])
            x,y = nx,ny
        if distance_num == 2:
            distance += 1
            distance_num = 0
        direction = (direction+1) % 4

# 술래와 도망자 사이 측정
def calculate_distance(runaway_coor):
    tagger_coor = tagger_route[tagger_idx]
    distance = abs(tagger_coor[0]-runaway_coor[0])+abs(tagger_coor[1]-runaway_coor[1])
    return distance
# 도망자가 가려는 위치가 격자 내에 있는지 체크
def is_in_map(runaway_coor):
    x,y,d = runaway_coor
    nx,ny = x+runner_dx[d],y+runner_dy[d]
    if 0<=nx<n and 0<=ny<n:
        return True
    return False
# 도망자가 가려는 위치에 술래가 있는지 체크
def is_tagger_place(runaway_coor):
    x, y, d = runaway_coor
    nx, ny = x + runner_dx[d], y + runner_dy[d]
    if nx==tagger_route[tagger_idx][0] and ny==tagger_route[tagger_idx][1]:
        return True
    return False
# 도망자 움직임
def move_runner():
    for people in range(m):
        runaway_coor = [runner[people][0],runner[people][1]]
        distance = calculate_distance(runaway_coor)
        if distance <= 3:
            # 격자 벗어 나면 방향 바꿔 주기
            if is_in_map(runner[people]) == False:
                new_d = abs(3-runner[people][2])
                runner[people][2] = new_d
            # 술래 없으면 이동
            if is_tagger_place(runner[people]) == False:
                x, y, d = runner[people]
                new_x, new_y = x + runner_dx[d], y + runner_dy[d]
                runner[people][0],runner[people][1] = new_x,new_y
# 술래 움직임
def move_tagger():
    global tagger_idx
    tagger_idx = (tagger_idx+1) % len(tagger_route)
# 술래가 도망자 잡음
def catch():
    num = 0
    tagger_x,tagger_y,tagger_d = tagger_route[tagger_idx][0],tagger_route[tagger_idx][1],tagger_route[tagger_idx][2]
    for c in range(3):
        catch_x,catch_y = tagger_x+c*tagger_dx[tagger_d],tagger_y+c*tagger_dy[tagger_d]
        if [catch_x,catch_y] not in trees:
            for people in range(m):
                runaway_x,runaway_y = runner[people][0],runner[people][1]
                if (catch_x==runaway_x and catch_y==runaway_y) and isCatched[people]==False:
                    isCatched[people] = True
                    num += 1
    return num



n,m,h,k = map(int,input().split())
# 도망자 방향(우.하.상.좌)
runner_dx = [0,1,-1,0]
runner_dy = [1,0,0,-1]
# 도망자 [x,y,d] 저장 => 좌표 체크 필수
runner = []
for _ in range(m):
    x,y,d = map(int,input().split())
    runner.append([x-1,y-1,d-1])
# 나무 [x,y] 저장
trees = []
for _ in range(h):
    x,y = map(int,input().split())
    trees.append([x-1,y-1])
# 술래 경로 저장 [x,y,d,꺾이는지여부] (상.우.하.좌)
tagger_dx = [-1,0,1,0]
tagger_dy = [0,1,0,-1]
tagger_route = []
store_tagger_route(n)
# 술래 위치
tagger_idx = 0
# 도망자 잡힌 여부
isCatched = [False for _ in range(m)]

answer = 0
for i in range(k):
    move_runner()
    move_tagger()
    answer += (i+1)*catch()
print(answer)