from collections import defaultdict
class UnionFind:

    def __init__(self):
        self.parents = defaultdict(int)
        self.ranks   = defaultdict(int)

    def make_set(self,node_list):
        for node in node_list:
            self.parents[node] = node
            self.ranks[node]   = 0
            
    def Union(self,node1,node2):
        node1_root = self.Find(node1)
        node2_root = self.Find(node2)

        if node1_root == node2_root:
             return

        if self.ranks[node1_root] < self.ranks[node2_root]:
             self.parents[node1_root] = node2_root

        elif self.ranks[node1_root] > self.ranks[node2_root]:
             self.parents[node2_root] = node1_root

        else:
            self.parents[node2_root] = node1_root
            self.ranks[node1_root]   += 1
            
    def Find(self,node):
        if self.parents[node] != node:
            self.parents[node] = self.Find(self.parents[node])    
        return self.parents[node]


    
        
            
if __name__ == "__main__":
    L=list(range(6))
    X=UnionFind()
    X.make_set(L)
    X.Union(1,0)
    X.Union(0,2)
    X.Union(3,4)
    X.Union(1,4)
    
    print X.parents
    print X.ranks

    print X.Find(4)
    print X.parents
