import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
g = [list(map(int, inp().rstrip().split())) for _ in range(n)]

dist = [[0] * n for _ in range(n)]

for k in range(n):
	for i in range(n):
		for j in range(n):
			# if g[i][k] + g[k][j] !=0:
			if g[i][k] and g[k][j]:				
				dist[i][j] = 1

for i in range(n):
	print(' '.join(map(str, dist[i])))