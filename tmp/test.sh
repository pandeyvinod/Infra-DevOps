#!/bin/zsh
for s3_buckets in `aws s3 ls | cut -f 3 -d ' '`
do
  printf  $s3_buckets
  #`aws s3a --bucket "$s3_buckets"`
  `aws s3api put-public-access-block  --bucket "$s3_buckets"  --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"`
  echo "\n"
done

