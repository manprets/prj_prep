#Question 1
#Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s,t):
    if len(s)==0 or len(t)==0:
        return False

    #create a dictionary with key being the character in the string s
    #and value being the number of times that particular character appears
    #in the string s
    char_dict_s={}
    for char_in_s in s:
        if char_in_s in char_dict_s.keys():
            char_dict_s[char_in_s]=char_dict_s[char_in_s]+1
        else:
            char_dict_s[char_in_s]=1

    #create a dictionary with key being the character in the string t
    #and value being the number of times that particular character appears
    #in the string t
    char_dict_t={}
    for char_in_t in t:
        if char_in_t in char_dict_t.keys():
            char_dict_t[char_in_t]=char_dict_t[char_in_t]+1
        else:
            char_dict_t[char_in_t]=1
            
    #look if characters in t are present in s
    for char_in_t in char_dict_t.keys():
        char_in_t_count = char_dict_t[char_in_t]
        if char_in_t in char_dict_s.keys():
            char_in_s_count = char_dict_s[char_in_t]
            #count in s should be greater than or equal to count in t
            if char_in_s_count>=char_in_t_count:
                pass
            else:
                return False
        else:
            return False
    
    
    return True

s="udacity"
t="ad"

print question1(s,t)
#answer should be: True

s="udacity"
t="udacity"

print question1(s,t)
#answer should be: True

s="udacity"
t="yticaduudacity"

print question1(s,t)
#answer should be: False

s="udacity"
t=""

print question1(s,t)
#answer should be: False


#Question 2
#Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

def is_palindrome(s,m):
    """returns True if string s of length m is a palindrome"""
    palindrome=True
    if m==1:
        palindrome=True
    else:
        mid=m/2
        counter=0
        while(counter<mid):
            #print counter,mid,s[counter],s[m-1-counter],palindrome
            if s[counter]==s[m-1-counter]:
                #mid=mid-1
                pass
            else:
               palindrome=False 
            counter=counter+1
    return palindrome

# Brute Force Approach:
# The substring can be of length 1 to n (length of s)
# For substr_len=m
# For all sub_str of length substr_len
# Find if above sub_str is a palindrome
# A palindromic string is one which reads same from the both direction
# can be done using stack as well
def question2(a):
    n=len(a) #length of string
    
    if n==0:
        return None
    if is_palindrome(a,n)==True:
        return a
    
    for substr_len in range(n,0,-1):            
        for start_idx in range(0,n-substr_len):
            substr=a[start_idx:start_idx+substr_len]
            #print substr_len,substr
            
            if is_palindrome(substr,substr_len)==True:
                return substr
    return None

a="bananas"
question2(a)
#answer should be: anana

a=""
print question2(a)
#answer should be: None

a="abracadabra"
print question2(a)
#answer could be one of: aca or ada

a="abracarba"
print question2(a)
#answer should be: abracarba


#Question 3
#Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
#
#{'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)], 
# 'C': [('B', 5)]}
#Vertices are represented as unique strings. The function definition should be question3(G)

#get the edge with the smallest weight from edges_list that is next in mst
#return shortest edge
def get_shortest_edge(edges_list,visited):
    #edge is a tuple (from_node, to_node, weight)
    shortest_edge=('','',99999)
    
    for i in range(len(edges_list)):
        if edges_list[i][1] not in visited:
            if shortest_edge[2]>edges_list[i][2]:
                shortest_edge=edges_list[i]
    
    return shortest_edge

#add shortest edge to mst
def add_to_mst(mst,shortest_edge):
    if shortest_edge[0] in mst.keys():
        mst[shortest_edge[0]].append((shortest_edge[1],shortest_edge[2]))
    else:
        mst[shortest_edge[0]]=[(shortest_edge[1],shortest_edge[2])]
    
    return mst
    
def question3(G):
    mst={}
    
    if len(G.keys())==0:
        return mst
    
    nodes_list=G.keys()
    node=nodes_list[0]
    visited=[node]
    
    while(len(visited)!=len(nodes_list)):
        edges_list=[]
        for v in visited:
            #print v
            e_list=G[v]
            for e in e_list:
                edges_list.append((v,e[0],e[1]))

        #print edges_list,visited
        #get shortest edge from list of edges
        shortest_edge=get_shortest_edge(edges_list,visited)
        visited.append(shortest_edge[1])
        
        #add shortest edge and node to mst
        mst=add_to_mst(mst,shortest_edge)
        
    return mst

