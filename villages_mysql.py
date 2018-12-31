#!/usr/bin/env python3 
import sys
import pymysql
import traceback
import logging
import requests
from bs4 import BeautifulSoup                    
import time
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()                     

def connect():
	connection = pymysql.connect(
    	host='localhost',
    	user='root',
    	password='h3llo2u',
    	db='serviceJobs',
	)
	return connection

def insertwords(connection, tahsil, city_id, turl):
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO tahsil (`name`, `city_id`, `tahsil_url`) VALUES (%s, %s, %s)"
			try:
				cursor.execute(sql, (tahsil, city_id, turl))
				print("Added to database, tahsil = "+tahsil+", city_id = "+str(city_id))
			except Exception as e:
				logging.error(traceback.format_exc())
		connection.commit()
	finally:
		connection.close()

def insertCity(connection, city_name, state_id, city_url):
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO cities (`city`, `state_id`, `city_url`) VALUES (%s, %s, %s)"
			try:
				cursor.execute(sql, (city_name, state_id, city_url))
				print("Added to database, city = "+city_name+", state_id = "+str(state_id))
			except Exception as e:
				logging.error(traceback.format_exc())
		connection.commit()
	finally:
		connection.close()

def insertVillage(connection, village_name, tahsil_id):
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO villages (`name`, `tahsil_id`) VALUES (%s, %s)"
			try:
				cursor.execute(sql, (village_name, tahsil_id))
				print("Added to database, village = "+village_name+", tahsil_id = "+str(tahsil_id))
			except Exception as e:
				logging.error(traceback.format_exc())
		connection.commit()
	finally:
		connection.close()

def UpdateCityUrl(connection, city_url, city_id):
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE cities SET `city_url`=%s WHERE `id` = %s"
			try:
				cursor.execute(sql, (city_url, city_id))
				print("Updated, city_id = "+str(city_id))
			except Exception as e:
				logging.error(traceback.format_exc())
		connection.commit()
	finally:
		connection.close()

def UpdateTahsilUrl(connection, tahsil_url, tahsil_id):
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE tahsil SET `tahsil_url`=%s WHERE `id` = %s"
			try:
				cursor.execute(sql, (tahsil_url, tahsil_id))
				print("Updated, tahsil_id = "+str(tahsil_id))
			except Exception as e:
				logging.error(traceback.format_exc())
		connection.commit()
	finally:
		connection.close()

def readData(connection, state_id):
	cities = {}
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM cities WHERE `state_id` = "+str(state_id)
			try:
				cursor.execute(sql)
				result = cursor.fetchall()
				for row in result:
					cities[row[0]]=str(row[1])
			except:
				print("Oops! Something wrong")
		connection.commit()
	finally:
		connection.close()
	return cities

def readAllCities(connection):
	# name and cityurl
	cities = {}
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM cities"
			try:
				cursor.execute(sql)
				result = cursor.fetchall()
				for row in result:
					cities[row[1]]=str(row[3])
			except:
				print("Oops! Something wrong")
		connection.commit()
	finally:
		connection.close()
	return cities

def readAllTahsil(connection):
	# id and url
	tahsils = {}
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM tahsil WHERE tahsil_url!=''"
			try:
				cursor.execute(sql)
				result = cursor.fetchall()
				for row in result:
					tahsils[row[0]]=str(row[3])
			except:
				print("Oops! Something wrong")
		connection.commit()
	finally:
		connection.close()
	return tahsils

