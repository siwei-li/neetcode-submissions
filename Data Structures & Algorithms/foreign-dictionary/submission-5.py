class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges = defaultdict(set)
        nodes = set()
        nodes_in_edges = set()
        ans = []
        visited = set()

        if len(words) == 1:
            return "".join(set(words[0]))

        for w in words:
            for c in w:
                nodes.add(c)
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            l = min(len(w1), len(w2))

            for j in range(l):
                if w1[j] != w2[j]:
                    edges[w1[j]].add(w2[j])
                    break
                if j == l-1 and len(w2) < len(w1):
                    return ""

        # in_deg = 0 as sources
        in_degs = defaultdict(int)
        for p in edges.keys():
            for c in edges[p]:
                in_degs[c] += 1
            nodes_in_edges.add(p)
            nodes_in_edges.add(c)
        # print(edges)
        
        def dfs(s):
            if s in visited:
                return
            visited.add(s)
            ans.append(s)
            print(s, ans)

            for c in edges[s]:
                in_degs[c] -= 1
                if in_degs[c] == 0:
                    dfs(c)
        

        starts = set(edges.keys())
        for s in starts:
            if in_degs[s] == 0:
                print(s)
                dfs(s)

        for n in nodes:
            if not n in nodes_in_edges:
                ans.append(n)
        
        # print(edges, ans)
        if len(ans) != len(nodes):
            return ""

        return ''.join(ans)
            

        