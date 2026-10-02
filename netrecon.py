import socket
import sys
import argparse
from dataclasses import dataclass, field, asdict
import json
import csv

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
    print(f"\nHost: {host.ip}\n")
    print(f"{'PORT':<12}{'STATE'}")
    for s in host.services:
        mark = "[+]" if s.status == "open" else "[-]"
        name = f"{s.port}/{s.protocol}"
        print(f"{name:<12}{mark} {s.status}")

def outputJson(host, path):
    r = asdict(host)
    with open(path, "w") as f:
        json.dump(r, f, indent=2)
        return 0

def outputCsv(host, path):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "port", "protocol", "status"])
        for s in host.services:
            writer.writerow([host.ip, s.port, s.protocol, s.status])


    
parser = argparse.ArgumentParser(description="NetRecon: Network recon tool")  # parser
parser.add_argument("target", help="IP address to scan")  # args.target
parser.add_argument("--ports", default="8000", help="comma-separated ports")  # args.ports
parser.add_argument("--output", help="JSON or CSV file to save results to") # args.output

args = parser.parse_args()
ports = args.ports.split(",")

host = Host(args.target)
for p in ports:
    host.services.append(checkPort(args.target, int(p)))

printHost(host)

if args.output:
    if args.output.endswith(".csv"):
        outputCsv(host, args.output)
        print(f"[+] Results saved to {args.output}")
    elif args.output.endswith(".json"):
        outputJson(host, args.output)
        print(f"[+] Results saved to {args.output}")
    else:
        print(f"[!] Unknown output type '{args.output}', use .json or .csv")
        sys.exit(1)
