#!/Users/jeffrey/Projects/ChessAI/GibbyServer/env/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import chess, chess.pgn
import argparse
import time
import multiprocessing
import signal
from typing import List
import uuid
from src.utils.translate import Translate
import numpy as np
from socketserver import ThreadingMixIn


# https://stackoverflow.com/questions/54858979/how-to-use-multiprocessing-with-requests-module

HOST = ''
PORT = 8888
THREADS = 10
MANAGER = None

class Query:
	def __init__(self):
		self.fen = None
		self.query_type = None
		self.key = None
		self.evaluation = None
		self.time_start = time.time()

	def get_dict(self):
		return {
			'fen' : self.fen,
			'query_type' : self.query_type,
			'key' : self.key,
			'evaluation' : self.evaluation,
			'ms' : round( (time.time() - self.time_start) * 1000),
		}



class Worker(multiprocessing.Process):
	def __init__(self, job_queue:multiprocessing.Queue, shm):
		super().__init__()
		self._job_queue = job_queue
		self._shm = shm

	def run(self):
		from src.model.value import ValueNetwork, ValueBuilder
		predictor = ValueNetwork(ValueBuilder.build_conv2d_default())
		predictor.load_weights('GibbyServer/src/model/bin/default_gibby.h5')
		print("worker started")
		try:
			while True:
				query:Query = self._job_queue.get()
				board = chess.Board(query.fen)
				matrix = Translate.board_to_matrix3d(board)
				self._shm[query.key] = predictor.predict(np.array	([matrix]))

		except KeyboardInterrupt:
			print("worker killed")

class Manager:
	def __init__(self) -> None:
		# process interupts gracefully
		signal.signal(signal.SIGTERM, self.commit_genocide)

		# spawn workers equal to thread count
		self.workers:List[Worker]  = []
		self.job_queue = multiprocessing.Queue()
		self.shm =  multiprocessing.Manager().dict()

		for _ in range(THREADS):
			p = Worker(self.job_queue, self.shm)
			self.workers.append(p)
			p.start()


	def queue_job(self, job_configuration):
		self.job_queue.put(job_configuration)

	def commit_genocide(self):
		for worker in self.workers:
			worker.join()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class GibbyServer(BaseHTTPRequestHandler):
	"""query using localhost:8888/<pgn>@<queryType>
	<pgn> should have %20 in place of spaces
	"""

	def do_GET(self):
		# check if data is query-able
		try:
			# the first character is always a /, so we skip over it
			data = self.path[1:].split('@')

			# split data into two parts, the query (pgn), and the queryType (policy or value)
			global MANAGER
			query = Query()
			query.fen = data[0].replace('%20', ' ')
			query.query_type = data[1]
			query.key = str(uuid.uuid4())

			MANAGER.queue_job(query)

			while query.key not in MANAGER.shm:
				pass

			query.evaluation = MANAGER.shm[query.key].tolist()
			MANAGER.shm.__delitem__(query.key)

			jsonData = json.dumps(query.get_dict())

			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes('%s' % jsonData,'utf-8'))

		except Exception as e:
			print(e)
		finally:
			pass



#TODO: add argument parsing for port and threads.
if __name__ == "__main__":
	try:
		# appoint manager
		MANAGER = Manager()

		# start the server
		print("SERVER STARTED")
		webServer = ThreadedHTTPServer((HOST, PORT), GibbyServer)
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass
	finally:
		# close the server
		print("SERVER CLOSED")
		webServer.server_close()
