def format(number):
    try:
    	n = int(number)
        if n is not None:
        	if n<1000:
        		return str(number)
        	elif n>=1000:
            	return "{:.1f}K".format(n/1000)
            elif n>=10000000:
            	pass

def main(num):
    format(num)

if __name__=='__main__':
	main(num)
