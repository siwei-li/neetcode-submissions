class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_d = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for c, pre in prerequisites:
            in_d[c] += 1
            graph[pre].append(c)
        # print(in_d, graph)

        ans = []
        visited = set()
        def dfs(l):
            # if not l:
            #     return
            for c in l:
                if c in visited:
                    continue
                deg = in_d[c]
                if deg == 0:
                    ans.append(c)
                    visited.add(c)
                    for n in graph[c]:
                        in_d[n] -= 1
                    
                    dfs(graph[c])

        dfs([i for i in range(numCourses)])

        return ans if len(ans) == numCourses else []
        