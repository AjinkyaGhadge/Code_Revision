class BinaryTree(Tree):

    #----------Abstract methods ------------------------
    def left(self,p):
        #Return a position representing p's left child, None if p doesn't have a left child
        raise NotImplementedError("Yet to be Implemented")
    def right(self,p):
        #Return a position representing p's right child, None if p doesn't have a right child
        raise NotImplementedError("Yet to be Implemented")
    #----------Concrete methods ------------------------
    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

