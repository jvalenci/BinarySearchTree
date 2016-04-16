'''Provides basic operations for Binary Search Trees using
a list representation.  In this representation, a BST is
either an empty list or a list consisting of a data value,
a BST called the left subtree and a BST called the right subtree
'''

def is_bintree(T):
    if type(T) is not list:
        return False
    if T == []:
        return True
    if len(T) != 3:
        return False
    if is_bintree(T[1]) and is_bintree(T[2]):
        return True
    return False

def bst_min(T):
    if T == []:
        return None
    if not T[1]:        
        return T[0]
    return bst_min(T[1])
    
def bst_max(T):
    if T == []:
        return None
    if not T[2]:        
        return T[0]
    return bst_max(T[2])
        
def is_bst(T):
    if not is_bintree(T):
        return False

    if T == []:
        return True

    if len(T) != 3:
        return False

    if not is_bst(T[1]) or not is_bst(T[2]):
        return False
    
    if T[1] == [] and T[2] == []:
        return True
    
    if T[2] == []:
        return bst_max(T[1]) < T[0]
    if T[1] == []:
        return T[0] < bst_min(T[2])
    return bst_max(T[1]) < T[0] < bst_min(T[2])
               
def bst_search(T,x):
    if T == []:
        return T
    if T[0] == x:
        return T
    if x < T[0]:
        return bst_search(T[1],x)
    return bst_search(T[2],x)

def bst_insert(T,x):
    if T == []:
        T.append(x)
        T.append([])
        T.append([])
    elif x < T[0]:
        T[1] = bst_insert(T[1],x)
    else:
        T[2] = bst_insert(T[2],x)
    return T

def delete_min(T):
    if T == []:
        return T
    
    if not T[1]:        
        T = T[2]
    else:
        T[1] = delete_min(T[1])
        
    return T

def bst_delete(T,x):
    if T == []:
        return [] 

    if x < T[0]:
        T[1] = bst_delete(T[1],x)
    elif x > T[0]:
        T[2] = bst_delete(T[2],x)    
    else:
        # T[0] == x
        if not T[1]:
            T = T[2]
        elif not T[2]:
            T = T[1]
        else:
            val = bst_min(T[2])
            T[2] = delete_min(T[2])
            T[0] = val
    return T

def print_func_space(x):
    print(x,end=' ')

def print_bintree(T,level=0):
    if T == []:
        print('-'*3*level+'|')
    else:
        print('-'*3*level + str(T[0]))
        print_bintree(T[1],level+1)
        print_bintree(T[2],level+1)

def inorder(T,f):
    if not is_bst(T):
        return
    if not T:
        return
    inorder(T[1],f)
    f(T[0])
    inorder(T[2],f)

# programming project: provide implementations for the functions below
# and add tests for these functions to the code in the block
# that starts "if __name__ == '__main__'"

def preorder(T,f):
	if not is_bst(T):
		return
	if not T:
		return
	f(T[0])
	preorder(T[1],f)
	preorder(T[2],f)

def postorder(T,f):
    if not is_bst(T):
        return
    if not T:
        return
    postorder(T[1],f)
    postorder(T[2],f)
    f(T[0])

def tree_height(T):
    if T == []:
        return 0

    if not T:
        return 0

    return (max(1 + tree_height(T[1]), 1 + tree_height(T[2])))

def balance(T):
    # returns the height of the left subtree of T
    # minus the height of the right subtree of T
    
    if abs(tree_height(T[1]) -  tree_height(T[2])) > 1:
        if tree_height(T[1]) > tree_height(T[2]):
            val = bst_max(T[1])
            bst_delete(T[1],val)
            temp = T[0]
            T[0] = val 
            bst_insert(T,temp)
            
        else:
            val = bst_min(T[2])
            bst_delete(T[2],val)
            temp = T[0]
            T[0] = val
            bst_insert(T,temp)
            
        balance(T)
    return T

# Modify the code below to test the above four functions    
if __name__ == '__main__':
    K = []
    
    for x in ['Joe','Bob', 'Phil', 'Paul', 'Marc', 'Jean', 'Jerry', 'Alice', 'Anne']:
        bst_insert(K,x)
    print('-' * 50)
    print("\nTree elements in sorted order\n")
    inorder(K,print_func_space)
    print()
    print('-' * 50)
    print('\nPrint full tree\n')
    print_bintree(K)
    print("\nDelete Bob and print tree\n")
    bst_delete(K,'Bob')
    print_bintree(K)
    print('-' * 50)
    print("\nPrint subtree at 'Phil'\n")
    print_bintree(bst_search(K,'Phil'))
    print('-' * 50)
    # YOUR TEST CODE GOES BELOW reset list for test
    
    K = []
    
    for x in ['Joe','Bob', 'Phil', 'Paul', 'Marc', 'Jean', 'Jerry', 'Alice', 'Anne']:
        bst_insert(K,x)
    
    print('Testing preorder()')
    print("\nTree elements in preorder\n")
    preorder(K,print_func_space)
    print()
    print('-' * 50)
    print('Testing postorder()')
    print("\nTree elements in post order\n")
    postorder(K,print_func_space)
    print()
    print('-' * 50)
    print('Testing treeheight()')
    print("\nTree height with original list\n")
    print(tree_height(K))
    print()
    print("\nTree height with names added to original list\n")
    bst_insert(K,'Mqdraah')
    bst_insert(K,'Mqderson')
    bst_insert(K,'Mqdersan')
    bst_insert(K,'Mqdersonh')
    bst_insert(K,'Mqdersonm')
    bst_insert(K,'Mqderson')
    print_bintree(K)
    print()
    print('Tree height is ' + str(tree_height(K)))
    print()
    print('-' * 50)
    print('Testing balance()')
    print("\nBalancing after adding more names to original list\n")
    print_bintree(balance(K))
    print()
    print('-' * 50)