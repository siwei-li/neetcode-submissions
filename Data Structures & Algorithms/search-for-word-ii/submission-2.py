class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        m, n = len(board), len(board[0])
        in_word = [[0] * n for _ in range(m)]
        dirs = ((1,0),(-1,0),(0,1),(0,-1))

        def is_valid(x, y):
            return x >= 0 and y >= 0 and x < m and y < n and not in_word[x][y]

        # build a trie
        trie = {}
        for word in words:
            dic = trie
            for c in word:
                if not c in dic:
                    dic[c] = {}
                dic = dic[c]
            dic["$"] = word


        def dfs(i, j, dic):
            c = board[i][j]
            if c in dic:
                # print(i, j, c, dic[c])
                in_word[i][j] = 1
                if "$" in dic[c]:
                    ans.append(dic[c]["$"])
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if is_valid(x, y):
                        dfs(x, y, dic[c])
                in_word[i][j] = 0

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
            

        return list(set(ans))
