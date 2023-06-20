import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = './data/layer_5.csv'
b_layer = np.genfromtxt(filename, delimiter=',')
ideal_num_particles = 1000000
indices = np.linspace(0, b_layer.shape[0] - 1, ideal_num_particles, dtype=int)
b_layer = b_layer[indices, :]

terrain_height = 0.20
z_center = np.arange(0.0,terrain_height,0.01)
num_patch = z_center.shape[0]
print("total number of layers is : ",num_patch)

num_particles_layer = b_layer.shape[0]

layers = np.zeros((num_particles_layer*num_patch,3))

for i in range(num_patch):
    for j in range(num_particles_layer):
        # layers[i*num_particles_layer+j,0] = float(b_layer[j,0] + np.random.rand() * 0.005)
        # layers[i*num_particles_layer+j,1] = float(b_layer[j,1] + np.random.rand() * 0.005)
        # layers[i*num_particles_layer+j,2] = float(b_layer[j,2] + z_center[i] + np.random.rand() * 0.001)
        
        # without randomize the particles' position
        layers[i*num_particles_layer+j,0] = float(b_layer[j,0] )
        layers[i*num_particles_layer+j,1] = float(b_layer[j,1] )
        layers[i*num_particles_layer+j,2] = float(b_layer[j,2] + z_center[i])
print(layers.shape)

terrain = np.concatenate((layers,b_layer),axis=0)
print(terrain.shape)


x = terrain[:,0]
y = terrain[:,1]
z = terrain[:,2]
print('done reading data file')
np.savetxt('sph_terrain_20.csv', terrain, delimiter=',')
print('done exporting data')
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x,y,z,c='black',marker='o',s=1,alpha=0.1)
ax.scatter(x,y,z,c='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim3d(0, 5)
ax.set_title('Point Cloud Visualization')
ax.view_init(elev=10, azim=30) 
plt.show()