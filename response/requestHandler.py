class MockFile():
    def read():
        return False

class RequestHandler():
    def __init__(self):
        self.content_type = ""
        self.contents = MockFile()

    def getContents(self):
        return self.contents.read()

    def read(self):
        return self.contents

    def setStatus(self, status):
        self.status = status

    def getStatus(self) -> int:
        return self.status

    def getContentType(self) -> str:
        return self.content_type

    def getType(self):
        return 'Static'
