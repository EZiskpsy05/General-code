import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# First equation for Red Bird: 

fig, ax = plt.subplots()

# Define the quadratic function
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = -2*(t-3)**2 + 15

# Create scatter plot and line plot of the function
scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2, = ax.plot(t, z, label=f'v0 = {v0} m/s')

ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Distance', ylabel='Height')
ax.legend()

# Set the animation parameters
interval = 30  # Interval between frames in milliseconds
num_frames = len(t)  # Number of frames in the animation
frame_interval = 0.05  # Time interval between frames in seconds
current_frame = 0  # Index of the current frame

def update(frame):
    global current_frame
    
    # Calculate the time corresponding to the current frame
    t_current = current_frame * frame_interval
    
    # Update the scatter plot and line plot with data corresponding to the current time
    x = t[t <= t_current]
    y = -2*(x-3)**2 + 15 + v0 * x
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    line2.set_xdata(x)
    line2.set_ydata(y)
    
    # Increment the current frame index
    current_frame += 1
    
    # Return the artists that have been updated
    return (scat, line2)

# Create the animation and display it
ani = animation.FuncAnimation(fig=fig, func=update, frames=num_frames, interval=interval)
plt.show()