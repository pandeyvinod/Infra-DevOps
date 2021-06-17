for s3_buckets in `aws s3 ls | cut -f 3 -d ' '`
do
  result=`aws s3api get-public-access-block --bucket $s3_buckets  --output json | jq '.PublicAccessBlockConfiguration.RestrictPublicBuckets'` 

    if [ "$result"  == "false" ]
      then 
        `echo "${s3_buckets}" >> public_buckets.csv`
         

    elif [ "$result"  == "true" ]
      then
        `echo  "${s3_buckets}" >> private_buckets.csv`
    else
      echo "\n"
    fi
done

