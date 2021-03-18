import threading
import json

class Client(threading.Thread):
    def __init__(self, addr, conn):
        threading.Thread.__init__(self)

        self._active = True

        self._addr = addr
        self._conn = conn

    def run(self):
        while self._active:
            # read the size from our buffer
            size = int(self._conn.recv(4))
            if not size:
                pass
            # read data
            data = self._conn.recv(size)

    def send(json_data):
        data = json.dumps(json_data).encode()
        
        # send the size of our message
        self._conn.sendall('%4d' % len(data))
        # send the message
        self._conn.sendall(data)