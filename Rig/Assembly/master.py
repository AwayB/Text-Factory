#The master variable, holding the current process' Target.

class Master():
    master = None
    def Init(self,initval=None):
        "Called by engage.main(self). Initialization of necessary values."
        self.master = initval
        
    def Grab(self, value):
        "Returns a value plucked from Master."
        return(self.master)
    
    @property
    def Master(self):
        "Returns Master."
        return (self.master)

    def _Load(self, value):
        "Master becomes value."
        master = value

    #@multiple
    def Find(self, value, target=master):
        "Finds value inside Master."
        for value in self.master:
            print(value)

    def Get(self, page):
        "Gets a webpage into Master."
        #Webgate.get(page)

    def Post(self,website):   
        "Posts master to website."
        #Webgate.post(page)
        
    def Send(self, file, address):
        "Sends file over network connection."
        #determine_network(ssh, nas, remote_comp).post(file, address)

    def Dump(self,file):
        "Dumps master to file."

    def Foreach(self):
        "unsure"

    def Replace(self,old, new):
        "Replace old by new in master."

    def Append(self): 
        "Append to position in master."

    def Extend(self): 
        "Extend at position in master."

    def Insert(self): 
        "Insert at position in master."

    def Pattern(self,pattern_file):
        "Return pattern."
        