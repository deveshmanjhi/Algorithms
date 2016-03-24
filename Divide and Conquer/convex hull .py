import sys
import matplotlib.pyplot as plt
class ConvexHull:

    def __init__(self,S = []):
        self.Points     = S
        self.ConvexHull = []
        self.QuickHull()
        self.Plot()


    def QuickHull(self):
        points = self.Points
        points.sort()
        A = points[0]
        B = points[-1]
        self.ConvexHull.append(A)
        self.ConvexHull.append(B)
        remaining_points = points[1:-1]
        S1,S2 = [],[]
        self.GetSubsets(A,B,S1,S2,remaining_points)
        #print "A = ",A
        #print "B = ",B
        #print S1
        #print S2
        self.FindHull(S1,A,B)
        self.FindHull(S2,B,A)
        
        

    def GetSubsets(self,A,B,S1,S2,remaining_points):
        ax,bx,ay,by = A[0],B[0],A[1],B[1]
        
        for point in remaining_points:
            cx,cy  = point[0],point[1] 
            if   ((bx - ax)*(cy - ay) - (by - ay)*(cx - ax)) > 0:
                S1.append(point)
            elif ((bx - ax)*(cy - ay) - (by - ay)*(cx - ax)) < 0:
                S2.append(point)



    def FindHull(self,Sk,P,Q):
        if len(Sk) == 0:
            return

        MinArea = -1*sys.maxint
        C       = 0
        for point in Sk:
            area  = self.ComputeArea(P,Q,point)
            if area > MinArea:
                C       = point
                MinArea = area
                
        self.ConvexHull.append(C)
        S1 ,S2 = [],[]
        #print "point c is ",C
        
        ax,bx,ay,by = P[0],C[0],P[1],C[1]
        for point in Sk:
            if point != C:
                cx,cy  = point[0],point[1]
                if   ((bx - ax)*(cy - ay) - (by - ay)*(cx - ax)) > 0:
                      S1.append(point)
        #print "s1 is",S1
        
                      
        ax,bx,ay,by = C[0],Q[0],C[1],Q[1]
        
        for point in Sk:
            if point != C:
                cx,cy  = point[0],point[1]
                if   ((bx - ax)*(cy - ay) - (by - ay)*(cx - ax)) > 0:
                      S2.append(point)
        #print "s2 is ",S2

        self.FindHull(S1, P, C)
        self.FindHull(S2, C, Q)
                
      
    def ComputeArea(self,P,Q,point):
        x_a,x_b,y_a,y_b,x_p,y_p = P[0],Q[0],P[1],Q[1],point[0],point[1]
        return (0.5)* abs((x_a - x_p) * (y_b-y_a) - (x_a - x_b)* (y_p - y_a))
            
        
    def Plot(self):
        points = self.ConvexHull
        points.sort()
        A,B = points[0],points[-1]
        remaining_points = points[1:-1]
        S1,S2 = [],[]
        self.GetSubsets(A,B,S1,S2,remaining_points)
        S1.sort()
        S2.sort()
        first  = [A]+S1+[B]
        second = [A]+S2+[B]
    
        px = map(lambda x:x[0],self.Points)
        py = map(lambda x:x[1],self.Points)
        plt.scatter(px, py)

        
        ans_x = map(lambda x:x[0],first)
        ans_y = map(lambda x:x[1],first)
        plt.plot(ans_x, ans_y, 'r-',markersize=10)
        ans_x = map(lambda x:x[0],second)
        ans_y = map(lambda x:x[1],second)
        plt.plot(ans_x, ans_y, 'r-',markersize=10)
        
        plt.show()
   
                
                
            
   
   
        
        
        
        
if __name__ == "__main__":

    points = [(5,0),(-5,0),(-4,3),(2,4),(-1,1),(4,3),(-2,-3),(2,-2),(4,-5)]
    #points  = [(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)]
    cvx = ConvexHull(points)
    print cvx.ConvexHull
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
