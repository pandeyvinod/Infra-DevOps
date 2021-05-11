#!/bin/bash
sum=0
while  read $num
do
  #read -p  "enter the $i number: " numbers
  sum=`expr $sum +  $num`
done < num.txt

echo "your total number is $sum"
avg=$(echo "scale=3; $sum / $num "| bc )
printf %.3f $avg
