class ObjectDataBaseTxt:
   
    def __init__(self, handler, name, mode):
        self.handler = handler
        self.name = name
        self.mode = mode
        
    def FindUser(self, user):
        try:
            self.handler = open(name)
            
            for line in self.handler:
                len = len(line)
                idx = line.find('#') # - nickname#passwd 
                result = user in line[0:idx]

            return result
            
        except:
            print('file not found:', self.name)
            exit()
    
    def create_account(self, user, passwd):
         try:
            self.handler = open(name,'a')
            
            self.hanlder.write(user + '#' + passwd + '\n')
     
        except:
            print('file not found:', self.name)
            exit()

    



        