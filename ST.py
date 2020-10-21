class node:
    def __init__(self,value=None):
        self.value=value
        self.right=None
        self.left=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,current):
        if value<current.value:
            if current.left==None:
                current.left=node(value)
            else:
                self._insert(value,current.left)
        elif value>current.value:
            if current.right==None:
                current.right=node(value)
            else:
                self._insert(value,current.right)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,current):
        if current!=None:
            self._print_tree(current.left)
            print(str(current.value))
            self._print_tree(current.right)


    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,current):

        if value==current.value:
            return True
        elif value<current.value and current.left!=None:
            return self._search(value,current.left)
        elif value>current.value and current.right!=None:
            return self._search(value,current.right)
        return False


ST = BST()
ST.insert("A")
ST.insert("A")
ST.insert("B")
ST.insert("C")
ST.insert("D")
ST.insert("E")
ST.insert("F")
ST.print_tree()
print(ST.search("A"))
print(ST.search("F"))
print(ST.search("Z"))