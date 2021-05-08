import json
import queue
import socket
import struct
import threading
from time import sleep
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

        self.broadcast = None # Broadcast event callback
        self.data = None # Temp place to store our socket data
        self.identified = False # Tell our frontend we have successfully "logged in"

    @property
    def queue(self):
        return self._queue

    @property
    def running(self):
        return self._running

    def get_data(self):
        try:
            for i in range(300):
                if self.data:
                    return self.data
                sleep(0.01)
            if not self.data: # search timeout
                return None
        except Exception as e:
            print(e)
            print("This should not happen, but it might")
        finally:
            self.data = None

    def handle_message(self):
        # read the size from our buffer
        size = self.s.recv(4)
        if not size:
            return
        size = struct.unpack('>i', size)[0]
        # read data
        data = self.s.recv(size)
        if not data:
            return

        Log.verbose('BACKEND', data)

        # parse the message
        msg = json.loads(data.decode("utf8"))
        # put the message in the queue
        self.queue.put(msg)

    def run(self):
        Log.info('BACKEND', 'Running')

        attempts = 5
        for i in range(attempts):
            try:
                self.s.connect((self.host, self.port))

                break
            except ConnectionRefusedError as e:
                Log.warning('BACKEND', f"Could not connect to server on {self.host}:{self.port}, retrying...")
                sleep(1)

            if i == attempts - 1:
                self._running = False

        self._handler.start()

        while self._running:
            try:
                self.handle_message()
            except (Exception, ConnectionResetError) as e:
                if isinstance(e, ConnectionResetError):
                    Log.warning('BACKEND', 'Remote server disconnected...')
                else:
                    Log.error("CLIENT", "Undefined behaviour from client, removing client...")

                    print(e)

                break

        self._handler.terminate()


    def send(self, json_data):
        data = json.dumps(json_data).encode()

        # send the size of our message
        self.s.sendall(struct.pack('>i', len(data)))
        # send the message
        self.s.sendall(data)

    def send_event(self, event, data = {}):
        self.send({ "event" : event, "data" : data })

    def terminate(self):
        Log.info('BACKEND', 'Terminating...')

        self._running = False
