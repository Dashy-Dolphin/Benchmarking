#!/bin/sh
loop_count=200000
mode='obstruction-free'
n_counter_list="1 2 3 4 5 8 10 13 15 18 20 23 25 27 30 33 35"
sleep_time=850


for n_counter in $n_counter_list
do 
    perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations hyperfine --warmup 2 "dune exec ./tx_loc_modes.exe $loop_count $mode $n_counter $sleep_time" -i
done

mode='lock-free'

for n_counter in $n_counter_list
do 
    perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations hyperfine --warmup 2 "dune exec ./tx_loc_modes.exe $loop_count $mode $n_counter $sleep_time" -i
done