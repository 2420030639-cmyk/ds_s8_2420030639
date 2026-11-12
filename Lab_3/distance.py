import numpy as np
from scipy.spatial import distance

pA = np.array([2, 4, 6])
pB = np.array([5, 1, 9])

e_dist = distance.euclidean(pA, pB)
print("Euclidean distance: ", e_dist)

similarity_e = 1/(1+e_dist)
print("Euclidean Similarity: ", similarity_e)

pC = np.array([4, 7, 9])
pD = np.array([2, 8, 3])

m_dist = distance.cityblock(pC, pD)
print("Manhattan distance: ", e_dist)

similarity_m = 1/(1+m_dist)
print("Manhattan Similarity: ", similarity_m)

print("\n")

e_dist = distance.euclidean(pA, pB)
print("Euclidean distance: ", e_dist)

similarity_e = 1/(1+e_dist)
print("Euclidean Similarity: ", similarity_e)

m_e_dist = distance.cityblock(pA, pB)
print("Manhattan distance: ", m_e_dist)

similarity_m_e = 1/(1+m_e_dist)
print("Manhattan Similarity: ", similarity_m_e)

pD = np.array([8, 3, 7])
pE = np.array([9, 0, 2])

#minkowski with p=3
minkowski_dist = distance.minkowski(pC, pD, p=3)
print("Minkowski distance (p=3): ", minkowski_dist)

similarity_minkowski = 1/(1+minkowski_dist)
print("Minkowski Similarity: ", similarity_minkowski)

minkowski_e_dist = distance.minkowski(pA, pB, p=2)
print("Minkowski distance (p=2): ", minkowski_e_dist)

similarity_e_minkowski = 1/(1+minkowski_e_dist)
print("Minkowski Similarity: ", similarity_e_minkowski)

minkowski_e_dist = distance.minkowski(pA, pB, p=1)
print("Minkowski distance (p=1): ", minkowski_e_dist)

similarity_e_minkowski = 1/(1+minkowski_e_dist)
print("Minkowski Similarity: ", similarity_e_minkowski)