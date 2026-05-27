class WordDictionary:

    def __init__(self):
        self.d = defaultdict(dict)
        

    def addWord(self, word: str) -> None:
        node = self.d
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["$"] = word


    def search(self, word: str) -> bool:
        node = self.d
        # print(word, node)
        for i, c in enumerate(word):
            stored_node = node
            if c == '.':
                res = False
                for contained_letter in node:
                    res = res or self.search(word[:i] + contained_letter + word[i + 1:]) 
                if res: return True
            elif c not in node:
                return False
            else:
                node = node[c]
                if "$" in node and node["$"] == word:
                    return True
        return False
        
