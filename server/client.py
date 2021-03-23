import json
import struct
import threading
# pylint: disable=no-name-in-module
from util.logger import Log

class Client(threading.Thread):
    def __init__(self, backend, addr, conn):
        threading.Thread.__init__(self)

        self._active = True

        self._addr = addr
        self._conn = conn

        self.backend = backend

    @property
    def active(self):
        return self._active

    @property
    def addr(self):
        return self._addr

    def handle_message(self):
        # read the size from our buffer
        size = struct.unpack('>i', self._conn.recv(4))[0]
        if not size:
            return
        # read data
        data = self._conn.recv(size)

        Log.verbose('BACKEND', data)

        # parse the message
        msg = json.loads(data.decode("utf8"))
        # put the message in the queue
        self.backend.queue.put(msg)

    def run(self):
        while self._active:
            try:
                self.handle_message()
            except (Exception,ConnectionResetError) as e:
                if (isinstance(e,ConnectionResetError)):
                    Log.warning("CLIENT", "Lost connection...")
                    break

                Log.error("CLIENT", "Undefined behaviour from client, removing client...")

                print(e)
                break
        self.backend.remove_client(self)

    def send(self, json_data):
        data = json.dumps(json_data).encode()
        
        # send the size of our message
        self._conn.sendall(struct.pack('>i', len(data)))
        # send the message
        self._conn.sendall(data)

    def send_event(self, event, data):
        self.send({ "event" : event, "data" : data })

    def terminate(self):
        Log.info("CLIENT", "Terminating client thread...")

        self._conn.close()

        self._active = False