import matplotlib.pyplot as plt
xpoints =  [1, 2, 3, 4, 5, 8, 10, 13, 15, 18, 20, 23, 25, 27, 30, 33, 35]
ypoints =  [86.4, 91.0, 87.4, 86.1, 85.5, 87.7, 87.4, 88.8, 86.4, 85.1, 90.3, 85.3, 88.6, 86.1, 87.7, 87.9, 87.3]

plt.plot(xpoints, ypoints,color = 'r',label = 'hybirid_100')


xpoints =  [1, 2, 3, 4, 5, 8, 10, 13, 15, 18, 20, 23, 25, 27, 30, 33, 35]
ypoints =  [ 87.6, 86.8, 90.1, 88.6, 85.9, 88.3, 86.6, 90.2, 88.1, 85.5, 89.4, 87.5, 90.0, 90.1, 86.8, 88.3, 87.9]

plt.plot(xpoints,ypoints , color = 'b',label = 'hybirid_500')



xpoints =  [1, 2, 3, 4, 5, 8, 10, 13, 15, 18, 20, 23, 25, 27, 30, 33, 35]
ypoints =  [ 87.3, 88.7, 85.6, 89.6, 88.0, 86.4, 88.0, 86.3, 83.4, 89.4, 89.1, 86.1, 88.6, 86.1, 87.4, 93.4, 84.8]

plt.plot(xpoints,ypoints , color = 'g',label = 'hybirid_1000')


plt.ylabel('Op time in ms')
plt.xlabel('No of Accumulators')
plt.title('CAS  Performance (Church)')
plt.legend()

plt.show()