def fetch_cities(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	city_list = soup.find_all('a')
	city_url_string = {}
	for city in city_list[1:-1]:
		city_url_string[city.string] = "http://vlist.in"+city['href']
	return city_url_string

def fetch_states_urls(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	state_list = soup.find_all('a')
	state_urls = []
	for state in state_list[:-1]:
		state_urls.append("http://vlist.in"+state['href'])
	return state_urls

def fetch_tahsil(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	tahsil_list = soup.find_all('a')
	tahsil_url_string = {}
	for tahsil in tahsil_list[2:-1]:
		tahsil_url_string[tahsil.string] = "http://vlist.in"+tahsil['href']
	return tahsil_url_string

def fetch_villages(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	village_list = soup.find_all('a')
	village_name = []
	for village in village_list[3:-1]:
		village_name.append(village.string)
	return village_name

			


def main():
	# connection  = connect()
	# dbAllcities = readAllCities(connection)

	connection  = connect()
	dbAllTahsils = readAllTahsil(connection)
	for tahsil_id, tahsil_url in dbAllTahsils.items():
		villages = fetch_villages(tahsil_url)
		for village in villages:
			connection  = connect()
			insertVillage(connection, village, tahsil_id)
		time.sleep(5)


	# for city_name, city_url in dbAllcities.items():
	# 	if len(city_url)>0:
	# 		dcityname = ''.join(e for e in city_name if e.isalnum())
	# 		# print("city_name="+str(city_name)+"city_url="+city_url)
	# 		url = page = requests.get(city_url)
	# 		soup = BeautifulSoup(page.content, 'html.parser')
	# 		tahsil_list = soup.find_all('a')
	# 		for t in tahsil_list[2:-1]:
	# 			otahsilname = ''.join(e for e in t.string if e.isalnum())
	# 			finalTahsilId=0
	# 			for db_tid, db_tname in dbAllTahsils.items():
	# 				dtname = ''.join(e for e in db_tname if e.isalnum())
	# 				if similar(otahsilname.lower(), dtname.lower())>0.95:
	# 					finalTahsilId=db_tid
	# 					break
	# 			if finalTahsilId>0:
	# 				connection  = connect()
	# 				UpdateTahsilUrl(connection, "http://vlist.in"+t['href'], finalTahsilId)
	# 		time.sleep(5)
			



	# states_url = fetch_states_urls(url)
	# for state in states_url:
	# 	page = requests.get(state)
	# 	soup = BeautifulSoup(page.content, 'html.parser')
	# 	district_list = soup.find_all('a')
	# 	for d in district_list[1:-1]:
	# 		# print(d.string+", "+"http://vlist.in"+d['href'])
	# 		dcityname = ''.join(e for e in d.string if e.isalnum())
	# 		finalCityId=0
	# 		for city_id, city_name in dbAllcities.items(): 
	# 			cyn = ''.join(e for e in city_name if e.isalnum())
	# 			if similar(dcityname.lower(), cyn.lower())>0.9:
	# 				# print("city_id="+str(city_id)+"city_name="+d.string)
	# 				finalCityId=city_id
	# 				break
	# 		if finalCityId>0:
	# 			# insert city url of this city
	# 			connection  = connect()
	# 			UpdateCityUrl(connection, "http://vlist.in"+d['href'], finalCityId)
	# 	time.sleep(5)


	# # villages= fetch_villages(url)
	# connection  = connect()
	# # insertwords(connection, villages, city_id)
	# dbcities = readData(connection, state_id)
	# print(dbcities)
	# print("---------------------")
 

	# for fcity_n, fcityurl in cities.items():
	# 	cy = ''.join(e for e in fcity_n if e.isalnum())
	# 	finalCityId=0
	# 	for city_id, city_name in dbcities.items():
	# 		cyn = ''.join(e for e in city_name if e.isalnum())
	# 		if similar(cy.lower(), cyn.lower())>0.9:
	# 			finalCityId=city_id
	# 			print("CN="+city_name+", CID="+str(city_id)+", DBCity="+fcity_n+", "+fcityurl)
	# 			break
	# 	if finalCityId==0:
	# 	    continue		
	# 	time.sleep(5)
	# 	tahsils_dict = fetch_tahsil(fcityurl)
	# 	for t in tahsils_dict:
	# 		connection  = connect()
	# 		insertwords(connection, t.string, city_id)
	
	# 	# for t in tahsils:
	# 	# 	print(t.string+", city_id="+str(finalCityId)+", city_name="+fcity_n)
	# 	# 	insertwords()
	# 	print("---------------------------")

if __name__ == '__main__':
	main()
	

