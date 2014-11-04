#!/usr/bin/python -t

import vk
import requests

class NSTVKFetcher:

	""" Fetches list of friends' id's from VK by reading a batch of 25 lists when necessaty and giving it out one by one.
		Written by NST team.
	"""
	_batch = []
	_vkapi = None

	def __init__(self, app_id, login, password):
		_batch = []
		print "NSTVKFetcher: NSTVKFetcher initialized";
		try:
			self._vkapi = vk.API(str(app_id), str(login), str(password))
		except Exception as e:
			raise e
			print "NSTVKFetcher: Could not establish connection."
			print type(e)

	def get_next(self):
		if not (self._batch) :
			print "NSTVKFetcher: Creating new batch..."
			self._batch = [(1, [2,3,4,5]), (2, [4,5,6,7]), (3, [10,12,14,15])]

		print "NSTVKFetcher: Batch has "+str(len(self._batch))+" entities, popping"

		next_tuple = self._batch.pop()
		print "NSTVKFetcher: Returning "+str(next_tuple[0])+"'s friends list"
		return next_tuple
