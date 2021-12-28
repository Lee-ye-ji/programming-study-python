import sys
from collections import deque

# bfs
def bfs(q, res, r, c):
    dr =  [1,-1,0,0]
    dc =  [0,0,1,-1]
    q = deque(q)
    while q:
        i, j = q.popleft()
        res[i][j]='.'
        for k in range(4):
            ni = i+dr[k]
            nj = j+dc[k]
            if 0<=ni<r and 0<=nj<c:
                res[ni][nj]='.'
    return res

def get_locs(arr, r, c):
    # 위치 저장
    q = []
    for i in range(r):
        for j in range(c):
            if arr[i][j]=='O':
                q.append((i,j))
    return q

def print_result(arr):
    for i in range(len(arr)):
        print(''.join(arr[i]))

def main():
    inp = sys.stdin.readline
    r, c, n = map(int, inp().rstrip().split())
    arr = [inp().rstrip() for _ in range(r)]
    res = [['O']*c for _ in range(r)]

    if n==1:
        print_result(arr)
        return
    if not n%2:
        print_result(res)
        return

    q = get_locs(arr, r, c)
    res = bfs(q, res, r, c)
    q = get_locs(res, r, c)

    if n%4==1 and q:
        print_result(arr)
        return
    
    print_result(res)

main()