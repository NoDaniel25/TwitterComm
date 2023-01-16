class TreeNode:
    def __init__(self, value, level):
        self.value = value  # data
        self.children = []  # references to other nodes
        self.level = level;

    def add_child(self, child_node):
        # creates parent-child relationship
        #print(child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        #print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self, level=0):
        # moves through each node referenced from self downwards
        print("---"*level + (">" if level != 0 else "") + repr(self.value) )
        for child in self.children:
            child.traverse(level+1)
