from collections import defaultdict

class Graph():

    def __init__(self, connections=[], directed=False,weighted=False):
        self.status_dict      = defaultdict(lambda : 1)
        self.graph_dict       = defaultdict(list)
        self.is_directed      = directed
        self.level_node       = defaultdict(lambda : 0)
        if weighted:
            self.add_connections(connections)#USE FOR WEIGHTED GRAPH
            
        
        '''   
        connections             : a list of tuples conatining edges:example below:
        weighted_connections    : [('A', 'B',4), ('B', 'C',10]
        directed                : set to true for a directed and false for undirected
        '''
    
    
    def add_connections(self,connections):
        if self.is_directed:         
           for source , destination , cost in connections:
                self.graph_dict[source].append((destination,cost))
                self.graph_dict[destination]
                self.status_dict[source]
                self.status_dict[destination]
                
        else:
           for source , destination , cost in connections:
           
                self.graph_dict[source].append((destination,cost))
                self.graph_dict[destination].append((source,cost))
                self.status_dict[source]
                self.status_dict[destination]

    def add_edge(self,node1, node2):
       
        self.graph_dict[node1].append(node2)
            
        if not self.is_directed:
            self.graph_dict[node2].append(node1)
                
      
    
    def add_vertex(self,node):
        self.graph_dict[node]
        self.status_dict[node]



    def is_connected(self,node1,node2):
        """ Is node1 directly connected to node2"""
        return  node1 in self.graph_dict and node2 in self.graph_dict[node1]

    def remove_node(self,node):
        
        for key,value in self.graph_dict.iteritems():
            try:
                value.remove(node)
            except:
                pass
        self.graph_dict.pop(node,None)
        self.status_dict.pop(node,None)
        '''If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised'''
            
        
    def remove_edge(self,node1,node2):
        try :
            self.graph_dict[node1].remove(node2)
        except:
            pass
    def pprint(self):
        for key,value in self.graph_dict.iteritems():
            print str(key)+":"+str(value)

if __name__ == "__main__":
    
        connections = [('A', 'B',0), ('B', 'C',0), ('B', 'D',0),('C', 'D',0), ('F', 'E',0), ('F', 'C',0)]

        g = Graph(connections,False,True)
        print g.status_dict
        g.pprint()
