from collections import defaultdict
import sys

class Graph:

    def __init__(self, connections=[], directed=False):
        self.graph_dict       = defaultdict(list)
        self.is_directed      = directed
        self.Add_Connections(connections)
        #N = no of nodes in graph
        self.N                = len(self.graph_dict.keys())
        self.dmat             = defaultdict(dict)
        self.path             = defaultdict(dict)
        self.Find_Distance_Matrix()
        self.Find_Path_Matrix()
    
        #print self.path

    def Add_Connections(self,connections):
        if self.is_directed:         
           for source , destination , cost in connections:
                self.graph_dict[source].append((destination,cost))
                self.graph_dict[destination]
    
        else:
           for source , destination , cost in connections:
           
                self.graph_dict[source].append((destination,cost))
                self.graph_dict[destination].append((source,cost))


    def Find_Distance_Matrix(self):
        mat = self.dmat
        for key,value in self.graph_dict.iteritems():
            mat[key][key] = 0
            for items in value:
                mat[key][items[0]] =  items[1]

        
        for keyi in self.graph_dict.keys():
            for keyj in self.graph_dict.keys():
                try:
                    x = mat[keyi][keyj]
                except:
                    mat[keyi][keyj] = sys.maxint
                
        
    def Find_Path_Matrix(self):
        mat  = self.dmat
        path = self.path
        for keyi in self.graph_dict.keys():
            for keyj in self.graph_dict.keys():
                if mat[keyi][keyj] == sys.maxint or mat[keyi][keyj] == 0:
                    path[keyi][keyj] = -1
                else:
                    path[keyi][keyj] = keyi
        
        
            
        
        
    def PrintMatrix(self,name=""):
        if name == "path":
            mat = self.path
            print "PATH MATRIX"
        else:
            print "DISTANCE MATRIX"
            mat = self.dmat

        L1 =  self.graph_dict.keys()
        L1.sort()
        for keyi in L1:
           for keyj in L1:
               print mat[keyi][keyj],
           print ""

                
    def pprint(self):
        for key,value in self.graph_dict.iteritems():
            print str(key)+":"+str(value)



    def Floyd_Warshall(self):
        N    = self.N
        mat  = self.dmat
        path = self.path
        L    = self.graph_dict.keys()
        L.sort()
        for K in L:
            for I in L:
                for J in L:
                    #I,J,K = str(i),str(j),str(k)
                    if mat[I][J] > mat[I][K]+mat[K][J]:
                        mat[I][J]= mat[I][K]+mat[K][J]
                        path[I][J] = path[K][J]

        
    def Find_Path(self,i,j):
        L = []
        path = self.path
        L.append(j)
        while(True):
            j = path[i][j]
            L.append(j)

            if j==i:
                break
            if j==-1:
                print "NO POSSIBLE PATH"
                return

        L.reverse()
        return L
        
            
        
            



if __name__ =="__main__":
    connections = [('0', '3',15), ('0', '1',3), ('0', '2',6),('1', '2',-2), ('2', '3',2), ('3', '0',1)]
    #connections = [('A', 'B',10), ('B', 'C',5), ('B', 'E',10),('B', 'D',5), ('A', 'D',5), ('D', 'E',20)]
    g = Graph(connections,True)
    #g.pprint()
    g.Floyd_Warshall()
    #print g.dmat
    #print g.path
    g.PrintMatrix("path")
    print g.Find_Path('0','3')
         
