###create a Python program that saves some data to AWS S3.###


from html_manager import HtmlManager
from AWS_manager import AWSmanager

             


   

manager =HtmlManager()

manager.create_file()
manager.save_file()

awsmanager = AWSmanager()
awsmanager.saveS3()

    







