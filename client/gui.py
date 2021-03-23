import threading

class GUI(threading.Thread):
    def __init__(self, backend):
        threading.Thread.__init__(self, daemon=True)

        self._running = True

        self.backend = backend

    @property
    def running(self):
        return self._running

    def run(self):
        while self._running:
            event = input("EVENT > ")
            data = input("DATA > ")

            self.backend.send_event(event, data)

    def terminate(self):
        self._running = False