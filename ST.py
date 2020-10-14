class Node: 
  

    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
  
def search(node,key):

  if key == node.key:
    return True

  if key < node.key:
      
      return search(node.left, key) 
  else:
    
      return search(node.right, key) 
  return False 

def insert( node, key): 
    if node is None: 
        return Node(key) 
    if key == node.key:
      return node
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 

    return node 
  

  


root = None
root = insert(root, "A")
root = insert(root, "A")
root = insert(root, "B")
root = insert(root, "C")
print(search(root,"C")) 
