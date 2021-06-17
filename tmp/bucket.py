import boto3
import datetime
import os
import time
import csv
from time import gmtime, strftime
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
import os
from botocore.exceptions import ClientError


s3 = boto3.client('s3')

response = s3.list_buckets()


ses = boto3.client('ses',region_name= 'us-east-1')

csvfile= open('/tmp/volume_report.csv', 'w')
writer = csv.writer(csvfile)
public_policy=[]
buc_name=[]
writer.writerow([
            'Bucket Name',
            'Access Details of Bucket'])



for bucket in response['Buckets']:
   
  try:
    buc_name = bucket["Name"]
    print (buc_name)
    enc = s3.get_public_access_block(Bucket=bucket['Name'])
    #print (enc)
   
    public_policy=enc['PublicAccessBlockConfiguration']['BlockPublicAcls']
    print (public_policy)
   
   
    #enc = s3.get_bucket_encryption(Bucket=bucket['Name'])
    #rules = enc['ServerSideEncryptionConfiguration']['Rules']
    #print('Bucket: %s, Encryption: %s' % (bucket['Name'], rules))

  except ClientError as e:
    if e.response['Error']['Code'] == 'BlockPublicAcls':
      #print('Bucket: %s, no BlockPublicAcls' % (bucket['Name']))
      print(False)
    else:
      #print("Bucket: %s, unexpected error: %s" % (bucket['Name'], e))
      print(False)
      #public_policy=False
    writer.writerow([buc_name,public_policy])


def lambda_handler(event, context):

    date_fmt = strftime("%Y_%m_%d", gmtime())
    #Give your file path
    filepath ='/tmp/volume_report.csv'
    filename ='report_Ireland'
    #Give your filename
    #mail("sadmin@sothebys.com","Sothebyscmssupport@cognizant.com,sadmin@sothebys.com","Sothebys s3 Notification","PFA The s3 lifecycle policy report.",filepath)
    mail("codename.sudipta@gmail.com","codename.sudipta@gmail.com","Clouddevil Volume Notification","PFA The Volume resource on N.california Region.",filepath)
    #s3.Object('pe-ami-report', filename+'_'+str(date_fmt)+'.csv').put(Body=open(filepath, 'rb'))

def mail(fromAddress,toAddress, subject, text, attach):
   
    #Multiple recipients could be there
    ###################################################################
    if(toAddress.find(',') > 1) :
        toAddress = toAddress.split(',')
    else :
        toAddress = list(toAddress.split())
    ###################################################################
   
    CHARSET = "UTF-8"
    msg = MIMEMultipart('alternative')
    msg['From'] = fromAddress
    msg['To'] = ','.join(toAddress)
    msg['Subject'] = subject
    text = MIMEText(text.encode(CHARSET), 'html', CHARSET)
    msg.attach(text)
    if(attach != None) :
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)
    try:
        response = ses.send_raw_email(
            Source=fromAddress,
            Destinations=toAddress,
            RawMessage={
                'Data':msg.as_string(),
            },
        )  
    except Exception as e:
        print("Some Error has occured stating " + str(e))
    else:
        print("Email sent! Message ID: %s" % response['MessageId'])

