# this script will list the public and private s3 buckets from your region
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3
import os
import time
import csv
import pprint
from botocore.configprovider import create_botocore_default_config_mapping
from botocore.exceptions import ClientError

from botocore.retries import bucket
# function from another file - ses email file
from ses_rawemail import * 

s3 = boto3.client('s3')
ses = boto3.client('ses', region_name='us-east-1')

csv_file = open('/tmp/volume_report.csv', 'w')
writer = csv.writer(csv_file)
public_policy = []
buc_name = []
writer.writerow(['Bucket Name', 'Access Details of Bucket'])

list_buckets = s3.list_buckets()
list = list_buckets['Buckets']

for buckets in list_buckets['Buckets']:
    try:
        buc_name = buckets["Name"]
        print(buc_name)
        #writer.writerow([buc_name])
        enc = s3.get_public_access_block(Bucket=buc_name)
        public_policy=enc['PublicAccessBlockConfiguration']['BlockPublicAcls']
        print(public_policy)
        writer.writerow([buc_name,public_policy])
    except ClientError as e:
        if e.response['Error']['Code'] == 'BlockpublicAcls':
            print('Bucket: %s, no BlockPublicAcls' % (buckets['Name']))
        else:
            print("Bucket: %s, unexpected error: %s" % (buckets['Name'], e))
        
csv_file.close()
def lambda_handler(event, context):
    date_fmt = time.strftime("%Y_%m_%d", time.gmtime())
    # give your file path
    filepath = '/tmp/volume_report.csv'
    filename = 'report_ireland'
    mail("pandeyvinod.india@gmail.com","pandeyvinod.india@gmail.com")

mail("pandeyvinod.india@gmail.com","pandeyvinod.india@gmail.com")
        