#!/usr/bin/env python3 
import sys
import pymysql
import traceback
import logging

def connect():
	connection = pymysql.connect(
    	host='localhost',
    	user='root',
    	password='h3llo2u',
    	db='vocabulary',
	)
	return connection

def insertwords(connection, words_dict):
	try:
		with connection.cursor() as cursor:
			for word, meaning in words_dict.items():
				sql = "INSERT INTO word_meaning (`word`, `meaning`) VALUES (%s, %s)"
				try:
					cursor.execute(sql, (word, meaning))
					print(word + " added successfully")
				except Exception as e:
					logging.error(traceback.format_exc())
		connection.commit()
	finally:
		connection.close()

def fetch_words(filename):
	with open(filename) as f:
		dictionary = {}
		for line in f:
			wordlist = line.split()
			word = wordlist[0]
			meaning = " ".join(wordlist[1:])
			dictionary[word] = meaning
		return dictionary
			


def main(filename):
	# word_meanings= fetch_words(filename)
	# connection  = connect()
	# insertwords(connection, word_meanings)

	


if __name__ == '__main__':
	main(sys.argv[1])
	

