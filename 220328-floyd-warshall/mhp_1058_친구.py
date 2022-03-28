# [입력]
import sys
INF = sys.maxsize
inp = sys.stdin.readline
n = int(inp().rstrip())
g = [list(inp().rstrip()) for _ in range(n)]

# [인접행렬 초기화]
for i in range(n):
	for j in range(n):
		if i==j:
			g[i][j] = 1
			continue
			
		g[i][j] = 1 if g[i][j]=='Y' else INF
		
# [인접행렬 업데이트 - 플로이드워셜]
for k in range(n):
	for i in range(n):
		for j in range(n):
            #if not g[i][j] and g[i][k] and g[k][j]:
			g[i][j] = min(g[i][k] + g[k][j], g[i][j])

# [유명한 사람 출력]
max_nfriend = 0
for i in range(n):
	li = [1 if 1<=j<=2 else 0 for j in g[i]]
	max_nfriend = max(sum(li)-1, max_nfriend)
		
print(max_nfriend)