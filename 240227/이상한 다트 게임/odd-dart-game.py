def rotate(X,D,K):
    global dart
    for i in range(X-1,N,X):
        newdisk = [0 for _ in range(M)]
        for j in range(len(dart[i])):
            # 시계
            if D==0:
                newdisk[(j+K)%N] = dart[i][j]
            # 반시계
            else:
                newdisk[(j-K+N)%N] = dart[i][j]
        for j in range(len(dart[i])):
            dart[i][j] = newdisk[j]

def erase():
    global dart
    Erase,NotErase = 1,0
    isErase = [[NotErase for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if dart[i][j]==dart[i][(j-1+M)%M]:
                isErase[i][j] = Erase
                isErase[i][(j-1+M)%M] = Erase
            if i>0 and dart[i][j]==dart[i-1][j]:
                isErase[i][j] = Erase
                isErase[i-1][j] = Erase
    for i in range(N):
        for j in range(M):
            if isErase[i][j]==Erase:
                dart[i][j]=0
    return sum([sum(i) for i in isErase])

def normalization():
    global dart
    AVG = sum(dart)//(N*M)
    for i in range(N):
        for j in range(M):
            if dart[i][j] > AVG:
                dart[i][j] -= 1
            elif dart[i][j] < AVG:
                dart[i][j] += 1
def get_answer():
    print(sum([sum(i) for i in dart]))

####### MAIN #######
N,M,Q = map(int,input().split())
dart = [list(map(int,input().split())) for _ in range(N)]

for _ in range(Q):
    X,D,K = map(int, input().split())
    rotate(X,D,K)
if not erase():
    normalization()
get_answer()