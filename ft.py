import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal

TMAX  = 6*np.pi
TSTEP = 0.01
WMAX  = 10
WSTEP = 0.01

def complex_to_array(c):
	"""converts complex numbers to (2,1) np array of reals"""
	a = np.array([[],[]])
	for n in c:
		a = np.append(a, [[np.angle(n)], [np.absolute(n)]], axis=1)
	return a

def g(t):
	"""Returns a predefined function of time for a given time vector"""
	#return signal.sawtooth(3*t, width=0.5)+1
	return np.cos(4*t) + np.cos(3*t) + 1
	#return np.cosh(t)
	#return np.cos(t)*np.sin(10*t)

def centre_of_mass(c):
	"""Returns the mean of a set of complex values"""
	m = 0
	for n in c:
		m += n
	return m/len(c)

fig = plt.figure()

ax2 = fig.add_subplot(2,2,1)
ax = fig.add_subplot(223, projection='polar')
ax3 = fig.add_subplot(224)





t = np.arange(0, TMAX, TSTEP)

ax2.plot(g(t))

data = [g(t)*np.e**(1j*0.0*t), centre_of_mass(g(t)*np.e**(1j*0.0*t)), np.array([[],[]])]

lines = []
line, = ax.plot(1)
lines.append(line)
line, = ax.plot(1, "ro")
lines.append(line)
line, = ax3.plot([],[])
lines.append(line)

ax.set_rmax(max(g(t))*1.1)
ax.set_rticks([])
ax3.set_xlim([0, WMAX])
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


ani = animation.FuncAnimation(fig, animate, np.arange(0, WMAX, WSTEP),
                              interval=25, blit=True, repeat=False)

plt.show()