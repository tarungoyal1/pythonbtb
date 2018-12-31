#!/usr/bin/env python3 
import sys
from random import shuffle
from itertools import islice
def fetch_words(filename):
	"""It fetches a list of words from a url

	Args: 
		url: URL of utf-8 text document

	Return:
		story_words: A list of string containing words.

	"""
	with open(filename) as allwords:
		raw = [x for x in allwords]
		wordlist = str(raw[0]).split()
		wordlist = [x for x in islice(wordlist, 10000)]
		shuffle(wordlist)
		# wordlist.sort(key=len)

	return wordlist

	# with open(filename) as allwords:
	# 	words = []
	# 	for word in allwords:
	# 		words.append(word.rstrip())
	# return words


def print_items(items):
		print(*items)



def main(url):
	words = fetch_words(url)
	print_items(words)


if __name__ == '__main__':
	url = sys.argv[1] # The 0th arg is module filename
	main(url)
	# 'http://sixty-north.com/c/t.txt'

