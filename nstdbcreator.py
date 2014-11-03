#!/usr/bin/python -t

from nstdbkeeper import NSTDBKeeper
from nstvkfetcher import NSTVKFetcher

def main():
	print "NSTDBCreator by NST team"
	print
	keeper = NSTDBKeeper()
	fetcher = NSTVKFetcher()

	personId = fetcher.get_next_id()
	friendsList = fetcher.get_friends_list(personId)
	keeper.insert(personId, friendsList)

if __name__ == "__main__":
	main()
