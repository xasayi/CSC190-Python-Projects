import time
class Node:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
  def __str__(self):
    return str(self.data)

class BinarySearchTree:
  def __init__(self, root = Node()):
    self.root = root

  def insert(self, val):
    if self.root.data == None:
      self.root = Node(val)
    else:
      self.insert_helper(val, self.root)

  def insert_helper(self, val, current):
    if val < str(current.data):
      if current.left == None:
        current.left = Node(val)
      else:
        self.insert_helper(val, current.left)
    else:
      if current.right == None:
        current.right = Node(val)
      else:
        self.insert_helper(val, current.right)

  def search(self, val):
    start = time.time()
    result = self.search_helper(val, self.root)
    end = time.time()
    if result == 0:
      print("Not Found")
      return 0
    elif result == 1:
      print("Found")
      return 1
    print("Time Elapsed " + str(end-start) + "seconds")

  def search_helper(self, val, current):
    if str(current.data) == val:
      return 1
    elif val < str(current.data):
      if current.left == None:
        return 0
      elif str(current.left) == val:
        return 1
      else:
        self.search_helper(val, current.left)

    elif val > str(current.data):
      if current.right == None:
        return 0
      elif str(current.right) == val:
        return 1
      else:
        self.search_helper(val, current.right)

def constructBST (fileName):
  T = BinarySearchTree()
  myfile = open(fileName, 'r')
  content = myfile.readlines()
  for line in content:
    T.insert(line)
  return T

if __name__ == "__main__":
    fname = "websites2.txt"

    print("--- Constructing BST ---")
    construct_flag = True
    try:
        bst = constructBST(fname)
        print("No syntax or runtime errors occured in constructBST.")
        print("Root: " + str(bst.root))
    except:
        print("Could not construct BST.")
        construct_flag = False

    if construct_flag:
        print("--- Basic Traversal Check ---")
        print("Leftmost traversal: ")
        curr_node = bst.root
        while curr_node != None:
            curr_node = curr_node.left
            print(curr_node)

        print("Rightmost traversal: ")
        curr_node = bst.root
        while curr_node != None:
            curr_node = curr_node.right
            print(curr_node)

        print("Basic traversal check complete.")

    print("Tester complete.")

    tree1 = constructBST("websites2.txt")
    tree1.search("cnn")
