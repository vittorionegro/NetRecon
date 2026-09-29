import socket

def check_port(host, port):
    sock = socket.socket()
    sock.settimeout(2)

    res = sock.connect_ex((host, port))

    if(res == 0):
        print("[+] ", port,"/tcp responded")
    else:
        print("[-] ", port,"/tcp didnt respond")
    sock.close()
    


check_port("127.0.0.1", 8000)
