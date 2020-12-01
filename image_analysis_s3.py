#importing csv
import csv
import boto3

with open('new_user_credentials (1).csv','r') as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[2]
        secret_access_key=line[3]

photo='mobile.png'
client=boto3.client('rekognition',region_name='eu-west-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)

response=client.detect_labels(Image={'S3Object': {
            'Bucket': 'naman-sure',
            'Name': photo
        }},MaxLabels=10)
print(response)