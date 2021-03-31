from time import sleep
import threading
# pylint: disable=no-name-in-module
from util.logger import Log

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
            if self.backend.queue.empty():
                sleep(0.0001)

                continue
            msg = self.backend.queue.get()

            handler = getattr(self, msg["event"].lower(), False)
            if not handler:
                Log.warning("EVENT_HANDLER", "No handler exists for event "+ msg["event"])
            else:
                handler(msg["data"])

            Log.verbose("EVENT_HANDLER", f"[{msg['event']}]: {msg['data']}")

            self.backend.queue.task_done()

    def message(self, data):
        print(data)

    def terminate(self):
        self._running = False