

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        m = {}

        def dfs(node):
            m[node] = UndirectedGraphNode(node.label)
            for w in node.neighbors:
                if m.get(w, 0) == 0:
                    n = dfs(w)
                    m[node].neighbors.append(n)
                else:
                    m[node].neighbors.append(m.get(w))
            return m[node]

        if node is None:
            return None

        dfs(node)
        return m[node]

import collections

class Solution1:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        q = collections.deque()
        m = {}

        def bfs(node):
            m[node] = UndirectedGraphNode(node.label)
            q.append(node)

            while len(q):
                x = q.popleft()
                for w in x.neighbors:
                    if m.get(w, 0) == 0:
                        m[w] = UndirectedGraphNode(w.label)
                        q.append(w)
                    m[x].neighbors.append(m[w])

            return m[node]

        if node is None:
            return None

        bfs(node)
        return m[node]