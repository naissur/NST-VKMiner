#!/usr/bin/python -t

import vk
import requests
import datetime
import time

class NSTVKFetcher:

	""" Fetches list of friends' id's from VK by reading a batch of 25 lists when necessaty and giving it out one by one.
		Written by NST team.
	"""
	_current_id = 0
	_batch = []
	_vkapi = None
	_time_last_fetched = datetime.datetime.now()
	_FETCH_INTERVAL_SECS = 0.34 					# < THAN A SECOND!

	def __init__(self, app_id, login, password):
		_batch = []
		_current_id = 0
		_time_last_fetched = datetime.datetime.now()
		_FETCH_INTERVAL_SECS = 1.0
		print "NSTVKFetcher: NSTVKFetcher initialized";
		try:
			self._vkapi = vk.API(str(app_id), str(login), str(password))
		except Exception as e:
			raise e
			print "NSTVKFetcher: Could not establish connection."
			print type(e)


	def get_new_id(self):
		self._current_id += 1

	def fetch_ready(self):
		time_now = datetime.datetime.now()
		elapsed = (time_now-self._time_last_fetched).microseconds/(10.0**6)
		if(elapsed > self._FETCH_INTERVAL_SECS):
			return True
		else:
			return False

	def fetch_batch(self):
		try:
			ids = []
			for index in xrange(25):
				self.get_new_id()
				ids.append(self._current_id)
			#ids = ['161629281', 
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   ##'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629281',
				   #'161629284']

			friends = self._vkapi('execute.getFriendsList', id0 = ids[0],
															id1 = ids[1],
															id2 = ids[2],
															id3 = ids[3],
															id4 = ids[4],
															id5 = ids[5],
															id6 = ids[6],
															id7 = ids[7],
															id8 = ids[8],
															id9 = ids[9],
															id10 = ids[10],
															id11 = ids[11],
															id12 = ids[12],
															id13 = ids[13],
															id14 = ids[14],
															id15 = ids[15],
															id16 = ids[16],
															id17 = ids[17],
															id18 = ids[18],
															id19 = ids[19],
															id20 = ids[20],
															id21 = ids[21],
															id22 = ids[22],
															id23 = ids[23],
															id24 = ids[24])

			

			print "NSTVKFetcher: Fetched new batch of friends data"
			res_list = []
			for i in xrange(len(friends)):
				if friends[i]:
					res_list.append( (ids[i], friends[i] ) )
			
			self._batch = res_list

			#self._batch = list((ids[i], friends[i]) for i in xrange(25) )
			self._time_last_fetched = datetime.datetime.now()

		except requests.exceptions.Timeout as e:
			self.fetch_batch() 										# CHANGE, RECURCIION IS BAAD
			print "NSTVKFetcher: Server timed-out, trying again..."

		except requests.exceptions.ConnectionError as e:
			print "NSTVKFetcher: Connection lost. Quitting..."
			raise r
		

	def get_next(self):
		if not (self._batch) :
			print "NSTVKFetcher: Waiting until fetch comes ready..."
			while not self.fetch_ready():
				pass
			print "NSTVKFetcher: Fetched a new batch"

			self.fetch_batch()

		print "NSTVKFetcher: Batch has "+str(len(self._batch))+" entities, popping"

		next_tuple = self._batch.pop()
		#print "NSTVKFetcher: Returning "+str(next_tuple[0])+"'s friends list"
		return next_tuple
