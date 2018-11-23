
import matplotlib.pyplot
import agentframework
import csv

#Read the CSV code and make an environment list
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []  #environment list
    for row in reader:
        rowlist = []
        for value in row:
           rowlist.append(value)
        environment.append(rowlist)

print(environment)

##make a plot of the environment        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
            
##a = agentframework.Agent(1,2)
##print(a)
##print(a.y)
##print(a.x)
##a.x = 4
##print(a.x)

#Distance between the agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Make the agent list and set the iteration 
num_of_agents = 10
num_of_iterations = 200
agents = []


#Give environment to the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))


      
#Move the agent and let them eat from the environment
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
        

            


