import threading

class EventHandler(threading.Thread):
    def __init__(self, backend):
        threading.Thread.__init__(self, daemon=True)

        self._running = True

        self.backend = backend

    @property
    def running(self):
        return self._running

    def run(self):
        while self._running:
            msg = self.backend.queue.get()

            handler = getattr(self, msg["event"])
            if not handler:
                print("No handler exists for event", msg["event"])
            else:
                handler(msg["data"])

            self.backend.queue.task_done()

    def MESSAGE(self, data):
        print(data)

    def terminate(self):
        self._running = False