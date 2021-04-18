import threading
from time import sleep
# pylint: disable=no-name-in-module
from util.logger import Log

class EventHandler(threading.Thread):
    def __init__(self, backend, config):
        threading.Thread.__init__(self, daemon=True)

        self._running = True

        self._config = config

        self.backend = backend

    @property
    def running(self):
        return self._running

    def run(self):
        while self._running:
            if self.backend.queue.empty():
                sleep(0.001)

                continue
            client, msg = self.backend.queue.get()

            handler = getattr(self, msg["event"].lower(), False)
            if not handler:
                Log.warning("EVENT_HANDLER", "No handler exists for event "+ msg["event"])
            else:
                handler(client, msg["data"])

            Log.verbose("EVENT_HANDLER", f"[{msg['event']}]: {msg['data']}")

            self.backend.queue.task_done()

    def terminate(self):
        self._running = False

# 
# Socket events below this
# 

    def broadcast(self, client, data):
        self.backend.broadcast(data)

    def get_log(self, client, data):
        pass

    def get_user(self, client, data):
        pass

    def get_user_searches(self, client, data):
        client.send_event("GET_USER_SEARCHES", client.searches)

    def identify(self, client, data):
        client.identify(data["data"])

    def list_users(self, client, data):
        clients = []

        for identifier in clients:
            client = clients[identifer]

            clients.append({
                "id": identifier,
                "info": client.identity()
            })

        client.send_event("LIST_USERS", clients)

    def list_popular_searches(self, client, data):
        pass

    def message(self, client, data):
        data = data["data"]
        identifier = data["id"]
        
        target = self.backend.get_client(identifier)
        target.send_event("MESSAGE", data["message"])

    def search(self, client, data):
        search = data.data

        client.searches.append(search)

        if search["type"] == 'all':
            data = self.backend.datahandler.search_all(search["query"], search["exact"])
        elif search["type"] == 'column':
            data = self.backend.datahandler.search_column(search.query["column"], search.query["value"], search["exact"])
        elif search["type"] == 'columns':
            data = self.backend.datahandler.search_columns(search.query["columns"], search.query["values"], search["exact"])

        client.send_event("SEARCH", data)