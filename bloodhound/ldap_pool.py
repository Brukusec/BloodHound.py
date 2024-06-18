# bloodhound/ldap_pool.py

from ldap3 import Server, Connection, ALL, SAFE_SYNC
from queue import Queue

class LDAPConnectionPool:
    def __init__(self, server_address, username, password, max_connections=2):
        self.server = Server(server_address, get_info=ALL)
        self.username = username
        self.password = password
        self.max_connections = max_connections
        self.pool = Queue(maxsize=max_connections)
        self._initialize_pool()

    def _initialize_pool(self):
        for _ in range(self.max_connections):
            conn = Connection(self.server, user=self.username, password=self.password, client_strategy=SAFE_SYNC, auto_bind=True)
            self.pool.put(conn)

    def get_connection(self):
        return self.pool.get()

    def release_connection(self, conn):
        self.pool.put(conn)

    def __del__(self):
        while not self.pool.empty():
            conn = self.pool.get()
            conn.unbind()
