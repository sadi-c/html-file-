###create a Python program that saves some data to AWS S3.###
import boto3
import logging
s3_client = boto3.client('s3')

class HtmlDocument:
    def __init__(self,content):
        self.content =content
    def __str__(self):
        return f"CODE: {self.content}"
        
class HtmlManager:
    def __init__(self):
        self.mydocument=None

    def create_file(self):
        content = """

    <html>
    <head>
        <title>{0}</title>
    </head>
    <body>
    
    <p>Hello, my name is Sadika!</p>
    
    </body>
    </html>



    """

        newdoc=HtmlDocument(content)
        self.mydocument = newdoc

    def save_file(self):
        with open("newdoc.html", "w") as file:
            file.write(self.mydocument.content)


             


    class AWSmanager:
        def __init__(self):

            pass
        

        def saveS3(self):
            boto3.client('s3').upload_file('sadikahtmlcode.html', 'lmtd-class', 'sadikahtmlcode.html')

            

manager =HtmlManager()

manager.create_file()
manager.save_file()

awsmanager=AWSmanager()
awsmanager.saveS3()

    







