import sys
def readseries(filename):
	with open(filename, mode='rt') as f:
		return [int(line.strip()) for line in f]

def main(filename):
	series = readseries(filename)
	print(series)


if __name__ == '__main__':
    main(filename=sys.argv[1])