#The master variable, holding the current process' Target.

def Init(initval=0):
    "Called by engage.main(). Initialization of necessary values."
    global master
    master = initval
    
def Grab(value):
    "Returns a value plucked from Master."
    global master
    return(value)
    
def Master():
    "Returns Master."
    global master
    return (master)

def _Load(value):
    "Master becomes value."
    global master
    master = value

def Find(value):
    "Finds value inside Master."
    

def Get():
    ""

def Post():   
    ""

def Dump():
    ""

def Foreach():
    ""

def Replace():
    ""

def Append(): 
    ""

def Extend(): 
    ""

def Insert(): 
    ""

def Pattern():
    ""
    