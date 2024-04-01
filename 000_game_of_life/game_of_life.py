import numpy as np
import matplotlib.pyplot as plt
import copy

cols = 100
rows = 100


grid = np.random.randint(2, size=(rows, cols))


fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary')


kernel = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

while True:
    old_grid = np.pad(grid, 1, mode='wrap')
    grid = np.zeros((cols,rows))
    for i in range(1,cols+1):
        for j in range(1,rows+1):
            neighbors = np.sum(old_grid[i-1:i+2, j-1:j+2] * kernel)
                        
            if neighbors == 3:
                    grid[i-1][j-1] = 1
            elif old_grid[i][j] == 1 and neighbors == 2:
                grid[i-1][j-1] = 1
            
    img.set_data(grid)
    plt.pause(0.01)
    
    if not plt.fignum_exists(fig.number):
        break

plt.show()