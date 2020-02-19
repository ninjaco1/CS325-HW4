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
print("Number of arguments:", len(sys.argv), "arguments.")
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
for i in range(len(adj_matrix)):
    print(adj_matrix[i][:len(adj_matrix)-(len(adj_matrix)-i)])


key =0
for i in range(n_point): # i and j are points
    for j in range(n_point):
        adj_matrix[i][j] = Data(distance(points[i],points[j]),points[i],points[j],key)
        key+=1
        #adj_matrix[i][j].show_all()
    # print(adj_matrix[i].distance)
    #print("\n")

#put everything in one array then sort, lower triangle
W = []
for i in range(len(adj_matrix)): # add weights to lower triangle
    for j in range(len(adj_matrix)-(len(adj_matrix)-i)):
        W.append(adj_matrix[i][j])

# for i in range(len(W)):
#     W[i].show_all()


print("")
for i in range(len(W)):
    W[i].show_all()
# a set that contain all edges
# for each vertex v in G.V(the vertex with):
#       make a set (v)
#for each edge (u,v) in G.E ordered by increasing order by weight(u,v):
#   if find_set(u) != find_set(v):
#   A = A union {(u,v)}
#   union(u,v)
#return A
def kruskal(W,points):
    A = [] # contains all edges,key
    T = [] # contain all points
    mergesort(W)
    for edge in range(len(W)):
        if (len(T) == len(points)) and (T == points): #if all the points are in the tree then break
            break
        if W[edge].p1 and W[edge].p2 in T:
            continue
        if W[edge].key not in A: # then add node
            if W[edge].p1 not in T:
                T.append(W[edge].p1)
            if W[edge].p2 not in T:
                T.append(W[edge].p2)
            A.append(W[edge].key)
    print ("A: %s"% (A))
    print ("T: %s" %T)


kruskal(W, points)
def main():
    pass
