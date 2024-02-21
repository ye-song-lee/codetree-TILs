def add_flour():
    global flour
    MIN = min(flour)
    for i in range(len(flour)):
        if flour[i] == MIN:
            flour[i] += 1

def make_dough(side_len,start_idx,end):
    dough = [[0 for x in range(side_len)] for y in range(side_len)]
    # 달팽이 회전
    direction = start_idx
    distance_num = 0
    distance = 1
    num = 0
    x,y = side_len//2,side_len//2
    if side_len%2==0:
        x,y = x-1,y-1
    dough[x][y] = flour[num]
    num += 1
    while True:
        for _ in range(distance):
            nx,ny = x+dx[direction],y+dy[direction]
            dough[nx][ny] = flour[num]
            num += 1
            if num == end:
                return dough
            x,y = nx,ny
        distance_num += 1
        if distance_num == 2:
            distance_num = 0
            distance += 1
        direction = (direction+1)%4

def roll_dough():
    # 한변 길이 구하기
    side_len = int(N**0.5)
    if int(N**0.5) != (N**0.5):
        side_len += 1
    # 방향 시작 idx 구하기
    if N == (side_len)**2:
        start_idx = 1
        if (side_len%2) != 0:
            start_idx += 2
    else:
        start_idx = 0
        if (side_len%2) == 0:
            start_idx += 2
    #
    if N == (side_len) ** 2:
        end = N
    elif N >= (side_len - 1) * (side_len):
        end = (side_len - 1) * (side_len)
    else:
        end = (side_len - 1) ** 2
    # 도우 말기
    dough = make_dough(side_len,start_idx,end)
    # 정사각형인 경우
    if N == (side_len)**2 :
        return [dough,[]]
    # 직사각형인 경우
    else:
        add = []
        for i in range((side_len-1)*(side_len),N):
            add.append(flour[i])
        return [dough,add]

def in_range(x,y,xlen,ylen):
    if 0<=x<xlen and 0<=y<ylen:
        return True
    return False

def press_dough(dough,add_dough,xlen,ylen):
    to_be_add = [[0 for y in range(ylen)] for x in range(xlen)]
    for x in range(xlen):
        for y in range(ylen):
            if dough[x][y]==0:
                continue
            for d in range(4):
                nx,ny = x+dx[d],y+dy[d]
                if in_range(nx,ny,xlen,ylen) and dough[nx][ny]!=0:
                    if dough[x][y]>dough[nx][ny]:
                        to_be_add[x][y] -= (dough[x][y]-dough[nx][ny])//5
                    else:
                        to_be_add[x][y] += (dough[nx][ny]-dough[x][y])//5

    to_be_add_2 = [0 for i in range(len(add_dough))]
    for i in range(len(add_dough)):
        if i==0:
            if dough[xlen-1][ylen-2]>add_dough[i]:
                to_be_add_2[i] += (dough[xlen-1][ylen-2]-add_dough[i])//5
                to_be_add[xlen-1][ylen-2] -= (dough[xlen-1][ylen-2]-add_dough[i])//5
            else:
                to_be_add_2[i] -= (add_dough[i]-dough[xlen-1][ylen-2])//5
                to_be_add[xlen-1][ylen-2] += (add_dough[i]-dough[xlen-1][ylen-2])//5
        if i+1<len(add):
            if add_dough[i]>add_dough[i+1]:
                to_be_add_2[i] -= (add_dough[i]-add_dough[i+1])//5
            else:
                to_be_add_2[i] += (add_dough[i+1]-add_dough[i])//5
        if i-1>=0:
            if add_dough[i]>add_dough[i-1]:
                to_be_add_2[i] -= (add_dough[i]-add_dough[i-1])//5
            else:
                to_be_add_2[i] += (add_dough[i-1]-add_dough[i])//5

    for x in range(xlen):
        for y in range(ylen):
            dough[x][y] += to_be_add[x][y]
    for i in range(len(add_dough)):
        add_dough[i] += to_be_add_2[i]

    new_dough = []
    for y in range(ylen):
       for x in range(xlen-1,-1,-1):
           if dough[x][y]!=0:
               new_dough.append(dough[x][y])
    for i in range(len(add_dough)):
        new_dough.append(add_dough[i])
    return new_dough

def fold_dough(dough):
    col_seq = [2,1,0,3]
    num_in_one_row = len(dough)//4
    new_dough = [[0 for i in range(num_in_one_row)] for j in range(4)]
    idx = 0
    for col in col_seq:
        if col%2==0:
            for row in range(num_in_one_row-1,-1,-1):
                new_dough[col][row] = dough[idx]
                idx += 1
        else:
            for row in range(num_in_one_row):
                new_dough[col][row] = dough[idx]
                idx += 1
    return [new_dough,4,num_in_one_row]

def check(dough):
    if max(dough)-min(dough)<=K:
        return True
    return False



#############################################
N, K = map(int,input().split())
flour = list(map(int,input().split()))
# 상-좌-하-우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0
while True:
    answer += 1
    add_flour()
    dough, add = roll_dough()
    dough = press_dough(dough, add, len(dough), len(dough))
    dough, xlen, ylen = fold_dough(dough)
    dough = press_dough(dough, [], xlen, ylen)
    if check(dough):
        break
    flour = dough
print(answer)