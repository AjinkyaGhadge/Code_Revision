# Code_Revision
#### Many times, like me we want to practice our Data-Structure and Algorithm basics. To make sure we don't forget our basics, the best thing is to practice and feel the joy of solving problems again. There are lot of resources on the web, so i'll only add some programs and explanations that were useful for me. I hope to use this as a revision, and maybe it will help anyother person in a similar situation!

### Programs
1. [Recursion](https://github.com/AjinkyaGhadge/Code_Revision/tree/master/Recursion_basics)

* Some other use-cases:
calculating depth of a tree.

# Tree

An abstract class for tree:
```
class Tree:
    class Location:
        #Abstract class that represents location of a single element
        def value(self):
            #return the element stored at this position
            raise NotImplementedError('Yet to be Implemented')
        def isequal(self,other):
            #return true if other position represents same location
            raise NotImplementedError("Yet to be Implemented")
        def isunequal(self,other):
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
```

## Computing Depth and Height

For a given position p, the depth of the tree at position p is the number of ancestors of p, excluding p itself.

For a tree the height is the maximum number of decendants of the root node, excluding the root node itself. 

Computation of both height and depth can be done recursively. They can be computed in O(n). Do look at the implementation of depth and height methods in the code above.

## Binary Tree

recursive definition of Binary tree:

1. A node say r, called the root
2. A binary tree called left sub-tree
3. A binary tree called right sub-tree


### Binary-Tree terminiology

1. External node is a node with no children
2. Internal node is a node which has atleast one child
3. Depth is sometimes aslo refered to as level


### Properties of a Binary Tree
n : number of nodes
n <sub>external</sub> : number of external nodes
n <sub>internal</sub> : number of internal nodes
h : height of the tree

1. h+1 <= n <= 2 <sup>n+1</sup> -1
2. 1 <= n <sub>external</sub> <= 2<sup>n</sup>
3. h <= n <sub>internal</sub> <= 2 <sup>h</sup> - 1
4. log(n+1)-1 <= h <= (n-1)/2




