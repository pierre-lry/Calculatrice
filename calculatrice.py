import math
def fibonacci(seuil, list = [1,2]) :
    while list[-1] <= seuil :
        list.append(list[-2] + list[-1])
    return set(list)
class calculatrice:
    def __init__(self):
        self.memory = None
    def addition(self,n1,n2):
        self.memory = n1 + n2
        return self.memory
    def multiplication(self,n1,n2,result=0):
        if (n1>0 and n2>0) or (n1<0 and n2<0):
            for _ in range(abs(n1)) :
                result += abs(n2)
        else:
            for _ in range(abs(n1)) :
                result -= abs(n2)
        self.memory = result
        return self.memory
    def soustraction(self,n1,n2):
        self.memory = n1 - n2
        return self.memory
    def division(self,n1,n2,q=0,r1=0,r2=0,r3=0):
        result0 = abs(n1)
        while result0 > abs(n2):
            result0 -= abs(n2)
            q += 1
        result1 = result0*10
        while result1 > abs(n2):
            result1 -= abs(n2)
            r1 += 1
        result2 = result1*10
        while result2 > abs(n2):
            result2 -= abs(n2)
            r2+= 1
        result3 = result2*10
        while result3 > abs(n2):
            result3 -= abs(n2)
            r3 += 1
        if n1*n2 > 0 :
            self.memory = float(f"{q}.{r1}{r2}{r3}")
        else:
            self.memory = float(f"-{q}.{r1}{r2}{r3}")
        return self.memory
    def reset(self):
        self.memory = 0
        return self.memory
    def total(self):
        return self.memory
    def exponentielle(self,n1,n2=0,somme=0): # on va procéder en utilisant le D.L de exp(x)
        for n in range(1000) :
            if n!=0:
                somme+=(n1**n)/math.factorial(n)
            else:
                somme +=1
        return somme
    def fibonacci(self,n1):
        if n1 in fibonacci(n1):
            return True
        return False
    def premier(self,n1):
        for nb in range(2,n1):
            if n1%nb == 0 :
                return False
        if n1 < 2 :
            return False
        return True
