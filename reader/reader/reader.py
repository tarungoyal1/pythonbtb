
def importable():
    print('I am importable')

def non_importable():
    print('I am not importable')

class Reader:
    
    def __init__(self, filename):
        self.f = open(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()

    def private(self):
        print('I can\'t be imported easily')

