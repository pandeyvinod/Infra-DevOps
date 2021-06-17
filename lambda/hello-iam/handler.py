
import os


def hello(event, context):
    print("hello world")
    return os.environ['FIRST_NAME']