G={'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}

print question3(G)
# answer should be: {'A': [('B', 2)], 'B': [('C', 5)]}

G={'A':[('B',2),('C',3),('D',3)],
   'B':[('A',2),('C',4),('E',3)],
   'C':[('A',3),('B',4),('D',5),('E',1),('F',6)],
   'D':[('A',3),('C',5),('F',7)],
   'E':[('B',4),('C',1),('F',8)],
   'F':[('C',6),('D',7),('E',8),('G',9)],
   'G':[('F',9)]
}
print question3(G)
#answer should be: {'A': [('B', 2), ('C', 3), ('D', 3)], 'C': [('E', 1), ('F', 6)], 'F': [('G', 9)]}

G={}
print question3(G)
#answer should be: {}

#Question 4
#Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be
#
#question4([[0, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [1, 0, 0, 0, 1],
#           [0, 0, 0, 0, 0]],
#          3,
#          1,
#          4)
#and the answer would be 3.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self):
        #traversal = str(self.root.value)
        #traversal = self.preorder_print(self.root.left,traversal)
        #traversal = self.preorder_print(self.root.right,traversal)
        traversal = self.preorder_print(self.root,"")
        return traversal[1:]
    
    def preorder_print(self,start,traversal):
        #print traversal
        if start:
            traversal = traversal + "-" + str(start.value)
            #print traversal
            if start.left:
                traversal=self.preorder_print(start.left,traversal)
                #print traversal
            if start.right:
                traversal=self.preorder_print(start.right,traversal)
                #print traversal
        #print traversal
        return traversal
    
def add_nodes_to_tree(start_node_val,start_node,T):
    #print start_node,start_node.value,start_node.left,start_node.right
    
    children=T[start_node_val]
    #print children
    for i in range(len(children)):
        if children[i]==1:
            #found child
            if i<start_node_val:
                #found left child
                start_node.left=Node(i)
                add_nodes_to_tree(i,start_node.left,T)
            else:
                start_node.right=Node(i)
                add_nodes_to_tree(i,start_node.right,T)
    
    
def maketree(T,r):
    tree=BST(r)
    add_nodes_to_tree(r,tree.root,T)
    return tree
    
def find_lca(start,n1,n2):
    lca=None
    if start.value==n1 or start.value==n2:
        lca=start.value
    elif start.value>min(n1,n2) and start.value<max(n1,n2):
        lca=start.value
    elif start.value<n1 and start.value<n2:
        lca=find_lca(start.right,n1,n2)
    elif start.value>n1 and start.value>n2:
        lca=find_lca(start.left,n1,n2)

    return lca
    
def question4(T,r,n1,n2):
    tree=maketree(T,r)
    #print tree.print_tree()
    
    lca=find_lca(tree.root,n1,n2)
    return lca
    
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
#answer should be: 3

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          0)
#answer should be: 0

question4([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          ],
          5,
          7,
          9)
#answer should be: 8

#Question 5
#Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
#
#class Node(object):
#  def __init__(self, data):
#    self.data = data
#    self.next = None

class Node(object): 
    def __init__(self, val): 
        self.data = val 
        self.next = None

class LinkedList(object):
    def __init__(self,data):
        head=Node(data)
        self.head=head
        self.next=None
        #self.head=head
        
    def add_node(self,new_val):
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=Node(new_val)
        
    def print_list(self):
        curr=self.head
        plist=str(curr.data)+"-"
        while(curr.next):
            curr=curr.next
            plist=plist+str(curr.data)+"-"
        plist=plist[0:len(plist)-1]
        
        print plist
        
    def get_length(self):
        length=1
        curr=self.head
        while(curr.next):
            curr=curr.next
            length=length+1
        return length
        
    def get_mth_from_end(self, m):
        #1st element from end=last element
        #2nd element from end=one before last element, len-1 from head
        #3rd element from end=two before last element, len-2 from head
        #4th element from end=three before last element, len-3 from head
        #5th element from end=four before last element, len-4 from head
        
        #steps to follow
        #first: find length of linked list
        #second: go to n-(m-1)=n-m+1 node
        #(n-m+1)th node is n-m steps ahead
        
        length=self.get_length()
        curr=self.head
        counter=length-m
        while(counter):
            curr=curr.next
            counter=counter-1
        
        return curr.data

#create a linked list
ll=LinkedList(1)
#n=Node(10)
#n.data=10
#print n.data,ll.head.data
ll.add_node(3)
ll.add_node(4)
ll.add_node(6)
ll.add_node(7)
ll.add_node(9)
ll.add_node(11)
ll.add_node(12)
ll.add_node(15)
#ll.print_list()
#print ll.get_length()

def question5(ll,m):
    if ll==None:
        return None
    if m==0 or m>ll.get_length():
        return None
    
    return ll.get_mth_from_end(m)

print question5(ll,2)
#answer should be: 12

print question5(None,2)
#answer should be: None

print question5(ll,0)
#answer should be: None

print question5(ll,10)
#answer should be: None

print question5(ll,5)
#answer should be: 7






