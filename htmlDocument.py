import boto3
class HtmlDocument:
    def __init__(self,content):
        self.content =content

class HtmlManager:
    def __init__(self):
        self.mydocument=None

    def create_file(self):
        content = """

        """

        newdoc=HtmlDocument(content)
        self.mydocument = newdoc

    def save_file(self):
        pass


    class AWSmanager:
        def __init__(self):

            pass

        def saveS3(self):
            



    




htmlString = "<div id='title'><a href='/' onclick='referHeader();'>Title</a></div>" 



