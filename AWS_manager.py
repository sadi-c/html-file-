import boto3
import logging



class AWSmanager:
    def __init__(self):
        self.client = boto3.client('s3')
        self.resource = boto3.resource('s3')
        
        
    def listBucketFile(self, bucketName):
        bucket = self.resource.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key)
            
    def saveS3(self):
        self.client.upload_file('sadika.html', 'lmtd-class', 'sadika.html')
        self.listBucketFile("lmtd-class")

            