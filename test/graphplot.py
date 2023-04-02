import matplotlib.pyplot as plt

import subprocess
import sys

loop_count = 200000
mode = 'obstruction-free'
n_counter = 1



xpoints = [1,2,3,4,5,8,10,13,15,18,20,23,25,27,30,33, 35]
#xpoints = [1]
ypoints = []
sleep= [100, 500, 1000]

for t1 in sleep:

    print ("hybrid mode with sleep time = ", t1, "ms")
    for x in xpoints:
        print(x)
        n_counter = x
        proc = subprocess.Popen(["hyperfine --warmup 2 \"dune exec ./tx_loc_modes.exe " + str(loop_count) + " " + mode + " " +str(n_counter) +" " + str(t1)+"\" -i" ], stdout=subprocess.PIPE, shell=True)
        #proc = subprocess.Popen(["hyperfine --warmup 2 \"dune exec ./tx_readers.exe 36288 " + str(n_counter) + "\""  ], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        out = out.decode()
        value = out.split('\n')[1].split()[4:6]
        value[0] = float(value[0])
        if (value[1] != 'ms'):
            value[0]  *= 1000
        ypoints.append(value[0])


    print("xpoints = ",xpoints)
    print("ypoints = ", ypoints)



    







print("\nLock-free mode\n")
print("xpoints = ",xpoints)
print("ypoints = ", ypoints)

# mode = 'obstruction-free'
# ypoints = []

# for x in xpoints:
#     print(x)
#     n_counter = x
#     proc = subprocess.Popen(["hyperfine --warmup 2 \"dune exec ./tx_loc_modes.exe " + str(loop_count) + " " + mode + " " +str(n_counter) +" " + str(sleep_time)+"\" -i" ], stdout=subprocess.PIPE, shell=True)
#     (out, err) = proc.communicate()

#     out = out.decode()
#     value = out.split('\n')[1].split()[4:6]
#     value[0] = float(value[0])
#     if (value[1] != 'ms'):
#         value[0]  *= 1000
#     ypoints.append(value[0])


# print("\nobstruction-free mode\n")
# print("xpoints = ",xpoints)
# print("ypoints = ", ypoints)