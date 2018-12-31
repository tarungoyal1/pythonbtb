print('exectuing the directory with __name__ = {}'.format(__name__))

import sys
import reader.reader

r = reader.reader.Reader('reader/reader/reader.py')
print(r.read())
