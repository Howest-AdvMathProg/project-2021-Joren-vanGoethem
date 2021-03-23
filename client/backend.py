import json
import queue
import socket
import struct
import threading
from handler import EventHandler
# pylint: disable=no-name-in-module
from util.logger import Log

class Backend(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self, daemon=True)

        self._handler = EventHandler(self)
        self._queue = queue.Queue()
        self._running = True

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = host
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

        self._handler.start()

        while self._running:
            size = struct.unpack('>i', self.s.recv(4))[0]
            if not size:
                continue
            # read data
            data = self.s.recv(size)

            Log.verbose('BACKEND', data)

            # parse the message
            msg = json.loads(data.decode("utf8"))
            # put the message in the queue
            self.queue.put(msg)

    def send(self, json_data):
        data = json.dumps(json_data).encode()
        
        # send the size of our message
        self.s.sendall(struct.pack('>i', len(data)))
        # send the message
        self.s.sendall(data)

    def send_event(self, event, data):
        self.send({ "event" : event, "data" : data })

    def terminate(self):
        Log.info('BACKEND', 'Terminating...')

        self._running = False