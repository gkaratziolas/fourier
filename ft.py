"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def complex_to_array(c):
	a = np.array([[],[]])
	for n in c:
		a = np.append(a, [[np.angle(n)], [np.absolute(n)]], axis=1)
	return a

fig = plt.figure()
ax = fig.add_subplot(312, projection='polar')

ax2 = fig.add_subplot(311)

ax3 = fig.add_subplot(313)


def g(t):
	return np.cos(4*t)+1# + np.cos(3*t)
	#return np.cosh(t)
	#return np.cos(t)*np.sin(10*t)

def centre_of_mass(c):
	m = 0
	for n in c:
		m += n
	return m/len(c)

t = np.arange(0, 6*np.pi, 0.01)
w=0.00

ax2.plot(g(t))

data = [g(t)*np.e**(1j*w*t), centre_of_mass(g(t)*np.e**(1j*w*t)), np.array([[0],[0]])]

lines = []
line, = ax.plot(1)
lines.append(line)
line, = ax.plot(1, "ro")
lines.append(line)
line, = ax3.plot(1)
lines.append(line)
#line, = ax.plot(1)
ax.set_rmax(2)
ax.set_rticks([])
ax3.set_xlim([0, 10])
ax3.set_ylim([-1, 1])


def animate(w):
	data[0] = g(t)*np.e**(1j*(w)*t)
	com = centre_of_mass(data[0])
	data[1] = [com]
	ft = np.array([[w], [com.real]])

	data[2] = np.append(data[2], ft, axis=1)

	#ax.plot(centre_of_mass(b))

	lines[0].set_data(complex_to_array(data[0]))
	lines[1].set_data(complex_to_array(data[1]))
	lines[2].set_data(data[2])

	return lines


ani = animation.FuncAnimation(fig, animate, np.arange(0, 10, 0.01),
                              interval=25, blit=True, repeat=False)

plt.show()