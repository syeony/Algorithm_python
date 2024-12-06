def solution(info, edges):
    
    def dfs(current, sheep, wolf, visited, max_sheep): # ㅋㅋㅋ...
        if wolf >= sheep:
            return max_sheep

        max_sheep = max(max_sheep, sheep)

        for i in visited:
            for j in adj[i]:
                if j not in visited:
                    # 새로운 집합 생성 후 추가
                    visited2 = set(visited) # 복사
                    visited2.add(j) # 추가

                    if info[j] == 0: # 양
                        max_sheep = dfs(j, sheep + 1, wolf, visited2, max_sheep)
                    else: # 늑대
                        max_sheep = dfs(j, sheep, wolf + 1, visited2, max_sheep)
                        
        return max_sheep
            
    adj = [[] for _ in range(len(info))]

    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)

    answer=dfs(0,1,0,{0},0) #현재,양수,늑대수,{방문},최대양
    
    return answer