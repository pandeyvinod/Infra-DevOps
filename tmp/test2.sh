#!/bin/bash
for s3_buckets in `aws s3 ls | cut -f 3 -d ' '`
do 
  if [ `aws s3api get-public-access-block --bucket cf-templates-hj1c3helgmef-us-east-1 --output json`.PublicAccessBlockConfiguration.RestrictPublicBuckets == "true" ] 
	then
		echo "hello pandey"
  else
	echo "cool man"
  fi
done
