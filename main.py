import socket
import sys

def check_server(address, port):
    # Create a TCP socket
    s = socket.socket()
    s.settimeout(2) # Give up after 2 seconds
    print(f"Attempting to connect to {address} on port {port}...")
    
    try:
        s.connect((address, port))
        print(f"SUCCESS: Connected to {address} on port {port}")
        return True
    except socket.error as e:
        print(f"FAILED: Connection to {address} on port {port} failed")
        return False
    finally:
        s.close()

if __name__ == '__main__':
    # Check if the user provided enough arguments
    # sys.argv[0] is the script name, [1] is the IP, [2] is the Port
    if len(sys.argv) != 3:
        print("Usage: python main.py <TARGET_IP> <PORT>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2]) # Convert text to number

    check_server(target_ip, target_port)