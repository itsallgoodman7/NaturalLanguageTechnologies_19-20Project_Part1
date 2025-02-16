class Node:
    """
    The Node class functions as a way to construct a tree using nodes that have
    children.
    Methods:
    - root
    - left
    - right
    - status
    - terminal
    """


    def __init__(self, root, left, right, end):
        """
        Constructor for the Node class. Root, left, right, terminal and status
        are set up here. Status is infered from whether a terminal value is
        provided or not.
        """
        self.root = root
        self.left = left
        self.right = right
        self.terminal = end
        self.status = True
        if end == None:
            self.status = False

    def status(self):
        """
        status allows the user to get the status of the node.
        @params: n/a.
        @return: boolean for whether it is a terminal node or not.
        """
        return self.status

    def root(self):
        return self.root
        
    def left(self):
        return self.left
        
    def right(self):
        return self.right

    def terminal(self):
        return self.terminal

  
