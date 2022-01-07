from copy import copy

class Node():
    def __init__(self, cat, name="None"):
        self.adjacent = []
        self.category = cat
        self.name = name

    def __hash__(self):
        return id(self).__hash__()

    @staticmethod
    def make_node(label):
        if label == "start":
            return Node("start", name="start")
        elif label == "end":
            return Node("end", name="end")
        elif label.isupper():
            return Node("big", name=label)
        else:
            return Node("small", name=label)

def get_node(lab, nodeLabels):
    if lab in nodeLabels:
        return nodeLabels[lab]
    else:
        node = Node.make_node(lab)
        nodeLabels[lab] = node
        return node

def read_graph(infile):
    nodeLabels = dict()
    with open(infile) as f:
        for line in f:
            nodeLab1, nodeLab2 = line.strip().split("-")
            node1 = get_node(nodeLab1, nodeLabels)
            node2 = get_node(nodeLab2, nodeLabels)
            node1.adjacent.append(node2)
            node2.adjacent.append(node1)

    start = nodeLabels["start"]
    return start

def count_paths(node, traversed):
    #print(node.name, list(map(lambda x: x.name, traversed)))
    if node.category == "end":
        return 1
    if len(set(node.adjacent) - traversed) == 0: 
        return 0
    numPaths = 0
    traversed = copy(traversed)
    if node.category in  ("small", "start"):
        traversed.add(node)
    for neighbor in node.adjacent:
        if neighbor not in traversed:
            numPaths += count_paths(neighbor, traversed)
    return numPaths

def main():
    infile = "input.txt"
    start = read_graph(infile)
    print(count_paths(start, set()))


if __name__ == "__main__":
    main()

            
                

