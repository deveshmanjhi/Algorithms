'''
*****************PRIORITY QUEUE********************
1) LIST INDEX STARTS FROM 1
2)BEFORE INSERTING ANY ELEMENT IN THE LIST MAKE SURE TO PUT [0,0] AT INDEX 0
3)SUPPLY THE DICTIONARY WHICH HASHES KEYS WITH INDEXES IN THE LIST
4)list example = [ [0,0],[key1,priority1],[key2,priority2],[key3,priority3] ]
'''



from collections import defaultdict
class PriorityQueue:

    def __init__(self,L=[(0,0)],dicti=defaultdict(int)):
        self.dicti  = dicti
        self.queue  = L
        self.length = len(L)-1
        if len(L)>1:
            self.build_heap()

    def build_heap(self):
        N = self.length
        for i in range(N/2,0,-1):
            self.heapify(i,N)
 

    def heapify(self,ind,N):
        arr   = self.queue
        left  = 2*ind       #left child
        right = 2*ind + 1   #right child

        if left <= N and arr[left][1] > arr[ind][1]:
            largest = left
        else:
            largest = ind

        if right <= N and arr[right][1] > arr[largest][1]:
            largest = right

        if (largest != ind):
            key_ind                 = arr[ind][0]
            key_largest             = arr[largest][0]
            self.dicti[key_ind]     = largest
            self.dicti[key_largest]  = ind
            arr[ind],arr[largest]   = arr[largest],arr[ind]  # swap both
            
            self.heapify(largest,N)

    def front(self):
        return self.queue[1]

    def dequeue(self):
        arr = self.queue 
        if self.length==0:
            return None
        N = self.length
        result = arr[1]
        self.dicti.pop(result[0])
        arr[1]  = arr[N]
        self.length -=1
        arr.pop()
        self.heapify(1,self.length)
        return result
        
        

    def increase_key(self,key,value):
        arr = self.queue
        ind = dicti[key]
        if (value < arr[ind][1]):
            return None

        arr[ind][1] = value
                                                 
        while (ind > 1 and arr[ind][1]> arr[ind/2][1]):
            key_child   = arr[ind][0]
            key_parent  = arr[ind/2][0]
            self.dicti[key_child] = ind/2
            self.dicti[key_parent]= ind
            arr[ind],arr[ind/2] = arr[ind/2],arr[ind]
            ind = ind/2

    def insert(self,value):
        arr           = self.queue
        length        = self.length
        length        += 1
        self.length   +=1
        self.dicti[value[0]] = self.length
        arr.append(value)
        
        ind = length
        while (ind > 1 and arr[ind][1]> arr[ind/2][1]):
            key_child             = arr[ind][0]
            key_parent            = arr[ind/2][0]
            self.dicti[key_child] = ind/2
            self.dicti[key_parent]= ind
            arr[ind],arr[ind/2]   = arr[ind/2],arr[ind]
            ind = ind/2

    def pprint(self):
        print self.queue[1:self.length+1]
        

if __name__=="__main__":
        l    = [[0,0],["A",1],["B",2],["C",3],["D",4],["E",5],["F",6],["G",7]]
        dicti = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7}
        p = PriorityQueue(l,dicti)
   
        p.increase_key("A",50)
        p.pprint()
        print p.dicti

        
        '''
        p.dequeue()
        p.dequeue()
        
        
        
       
        p.insert(("H",8))
        p.insert(("I",9))
        p.pprint()
        print p.dicti
    
        print p.dequeue()
        print p.dequeue()
        print p.dequeue()
        print p.dequeue()
        print p.dequeue()
        p.pprint()
        print p.length
        '''


        




                            
                                        













         
                                                 
                    


                                                 
        
                                                 

                                                 
        
