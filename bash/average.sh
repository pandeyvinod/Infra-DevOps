#!/bin/bash
sum=0
read -p "how many numbers: " choice 
for i in $(seq 1 $choice)
do
  read -p  "enter the $i number: " numbers
  sum=`expr $sum +  $numbers`
done

echo "your total number is $sum"
avg=$(echo "scale=3; $sum / $choice "| bc )
printf %.3f $avg
