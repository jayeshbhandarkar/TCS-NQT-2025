from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(10000)

def solve_max_towers():
    T = int(input())
    
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        graph = defaultdict(list)
        for _ in range(N - 1):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * N
        result = [0]
        
        def dfs(u, crystals, restored, curr_A):
            if restored[u]:
                return 0
            cost = curr_A[u]
            if crystals < cost:
                return 0
            
            crystals -= cost
            restored[u] = True
            result[0] += 1
            
            for v in graph[u]:
                if not restored[v]:
                    curr_A[v] = max(0, curr_A[v] - B[u])
            
            neighbors = sorted([v for v in graph[u] if not restored[v]], key=lambda x: curr_A[x])
            for v in neighbors:
                dfs(v, crystals, restored, curr_A)
        
        max_restored = 0
        for start in range(N):
            restored = [False] * N
            curr_A = A[:]
            result = [0]
            dfs(start, K, restored, curr_A)
            max_restored = max(max_restored, result[0])
        
        print(max_restored)

solve_max_towers()
