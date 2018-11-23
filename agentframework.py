import random

#set the class of agents and give the agent environment
class Agent(): 
    
    def __init__ (self,environment):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.store = 0  #each agent starts with no food to eat
        #pass

    '''
    def __init__ (self):
        print("construct agent")
        self.x = 1
        pass
    '''

        
    def move(self):
        if random.random() < 0.5:
            self.y  = (self.y  + 1) % 100
        else:
            self.y  = (self.y  - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    #Add method to our agent
    def eat(self): 
       if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 