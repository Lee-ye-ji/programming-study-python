# [입력]
import sys
inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
g = [list(map(int, inp().rstrip().split())) for _ in range(n)]

# [인접행렬 생성]
infos = []
for _ in range(m):
	a, b, c = map(int, inp().rstrip().split())
	infos.append((a,b,c))

# [인접행렬 업데이트] - 거쳐서 가는 최소거리
for k in range(n):
	for i in range(n):
		for j in range(n):
			g[i][j] = min(g[i][j], g[i][k] + g[k][j])

# [결과 출력]
for i in range(m):
	a, b, c = infos[i]
	print("Enjoy other party" if g[a-1][b-1] <= c else "Stay here")