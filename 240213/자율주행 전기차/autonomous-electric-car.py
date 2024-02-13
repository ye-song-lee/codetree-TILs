from collections import deque

def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def get_distance(sx,sy,ex,ey):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    isVisited = [[False for i in range(N)] for j in range(N)]
    distance = [[0 for i in range(N)] for j in range(N)]
    q = deque()
    q.append((sx,sy))
    isVisited[sx][sy]=True
    while q:
        x,y = q.popleft()
        if (x,y) == (ex,ey):
            return distance[ex][ey]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if in_range(nx,ny) and isVisited[nx][ny]==False and grid[nx][ny]==0:
                q.append((nx,ny))
                isVisited[nx][ny]=True
                distance[nx][ny]=distance[x][y]+1
    return -1

def select_person():
    minimum = (N*N+1,N,N)
    minimum_person = -1
    for i in range(M):
        if isArrived[i]==ARRIVED:
            continue
        distance = get_distance(car_pos[0],car_pos[1],starts[i][0],starts[i][1])
        # 차가 해당 승객에게 도달할 수 없음
        if distance == -1:
            return [-1,-1]
        person_priority = (distance,starts[i][0],starts[i][1])
        if person_priority < minimum:
            minimum = person_priority
            minimum_person = i
    return [minimum_person,minimum]

def car_get_person():
    global C,car_pos,isArrived
    person_idx,info = select_person()
    if person_idx == -1:
        C = -1
        return -1
    distance,px,py = info
    if C - distance < 0:
        C = -1
        return -1
    C -= distance
    distance_to_go = get_distance(px,py,ends[person_idx][0],ends[person_idx][1])
    if C - distance_to_go < 0:
        C = -1
        return -1
    C += distance_to_go
    car_pos = [ends[person_idx][0],ends[person_idx][1]]
    isArrived[person_idx] = ARRIVED
    return 0

##################################################################
N,M,C = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
car_x,car_y = map(int,input().split())
car_pos = [car_x-1,car_y-1] # 차의 x,y
starts,ends = [],[] # 승객의 출발점,도착점
for _ in range(M):
    sx,sy,ex,ey = map(int,input().split())
    starts.append([sx-1,sy-1])
    ends.append([ex-1,ey-1])
ARRIVED,NOT_ARRIVED = 1,0
isArrived = [NOT_ARRIVED for _ in range(M)] # 각 승객이 목적지에 도착했는지

while sum(isArrived)<M:
    isFinish = car_get_person()
    if isFinish == -1:
        break

print(C)