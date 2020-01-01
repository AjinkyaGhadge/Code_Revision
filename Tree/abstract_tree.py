class Tree:

    class Position:
        #Abstract class that represents location of a single element
        def element(self):
            #return the element stored at this position
            raise NotImplementedError('Yet to be Implemented')
        
        def __eq__(self,other):
            #return true if other position represents same location
            raise NotImplementedError("Yet to be Implemented")
        
        def __ne__(self,other):
            #return true if other position doesn't represent the same location
            raise NotImplementedError("Yet to be Implemnted")

    
    def root(self):
        #return position representing the tree's root(or None if empty)
        raise NotImplementedError("Yet to be Implemented")
    
    def parent(self,p):
        #return position representing p's parent(or None if p is root)
        raise NotImplementedError("Yet to be Implemented")
   
    def num_children(self,p):
        #return number of children a position p has 
        raise NotImplementedError("Yet to be Implemented")
    
    
    def children(self,p):
        #return an iteration of postions representing children of the node at position p
        raise NotImplementedError("Yet to be Implemented")
    
    def __len__(self):
        #return total number of elements in a tree
        raise NotImplementedError("Yet to be Implemented")
    
    def is__root(self,p):
        #return true if the position represents the root node of the tree
        return self.root() == p 
    
    def is_leaf(self):
        #return true if position p doesnot have any children 
        return self.num_children(self) == 0
    
    def is_empty(self):
        #return true if the tree is empty
        return len(self) == 0
    
    def depth(self,p):
        #method to calculate depth of a tree
        if self.is__root(p):
            return 0
        else:
            return 1+ self.depth(self.parent(p))
    
    def _height(self,p):
        #method to calculate height of tree
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))
        