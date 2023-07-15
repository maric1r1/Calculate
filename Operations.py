class Operation:
    number = 0

    def __init__(self,*arg):
        self.number = arg[0]
    
    def sum(self):
       s = 0
       for i in range(len(self.number)):
            s += int(self.number[i])
       return s
    
    def dim(self):
        s = 0
        for i in range(len(self.number)):
            if i == 0:
                s = int(self.number[i])
            else:
                s -= int(self.number[i])
        return s
    
    def mult(self):
        s = 1
        for i in range(len(self.number)):
            s *= int(self.number[i])
        return s
    
    def div(self):
        return int(self.number[0])/int(self.number[1])

