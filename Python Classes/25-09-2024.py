import time as t
def testFn():
    pass
startTime=t.time()
testFn()
endTime=t.time()
runTimeInSec=endTime-startTime
print(f"\nTime to execute function is {runTimeInSec/60}min")



def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == "__main__":