'''
****************************SOME THEORY************************
IF NODE_INDEX = i:
        PARENT_NODE = i/2
        LEFT_CHILD  = 2*i
        RIGHT_CHILD = 2*i+1

IF NO OF NODES = N:
        LEAF NODES CAN BE ACCESED BY INDEXES:
        N/2+1,N/2+2.....N(LAST LEAF NODE)

1) INDEXING STARTS FROM 1 IN THE LIST;HENCE AT 0 INDEX WE HAVE 0
    TO DENTOE NULL PARENT OF ROOT

********************************************************************
'''


class Heap:

    def __init__(self,LIST,N):

        NewList = [0]+LIST #APPEND 0 IN THE BEGINNING TO DENOTE NULL PARENT OF ROOT

        self.N        = N
        self.heap  = NewList


    def MaxHeapify(self,i,N):

        left , right = 2*i ,  2*i+1 #GET LEFT AND RIGHT CHILD INDEX

        #SELECT LARGER CHILD INDEX AND PUT IN largest IF NOT THEN PUT index (i) IN largest
        #AND AGAIN RECURSIVELY CALL MaxHeapify WITH NOW index(i) = largest IF SWAP TAKES PLACE

        if left <= N and self.heap[left] > self.heap[i]:
            largest = left
        else:
            largest = i

        if right <= N and self.heap[largest]  < self.heap[right]:
            largest = right

        if largest != i:
            self.heap[i] , self.heap[largest] = self.heap[largest] , self.heap[i]
            self. MaxHeapify(largest,N)


    def BuildHeap(self):
        N = self.N
    #BUILD HEAP BY CALINNG MaxHeapify ON INTERNAL NODES
        for i in range (N/2,0,-1):
            self.MaxHeapify(i,N)

    def HeapSort(self):
    #FIRST BUILD HEAP
        self.BuildHeap()
        N              = self.N
        heap_size = N
    #NOW PUT SWAP ROOT WITH LAST LEAF AND DECREASE heap_size BY 1 AND CALL MaxHeapify ON ROOT
    #REAPEAT THE PROCEDURE
        for i in range (N,1,-1):
            self.heap[i] , self.heap[1] = self.heap[1] , self.heap[i]
            heap_size -= 1
            self.MaxHeapify(1,heap_size)

    def pprint(self):
        #TO PRINT SORTED ARRAY
        #WE START FROM 1 BEACUSE AT 1 WE HAVE NULL
        print "Sorted Array:"
        print self.heap[1:]



if __name__ == "__main__":
    '''
    L = [9,8,2,7,4,5]
    h = Heap(L,6)
    h.HeapSort()
    h.pprint()
    '''
    print "Enter elements"
    x = [int(x) for x in raw_input().split()]
    H = Heap(x,len(x))
    H.HeapSort()
    H.pprint()
