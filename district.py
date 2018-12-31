#!/usr/bin/env python3 
import sys
import pymysql
import traceback
import logging
import requests
from bs4 import BeautifulSoup                                            

# def connect():
# 	connection = pymysql.connect(
#     	host='localhost',
#     	user='root',
#     	password='h3llo2u',
#     	db='serviceJobs',
# 	)
# 	return connection

# def insertwords(connection, villages, tahsil_id):
# 	try:
# 		with connection.cursor() as cursor:
# 			counter=0
# 			for village in villages:
# 				sql = "INSERT INTO villages (`name`, `tahsil_id`) VALUES (%s, %s)"
# 				try:
# 					cursor.execute(sql, (village, tahsil_id))
# 					print(village + " added successfully")
# 					counter+=1
# 				except Exception as e:
# 					logging.error(traceback.format_exc())
# 			print(str(counter)+" villages added to tahsil_id="+str(tahsil_id))
	# 	connection.commit()
	# finally:
	# 	connection.close()

# def fetch_villages(url):
# 	page = requests.get(url)
# 	soup = BeautifulSoup(page.content, 'html.parser')
# 	villages_list = soup.find_all('a')
# 	string_list = []
# 	for village in villages_list[3:-1]:
# 	    string_list.append(village.string)
# 	return string_list
			


def main(url):
	# villages= fetch_villages(url)
	# connection  = connect()
	# insertwords(connection, villages, 7)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	list = soup.find_all('a')
	for d in list[1:-1]:
		murl = "http://vlist.in"+d['href']
		print(murl)
		# page = requests.get(murl)
		# soup = BeautifulSoup(page.content, 'html.parser')
		# mlist = soup.find_all('a')
		# for t in mlist[1:-1]:
		# 	turl = "http://vlist.in"+t['href']
		# 	print(turl)


	


if __name__ == '__main__':
	main(sys.argv[1])
	

