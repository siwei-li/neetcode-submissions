class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def diff_one(a, b):
            assert len(a) == len(b)

            cnt = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    cnt += 1

            return cnt == len(a) - 1
        
        q = deque()
        level = 1
        visited = [0] * len(wordList)

        for i, w in enumerate(wordList):
            if w == endWord:
                q.append(i)
        

        while q:
            # print(q)
            nq = []
            for i in q:
                w = wordList[i]
                visited[i] = 1
                if diff_one(w, beginWord):
                    return level + 1
                
                for ni, nw in enumerate(wordList):
                    if visited[ni]:
                        continue
                    if diff_one(nw, w):
                        nq.append(ni)

            if not nq:
                break
            level += 1
            q = nq

        return 0