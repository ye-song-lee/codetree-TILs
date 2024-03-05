def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False
def can_make_rectangular(x,y,width,length):
    ver_coor = [(x,y)]
    for d in range(len(dx)):
        if d%2==0:
            nx,ny = x+dx[d]*width,y+dy[d]*width
        else:
            nx,ny = x+dx[d]*length,y+dx[d]*length
        if in_range(nx,ny)==False:
            return False
        else:
            x,y = nx,ny
            ver_coor.append((nx,ny))
    return ver_coor

def coor_in_border(rec_coor,width,length):
    border_coor = []
    x,y = rec_coor[0]
    for d in range(len(dx)):
        have_to_go = length
        if d%2==0:
            have_to_go = width
        for go in range(have_to_go):
            nx,ny = x+dx[d],y+dy[d]
            x,y = nx,ny
            border_coor.append((nx,ny))
    border_coor.sort(key=lambda x:(x[0],x[1]))
    return border_coor

def coor_in_rec(ver_coor,width,length):
    border_coor = []
    rec_coor = []
    x,y = ver_coor[0]
    for d in range(len(dx)):
        have_to_go = length
        if d%2==0:
            have_to_go = width
        for go in range(have_to_go):
            nx,ny = x+dx[d],y+dy[d]
            x,y = nx,ny
            border_coor.append((nx,ny))
    border_coor.sort(key=lambda x:(x[0],x[1]))
    # 내부 넣기
    rec_coor.append(border_coor[0])
    for b in range(1,len(border_coor)-1,2):
        sx,sy = border_coor[b]
        ex,ey = border_coor[b+1]
        for ny in range(sy,ey+1):
            rec_coor.append((sx,ny))
    rec_coor.append(border_coor[-1])
    return rec_coor

def get_tribe_num(ver_coor,border_coor):
    tribe = [0,0,0,0,0]
    one,two,three,four,_ = ver_coor
    sx,ex = border_coor[0][0],border_coor[-1][0]
    for tmpx in range(sx+1):
        for y in range(N):
            if (tmpx,y)==three:
                tribe[0] += people[tmpx][y]
            elif y<=three[1]:
                tribe[1] += people[tmpx][y]
            else:
                tribe[2] += people[tmpx][y]
    idx1, idx2 = 1, 2
    for b in range(1,len(border_coor)-1,2):
        x,sy = border_coor[b]
        _,ey = border_coor[b+1]
        if x==four[0]:
            idx1 += 2
        if x==(two[0]+1):
            idx2 += 2
        for y in range(N):
            if sy<=y<=ey:
                tribe[0] += people[x][y]
            elif y<sy:
                tribe[idx1] += people[x][y]
            else:
                tribe[idx2] += people[x][y]
    for tmpx in range(ex,N):
        for y in range(N):
            if (tmpx,y)==one:
                tribe[0] += people[tmpx][y]
            elif y<one[1]:
                tribe[3] += people[tmpx][y]
            else:
                tribe[4] += people[tmpx][y]
    return tribe

####### MAIN ########
N = int(input())
people = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,-1,1,1]
dy = [1,-1,-1,1]
answer = 1000000000
for width in range(1,N-1): # 사각형 가로
    for length in range(1,N-1): # 사각형 세로
        for i in range(N): # 좌표 x
            for j in range(N): # 좌표 y
                ver_coor = can_make_rectangular(i,j,width,length)
                if ver_coor != False:
                    border_coor = coor_in_border(ver_coor,width,length)
                    tribe = get_tribe_num(ver_coor,border_coor)
                    #print(ver_coor,tribe,max(tribe)-min(tribe))
                    if max(tribe)-min(tribe) < answer:
                        answer = max(tribe)-min(tribe)
print(answer)