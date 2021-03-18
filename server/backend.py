import threading
from .client import Client

class Backend(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)

        self._clients = []
        self._running = True

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = '0.0.0.0'
        self.port = port

    @property
    def running(self):
        return self._running

    def broadcast(self, message):
        pass

    def run(self):
        self.s.bind((self.host, self.port))

        # queue up to 5 unaccepted connections
        self.s.listen(5)

        while self.running:
            # blocking call
            conn, addr = self.s.accept()

            client = Client(addr, conn)

            self._clients.append(client) 

    def terminate(self):
        # self.broadcast("Server is closing")

        self.running = False
