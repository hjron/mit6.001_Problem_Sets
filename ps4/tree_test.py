from tree import *

tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))),
             Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)),
                     Node(14, Node(12), Node(21, Node(20), Node(26))))

tr1 = Node(5,Node(15,None,Node(16,Node(30),Node(17))),Node(6,Node(20,None,Node(45)),Node(11)))
tr2 = Node(2,Node(3,Node(4),Node(5,Node(6))),Node(7,None,Node(8,Node(9),Node(1))))
tr3 = Node(5, Node(1), Node(5, Node(5)))
tr4 = Node(21, Node(15, Node(7), Node(11)), Node(3, Node(2), Node(1)))
tr5 = Node(4, Node(10, Node(18), Node(11)), Node(5, Node(7), Node(8)))

def traverse(node):
    # base case: node is a leaf, height is 0
    if node != None:
        print(node.get_value())
    if node is None:
        return -1 

    # recurse through the tree until we meet the base case
    # left = traverse(node.get_left_child())
    # right = traverse(node.get_right_child())

    return 1 + max(traverse(node.get_left_child()), traverse(node.get_right_child()))

def max_compare(child_value, parent_value):
    return child_value < parent_value

def min_compare(child_value, parent_value):
    return child_value > parent_value

def is_heap(tree, compare_func):
    if tree is None or (tree.get_left_child() is None and tree.get_right_child() is None):
        return True
    
    if tree.get_right_child() is not None:
        return compare_func(tree.get_right_child().get_value(), tree.get_value()) and \
                is_heap(tree.get_right_child(), compare_func) and \
                is_heap(tree.get_left_child(), compare_func)

    if tree.get_left_child() is not None:
        return compare_func(tree.get_left_child().get_value(), tree.get_value()) and \
                is_heap(tree.get_left_child(), compare_func)

    return False


# compare_func(tree.get_left_child().get_value(), tree.get_value()) and \
print('tr1 is a min heap', is_heap(tr1, min_compare))
print('tr2 is a min heap', is_heap(tr2, min_compare))
# print('tree1 should be 2:', traverse(tree1))
# print('tree2 should be 3:', traverse(tree2))
# print('tree3 should be 3:', traverse(tree3))
# 
# print('tr1 should be 3:', traverse(tr1))
# print('tr2 should be 6:', traverse(tr2))
# print('tr3 should be 2:', traverse(tr3))

# print(is_heap(tree1, max_compare))
# print(is_heap(tree1, min_compare))
