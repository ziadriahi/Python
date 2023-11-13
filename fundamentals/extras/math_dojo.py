class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        i=0
        res=0
        somme=0
        self.result += num
        for i in range (len(nums)) :
            var = nums[i]
            res = tuple([self.result]) + var
            #print()
        for i in res :
            somme += i
        
        self.result = somme
    
    def subtract(self, num, *nums):
        i=0
        res=0
        somme=0
        self.result -= num
        for i in range (len(nums)) :
            var = nums[i]
            res = tuple([self.result]) + var
            #print()
        for i in res :
            somme -= i
        
        self.result = somme

md = MathDojo()
md.add(2,(3,4,5))
print(md.result)
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

