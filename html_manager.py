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
        with open("sadika.html", "w") as file:
            file.write(self.mydocument.content)

