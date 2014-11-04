#!/usr/bin/python -t

from nstdbkeeper import NSTDBKeeper
from nstvkfetcher import NSTVKFetcher
import sys

def main():
	if len(sys.argv) < 4:
		print "Usage: nstdbcreator <app_id> <login> <password>"
		quit()

	print "NSTDBCreator by NST team"
	app_id = sys.argv[1]
	login = sys.argv[2]
	password = sys.argv[3]

	try:
		fetcher = NSTVKFetcher(app_id, login, password)
		keeper = NSTDBKeeper()
	except Exception as e:
		print e
		print "Not initialized, quitting..."
		quit()

	(person_id, frient_list) = fetcher.get_next()
	keeper.insert(person_id, frient_list)

if __name__ == "__main__":
	main()
