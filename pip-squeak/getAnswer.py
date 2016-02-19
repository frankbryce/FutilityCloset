from sys import argv
from functools import lru_cache

# returns the most likely total that will be obtained by throwing
# a fair die bearing the numbers 1,2,3,4,5,6 repeatedly until the
# running total first exceeds the positive integer n
@lru_cache(maxsize=256)
def getAnswer(n):
    opts = {}
    def addToOpts(i,p):
        if i not in opts:
            opts[i] = 0
        opts[i] += p
    for i in range(1,7): # 1,2,3,4,5,6
        if i>n: 
            addToOpts(i,1/6)
            continue
        subOpts = getAnswer(n-i)
        for subOpt in subOpts:
            addToOpts(i+subOpt, (1/6)*subOpts[subOpt])
    return opts

if __name__=="__main__":
    print(getAnswer(int(argv[1])))