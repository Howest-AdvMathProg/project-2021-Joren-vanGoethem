import queue
import socket
import threading
from client import Client
from datahandler import DataHandler
from eventhandler import EventHandler
# pylint: disable=no-name-in-module
from util.logger import Log

class Backend(threading.Thread):
    def __init__(self, config):
        threading.Thread.__init__(self, daemon=True)

        self._clients = {}
        self._queue = queue.Queue()
        self._running = True

        self.datahandler = DataHandler(self, config["datahandler"])
        self._eventhandler = EventHandler(self, config["eventhandler"])

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.host = config["server"]["ip"]
        self.port = config["server"]["port"]

    @property
    def clients(self):
        return self._clients

    @property
    def queue(self):
        return self._queue

    @property
    def running(self):
        return self._running

    def broadcast(self, message):
        for addr in self._clients:
            self._clients[addr].send_event("BROADCAST", message)

    def get_client(self, client_resolvable):
        return self._clients[client_resolvable]

    def remove_client(self, client_resolvable):
        if isinstance(client_resolvable, Client):
            client = client_resolvable
        else:
            client = self._clients[client_resolvable]

        client.terminate()

        self._clients.pop(client.addr, None)

    def run(self):
        Log.info('BACKEND', 'Running')

        self.s.bind((self.host, self.port))

        # queue up to 5 unaccepted connections
        self.s.listen(5)

        self._eventhandler.start()

        while self.running:
            # blocking call
            conn, addr = self.s.accept()

            Log.verbose('BACKEND', 'Client connected: {}'.format(addr))

            client = Client(self, addr, conn)
            client.start()

            self._clients[addr] = client

    def terminate(self):
        if self._running:
            Log.info('BACKEND', 'Terminating...')

            self._eventhandler.terminate()

            self._running = False
