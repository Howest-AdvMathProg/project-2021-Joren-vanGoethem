import queue
import socket
import threading
from client import Client
from handler import EventHandler
# pylint: disable=no-name-in-module
from util.logger import Log

class Backend(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self, daemon=True)

        self._clients = {}
        self._queue = queue.Queue()
        self._running = True

        self._handler = EventHandler(self)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = "0.0.0.0"
        self.port = port

    @property
    def queue(self):
        return self._queue

    @property
    def running(self):
        return self._running

    def broadcast(self, message):
        for client in self._clients:
            client.send_event("BROADCAST", message)

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

        self._handler.start()

        while self.running:
            # blocking call
            conn, addr = self.s.accept()

            Log.verbose('BACKEND', 'Client connected: {}'.format(addr))

            client = Client(self, addr, conn)
            client.start()

            self._clients[addr] = client

    def terminate(self):
        Log.info('BACKEND', 'Terminating...')
        # self.broadcast("Server is closing")
        self._handler.terminate()

        self._running = False
