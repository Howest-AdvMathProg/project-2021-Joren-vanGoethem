import json
import queue
import threading
import socket
# pylint: disable=no-name-in-module
from util.logger import Log

class Backend(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self, daemon=True)

        self._queue = queue.Queue()
        self._running = True

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = '127.0.0.1'
        self.port = port

    @property
    def queue(self):
        return self._queue

    @property
    def running(self):
        return self._running

    def run(self):
        Log.info('BACKEND', 'Running')

        self.s.connect((self.host, self.port))
        
        msg = "Bonjour"

        self.s.sendall(bytes('%4d' % len(msg), 'utf-8'))
        self.s.sendall(bytes(msg, 'utf-8'))

        while self._running:
            size = int(self.s.recv(4))
            if not size:
                continue
            # read data
            data = self.s.recv(size)

            Log.verbose('BACKEND', data)

            # parse the message
            msg = json.loads(data.decode("utf8"))
            # put the message in the queue
            self.queue.put(msg)

    def terminate(self):
        Log.info('BACKEND', 'Terminating...')

        self._running = False