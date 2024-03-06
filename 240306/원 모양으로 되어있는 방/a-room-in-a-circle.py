import sys
def get_distance(people_from_start):
    distance = 0
    for p in range(1,N):
        distance += p*people_from_start[p]
    return distance

N = int(input())
people = []
for i in range(N):
    people.append(int(input()))
answer = sys.maxsize
people_from_start = []
for i in range(N):
    people_from_start = people[i:]+people[:i]
    distance = get_distance(people_from_start)
    if distance < answer:
        answer = distance
print(answer)