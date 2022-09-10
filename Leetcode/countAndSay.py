class Count:

    def __init__(self):
        self.hmap = {}
    
    def countAndSay(self, n: int) -> str:
        res = "1"
        
        while n > 1:
            temp, number, count = "", res[0], 0
            
            for x in res:
                if x == number:
                    count += 1
                    
                else:
                    temp += str(count)
                    temp += number
                    number = x
                    count = 1
            
            
            # base
            temp += str(count)
            temp += number
            
            n -= 1
            
            res = temp
            
        return res
    
    
    def makeHmap(self):
        for x in range(1, 31):
            self.hmap[x] = self.countAndSay(x)
            

myCount = Count()

myCount.makeHmap()

print(myCount.hmap)
        
    