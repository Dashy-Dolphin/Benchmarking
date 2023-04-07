import subprocess
import sys

loop_count = 200000
mode = 'obstruction-free'
n_counter = sys.argv[1]
n_accumulators = sys.argv[2]


perf_count = 10

xpoints = [1250, 1150, 1050, 950, 850, 750, 650, 550, 450]
ypoints = []

for x in xpoints:
   
        print ("obstruction-free with sleep time = ", x, "ms")
    
      
        avg_miss_rate = float(0.0)

        for lp in range(perf_count):
            proc = subprocess.Popen(["perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations  dune exec ./tx_loc_modes.exe " + str(loop_count) + " " + mode + " " +str(n_counter) +" "+ str(n_accumulators) + " " + str(x) ], stdout=subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
        
            (out, err) = proc.communicate()

        
        
            err = err.decode()
        
            
        
            err = err.split('\n')
            
            err = err[6]
            err = err.split(' ')
            i= 0
            while 1:
                if err[i] == '%':
                    break

                i=i+1

            err = err[i - 1]
           
            avg_miss_rate = avg_miss_rate + float(err)
        
        avg_miss_rate = avg_miss_rate/perf_count
        ypoints.append(avg_miss_rate)

print("xpoints = ",xpoints)
print("ypoints = ", ypoints)


