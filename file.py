import sys

def main(filename):
	f = open(filename, mode='r')
	for line in f:
		print(line)

if __name__== '__main__':
	main(sys.argv[1])
