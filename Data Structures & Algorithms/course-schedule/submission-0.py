class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans = []

        q = deque()
        in_d = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for c, pre in prerequisites:
            in_d[c] += 1
            graph[pre].append(c)

        for i, deg in enumerate(in_d):
            if deg == 0:
                q.append(i)
                ans.append(i)
        
        while q:
            c = q.popleft()
            for n in graph[c]:
                in_d[n] -= 1
                if in_d[n] == 0:
                    q.append(n)
                    ans.append(n)



        return len(ans) == numCourses