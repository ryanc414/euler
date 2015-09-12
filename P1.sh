#!/bin/bash
N1=3
N2=5
SUM=0
N_MAX=1000
i=1

while [[ $i -lt $N_MAX ]]
do
    if [[ $i%$N1 -eq 0 ]] || [[  $i%$N2 -eq 0 ]] 
    then
        let SUM+=$i
    fi
    let i++
done

echo $SUM

