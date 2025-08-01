
class MyownException(Exception):

    def __init__(self,message):
        self.message=message
        super().__init__(self,message)

def testmethod(inp):
    try:
        if isinstance(inp,int):
            return inp**2
        raise MyownException("Input must be integer")
    except MyownException as e:
        return f"exception raise:{e.message}"


print(testmethod('40'))



