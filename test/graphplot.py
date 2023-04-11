import subprocess
import sys

loop_count = 200000
n_counter = sys.argv[1]
n_accumulators = sys.argv[2]

left = int(sys.argv[3])
right = int( sys.argv[4])


sleep = []
while (left != right):
      sleep.append(left)
      left = int(left) + 50

sleep.append(right)
sleep = sleep[::-1]
      

ypoints = []

mode = 'obstruction-free'

for t1 in sleep:
      
        print ("obstruction-free with sleep time = ", t1, "ms")
      
        proc = subprocess.Popen(["hyperfine --warmup 2 \"dune exec ./tx_loc_modes.exe " + str(loop_count) + " " + mode + " " +str(n_counter) +" "+str(n_accumulators) + " " + str(t1)+"\" -i" ], stdout=subprocess.PIPE, shell=True)
      
        (out, err) = proc.communicate()

       
        out = out.decode()
        value = out.split('\n')[1].split()[4:6]
        value[0] = float(value[0])
        if (value[1] != 'ms'):
            value[0]  *= 1000
        ypoints.append(value[0])



print("xpoints = ",sleep)
print("ypoints = ", ypoints)









