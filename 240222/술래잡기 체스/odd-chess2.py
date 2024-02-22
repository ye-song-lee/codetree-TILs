def initialize():
    global tagger_d, thief_xy, answer
    answer += (chess_with_thief_num[0][0]+1)
    tagger_d = chess_with_d[0][0]
    thief_xy[chess_with_thief_num[0][0]] = (-1,-1)
    chess_with_thief_num[0][0] = -1

def in_range(x,y):
    if 0<=x<4 and 0<=y<4:
        return True
    return False

def simulate_once(tagger_d,tagger_xy,thief_xy,chess_with_d,chess_with_thief_num,tmp_score):
    global answer
    # return문 -> 조건

    # thief_turn
    for i in range(len(thief_xy)):
        x,y = thief_xy[i]
        if (x,y)==(-1,-1):
            pass
        for d in range(8):
            nd = (chess_with_d[x][y]+d) % 8
            nx,ny = x+dx[nd],y+dy[nd]
            if (nx,ny)!=tagger_xy and in_range(nx,ny):
                idx_switched = chess_with_thief_num[nx][ny]
                thief_xy[i],thief_xy[idx_switched] = thief_xy[idx_switched],thief_xy[i]
                chess_with_d[x][y],chess_with_d[nx][ny] = chess_with_d[nx][ny],nd
                chess_with_thief_num[x][y],chess_with_thief_num[nx][ny] = chess_with_thief_num[nx][ny],chess_with_thief_num[x][y]
                break
    # tagger_turn
    isTaggerMove = False
    for i in range(1,4):
        nx,ny = tagger_xy[0]+dx[tagger_d]*i,tagger_xy[1]+dy[tagger_d]*i
        # 도둑 잡음
        if in_range(nx,ny) and chess_with_thief_num[nx][ny]!=-1:
            tmp_chess_with_d = [[x for x in y] for y in chess_with_d]
            tmp_chess_with_d[tagger_xy[0]][tagger_xy[1]] = -1
            tmp_chess_with_thief_num = [[x for x in y] for y in chess_with_thief_num]
            tmp_chess_with_thief_num[tagger_xy[0]][tagger_xy[1]] = -1
            # 술래꺼 비워줌 + 값 교체
            #chess_with_d[tagger_xy[0]][tagger_xy[1]] = -1
            #chess_with_thief_num[tagger_xy[0]][tagger_xy[1]] = -1
            chased_thief_num = chess_with_thief_num[nx][ny]
            #tagger_xy = (nx,ny)
            #tagger_d = chess_with_d[nx][ny]
            #thief_xy[chased_thief_num] = (-1,-1)
            tmp_thief_xy = [(x,y) for (x,y) in thief_xy]
            tmp_thief_xy[chased_thief_num] = (-1, -1)
            #chess_with_thief_num[nx][ny] = -1
            tmp_chess_with_thief_num[nx][ny] = -1
            # 다시 시뮬레이션 -> 인자로 다 넘겨줘야될듯
            isTaggerMove = True
            simulate_once(chess_with_d[nx][ny],(nx,ny),thief_xy,tmp_chess_with_d,tmp_chess_with_thief_num,tmp_score+(chased_thief_num+1))
    if isTaggerMove == False:
        if tmp_score > answer:
            answer = tmp_score
            return



################# MAIN ################
thief_xy = [(-1,-1) for _ in range(16)]
chess_with_d = [[-1 for x in range(4)] for y in range(4)]
chess_with_thief_num = [[-1 for x in range(4)] for y in range(4)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
tagger_xy = (0,0)
tagger_d = -1
answer = 0

for i in range(4):
    tmp = list(map(int,input().split()))
    for j in range(4):
        p,d = tmp[j*2],tmp[j*2+1]
        thief_xy[p-1] = (i,j)
        chess_with_thief_num[i][j] = (p-1)
        chess_with_d[i][j] = (d-1)

initialize()
simulate_once(tagger_d,tagger_xy,thief_xy,chess_with_d,chess_with_thief_num,answer)
print(answer)