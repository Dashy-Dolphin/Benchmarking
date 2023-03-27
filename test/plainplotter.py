import matplotlib.pyplot as plt

xpoints =  [1, 2, 3, 4, 5, 8, 10, 13, 15]
ypoints =  [1482.0, 807.8, 624.6, 508.3, 521.6, 522.6, 562.6, 602.9, 642.1]





plt.plot(xpoints, ypoints,color = 'r',label = 'lock-free')


xpoints =  [1, 2, 3, 4, 5, 8, 10, 13, 15]
ypoints =  [1502.0, 777.9, 545.1, 493.6, 512.9, 529.5, 559.8, 612.9, 670.6]





plt.plot(xpoints,ypoints , color = 'b',label = 'obstruction-free')
plt.ylabel('Op time in ms')
plt.xlabel('No of Counters')
plt.title('Read  Performance (Sasi)')
plt.legend()

plt.show()


