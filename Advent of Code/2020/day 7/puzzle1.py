#imports
import regex; #used to process input
#we use regex over re for repeating capture groups
#i.e. the match.captures() function






#this is a graph problem. Just a DFS
#but we'll need to implement the graph


#class to represent bags of different colors
class Bag():
    def __init__(self, color):
        self.color = color; #string that stores bag color

        self.contains = {}; #adjacency list of bags this color can contain
                            #key is bag, value is number it contains
        self.isContained = {}; #reverse adjacency list of bags that contain this
                                #key is bag, value is number it contains

    def addContains(self, innner, num):
        """add an edge that this bag contains num * inner bag"""
        self.contains[inner] = num;

    def addIsContained(self, outer, num):
        """add a reverse edge that num * this is contained by outer bag"""
        self.isContained[outer] = num;


graph = {}; #dictionary. Key is a color string, value is a node (aka bag)




#store input in graph
pattern = regex.compile(r'(.+) bags contain( (\d+) ([^\d\n]+) bag(s)?,?)*\.'); #this kills me

with open("input1.txt") as f:
    fulltext = f.read();

collection = pattern.finditer(fulltext) #match pattern to input
for match in collection: #aka for line in file

    #unpack captured groups
    outerColor = match.group(1)
    innerColors = zip(match.captures(3), match.captures(4))

    #find outer bag
    if outerColor not in graph:
        graph[outerColor] = Bag(outerColor)
    outer = graph[outerColor]

    #loop through inner bags and add vertices
    for bagNum, innerColor in innerColors:
        
        if innerColor not in graph:
            graph[innerColor] = Bag(innerColor)
        inner = graph[innerColor]

        outer.addContains(inner, bagNum)
        inner.addIsContained(outer, bagNum)

#cool so input has been processsed
#now we do the BFS
#we should use a linked list queue but I don't care enough
start = "shiny gold"
bagQueue = [graph[start]]
reachableBags = []
while len(bagQueue) > 0:
    
    currBag = bagQueue.pop(0)

    if currBag not in reachableBags: #handle cycles
        reachableBags.append(currBag)
        for bag in currBag.isContained:
            bagQueue.append(bag)

print(len(reachableBags) - 1)



        
    



