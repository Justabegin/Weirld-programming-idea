linklist = ['b','a','e','c','d']
startpointer = 2
linklistpointer = [3,0,5,4,2]
# Find the position of last element in the linklist
def findfinal(arraypointer,start):
    length = len(arraypointer)
    for i in range(length):
        if arraypointer[start] !=5 :
            start = arraypointer[start]
    return start
endpointer = findfinal(linklistpointer,startpointer)
startpointer = endpointer
def changecontentoflinklistpointer(arraypointer,endpointer):
    length = len(arraypointer)
    linklistpointer1 = [length,length,length,length,length]
    for i in range(length-1) :
        for i in range(length):
            if arraypointer[i] == endpointer :
                linklistpointer1[endpointer] = i
                endpointer =  i
    return linklistpointer1        
newlinklistpointer = changecontentoflinklistpointer(linklistpointer,endpointer)
print(endpointer)
print(newlinklistpointer)
def printlinklist(linklist,linklistpointer,startpointer):
    length = len(linklist) 
    for i in range(length):
        print(linklist[startpointer])
        startpointer = linklistpointer[startpointer]
printlinklist(linklist,newlinklistpointer,endpointer)



