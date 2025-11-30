import socket
import sys

def check_server(address, port):
    # Create a TCP socket
    s = socket.socket()
    print(f"Attempting to connect to {address} on port {port}...")
    
    try:
        s.connect((address, port))
        print(f"SUCCESS: Connected to {address} on port {port}")
        return True
    except socket.error as e:
        print(f"FAILED: Connection to {address} on port {port} failed")
        print(f"Error: {e}")
        return False
    finally:
        s.close()

if __name__ == '__main__':
    # Default check google.com on port 80 (HTTP)
    check_server("google.com", 80)