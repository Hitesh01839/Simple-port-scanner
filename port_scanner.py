import socket
import platform  # For getting the operating system name
import subprocess  # For executing the command


def ping_ip(ip_addr):
    """
    Returns True if host (str) responds to a ping request.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_addr]
    return subprocess.call(command) == 0


open_ports = []

def scan_port(target_ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt (in seconds)
        sock.settimeout(1)

        # Attempt to connect to the target IP and port
        result = sock.connect_ex((target_ip, port))

        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        else:
            print(f"Port {port} is closed")

        # Close the socket
        sock.close()

    except socket.error:
        print(f"Could not connect to {target_ip}:{port}")


def main():
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port: ").strip())
    end_port = int(input("Enter the ending port: ").strip())

    print(f"Scanning ports {start_port} to {end_port} on {target_ip}...")

    ping_res = ping_ip(target_ip)
    if (ping_res):
        for port in range(start_port, end_port + 1):
            scan_port(target_ip, port)
        print(f"Open ports are: {open_ports}")

    else:
        print("The target is not responding to ping requests, maybe it is not up!!")

if __name__ == "__main__":
    main()
