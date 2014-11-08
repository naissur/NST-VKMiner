#!/usr/bin/python -t

from py2neo import neo4j
from py2neo.neo4j import Node
from py2neo.neo4j import Relationship
from py2neo import node
from py2neo import rel

class NSTDBKeeper:

	""" Creates database.
		To be used in connection with NSTVKFetcher.
		Written by NST team.
	"""
	""" Main connection to database
	"""
	_graph_db = None
	_batch = None
	_nodes_index = None
	_rels_index = None
	MAXIMUM_BATCH_LENGTH = None
	_counter = 0
	

	def __init__(self, maximum_batch_length):
		try:
			self._graph_db = neo4j.GraphDatabaseService()
			self._batch = neo4j.WriteBatch(self._graph_db)
			self._graph_db.clear()
			self._nodes_index = self._graph_db.get_or_create_index(neo4j.Node, "nodes_index")
			self._rels_index = self._graph_db.get_or_create_index(neo4j.Relationship, "rels_index")
			self.MAXIMUM_BATCH_LENGTH = maximum_batch_length
			print "NSTDBKeeper: NSTDBKeeper initialized"
		except Exception as e:
			print "NSTDBKeeper: Exception in DB init"
			print e
			raise e


	def insert(self, personId, friendList):
		id_node = self._batch.get_or_create_in_index(neo4j.Node, self._nodes_index, "vk_id", personId, node(id=personId))
		self._counter += 1
		for friend_id in friendList:
			friend_node = self._batch.get_or_create_in_index(neo4j.Node, self._nodes_index, "vk_id", friend_id, node(id=friend_id))
			self._batch.get_or_create_in_index(neo4j.Relationship, self._rels_index, "rel_id", str(min(personId,friend_id))+"_"+str(max(personId, friend_id)), rel(id_node, "FRIEND", friend_node))
			self._counter += 2
		if self._counter >= self.MAXIMUM_BATCH_LENGTH: 
			print "NSTDBKeeper: Batch is full, running transaction"
			self._batch.run()
			self._batch.clear()   # Clears all batch requests
			self._counter = 0
	

	def __del__(self):
		print "NSTDBKeeper: Running the last transaction"
		self._batch.run()
		print "Successfully destroyed NSTDBKeeper"
