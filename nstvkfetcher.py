#!/usr/bin/python -t

class NSTVKFetcher:

	""" Fetches list of friends' id's from VK and has internal id counter.
		Written by NST team.
	"""
	_id = 0

	def __init__(self):
		self._id = 0
		print "NSTVKFetcher: NSTVKFetcher initialized";

	def get_next_id(self): 
		print "NSTVKFetcher: Incrementing id..."
		self._id += 1
		return str(self._id)

	def get_friends_list(self, id):
		print "NSTVKFetcher: Returning "+id+"'s friends list..."
		result = []
		result.append(id)
		return result
