#!/usr/bin/python -t

from nstdbkeeper import NSTDBKeeper
from nstvkfetcher import NSTVKFetcher
import sys
import time

def main():
	if len(sys.argv) < 4:
		print "Usage: nstdbcreator <app_id> <login> <password>"
		quit()

	print "NSTDBCreator by NST team"
	app_id = sys.argv[1]
	login = sys.argv[2]
	password = sys.argv[3]


	MAX_ID = 10000
	START_ID = 1

	try:
		fetcher = NSTVKFetcher(app_id, login, password, start_id=START_ID)
		keeper = NSTDBKeeper(maximum_batch_length=2000, clear = False)

	except Exception as e:
		print e
		print "Not initialized, quitting..."
		quit()

	
	total_ids = 0
	total_rels = 0

	for i in xrange(MAX_ID):
		try:
			#res_list = []
			#while res_list == []:
				#(person_id, friend_list) = fetcher.get_next()
				#res_list = []
				#for friend in friend_list:
					#if friend < person_id:
						#res_list.append(friend)
			res_list = []
			while res_list == []:  #add only people with 1 or more friends
				(person_id, friend_list) = fetcher.get_next()
				if friend_list:    #if friend_list is empty, no need to go on
					res_list = list( friend_id for friend_id in friend_list if (friend_id < person_id) and (friend_id > START_ID))
				else:
					continue

			print "NSTDBCreator: now at node",person_id
			keeper.insert(person_id, res_list)
			total_ids += 1
			total_rels += len(res_list)
		except Exception as e:
			print e
			print "Stopped fetching due to exception. Quitting..."
			quit()

	print "NSTDBCreator: total ids fetched: ",total_ids
	print "NSTDBCreator: total relationships fetched: ",total_rels
	del fetcher
	del keeper

if __name__ == "__main__":
	main()
