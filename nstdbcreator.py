#!/usr/bin/python -t

from nstdbkeeper import NSTDBKeeper
from nstvkfetcher import NSTVKFetcher

def main():
	print "NSTDBCreator by NST team"
	keeper = NSTDBKeeper()
	fetcher = NSTVKFetcher()

	(person_id, frient_list) = fetcher.get_next()
	keeper.insert(person_id, frient_list)

if __name__ == "__main__":
	main()
