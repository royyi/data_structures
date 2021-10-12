# Roy Yi
# 9/22/21
# Implement trie data structure

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        '''insert a word into the trie'''
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node['$'] = '' 

    def dfs(self, node, word, res):
        if '$' in node:
            res.append(word)

        for c in node:
            if c != '$':
                self.dfs(node[c], word+c, res)

    def search(self, query):
        '''returns list of all matches inside trie'''
        node = self.root
        for c in query:
            if c in node:
                node = node[c]
            else:
                return []

        res = []
        self.dfs(node, query, res) 
        return res

def main():
    t = Trie()

    for word in ['ada', 'ann', 'andy', 'amanda', 'bill', 'bob', 'can', 'canada']:
        t.insert(word)

    print(t.search("an"))

if __name__ == "__main__":
    main()
