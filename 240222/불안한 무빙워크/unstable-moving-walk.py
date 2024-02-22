# 내린 사람들 제거
def rearrage_people():
    global people
    new_people = []
    for p in people:
        if p != -1:
            new_people.append(p)
    people = new_people
def turn_clockwise():
    global first_point
    first_point = (first_point-1+2*N) % (2*N)
    # n번칸에 위치하면 내리기
    for i in range(len(people)):
        if people[i] == (first_point+(N-1)) % (2*N):
            people[i] = -1
    rearrage_people()

def move_people():
    global people,safety
    for i in range(len(people)):
        ni = (people[i]+1) % (2*N)
        # 이미 사람이 있는곳 or 안전성 0인곳
        if (ni in people) or (safety[ni]==0):
            continue
        # 이동
        people[i] = ni
        # 이동으로 인한 안정성 감소
        safety[ni] -= 1
        # n번칸에 위치하면 내리기
        if ni == (first_point+(N-1))%(2*N):
            people[i] = -1
    rearrage_people()

def add_person():
    global people, safety
    if (first_point not in people) and (safety[first_point] != 0):
        people.append(first_point)
        safety[first_point] -= 1

def isNotOK():
    num = 0
    for s in safety:
        if s == 0:
            num += 1
    if num >= K:
        return True
    return False

############### MAIN ###################
N,K = map(int,input().split())
safety = list(map(int,input().split()))
people = []
first_point = 0
answer = 0

while True:
    answer += 1
    turn_clockwise()
    move_people()
    add_person()
    if isNotOK():
        break

print(answer)