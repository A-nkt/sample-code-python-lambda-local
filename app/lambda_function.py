import os

def lambda_handler(event, context):
    bucket = os.environ["BUCKET_NAME"]
    print("bucket :",bucket)
    return "Hello world"