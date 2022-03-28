import sys
INF = sys.maxsize
inp = sys.stdin.readline

n, m = map(int, inp().rstrip().split())

dist = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
	dist[i][i] = 0
	
for _ in range(m):
	a, b = map(int, inp().rstrip().split())
	dist[a][b] = 1
	dist[b][a] = 1

for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

min_node = INF
least = INF

for i in range(1, n+1):
	# if sum(dist[i]) < least:
		# least = sum(dist[i])
	if sum(dist[i][1:]) < least:
		least = sum(dist[i][1:])
		min_node = i
		
print(min_node)