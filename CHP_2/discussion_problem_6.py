# visualizing total displacement vs total distance traveled
# average velocity is the ratio of total displacement / total time elapsed
# average speed is the ration of total distance traveled / total time elapsed

import numpy as np
import matplotlib.pyplot as plt

# Define points for the path
points = np.array([[0, 0], [2, 3], [4, 1], [6, 4], [8, 2]])

# Calculate total displacement (vector from start to end)
displacement = points[-1] - points[0]

# Plot the path (total distance traveled)
plt.figure(figsize=(8, 8))
for i in range(len(points) - 1):
    plt.plot([points[i, 0], points[i+1, 0]], [points[i, 1], points[i + 1, 1]], 'bo-', label='Path' if i == 0 else "")

# Plot the total displacement vector
plt.quiver(points[0,0], points[0,1], displacement[0], displacement[1], angles='xy', scale_units='xy', scale=1, color='red', label='Displacement')

# Annotate points
for i, point in enumerate(points):
    plt.text(point[0] + 0.2, point[1] + 0.2, f'P{i+1}', fontsize=12)

# Set plot limits
plt.xlim(-1,10)
plt.ylim(-1,5)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Total Displacement vs Total Distance Traveled')
plt.legend()
plt.grid(True)
plt.show()