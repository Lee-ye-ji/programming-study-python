# [입력]
import sys
inp = sys.stdin.readline
t = int(inp().rstrip())

for _ in range(t):
	n = int(inp().rstrip())
	locs = []
	for _ in range(n+2):
		x, y = map(int, inp().rstrip().split())
		locs.append((x, y))
		
	# [인접행렬 초기화]
	g = [[0]*(n+2) for _ in range(n+2)]

	for i in range(n+2):
		g[i][i] = 1

	# [인접행렬 업데이트1 - 직행 도달 가능여부]
	for i in range(n+2):
		for j in range(n+2):
			dist = abs(locs[i][0] - locs[j][0]) + abs(locs[i][1] - locs[j][1])
			g[i][j] = 1 if dist<=1000 else 0
			
	# [인접행렬 업데이트2 - 거쳐서 도달 가능여부]
	for k in range(n+2):
		for i in range(n+2):
			for j in range(n+2):
				if not g[i][j] and g[i][k] and g[k][j]:
					g[i][j] = 1
					
	# [집-락페 가능여부 출력]
	print("happy" if g[0][n+1] else "sad")