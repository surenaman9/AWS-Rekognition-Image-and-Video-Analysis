#importing csv
import csv
import boto3

with open('new_user_credentials (1).csv','r') as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[2]
        secret_access_key=line[3]

photo='tree.jpg'
client=boto3.client('rekognition',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
with open(photo,'rb') as source_image:
    source_byte=source_image.read()

response=client.detect_labels(Image={'Bytes':source_byte},MaxLabels=10)
print(response)