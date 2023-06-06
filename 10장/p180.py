import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
coords, feat = make_blobs(centers=3, random_state=20)
plt.scatter(coords[:,0], coords[:,1], marker='o', c=feat)
plt.show()