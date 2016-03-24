
def BinaryInt(x):
    return int(x,2)

def IntBinary(x):
    return '{0:b}'.format(x)

def Adjust(x,y):
    sA = '{0:b}'.format(x)
    sB = '{0:b}'.format(y)
    if len(sA) == 1 and len(sB)==1:
        return [sA,sB]
    else:
        length = max(len(sA),len(sB))
        if length == 2:
            sA = '{0:02b}'.format(x)
            sB = '{0:02b}'.format(y)
            return [sA,sB]
        if length == 3 or length ==4 :
            sA = '{0:04b}'.format(x)
            sB = '{0:04b}'.format(y)
            return [sA,sB]
        if length > 4 and length < 9:
            sA = '{0:08b}'.format(x)
            sB = '{0:08b}'.format(y)
            return [sA,sB]
        if length >=9:
            sA = '{0:016b}'.format(x)
            sB = '{0:016b}'.format(y)
            return [sA,sB]
            
            
        
    



def mult(A,B):
    if len(A) == 1:
        return int(A[0])*int(B[0])
    else:
        mid = len(A)//2
        p,q,r,s = A[0:mid],A[mid:],B[0:mid],B[mid:]
        pr = mult(p,r)
        ps = mult(p,s)
        qr = mult(q,r)
        qs = mult(q,s)

        sums = ps+qr

        n    = len(A)

        ans = (pr << n) + ( sums << n//2 ) + qs

        return ans



        

def FastMult(A,B):
 
    
    if len(A) == 1:
        return int(A[0])*int(B[0])
    else:
        mid = len(A)//2
        p,q,r,s = A[0:mid],A[mid:],B[0:mid],B[mid:]
        
        sumA  =  BinaryInt(p)+BinaryInt(q)
        sumB  =  BinaryInt(r)+BinaryInt(s)
        
        sumA,sumB = Adjust(sumA,sumB)
        pr    =  FastMult(p,r)
        qs    =  FastMult(q,s)
        prod  =  FastMult(sumA,sumB)

        sums  =  prod - pr - qs
        n     =  len(A)
        ans   = (pr << n) + (sums << n//2) +qs
        return ans
        
        
print mult('1010','1010')
print FastMult('1010','1010')
        
        
    
