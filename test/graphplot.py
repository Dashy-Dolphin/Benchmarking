import matplotlib.pyplot as plt

import subprocess

loop_count = 200000
mode = 'lock-free'
n_counter = 1
xpoints = [1,2,3,4,5,10,15,20]
#xpoints = [1]
ypoints = []

for x in xpoints:
    n_counter = x
    proc = subprocess.Popen(["hyperfine --warmup 2 \"dune exec ./tx_loc_modes.exe " + str(loop_count) + " " + mode + " " +str(n_counter) +"\" -i --show-output" ], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    out = out.decode()
    value = out.split('\n')[1].split()[4:6]

    if (value[1] != 'ms'):
        value[0]  *= 1000
    ypoints.append(value[0])


    






#xpoints = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,2048,4096,8096, 160192, 320384])

#ypoints = np.array([5767, 2972, 1594 , 874.2 , 537.8 , 342.7  , 390.9, 459.7, 462.6, 461.3, 460.1, 463.7,476.4,461.6 , 483.3,  529.2])
#ypoints = np.array([5762, 2967 ,  1584, 872.4,530.9,  348.0,    379.7,  462.5,459.3, 455.0,459.7, 481.0, 463.2 ])
#ypoints = np.array([    73.4, 78.4, 79.7, 79.8, 81.0,81.8,106.7, 1108,140727])

plt.plot(xpoints, ypoints)
plt.ylabel('Op time in ms')
plt.xlabel('No of Counters')
plt.title('CAS Performance (Lock-free)')

plt.show()

print("\n")
print("xpoints = ",xpoints)
print("ypoints = ", ypoints)

