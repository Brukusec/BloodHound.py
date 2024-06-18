#! /usr/bin/env python

import bloodhound
from bloodhound.ldap_pool import LDAPConnectionPool

def main():
    # Inicialize o pool de conexões LDAP aqui, se necessário
    ldap_pool = LDAPConnectionPool(server_address, username, password)
    bloodhound.main()

if __name__ == "__main__":
    main()
