import os
from dotenv import load_dotenv
import boto3

load_dotenv()

session = boto3.session.Session()
s3_client = session.client('s3', 
    region_name='sfo3',
    endpoint_url='https://sfo3.digitaloceanspaces.com',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])