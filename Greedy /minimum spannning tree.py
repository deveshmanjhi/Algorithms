from weighted_graph_implement import *
from union_find import *
from priority_queue import *
from collections import defaultdict
import sys


class MinimumSpanningTree:

    def Krushkal(self,g,weighted_edge_list=[],N=0):
        '''
        weighted_edge_list = [(source,destination,cost),(source,destination,cost)]
        N                  = No of vertices
        sellf.edge_list    = [(source,destination,cost),(source,destination,cost)]
        '''
        node_list ,edge_list,minimum_tree = [],[],[]
        
        if len(weighted_edge_list) == 0:# if weighted edge list is not given;get edges from graph
            node_list,edge_list=self.get_edges(g)
            
            N = len(node_list)
        else:
            node_list = list(range(1,N+1))
            edge_list = weighted_edge_list
     
        uf = UnionFind()
        uf.make_set(node_list)
        edge_list.sort(key=lambda x:x[2])
        #print self.edge_list
        
    
        for edge in edge_list:
            
            root1 = uf.Find(edge[0])
            root2 = uf.Find(edge[1])
        
            if root1 != root2:
                uf.Union(edge[0],edge[1])
                minimum_tree.append(edge)
                
            if len(minimum_tree) == N-1:# your tree is complete now
                 break
                
        return minimum_tree  




    def Prims(self,g,src_node,weighted_edge_list=[],N=0):
        minimum_tree                = [] 
        node_list ,edge_list,parent,key = [],[],defaultdict(int),defaultdict(int)
        pq = priority_dict()
        if len(weighted_edge_list) == 0:
            node_list,edge_list=self.get_edges(g)
            
            N = len(node_list)
        else:
            node_list = list(range(1,N+1))
            edge_list = weighted_edge_list
        for node in node_list:
            parent[node] = None
            pq[node]   = sys.maxsize
            key[node]  = sys.maxsize
            
        pq[src_node] = 0
        
        while len(pq) !=0:
             node = pq.pop_smallest()
             for nbs in g.graph_dict[node]:
                 destination = nbs[0]
                 cost        = nbs[1]
                 if destination in pq and cost < pq[destination]:
                     parent[destination] = node
                     pq[destination]     = cost
                     key[destination]    = cost
        for node in parent:
            if parent[node]!=None:
                minimum_tree.append((node,parent[node],key[node]))
                 
        return minimum_tree




    def get_edges(self,g):
        node_list = g.graph_dict.keys()
        edge_list=[]
        for node in node_list:
            for edge in g.graph_dict[node]:
                source = node
                destination = edge[0]
                cost  = edge[1]
                edge_list.append((source,destination,cost))
            
        return (node_list,edge_list)



if __name__ == "__main__":
    connections = [("A","B",7),("B","C",8),("A","D",5),("B","D",9),("B","E",7),("C","E",5),("D","E",15),("D","F",6),("F","E",8),("E","G",9),("F","G",11)]
    g=Graph(connections,False,True)
    g.pprint()
    
    mst = MinimumSpanningTree()
    #print mst.Krushkal(g)
    print mst.Prims(g,"A")




















            
        
            
       
            
        
    
