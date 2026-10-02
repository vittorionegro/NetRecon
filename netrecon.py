import socket
import sys
import argparse
from dataclasses import dataclass, field

@dataclass
class Service:
    port: int
    protocol: str
    status: str

@dataclass
class Host:
    ip: str
    services: list[Service] = field(default_factory=list)

def checkPort(host, port):
    sock = socket.socket()
    sock.settimeout(2)

    res = sock.connect_ex((host, port))

    if(res == 0):
        sock.close()
        return(Service(port, protocol="tcp", status="open"))
    
    else:
        sock.close()
        return(Service(port, protocol="tcp", status="closed"))

def printHost(host):
    print(host.ip)
    for s in host.services:
        print(f"{s.port}/{s.protocol} {s.status}")
    
parser = argparse.ArgumentParser(description="NetRecon: Network recon tool")  # parser
parser.add_argument("target", help="IP address to scan")  # args.target
parser.add_argument("--ports", default="8000", help="comma-separated ports")  # args.ports

args = parser.parse_args()
ports = args.ports.split(",")

host = Host(args.target)
for p in ports:
    host.services.append(checkPort(args.target, int(p)))
    print(host)