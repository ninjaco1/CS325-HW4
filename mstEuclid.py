import sys
import math

class Data(object):
    def __init__(self, distance, p1, p2,key):
        self.key = key
        self.distance = distance
        self.p1 = p1
        self.p2 = p2

    def show_all(self):
        print("distance: %s p1: %s p2: %s key: %s" % (self.distance, self.p1, self.p2, self.key))

    def format(self):
        print("%s - %s        %s"%(self.p1, self.p2, self.distance))

def distance(p1,p2):
    #x=[0] y=[1]
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    total = math.sqrt(x**2 + y**2)
    return round(total)


def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        #divide
        mergesort(left)
        mergesort(right)

        i = j = 0 #left and right
        k = 0 # main array
        #conquer
        while i < len(left) and j < len(right):
            if left[i].distance < right[j].distance:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1



# to show command line arguments
#print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))
text_name = str(sys.argv[1])
#print (text_name)

# read lines from file
file = open(text_name,"r")
lines = file.readlines()#reads all the lines in the file
file.close()
#print(lines)
current_line = 0

temp = [int(i) for i in lines[0].split() if i.isdigit()]
n_point = temp[0] # number of points
#print (n_point)

# putting the set of points in an array
points = [] #set of points
for num in range(n_point):
    points.append([int(i) for i in lines[num+1].split() if i.isdigit()])
#print(points)

# making the adjaceny matrix
adj_matrix = [[0 for i in range(n_point)] for j in range(n_point)]
# for i in range(len(adj_matrix)):
#     print(adj_matrix[i])

#prints out lower trinagle without zeros
# for i in range(len(adj_matrix)):
#     print(adj_matrix[i][:len(adj_matrix)-(len(adj_matrix)-i)])


key =0
for i in range(n_point): # i and j are points
    for j in range(n_point):
        adj_matrix[i][j] = Data(distance(points[i],points[j]),points[i],points[j],key)
        key+=1
        #adj_matrix[i][j].show_all()
    #print(adj_matrix[i].distance)
    #print("\n")

#put everything in one array then sort, lower triangle
W = []
for i in range(len(adj_matrix)): # add weights to lower triangle
    for j in range(len(adj_matrix)-(len(adj_matrix)-i)):
        W.append(adj_matrix[i][j])

# for i in range(len(W)):
#     W[i].show_all()


print("")
# for i in range(len(W)):
#     W[i].show_all()
# a set that contain all edges
# for each vertex v in G.V(the vertex with):
#       make a set (v)
#for each edge (u,v) in G.E ordered by increasing order by weight(u,v):
#   if find_set(u) != find_set(v):
#   A = A union {(u,v)}
#   union(u,v)
#return A

#finding a cycle

#cycle(W,points)
def find(parent,rank,vertex):
    if parent[vertex] == vertex:
        return parent[vertex]
    return find(parent, rank, parent[vertex])

def union(parent,rank,root1,root2):
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root2] > rank[root1]:
        parent[root1]=root2
    else:
        parent[root1] = root2
        rank[root2] +=1

def makeset(parent,rank,vertex):
    parent[vertex] = vertex
    rank[vertex] = 0


def MST(W,points):
    A=[]
    rank = [-1 for i in range(len(points))] #disjoint set rank
    parent = [-1 for i in range(len(points))] # disjoint set
    for i in range(len(points)):
        makeset(parent, rank,i)
    mergesort(W)
    for i in range(len(W)):
        p1_index = p2_index = -1
        for k in range(len(points)):
            if W[i].p1 == points[k]:
                p1_index = k# node key value
                break

        for k in range(len(points)):
            if W[i].p2 == points[k]:
                p2_index = k
                break
        root1 = find(parent,rank,p1_index)
        root2 = find(parent, rank,p2_index)
        if root1 != root2:
            A.append(W[i])#.key
            union(parent, rank, root1,root2)

    print("Edges in MST")
    print("Point [x,y]         Distance")
    total_distance =0
    for i in range(len(A)):
        A[i].format()
        total_distance += A[i].distance
    print("         Total distance %s"% total_distance)
    #print("A: %s"% A)
MST(W,points)

#kruskal(W, points)
def main():
    pass
