import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# Data: Car name, length (mm), width (mm), height (mm)
car_data = [
    ("VW Golf Mk2", 3985, 1665, 1415, 'red'),
    ("Mazda MX-5 NB", 3975, 1680, 1225, 'orange'),
    ("Peugeot 307CC", 4357, 1759, 1437, 'lightblue'),
    ("Opel Astra F Caravan", 4280, 1688, 1490, 'darkblue'),
    ("Peugeot 308 1st Gen", 4276, 1815, 1498, '#7e7e7e'),
    ("Skoda Octavia 1st Gen Wagon", 4511, 1731, 1448, '#d4d4d4'),
    ("Lexus IS200", 4400, 1725, 1410, '#ffffff'),
    ("Honda Civic 6th Gen Hatch", 4180, 1695, 1390, '#e9e9e9'),
    ("Opel Zafira B", 4467, 1781, 1670, '#e9e9e9'),
    ("Toyota Corolla 2020 Hatch", 4375, 1799, 1421, '#581845'),
    ("Nissan 350Z", 4310, 1816, 1315, '#000000'),
    ("Honda CR-V 1st Gen", 4515, 1750, 1710, '#023909'),
    ("BMW E36 ", 4433, 1710, 1360, '#e0d200'),
    ("BMW E38", 4984, 1850, 1445, '#000000')
    
]
fig = plt.figure(figsize=(12, 8))  # Adjust figure size
ax = fig.add_subplot(111, projection='3d')

# Initialize the Y-offset starting position
y_offset = 0
x_offset = 0

# Set axis limits (adjust these based on the range of your data)
ax.set_xlim([0, 7000])  # Limit for car lengths
ax.set_zlim([0, 7000])  # Limit for car heights
ax.set_ylim([0, 24000])

# Plot each car as a box with length, width, and height
for model, length, width, height, color in car_data:
    # Vertices of the cuboid representing the car's dimensions
    vertices = [
        [0, y_offset, 0], [0 + x_offset , y_offset + width, 0],
        [length, y_offset + width, 0], [length, y_offset, 0],
        [0, y_offset, height], [0, y_offset + width, height],
        [length, y_offset + width, height], [length, y_offset, height]]
    
    faces = [[vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [7, 6, 2, 3]],
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]]]

    # Create a 3D polygon collection for the car
    poly3d = Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='black', alpha=0.7)
    
    # Plot each car with a y-offset based on previous cars' widths and some padding
    ax.add_collection3d(poly3d, zs=y_offset, zdir='y')

    # Add a label for the car model
    ax.text(length / 2, y_offset + width / 2, height + 1000, model, ha='center', fontsize=20)

    # Update y_offset to include current car width and a padding of 100mm
    y_offset += width + 500

# Set labels and limits
ax.set_xlabel('Length (mm)')
ax.set_ylabel('Y Offset (model separation based on width)')
ax.set_zlabel('Height (mm)')
ax.set_title('3D Car Size Comparison (No Overlap)')

# Set view angle
ax.view_init(20, 120)

# Show plot
plt.tight_layout()
plt.show()