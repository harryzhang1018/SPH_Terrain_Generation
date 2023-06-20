import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = './data/layer_5.csv'
data = np.genfromtxt(filename, delimiter=',')
print(data.shape[0])
# ideal_num_particles = 1500000
# indices = np.linspace(0, data.shape[0] - 1, ideal_num_particles, dtype=int)
# data = data[indices, :]

x = data[:,0]
y = data[:,1]
z = data[:,2]

print('done reading data file')
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,c='black',marker='o',s=1,alpha=0.1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim3d(0, 5)
ax.set_title('Point Cloud Visualization')
ax.view_init(elev=10, azim=30) 
plt.show()