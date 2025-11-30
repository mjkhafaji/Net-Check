# Net-Check

**Net-Check** is a lightweight Python utility designed to verify TCP connectivity to remote servers and ports. It serves as a programmatic alternative to Telnet for network troubleshooting.

## Features
- **TCP Socket Connection:** Direct socket verification without ICMP (Ping).
- **Error Handling:** Distinguishes between connection refusals and timeouts.
- **Lightweight:** Uses only standard Python libraries.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** `socket`, `sys`

## Usage

1. Clone the repository:
    git clone https://github.com/YOUR_USERNAME/net-check.git

2. Run the script:
    python main.py

3. (Optional) Edit main.py to change the target address (default is google.com on port 80).

## Future Improvements
* Add CLI arguments to pass IP and Port dynamically.
* Implement logging to a local file.
* Add bulk scanning from a CSV inventory file.