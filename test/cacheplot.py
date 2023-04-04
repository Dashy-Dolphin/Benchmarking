import subprocess
import sys

loop_count = 200000
mode = 'obstruction-free'
n_counter = 1



xpoints = [1,2,3,4,5,8,10,13,15,18,20,23,25,27,30,33, 35]
ypoints = []
sleep = [85,150,250, 350, 450 , 550, 650, 750, 850, 950]

for t1 in sleep:
    ypoints = []
    print ("obstruction-free with sleep time = ", t1, "ms")
    for x in xpoints:
        print(x)
        n_counter = x
        proc = subprocess.Popen(["perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations  ../_build/default/test/tx_loc_modes.exe " + str(loop_count) + " " + mode + " " +str(n_counter) +" " + str(t1) ], stdout=subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
      
        (out, err) = proc.communicate()

       
      
        err = err.decode()
     
        
    
        err = err.split('\n')
     
        err = err[4]
        err = err.split(' ')
        err = err[36]
        print(err)
        input()


    print("xpoints = ",xpoints)
    print("ypoints = ", ypoints)
