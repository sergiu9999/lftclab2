class node:
    def __init__(self,value=None,id=None):

        self.id=id
        self.value=value
        self.right=None
        self.left=None

class BST:
    def __init__(self):
        self.root=None
        self.counter=0
    def insert(self,value):
        if self.root==None:
            self.root=node(value,self.counter)
            self.counter=self.counter+1
        else:
            self._insert(value,self.root)

    def _insert(self,value,current):
        if value<current.value:
            if current.left==None:
                current.left=node(value,self.counter)
                self.counter=self.counter+1
            else:
                self._insert(value,current.left)
                self.counter = self.counter + 1
        elif value>current.value:
            if current.right==None:
                current.right=node(value,self.counter)
                self.counter=self.counter+1
            else:
                self._insert(value,current.right)
                self.counter=self.counter+1


    def print_tree(self,file):
        if self.root!=None:
            self._print_tree(self.root,file)

    def _print_tree(self,current,file):
        if current!=None:
            self._print_tree(current.left,file)
            file.write((str(current.value)+" "+str(current.id))+"\n")
            self._print_tree(current.right,file)

    def search(self,value):
        if self.root!=None:
            return self._search(    value,self.root)
        else:
            return -1

    def _search(self,value,current):

        if value==current.value:
            return current.id
        elif value<current.value and current.left!=None:
            return self._search(value,current.left)
        elif value>current.value and current.right!=None:
            return self._search(value,current.right)
        return -1


