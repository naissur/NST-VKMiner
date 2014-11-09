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
	_batch_ids = []
	_vkapi = None
	_time_last_fetched = datetime.datetime.now()
	_FETCH_INTERVAL_SECS = 0.34 					# < THAN A SECOND!

	def __init__(self, app_id, login, password, start_id=1):
		self._batch = []
		self._current_id = start_id
		self._time_last_fetched = datetime.datetime.now()
		self._FETCH_INTERVAL_SECS = 0.34
		print "NSTVKFetcher: NSTVKFetcher initialized";
		try:
			self._vkapi = vk.API(app_id = str(app_id), user_login = str(login), user_password = str(password), timeout = 30)
		except Exception as e:
			raise e
			print "NSTVKFetcher: Could not establish connection."
			print type(e)


	def get_new_id(self):
		self._current_id += 1

	def fetch_ready(self):
		time_now = datetime.datetime.now()
		elapsed = (time_now-self._time_last_fetched).microseconds/(1e6)
		if(elapsed > self._FETCH_INTERVAL_SECS):
			return True
		else:
			return False

	def fetch_batch(self, get_new_batch = True):
		try:
			if get_new_batch:
				self._batch_ids = []
				for index in xrange(25):
					self.get_new_id()
					self._batch_ids.append(self._current_id)

			friends = self._vkapi('execute.getFriendsList', id0 = self._batch_ids[0],
															id1 = self._batch_ids[1],
															id2 = self._batch_ids[2],
															id3 = self._batch_ids[3],
															id4 = self._batch_ids[4],
															id5 = self._batch_ids[5],
															id6 = self._batch_ids[6],
															id7 = self._batch_ids[7],
															id8 = self._batch_ids[8],
															id9 = self._batch_ids[9],
															id10 = self._batch_ids[10],
															id11 = self._batch_ids[11],
															id12 = self._batch_ids[12],
															id13 = self._batch_ids[13],
															id14 = self._batch_ids[14],
															id15 = self._batch_ids[15],
															id16 = self._batch_ids[16],
															id17 = self._batch_ids[17],
															id18 = self._batch_ids[18],
															id19 = self._batch_ids[19],
															id20 = self._batch_ids[20],
															id21 = self._batch_ids[21],
															id22 = self._batch_ids[22],
															id23 = self._batch_ids[23],
															id24 = self._batch_ids[24])

			

			#print "NSTVKFetcher: Fetched new batch of friends data"
			#res_list = []
			#for i in xrange(len(friends)):
				#if friends[i]:
					#res_list.append( (self._batch_ids[i], friends[i] ) )
			
			#self._batch = res_list
			self._batch = zip(self._batch_ids,friends)   # Should be faster, and so much easier to read. Does'nt handle people with no friends, but that can be done in main program

			#self._batch = list((ids[i], friends[i]) for i in xrange(25) )
			self._time_last_fetched = datetime.datetime.now()

		except requests.exceptions.Timeout as e:
			#self.fetch_batch() 										# CHANGE, RECURCIION IS BAAD
			print "NSTVKFetcher: Server timed-out"
			print "NSTVKFetcher: Stopped at", self.get_new_id()
			print "NSTVKFetcher: Trying again..."
			self.fetch_batch(get_new_batch = False)

		except requests.exceptions.ConnectionError as e:
			print "NSTVKFetcher: Connection lost. Quitting..."
			raise r
		

	def get_next(self):
		if not (self._batch) :
			#print "NSTVKFetcher: Waiting until fetch comes ready..."
			while not self.fetch_ready():
				pass

			self.fetch_batch()
			#print "NSTVKFetcher: Fetched a new batch"

		#print "NSTVKFetcher: Batch has "+str(len(self._batch))+" entities, popping"

		next_tuple = self._batch.pop()
		#print "NSTVKFetcher: Returning "+str(next_tuple[0])+"'s friends list"
		return next_tuple
