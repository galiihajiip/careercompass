import socket

_orig_getaddrinfo = socket.getaddrinfo

def _ipv4_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    # force AF_INET (IPv4)
    family = socket.AF_INET
    return _orig_getaddrinfo(host, port, family, type, proto, flags)

socket.getaddrinfo = _ipv4_getaddrinfo

import sys
from pip._internal.cli.main import main
if __name__ == '__main__':
    sys.exit(main())
