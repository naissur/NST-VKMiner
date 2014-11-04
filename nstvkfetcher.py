#!/usr/bin/python -t

class NSTVKFetcher:

	""" Fetches list of friends' id's from VK and has internal id counter.
		Written by NST team.
	"""
	_id = 0

	def __init__(self):
		self._id = 0
		print "NSTVKFetcher: NSTVKFetcher initialized";

	def get_next(self):
		self._id += 1


		res_id = self._id
		print "NSTVKFetcher: Returning "+str(self._id)+"'s friends list..."
		res_list = [self._id]
		return (res_id, res_list)
