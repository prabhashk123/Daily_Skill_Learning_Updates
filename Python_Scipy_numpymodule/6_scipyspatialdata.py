# Working with spatial data: it refers to data that is represented in a geometric space.
# Triangulation: one method to generate these triangulation through the point is delaunay() triangulation.

# here now we will create a triangualtion from some points:
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
# make one triangle in ploygeon 
pb = np.array([[2,4], [3,4], [3,0], [2,2], [4,1]])
# simplicies generalize in traingle
simplices = Delaunay(pb).simplices
# use range ka
plt.triplot(pb[:,0], pb[:,1], simplices)
plt.scatter(pb[:,0], pb[:,1], color='r')
plt.show()

## Convex HUll: it is the smallest polygon that covers all of the given point:
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

pb = np.array([[2,4], [3,4], [3,0], [2,2], [4,1], [1,2], [5,0], [3,1],[1,2],[0,2]])
# hull as var like any name
hull = ConvexHull(pb)
hull_points = hull.simplices
plt.scatter(pb[:,0], pb[:,1])
for simplex in hull_points:
    plt.plot(pb[simplex,0], pb[simplex,1], 'k-')
plt.show() 

## KDTrees: they are a data structures optimized for the nearest neighbour queries.
from scipy.spatial import KDTree
# touple array
pb = [(1,-1), (2,3), (-2,3), (2,-3)]
tree = KDTree(pb)
res = tree.query((1,1)) # query calculated distance than location 
print(res) 
# o/p is (2.0, 0) here 2.0 is distance and 0 is location like position index

##vvi. Distance matrix: it is used to find the various types of distance between 2 points . there are basically 2 types: Euclidean Distance, Cosine Distance.
# Euclidean Distance: 
from scipy.spatial.distance import euclidean
# 2 vector basis on angle and all yeha point 1 and 2
p1 = (1,0)
p2 = (10,2)
pb = euclidean(p1, p2)
print(pb) 

## Cosine Distance: 
from scipy.spatial.distance import cosine
p1 = (1,0)
p2 = (10,2)
pb = cosine(p1, p2)
print(pb)