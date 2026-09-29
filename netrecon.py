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

check_port(target, 8000)
