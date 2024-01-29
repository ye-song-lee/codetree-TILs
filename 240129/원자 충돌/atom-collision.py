def move():
    global atoms,grid
    # grid 초기화
    grid = [[[] for x in range(N)] for y in range(N)]
    for idx in range(len(atoms)):
        # 죽은 원자는 pass
        if atoms[idx] == []:
            continue
        # 원자 움직이고 grid와 atoms에 저장
        x,y,m,s,d = atoms[idx]
        nx,ny = (x+dx[d]*s)%N,(y+dy[d]*s)%N
        atoms[idx][0],atoms[idx][1] = nx,ny
        grid[nx][ny].append(idx)

def synthesis():
    global grid
    for ii in range(N):
        for jj in range(N):
            if len(grid[ii][jj]) >= 2:
                nm = sum([atoms[tmp][2] for tmp in grid[ii][jj]]) // 5
                ns = sum([atoms[tmp][3] for tmp in grid[ii][jj]]) // len(grid[ii][jj])
                if nm != 0:
                    even = 0
                    for atom_idx in grid[ii][jj]:
                        if atoms[atom_idx][4] % 2 == 0:
                            even += 1
                    if even == 0 or even == len(grid[ii][jj]):
                        nd = 0
                    else:
                        nd = 1
                # 원래 있던거 제거
                for atom_idx in grid[ii][jj]:
                    atoms[atom_idx]=[]
                grid[ii][jj] = []
                # 새로운 원자 넣어주기
                if nm != 0:
                    original_len = len(atoms)
                    for plus in range(4):
                        atoms.append([ii,jj,nm,ns,nd+2*plus])
                        grid[ii][jj].append(original_len+plus)

def get_answer():
    answer = 0
    for idx in range(len(atoms)):
        # 죽은 원자는 pass
        if atoms[idx] == []:
            continue
        # 그 외 원자
        answer += atoms[idx][2]
    return answer

##################################################
N,M,K = map(int,input().split())
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
grid = [[[] for x in range(N)] for y in range(N)]
atoms = []
for i in range(M):
    x,y,m,s,d = map(int,input().split())
    atoms.append([x-1,y-1,m,s,d])
for i in range(K):
    move()
    synthesis()
answer = get_answer()
print(answer)