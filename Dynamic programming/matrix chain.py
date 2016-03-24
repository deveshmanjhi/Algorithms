import sys


class MatrixChain:

    def __init__(self,L = []):
          
        self.Lis    = L
        self.N      = len(L)
    
        '''
        For simplicity of the program, 
        one extra row and one extra column are allocated in M[][].  
        0th row and 0th column of M[][] are not used
        self.M      = cost matrix where M[i][j] denotes cost of multiplying matrix from i to j
        self.F      = Factor matrix to store k values for i,j pair
        self.P      = A list to store dimensions denoted P[0],P[1]...P[n],where P[0]..P[n-1] store no of rows in Ai...An-1 and P[n] store An matrix column
        self.ans    = will have matrix multiplication expression of Ai's with brackets
        self.mults  = will have least required multiplications
        '''
      
        self.M      = [[-1]*(self.N+1) for x in range(self.N+1)]
        self.F      = [[-1]*(self.N+1) for x in range(self.N+1)]
        self.P      = [-1]*(self.N+1)

      
        self.ans    = ""
        self.mults  = 0
        self.CalculateP()
        self.FillMatrix()


    def CalculateP(self):
        '''
        Fill in the P list
        In loop fill P[0]..P[n-1] with the no of rows in Ai
        Then using separate statement fill P[n] with column of An
        '''
        for i in range(self.N):
            self.P[i] = self.Lis[i][0]

        
        self.P[-1]    = self.Lis[-1][1] 


    def FillMatrix(self):
        N = self.N
        M = self.M
        P = self.P
        F = self.F
        for size in range (N):
            for i in range(1,N - size+1):
                j = i+size
                if i==j:
                    M[i][j] = 0
                else:
                    minvalue = sys.maxint
                    mink     = -1
                    for k in range(i,j):
                        '''
                        compute cost of Multiplying chain Ai to Aj and select k for which cost is minimum
                        '''
                        cost = M[i][k]+M[k+1][j]+P[i-1]*P[k]*P[j]
                        if cost < minvalue:
                            minvalue = cost
                            mink     = k

                    M[i][j] = minvalue
                    F[i][j] = mink

        self.mults = M[1][N]
        l          = []
        self.PutBrackets(1,self.N,l)
        self.ans =  "".join(l)
       
                            
                        
    def PutBrackets(self,i,j,l):
        if i==j:
            l.append("A"+str(i))
        else:
             k = self.F[i][j]
             l.append("(")
             self.PutBrackets(i,k,l)
             l.append("*")
             self.PutBrackets(k+1,j,l)
             l.append(")")
        

    def PrintMatrix(self):
        
        for i in range(1,self.N+1):
            print self.M[i][1:]

        for i in range(1,self.N+1):
            print self.F[i][1:]
        
        
        






if __name__ == "__main__":

    lis1 = [(4,10),(10,3),(3,12),(12,20),(20,7)]
    lis2 = [(40,20),(20,30),(30,10),(10,30)]
    lis3 = [(10,20),(20,30)]

    mx = MatrixChain(lis1)
    print mx.PrintMatrix()
    print mx.mults
    print mx.ans
    
    
        
