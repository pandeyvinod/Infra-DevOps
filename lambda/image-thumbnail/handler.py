# thumbnail Generator from raw image
import boto3
import cStringIO
import os

size = os.environ.get('THUMBNAIL_SIZE')
s3 = boto3.client('s3')


def s3_thumbnail_generator(event, context):
    print(event)
