import sys
from itertools import islice, count

def sequence():
	"""Generate Racaman's sequence."""
	seen=set()
	a=0
	for n in count(1):
		yield a
		seen.add(a)
		c = a-n
		if c<0 or c in seen:
			c = a + n
		a=c

def writeseqeunce(filename, num):
	f = open(filename, mode='wt', encoding='utf-8')
	f.writelines("{0}\n".format(r) for r in islice(sequence(), num+1))
	f.close()


if __name__ == '__main__':
	writeseqeunce(sys.argv[1], int(sys.argv[2]))