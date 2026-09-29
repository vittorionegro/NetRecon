import socket
import sys

def check_port(host, port):
    sock = socket.socket()
    sock.settimeout(2)

    res = sock.connect_ex((host, port))

    if(res == 0):
        print(f"[+] {port}/tcp responded")
    else:
        print(f"[-] {port}/tcp didn't respond")
    sock.close()
    


if len(sys.argv) < 2:
    print("Usage: python netrecon.py <target>")
    sys.exit(1)
target = sys.argv[1]

if len(sys.argv) > 3 and sys.argv[2] == "--ports":
    ports = sys.argv[3]
else:
    ports = "8000"

nports = ports.split(",")

for port in nports:
    check_port(target, int(port))
