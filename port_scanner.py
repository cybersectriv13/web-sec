import socket
from datetime import datetime

target = "127.0.0.1"
ports = range(8000, 8100)

print(f"Scanning {target} at {datetime.now()}")
open_ports = []

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)
    result = sock.connect_ex((target, port))  # returns 0 on success, avoids try/except per port
    if result == 0:
        open_ports.append(port)
        print(f"Port {port}: OPEN")
    sock.close()

print(f"Open ports: {open_ports}")
