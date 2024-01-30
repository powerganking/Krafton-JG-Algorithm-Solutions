'''
2098 외판원
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.
1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다) 
이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.
각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다.
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 비용은 대칭적이지 않다.
즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다.
W[i][i]는 항상 0이다. 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.
N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

입력
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0

출력
35

'''

import sys
N = int(input())
world = []
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))

dp = {}


def DFS(now, visited):
    # 모든 도시를 방문한 경우
    if visited == (1 << N) - 1:
        # 다시 출발 도시로 갈 수 있는 경우 출발 도시까지의 비용 반환
        if world[now][0]:
            return world[now][0]
        else:
            # 갈 수 없는 경우 무한대 반환 (이 경로가 최소비용으로 채택되지 않게)
            return int(1e9)

    # 이전에 계산된 경우 결과 반환
    if (now, visited) in dp:
        return dp[(now, visited)] # now까지 방문한 최소 비용

    min_cost = int(1e9)
    for next in range(1, N):
        # 비용이 0이어서 갈 수 없거나, 이미 방문한 루트면 무시
        if world[now][next] == 0 or visited & (1 << next):
            continue
        cost = DFS(next, visited | (1 << next)) + world[now][next]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost  # 현재도시까지 방문한 경우 중에서 최소 비용이 드는 루트의 비용 저장
    return min_cost  # 현재도시까지 방문하는 비용 리턴


print(DFS(0, 1))  # now: 0번째 도시부터 방문, visited: 0번째 도시 방문 처리