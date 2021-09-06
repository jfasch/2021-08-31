import sys
import matplotlib.pyplot as plt


filename = sys.argv[1]
f = open(filename)

# axes: time, pressure, temperature
time = []
pressure = []
temperature = []

for line in f:
    print('Ganze Zeile:', line)
    line = line.rstrip() # eat off training linefeed ('\n')
    t, p, T = line.split(';')
    time.append(float(t))
    pressure.append(float(p))
    temperature.append(float(T))

# print('time axis:', time)
# print('pressure values:', pressure)
# print('temperature values:', temperature)

plt.plot(time, pressure)
plt.plot(time, temperature)
plt.show()
#plt.savefig('x.jpg')
