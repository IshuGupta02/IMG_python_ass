class matrix:
    def __init__(self, values):
        self.values=values

    def __add__(self, other): 
        
        if len(self.values)!=len(other.values):
            raise ValueError('Dimensions of the matices are different!')
        # ans=[[None]*len((self.values)[1])]*len(self.values)
        ans=[[0 for l in range(len((self.values)[1]))]for m in range(len(self.values))]

        p=0
        for i in self.values:
            if len(i)!=len((other.values)[p]):
                raise ValueError('Dimensions of the matices are different!')
            # j=(other.values)[p]
            t=0
            for k in i:
                ans[p][t]=k+(other.values)[p][t]
                t=t+1
            p=p+1
        return matrix(ans)


    def __sub__(self, other):
        if len(self.values)!=len(other.values):
            raise ValueError('Dimensions of the matices are different!')
        ans=[[None for l in range(len((self.values)[1]))]for m in range(len(self.values))]

        p=0
        for i in self.values:
            if len(i)!=len((other.values)[p]):
                raise ValueError('Dimensions of the matices are different!')
            # j=(other.values)[p]
            t=0
            for k in i:
                ans[p][t]=k-(other.values)[p][t]
                t=t+1
            p=p+1
        return matrix(ans)

    def __mul__(self, other):
        k= len(other.values)
        ans=[[None for l in range(len((self.values)[1]))]for m in range(len(self.values))]
        
        i=0
        for p in self.values:
            if len(p)!=k:
                raise ValueError('Dimensions of the matices are not appropriate!')
            x=0
            while x<len(other.values[1]):
                s=0
                sum=0
                while s<k:
                    sum=sum+p[s]*other.values[s][x]
                    s=s+1
                ans[i][x]=sum
                x=x+1
            i=i+1

        return matrix(ans)

    def getcofactor(self,m, i, j):
        return matrix([row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])])
 
    def __abs__(self):

        if(len(self.values)!=len(self.values[0])):
            raise ValueError('This is not a square matrix!')
    
        if(len(self.values) == 2):
            value = self.values[0][0] * self.values[1][1] - self.values[1][0] * self.values[0][1]
            return value
    
        Sum = 0

        for current_column in range(len(self.values)):
    
            sign = (-1) ** (current_column)
    
            sub_det = abs(self.getcofactor(self.values, 0, current_column))
    
            Sum += (sign * self.values[0][current_column] * sub_det)
    
        return Sum


    def __pow__(self, other):
        if len(self.values)!=len(self.values[1]):
            raise ValueError('power can only be calculated for square matrices!')

        a=matrix([[0 for l in range(len(self.values))]for m in range(len(self.values))])

        i=0
        while i<len(self.values):
          
            a.values[i][i]=1
            i=i+1

        if other==0:
            return a

        b=self

        complete=1

        while complete<other:
            a=self
            times=1

            while times*2<=(other-complete):
                a=a*a
                times=times*2

            complete=complete+times
            b=b*a

        return b