import socket

def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
            sock.close()
        except socket.gaierror:
            print(f"Hostname {host} could not be resolved.")
            break
        except socket.error:
            print(f"Could not connect to server {host}")
            break

host = "www.example.com"
start_port = 1
end_port = 100
scan_ports(host, start_port, end_port)
