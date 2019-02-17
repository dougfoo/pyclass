print ('hello world')

file = open("mytest.py")
print (file)
lines = file_object.readlines()
print (len(lines))

def exp(x,y):
    return x^y

def add (x , y):
    return x+y

def sub (x, y ):
    return x-y

def mult (x,y):
    return x*y

def div (x,y):
    if (y == 0):
        return 0  # ? is that what we want to do?
    else:
        return x/y   # this will return a float ? or int ?  (py2 vs 3 dependant)

# test this
numbers = [-1,0,1,2,3,4,5,6]
for i in numbers:
    print ("div: %d/%d %f"%(i,i+1,div(i,i+1)))
    print ("mult: %d*%d %d"%(i,i+1,mult(i,i+1)))
    print ("add: %d+%d %d"%(i,i+1,add(i,i+1)))
    print ("sub: %d-%d %d"%(i,i+1,sub(i,i+1)))
    print ('----')

